import psycopg2 as pg2

Pass="Your Password"

""" create tables in the PostgreSQL database"""

area_dict={ 28:"Taipei", 8:"New_Taipei",18:"Keelung",11:"Yilan", 16:"Taoyuan", 20:"Hsinchu",
            15:"Miaoli", 2:"Taichung",22:"Changhua",13:"Nantou",19:"Yunlin", 21:"Chiayi", 
            10:"Tainan", 17:"Kaoshiung", 14:"Pingtung", 12:"Hualien",9:"Taitung",24:"Kinmen",23:"Penghu"}

def create_table():
    commands = (
        """
        CREATE TABLE Taipei (
            time_int INTEGER,
            time varchar(8),
            type varchar(10),
            theater varchar(50),
            title INTEGER,
            PRIMARY KEY(title,theater, type, time)
        )
        """,
        """
        CREATE TABLE New_Taipei (
            time_int INTEGER,
            time varchar(8),
            type varchar(10),
            theater varchar(50),
            title INTEGER,
            PRIMARY KEY(title,theater, type, time)
        )
        """,
        """
        CREATE TABLE Keelung (
            time_int INTEGER,
            time varchar(8),
            type varchar(10),
            theater varchar(50),
            title INTEGER,
            PRIMARY KEY(title,theater, type, time)
        )
        """,
        """
        CREATE TABLE Yilan (
            time_int INTEGER,
            time varchar(8),
            type varchar(10),
            theater varchar(50),
            title INTEGER,
            PRIMARY KEY(title,theater, type, time)
        )
        """,
        """
        CREATE TABLE Taoyuan (
            time_int INTEGER,
            time varchar(8),
            type varchar(10),
            theater varchar(50),
            title INTEGER,
            PRIMARY KEY(title,theater, type, time)
        )
        """,
        """
        CREATE TABLE Hsinchu (
            time_int INTEGER,
            time varchar(8),
            type varchar(10),
            theater varchar(50),
            title INTEGER,
            PRIMARY KEY(title,theater, type, time)
        )
        """,
        """
        CREATE TABLE Miaoli (
            time_int INTEGER,
            time varchar(8),
            type varchar(10),
            theater varchar(50),
            title INTEGER,
            PRIMARY KEY(title,theater, type, time)
        )
        """,
        """
        CREATE TABLE Taichung (
            time_int INTEGER,
            time varchar(8),
            type varchar(10),
            theater varchar(50),
            title INTEGER,
            PRIMARY KEY(title,theater, type, time)
        )
        """,
        """
        CREATE TABLE Changhua (
            time_int INTEGER,
            time varchar(8),
            type varchar(10),
            theater varchar(50),
            title INTEGER,
            PRIMARY KEY(title,theater, type, time)
        )
        """,
        """
        CREATE TABLE Nantou (
            time_int INTEGER,
            time varchar(8),
            type varchar(10),
            theater varchar(50),
            title INTEGER,
            PRIMARY KEY(title,theater, type, time)
        )
        """,
        """
        CREATE TABLE Yunlin (
            time_int INTEGER,
            time varchar(8),
            type varchar(10),
            theater varchar(50),
            title INTEGER,
            PRIMARY KEY(title,theater, type, time)
        )
        """,
        """
        CREATE TABLE Chiayi (
            time_int INTEGER,
            time varchar(8),
            type varchar(10),
            theater varchar(50),
            title INTEGER,
            PRIMARY KEY(title,theater, type, time)
        )
        """,
        """
        CREATE TABLE Tainan (
            time_int INTEGER,
            time varchar(8),
            type varchar(10),
            theater varchar(50),
            title INTEGER,
            PRIMARY KEY(title,theater, type, time)
        )
        """,
        """
        CREATE TABLE Kaoshiung (
            time_int INTEGER,
            time varchar(8),
            type varchar(10),
            theater varchar(50),
            title INTEGER,
            PRIMARY KEY(title,theater, type, time)
        )
        """,
        """
        CREATE TABLE Pingtung (
            time_int INTEGER,
            time varchar(8),
            type varchar(10),
            theater varchar(50),
            title INTEGER,
            PRIMARY KEY(title,theater, type, time)
        )
        """,
        """
        CREATE TABLE Hualien (
            time_int INTEGER,
            time varchar(8),
            type varchar(10),
            theater varchar(50),
            title INTEGER,
            PRIMARY KEY(title,theater, type, time)
        )
        """,
        """
        CREATE TABLE Taitung (
            time_int INTEGER,
            time varchar(8),
            type varchar(10),
            theater varchar(50),
            title INTEGER,
            PRIMARY KEY(title,theater, type, time)
        )
        """,
        """
        CREATE TABLE Kinmen (
            time_int INTEGER,
            time varchar(8),
            type varchar(10),
            theater varchar(50),
            title INTEGER,
            PRIMARY KEY(title,theater, type, time)
        )
        """,
        """
        CREATE TABLE Penghu (
            time_int INTEGER,
            time varchar(8),
            type varchar(10),
            theater varchar(50),
            title INTEGER,
            PRIMARY KEY(title,theater, type, time)
        )
        """
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
    print('Tables created')
    # cur.execute('SELECT version()')

    for c in commands:
        cur.execute(c)
    conn.commit()

    # display the PostgreSQL database server version
    # db_version = cur.fetchone()
    # print(db_version)

    # close the communication with the PostgreSQL
    cur.close()

    conn.close()
    print('Database connection closed.')