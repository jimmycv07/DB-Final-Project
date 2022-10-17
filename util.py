import psycopg2 as pg2
import pandas as pd
area_dict={ 28:"Taipei", 8:"New_Taipei",18:"Keelung",11:"Yilan", 16:"Taoyuan", 20:"Hsinchu",
            15:"Miaoli", 2:"Taichung",22:"Changhua",13:"Nantou",19:"Yunlin", 21:"Chiayi", 
            10:"Tainan", 17:"Kaoshiung", 14:"Pingtung", 12:"Hualien",9:"Taitung",24:"Kinmen",23:"Penghu"}

Pass="YourPassword"

def insert_list(area,var):
    sql = "INSERT INTO " 
    sql+=area_dict[area]
    sql+="(time_int, time, type, theater, title) VALUES(%s, %s, %s, %s, %s)"
    conn = pg2.connect(
    host="database-1.cxeqjrvpiheo.us-east-1.rds.amazonaws.com",
    database="movie",
    user="jimmycv07",
    password=Pass,
    port='5432')


    cur = conn.cursor()
    # cur.execute(sql, ( 100, "1:00","IMAX", "theater_list", 11809))
    cur.executemany(sql, var)
    # print(cur.rowcount)
    
    conn.commit()
    cur.close()
    conn.close()

def delete_data():
    conn = pg2.connect(
    host="database-1.cxeqjrvpiheo.us-east-1.rds.amazonaws.com",
    database="movie",
    user="jimmycv07",
    password=Pass,
    port='5432')


# create a cursor
    cur = conn.cursor()
    # cur.execute("DELETE FROM Taipei WHERE time_int = %s", (1360,))
    cur.execute("DELETE FROM Hualien")
    # cur.executemany(sql, time_int_list, time_list, type_list, theater_list, title_list)
        # commit the changes to the database
    conn.commit()
        # close communication with the database
    cur.close()
    conn.close()

def select(area, movie, time, explain=0):
    conn = pg2.connect(
    host="database-1.cxeqjrvpiheo.us-east-1.rds.amazonaws.com",
    database="movie",
    user="jimmycv07",
    password=Pass,
    port='5432')
    
    if not area:
        for a in area_dict:
            sql = "SELECT theater, type, time FROM "
            sql+=area_dict[a]
            sql+=" WHERE title=%s and time_int>%s"
            sql+=" ORDER BY time_int "

            if explain:
                sql="EXPLAIN ANALYZE " +sql
            cur = conn.cursor()
            cur.execute(sql, (movie, time))
            res = cur.fetchone()
            if explain:
                while res is not None:
                    print(res)
                    res=cur.fetchone()
            else:
                if res is None:
                    # print("Sorry, no available showings currently:(...")
                    continue
                else:
                    print(area_dict[a])
                    while res is not None:
                        print(f"{res[0]} {res[1]} {res[2]}") 
                        res=cur.fetchone()
                    print("====================")
    elif not movie:
        movie_dict={}
        df = pd.read_csv('movie_id.csv')

        # print(df) 
        for i,x in enumerate(df["ID"]):
            movie_dict[int(x)]=df["movie"][i]
        sql = "SELECT theater, type, time, title FROM "
        sql+=area_dict[area]
        sql+=" WHERE time_int>%s"
        sql+=" ORDER BY time_int "

        if explain:
            sql="EXPLAIN ANALYZE " +sql
        cur = conn.cursor()
        cur.execute(sql, (time,))
        res = cur.fetchone()
        if explain:
            while res is not None:
                print(res)
                res=cur.fetchone()
        else:
            if res is None:
                print("Sorry, no available showings currently:(...")
            else:
                while res is not None:
                    print(f"{movie_dict[res[3]]}: {res[0]} {res[1]} {res[2]}") 
                    res=cur.fetchone()

    else:

        sql = "SELECT theater, type, time FROM "
        sql+=area_dict[area]
        sql+=" WHERE title=%s and time_int>%s"
        sql+=" ORDER BY time_int "

        if explain:
            sql="EXPLAIN ANALYZE " +sql
        cur = conn.cursor()
        cur.execute(sql, (movie, time))
        res = cur.fetchone()
        if explain:
            while res is not None:
                print(res)
                res=cur.fetchone()
        else:
            if res is None:
                print("Sorry, no available showings currently:(...")
            else:
                while res is not None:
                    # print(res)
                    print(f"{res[0]} {res[1]} {res[2]}") 
                    res=cur.fetchone()

    cur.close()
    conn.close()

def select_cnt(area):
    conn = pg2.connect(
    host="database-1.cxeqjrvpiheo.us-east-1.rds.amazonaws.com",
    database="movie",
    user="jimmycv07",
    password=Pass,
    port='5432')

    sql = "SELECT COUNT(*) FROM "
    sql+=area_dict[area]

    cur = conn.cursor()
    cur.execute(sql)
    res = cur.fetchone()
    while res is not None:
        print(f"{area_dict[area]} : {res[0]}") 
        res=cur.fetchone()
        # close communication with the database
    cur.close()
    conn.close()

def command(sql):
    conn = pg2.connect(
    host="database-1.cxeqjrvpiheo.us-east-1.rds.amazonaws.com",
    database="movie",
    user="jimmycv07",
    password=Pass,
    port='5432')
    
    cur = conn.cursor()
    cur.execute(sql)
    cur.close()
    conn.commit()
    conn.close()

if __name__=='__main__':
    # insert_list(28,[])
    # insert_list(28,1360 , "22:40", "IMAX", "MITSUI OUTLET PARK", 11352)
    delete_data()

    # for a in area_dict:
    #     select_cnt(a)


    # command('set enable_seqscan TO on')
    # command('set enable_bitmapscan TO on')
    # # command('set enable_seqscan TO on')

    # select(8, 10159,600)
    # select(8, 10159,600,1)

    # command('''CREATE INDEX Index_Taipei_time on Taipei(time_int)''' )
    # command('''CREATE INDEX Index_Taipei_title on Taipei using HASH("title")''' )
    # command('''CREATE INDEX Index_New_Taipei_time on New_Taipei(time_int)''' )
    # command('''CREATE INDEX Index_New_Taipei_title on New_Taipei using HASH("title")''' )