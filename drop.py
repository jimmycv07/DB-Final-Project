import psycopg2 as pg2

Pass="Your Password"

def drop_table():
    commands=(
        '''
        DROP TABLE Taipei
        ''',
        '''
        DROP TABLE New_Taipei
        ''',
        '''
        DROP TABLE Keelung
        ''',
        '''
        DROP TABLE Yilan
        ''',
        '''
        DROP TABLE Taoyuan
        ''',
        '''
        DROP TABLE Hsinchu
        ''',
        '''
        DROP TABLE Miaoli
        ''',
        '''
        DROP TABLE Taichung
        ''',
        '''
        DROP TABLE Changhua
        ''',
        '''
        DROP TABLE Nantou
        ''',
        '''
        DROP TABLE Yunlin
        ''',
        '''
        DROP TABLE Chiayi
        ''',
        '''
        DROP TABLE Tainan
        ''',
        '''
        DROP TABLE Kaoshiung
        ''',
        '''
        DROP TABLE Pingtung
        ''',
        '''
        DROP TABLE Hualien
        ''',
        '''
        DROP TABLE Taitung
        ''',
        '''
        DROP TABLE Kinmen
        ''',
        '''
        DROP TABLE Penghu
        '''
    )

    print('Connecting to the PostgreSQL database...')
    conn = pg2.connect(
        host="database-1.cxeqjrvpiheo.us-east-1.rds.amazonaws.com",
        database="movie",
        user="jimmycv07",
        password=Pass,
        port='5432')


    # create a cursor
    cur = conn.cursor()
            
    # execute a statement
    # cur.execute('SELECT version()')

    for c in commands:
        cur.execute(c)
    conn.commit()
    print('Tables dopped')

    # display the PostgreSQL database server version
    # db_version = cur.fetchone()
    # print(db_version)

    # close the communication with the PostgreSQL
    cur.close()

    conn.close()
    print('Database connection closed.')