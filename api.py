import requests
import sqlite3
import sys

try:
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute('create table temperature (date text, feelslike text)')

    response = requests.get('https://weather.visualcrossing.com/VisualCrossingWebservices')
    data = response.json()
    for item in data['days']:
        # print(i)
        dt = items.get('datatime')
        fl = item.get('feelslike')
        # print(dt, fl)
        cursor.execute('insert into temperature values (? ?)', (dt, fl,))
    conn.commit()

    cursor.execute('select * from temperature')
    wdata = cursor.fetchall()
    for data in wdata:
        print('The weather feels like from the database table: ', data)
        if data[1] > '12.0':
            print(data)

except Exception as e:
    conn.rollback() # incomplete if one fails instead of all errors
    print('Error: ', e)
    print(' -- ', sys.exc_info()[0])

conn.close()





# end
