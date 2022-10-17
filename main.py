import datetime
import pandas as pd
from util import select





if __name__=='__main__':

    area_dict={28:"Taipei", 8:"New_Taipei",18:"Keelung",11:"Yilan", 16:"Taoyuan", 20:"Hsinchu",
            15:"Miaoli", 2:"Taichung",22:"Changhua",13:"Nantou",19:"Yunlin", 21:"Chiayi", 
            10:"Tainan", 17:"Kaoshiung", 14:"Pingtung", 12:"Hualien",9:"Taitung",24:"Kinmen",23:"Penghu"}
    movie_dict={}
    df = pd.read_csv('movie_id.csv')

    # print(df) 
    for i,x in enumerate(df["ID"]):
        movie_dict[int(x)]=df["movie"][i]
    while 1:
        cnt=0
        print("0 for no area restriction :)")
        for a in area_dict:
            cnt+=1
            print(f"{a}: {area_dict[a]} ", end='')
            if not (cnt%10):
                print()
        print("\n\nInput the ID of the area you want to watch the movie at: ",end='')
        area=int(input())
        print()
        
        cnt=0
        if area:
            print("00000 for you want to watch any movie :)")
        for m in movie_dict:
            cnt+=1
            print(f"{m}: {movie_dict[m]} ", end='')
            if not (cnt%5):
                print()
        print("\n\nInput the ID of the movie you want to watch: ", end='')
        movie=int(input())
        
        now=datetime.datetime.now()
        t=now.hour*60+now.minute

        if not area:
            print(f"\nAvailable {movie_dict[movie]} showings in Taiwan for you: ")
        elif not movie:
            print(f"\nAll available movie showings in {area_dict[area]} for you: ")
        else:
            print(f"\nAvailable {movie_dict[movie]} showings in {area_dict[area]} for you: ")
        select(area, movie, t)
        # select(area, movie, t,1)

        print("\nLook for another movie?   [1/0] ", end='')
        temp=int(input())
        print()
        if not temp:
            print("Enjoy your movie:p")
            break
