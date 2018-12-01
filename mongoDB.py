
# coding: utf-8

# In[19]:


from EC601_Mini_Project_1 import *
from pymongo import MongoClient
import sys
import re

def insert_user_info(user_name):
    conn = MongoClient('127.0.0.1', 27017)
    db = conn.EC601
    user_set = db.user_info
    user_set.insert_one({"user_id":user_set.find().count(), "user_name":user_name})
    conn.close()
    return user_set.find().count()


# In[20]:


def insert_transaction(user_id,user_name,twitter_account,img_num,img_labels):
    conn = MongoClient('127.0.0.1', 27017)
    db = conn.EC601
    transaction_set = db.transactions
    transaction_set.insert_one({"user_id":user_id,"user_name":user_name,"twitter_account":twitter_account,"img_num":img_num,"img_labels"
    :img_labels})
    conn.close()


# In[26]:


def query_Labels(words):
    conn = MongoClient('127.0.0.1', 27017)
    db = conn.EC601
    transaction_set = db.transactions
    my_set = transaction_set.find({'img_labels':re.compile(words)})
    for words in my_set:
        print("user_id: '%s', user_name:'%s', twitter_account: '%s'" %                 (words['user_id'], words['user_name'], words['twitter_account']))


# In[22]:


def most_popular_label():
    conn = MongoClient('127.0.0.1', 27017)
    db = conn.EC601
    transaction_set = db.transactions
    results = transaction_set.find()
    dic = {}
    for row in results:
        list = row['img_labels']
        for word in list:
            if dic.get(word):
                dic[word] += 1
            else:
                dic[word] = 1
    print(sorted(dic.items(), key=lambda item:item[1], reverse = True)[0][0])
    conn.close()


# In[27]:


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
                a = input("If you want to get the most popular labels, please enter Y")
                if a == 'Y':
                    most_popular_label()
                else:
                    print('end')
                    break
        else:
            img_num = len(get_all_tweets(screen_name))
            if img_num == 0:
                print('Invalid twitter account or no picture in this twitter account')
            else:
                Label = analysis_content(screen_name)
                insert_transaction(last_user_id,user_name,screen_name,img_num,Label)

