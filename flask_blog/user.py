from flask import Flask, render_template, request, url_for, flash, redirect, session
from werkzeug.exceptions import abort
from werkzeug.security import generate_password_hash, check_password_hash
from flask_paginate import Pagination, get_page_args
import MySQLdb
from tag import get_tags
from question import pagefunction
from question import showQuestion_byscore_help,sort_que_by_time
# from particular_question import particular_que_from_id,answer_from_parent_id,score_question,score_answer,sort_ans_by_time
# from user import check_login
import re
app = Flask(__name__)

def requestConnection():
    mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='root',
    db='askq')
    return mydb

def requestCursor(conn):
    return conn.cursor()
app.config['SECRET_KEY'] = 'your secret key'




def dis_user(id):
        conn = requestConnection()
        cursor = requestCursor(conn)
        cursor.execute('SELECT Creation_Date from User where ID = ' + str(id))
        date = cursor.fetchone()
        # cursor.execute('SELECT website_url  from User where ID = ' + str(id))
        # websiteurl = cursor.fetchone()
        # cursor.execute('SELECT profile_image_url  from User where ID = ' + str(id))
        # profile = cursor.fetchone()
        # cursor.execute('SELECT About_me  from User where ID = ' + str(id))
        # about=cursor.fetchone()
        detail=cursor.execute('SELECT * from User where ID = ' + str(id))
        detail=cursor.fetchone()
        if date:
            date = date[0]
            d = date.day
            mth = date.month
            ye = date.year
            # print(profile[0])
            date = str(d) + "/" + str(mth) + "/"+ str(ye)
        else:
            date=""
        cursor.close()
        conn.close()
        return (date,detail)


def editDisplayname(id,name):
    conn = requestConnection()
    cursor = requestCursor(conn)
    p=cursor.execute('Update User set Display_Name='+str(name)+' where Id= '+str('id'))
    conn.commit()
    cursor.close()
    conn.close()
    return "Done"

def editAboutme(id,name):
    conn = requestConnection()
    cursor = requestCursor(conn)
    p=cursor.execute('Update User set About_me="'+str(name)+'" where Id= '+str(id))
    conn.commit()
    cursor.close()
    conn.close()
    return "Done"

def list_of_user_date(page,date,upvote,downvote,reputation):
    conn = requestConnection()
    cursor = requestCursor(conn)
    offset=(page-1)*30
    if date:
        p=cursor.execute('select * from User order by Creation_Date limit 30 offset '+str(offset))
        p=cursor.fetchall()
    elif upvote:
        p=cursor.execute('select * from User order by up_votes limit 30 offset '+str(offset))
        p=cursor.fetchall()
    elif downvote:
        p=cursor.execute('select * from User order by down_votes limit 30 offset '+str(offset))
        p=cursor.fetchall()
    else:
        p=cursor.execute('select * from User order by reputation limit 30 offset '+str(offset))
        p=cursor.fetchall()
    cursor.close()
    conn.close()
    return list(p)