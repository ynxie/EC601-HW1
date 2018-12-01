
# coding: utf-8

# In[1]:


from EC601_Mini_Project_1 import *
import pymysql
import sys

def insert_user_info(user_name):
    db = pymysql.connect("127.0.0.1", "root", "xie,yuning.", "EC601")
    cursor = db.cursor()
    sql = "INSERT INTO user_info(user_name) VALUES(\'%s\')" % (user_name)
    last_user_id = 0
    try:
        cursor.execute(sql)
        last_user_id = cursor.lastrowid
        db.commit()
    except:
        db.rollback()
        print("error")
    finally: 
        db.close()
    return last_user_id        


# In[2]:


def insert_transaction(user_id,twitter_account,img_num,img_labels):
    db = pymysql.connect("127.0.0.1", "root", "xie,yuning.", "EC601")
    cursor = db.cursor()
    sql = "INSERT INTO transaction(user_id,twitter_account,img_num,img_labels) VALUES(\'%d\',\'%s\',\'%d\',\'%s\')" % (user_id,twitter_account,img_num,img_labels)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        print("error")
    finally: 
        db.close()


# In[6]:


def query_Labels(words):
    db = pymysql.connect("127.0.0.1", "root", "xie,yuning.", "EC601")
    cursor = db.cursor()
    sql = "SELECT * FROM transaction a join user_info b on a.user_id = b.user_id WHERE img_labels like '%s'" %('%'+words+'%')
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            user_id = row[1]
            twitter_account = row[2]
            user_name = row[6]
            print("user_id: '%s', user_name:'%s', twitter_account: '%s'" %                   (user_id, user_name, twitter_account))
    except:
        print("Error: unable to fetch data")
    finally: 
        db.close()


# In[7]:


def average_img_num():
    db = pymysql.connect("127.0.0.1", "root", "xie,yuning.", "EC601")
    cursor = db.cursor()
    sql = "SELECT avg(img_num) FROM transaction"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        print(results[0][0])
    except:
        print("Error: unable to fetch data")
    finally: 
        db.close()


# In[8]:


def most_popular_label():
    db = pymysql.connect("127.0.0.1", "root", "xie,yuning.", "EC601")
    cursor = db.cursor()
    sql = "SELECT img_labels FROM transaction"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        dic = {}
        for row in results:
            list = row[0].split(',')
            for word in list:
                if dic.get(word):
                    dic[word] += 1
                else:
                    dic[word] = 1
        print(sorted(dic.items(), key=lambda item:item[1], reverse = True)[0][0])
    except:
        print("Error: unable to fetch data")
    finally:
        db.close()


# In[10]:


if __name__ == '__main__':
    user_name = input("Please input a user name")
    last_user_id = insert_user_info(user_name)
    while(True):
        screen_name = input("Please input a twitter account")
        if screen_name == 'exit':
            print('end')
            sys.exit()
        elif screen_name == 'query':
            while(True):
                words = input("Please input a word you want to query")
                if words == 'exit':
                    print('end')
                    break
                else:
                    query_Labels(words)
        elif screen_name == 'statistics':
            while(True):
                a = input("If you want to count the number of images per feed, please enter Y, else enter N to get the most popular labels")
                if a == 'Y':
                    average_img_num()
                elif a == 'exit':
                    print('end')
                    break
                elif a == 'N':
                    most_popular_label()
        else:
            img_num = len(get_all_tweets(screen_name))
            if img_num == 0:
                print('Invalid twitter account or no picture in this twitter account')
            else:
                Label = analysis_content(screen_name)
                img_labels = ', '.join(Label)
                insert_transaction(last_user_id,screen_name,img_num,img_labels)

