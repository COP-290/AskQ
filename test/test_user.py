from werkzeug.exceptions import abort
from flask_paginate import Pagination, get_page_args
import MySQLdb
# app=Flask(__name__)
import unittest
import csv
import MySQLdb
import datetime
def requestConnection():
    mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='root',
    db='askq')
    return mydb

def requestCursor(conn):
    return conn.cursor()

def dis_user(id):
        conn = requestConnection()
        cursor = requestCursor(conn)
        cursor.execute('SELECT Creation_Date from User where ID = ' + str(id))
        date = cursor.fetchone()
        detail=cursor.execute('SELECT * from User where ID = ' + str(id))
        detail=cursor.fetchone()
        date = date[0]
        d = date.day
        mth = date.month
        ye = date.year
        # print(profile[0])
        date = str(d) + "/" + str(mth) + "/"+ str(ye)
        cursor.close()
        conn.close()
        return (date,detail)


# print(dis_user(66))
import unittest
import csv
import MySQLdb
import datetime
# from flaskblog.user import dis_user
L=('1/8/2006', (66, 'Satyam', 'Something needs to be written there', datetime.datetime(2006, 8, 1, 15, 45, 37), None, 'India', 378, 893, 98, 'https://static.vecteezy.com/system/resources/previews/005/544/718/original/profile-icon-design-free-vector.jpg', 'www.gooogle.com', '1234'))
class Test_User(unittest.TestCase):
        def test_dis_User(self):
                x = dis_user(66)
                # print(x)
                self.assertEqual((L),x)