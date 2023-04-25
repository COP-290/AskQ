
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
from flask_paginate import Pagination, get_page_args
import MySQLdb
app=Flask(__name__)

def requestConnection():
    mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='root',
    db='askq')
    return mydb

def requestCursor(conn):
    return conn.cursor()

# def get_id_question(tag):
#     conn = requestConnection()
#     cursor = requestCursor(conn)
#     tags = '"' + tag + '"'
#     l = cursor.execute('SELECT ID FROM Tag where tags= ' + tags)
#     l = cursor.fetchall()
#     ans = []
#     for i in range(len(l)):
#         ans.append(l[i][0])
#     return ans


def questionTag_from_id(id): # list of tag from question id
    conn=requestConnection()
    cursor=requestCursor(conn)
    l=cursor.execute('SELECT tags FROM Tag where id = ' + str(id))
    l=cursor.fetchall()
    tag_list=[]
    for k in range(0,len(l)):
        tag_list.append(l[k][0])
    cursor.close()
    conn.close()
    return tag_list



def question_from_tag(tag,offset):
    Ans=[]
    conn=requestConnection()
    cursor=requestCursor(conn)
    tags = '"' + tag + '"'
    f = str(offset)
    a=cursor.execute('select ID from Tag where tags = '+ tags +' limit 3 offset '+ f  )
    a=cursor.fetchall()
    for i in range(len(a)):
        l=cursor.execute('SELECT * FROM Question where id = ' + str(a[i][0]))
        l=cursor.fetchall()
        m = cursor.execute('SELECT tags FROM Tag where id = ' + str(a[i][0]))
        m = cursor.fetchall()
        M = []
        for i in range(len(m)):
            M.append( m[i][0])
        L = list(l)
        L.append(M)
        Ans.append(L)  
    cursor.close()
    conn.close()        
    return Ans

# print(len(question_from_tag(".net",255)))
# a=((question_from_tag("mysql",0)))
# print(len(a))


def complete_question_with_taglist(l,n):
    ans=[]
    for i in range(0,n):
        a=l[i][0]
        b=questionTag_from_id(a)
        c=[]
        c.append(l[i])
        c.append(b)
        ans.append(c)
    return ans
# print(complete_question_with_taglist(a,3))

# Not able to do unit test for this
def question_page(val): # took care when question is less than 3 
    conn=requestConnection()
    cursor=requestCursor(conn)
    p=cursor.execute('SELECT count(ID) FROM Question') # This is not giving correct answer why?
    p=cursor.fetchall()
    total = (p[0][0])
    cursor.close()
    conn.close()
    return total



def question_page2(val,page): # took care when question is less than 3 
    conn=requestConnection()
    cursor=requestCursor(conn)
    per_page=3
    offset=(page-1)*per_page
    if val==0:
        l=cursor.execute('SELECT * FROM Question ORDER BY Creation_Date DESC limit 3 offset '+str(offset))
    elif val==1:
        l=cursor.execute('SELECT * FROM Question ORDER BY Score DESC limit 3 offset '+str(offset))
    l=cursor.fetchall()
    n=len(l)
    ans=complete_question_with_taglist(l,n)
    cursor.close()
    conn.close()
    # return (ans,n,page,3,pagination)
    return ans

# print(question_page(1))

def showQuestion_byscore_help(page):
    a=question_page2(1,page)
    return a

def sort_que_by_time(page):
    # b=question_page(0)
    b=question_page2(0,page)
    return b

def sort_que_by_time_number():
    # b=question_page(0)
    b=question_page(0)
    return b    
# print(question_page(1))
# # print(sort_que_by_time())
# if __name__=="__main__":
#     app.run(host='0.0.0.0',debug=True,port=7000)

def pagefunction(tag='flex'):
    conn = requestConnection()
    cursor = requestCursor(conn)
    page, per_page, offset = get_page_args(page_parameter='page',per_page_parameter='per_page')
    per_page=3
    offset=(page-1)*per_page
    l=question_from_tag(tag,offset)
    cursor.close()
    conn.close()
    return (l)

def pagefunction2(page,tag='flex'):
    per_page=3
    offset=(page-1)*per_page
    l=question_from_tag(tag,offset)
    return l

def pagefunction_number(tag='flex'):
    conn = requestConnection()
    cursor = requestCursor(conn)
    per_page=3
    page = 1
    offset=(page-1)*per_page
    tags='"'+tag+'"'
    p=cursor.execute('SELECT count(id) FROM Tag where tags='+str(tags))
    p=cursor.fetchall()
    total = (p[0][0])
    cursor.close()
    conn.close()
    return total

def pagefunction_number_all():
    conn = requestConnection()
    cursor = requestCursor(conn)
    per_page=3
    page = 1
    offset=(page-1)*per_page
    p=cursor.execute('SELECT count(id) FROM Tag')
    p=cursor.fetchall()
    total = (p[0][0])
    cursor.close()
    conn.close()
    return total



def  question_from_list_of_tag(taglist,page):
    conn = requestConnection()
    cursor = requestCursor(conn)
    idlist=[]
    offset=(page-1)*3
    for k in taglist:
       k='"'+k+'"'
       b=cursor.execute('select id from Tag where tags='+str(k))
       b=cursor.fetchall()
       idlist += [x[0] for x in b]
    ans=[]
    n=len(idlist)
    question_id_string = "("+','.join(map(str, idlist))+")"
    p=cursor.execute(f"""select * from Question where id in {question_id_string} limit 3 offset {offset}""")
    p=cursor.fetchall()
    ans.append(complete_question_with_taglist(p,len(p)))
    cursor.close()
    conn.close()
    return ans[0]

def  question_from_list_of_tag_number(taglist):
    conn = requestConnection()
    cursor = requestCursor(conn)
    idlist=[]
    for k in taglist:
       k='"'+k+'"'
       b=cursor.execute('select id from Tag where tags='+str(k))
       b=cursor.fetchall()
       idlist = [x[0] for x in b]
    ans=[]
    n=len(idlist)
    print(idlist[101:])
    return n

# print(question_from_list_of_tag_number([".net"]))

# we are getting a list and thus sort them by score 
def sort_quesbyTag(tag,page): # remember to add Tag list in the question
    # conn = requestConnection()
    # cursor = requestCursor(conn)
    # per_page=3
    # offset=(page-1)*per_page
    # tag='"'+tag+'"'
    # l=cursor.execute('SELECT Question.Id,Question.Owner_User_Id,Question.Creation_Date,Question.Score,Question.Title,Question.Body from Question inner join Tag where Tag.tags='+str(tag)+' and Question.Id=Tag.Id order by Score Desc limit 3 offset '+str(offset))
    # l=cursor.fetchall()
    # cursor.close()
    # conn.close()
    # ans=complete_question_with_taglist(l,len(l))
    # ans=question_from_list_of_tag([tag],page)
    offset=(page-1)*3
    ans=question_from_tag(tag,offset)
    return ans

# print(question_from_list_of_tag(["flex","c","python","javascript"],1))
# print(sort_quesbyTag('mysql',1))

