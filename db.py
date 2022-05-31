import sqlite3
import sys

try:
    conn = sqlite3.connect(':memory:')
    # only re-create the db when executing/running
    # conn = sqlite3.connect('allmymovies.db')
    conn.row_factory = sqlite3.Row
    # ret dict mv['genre'] not tuple mv[0]
    cursor = conn.cursor()

    cursor.excute('''
    create table movies (id int primary key, name text, genre text)
    ''')
    cursor.excute('''
    create table movies (id int primary key, name text, genre text, language text)
    ''')
    cursor.execute('insert into movies values (1, 'Batman', 'Comedy')')
    cursor.execute('insert into movies values (2, 'Helmet', 'Poetry', 'English')')

    # security
    val = 'delete * from movies'
    val = website url
    print('select count(*) from movies %s' %val)
    cursor.execute('select * from movies where genre = %s' %val)
    cursor.execute('select * from movies where genre = ?', (val,))

    cursor.execute('select * from movies union all select * from books')
    # cursor.execute('drop table movies')
    movies = cursor.fetchone()
    print(movies.keys())
    # books = cursor.fetchall()
    # movies = cursor.fetchall()
    # movies = set(movies) # no duplicates tuple -> set
    # for mv in movies:
    #     print(mv['name'])

    conn.commit() #

except Exception as e:
    conn.rollback() # catch/print failures for key error...etc
    print('ERROR', e)




# end
