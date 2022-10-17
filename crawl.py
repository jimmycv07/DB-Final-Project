import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from pyquery import PyQuery as pq
from datetime import date
from bisect import bisect_left
from util import insert_list
from drop import drop_table
from createTable import create_table
import time


# drop_table()
# create_table()
options = Options()
options.add_argument("--disable-notifications")

tt=time.time() 
chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
chrome.get("https://movies.yahoo.com.tw/")
time.sleep(15)
chrome.maximize_window()

button = chrome.find_element(By.XPATH, '//*[@id="sbox_mid"]')
button.click()
time.sleep(10)


soup = BeautifulSoup(chrome.page_source, 'html.parser')
movie_html = soup.find("select", attrs={'name':"movie_id"})
movie_item = movie_html.find_all("option",attrs={'data-name':re.compile('.*')})
chrome.quit()

print(movie_html)

title_dict={}
title_list = []
id_list = []

for info in movie_item:
    # print(info)
    # print(type(info))
    print("Movie: {}, ID: {}".format(info["data-name"], info["value"]))
    title_dict[int(info["value"])]=info["data-name"]
    id_list.append(int(info["value"]))
    title_list.append(info["data-name"])

df_movie_id = pd.DataFrame()
df_movie_id["ID"]=id_list
df_movie_id["movie"]=title_list
df_movie_id.to_csv("./movie_id.csv",encoding="utf-8-sig")


today=date.today()
cur_date=today.strftime("%Y-%m-%d")
print(cur_date)

area_dict={ 28:"Taipei", 8:"New_Taipei",18:"Keelung",11:"Yilan", 16:"Taoyuan", 20:"Hsinchu",
            15:"Miaoli", 2:"Taichung",22:"Changhua",13:"Nantou",19:"Yunlin", 21:"Chiayi", 
            10:"Tainan", 17:"Kaoshiung", 14:"Pingtung", 12:"Hualien",9:"Taitung",24:"Kinmen",23:"Penghu"}

for a in area_dict:
    for m in title_dict:
        url = "https://movies.yahoo.com.tw/ajax/pc/get_schedule_by_movie"

        payload = {'movie_id':str(m),
                'date':cur_date,
                'area_id':str(a),
                'theater_id':'',
                'datetime':'',
                'movie_type_id':''}

        resp = requests.get(url, params=payload)
        # print(resp.url)
        #print(resp.json()['view'])  #json原始碼
        #print(resp.json())
        json_data = resp.json()
        # print(json_data['view'])

        soup = BeautifulSoup(json_data['view'],'lxml')
        html_elem = soup.find_all("ul", attrs={'data-theater_name':re.compile(".*")})
        # print(html_elem) 
        print(title_dict[m])

        theater_list = []
        for item in html_elem:
            type_list= []
            time_list = []
            time_int_list=[]
            #print(item)
            theater = item.find("li",attrs={"class":"adds"})
            #print(theater)
            print("theater： {}".format(theater.find("a").text))
            
            info = item.find_all(class_="gabtn")
            #print(info)
            for i in info:
                #print(i)
                print(i["data-movie_time"],i["data-movie_type"])
                t=i["data-movie_time"].split(':')
                if int(t[0]):
                    t_int= int(t[0])*60+int(t[1])
                else:
                    t_int= 24*60+int(t[1])
                I=bisect_left(time_int_list,t_int)
                if  I!= len(time_int_list) and time_int_list[I]==t_int:
                    continue
                time_int_list.insert(I,t_int)
                theater_list.insert(I,theater.find("a").text)
                time_list.insert(I,i["data-movie_time"])
                type_list.insert(I,i["data-movie_type"])
            # print("====================")
            
            var=[]
            for i in range(len(time_list)):
                var.append((time_int_list[i], time_list[i], type_list[i], theater.find("a").text, m))
            print(var)
            # insert_list(a, var)

print(f"{(time.time()-tt)//60}m {time.time()%60}s ")



# df = pd.DataFrame()

# df["戲院"] = theater_list
# df["類型"] = type_list
# df["時刻"] = time_list
# df.to_csv("./movie_schedule.csv",encoding="utf-8-sig")