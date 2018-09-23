
# coding: utf-8

# In[4]:


#Author：Yuning Xie
#Professor: Osama
#Course: EC601


import tweepy #https://github.com/tweepy/tweepy
from tweepy import OAuthHandler
import json
import wget
import ffmpeg
import io
import os
from google.cloud import vision
from google.cloud.vision import types
import glob
import cv2

#Twitter API credentials
consumer_key = "input your keys"
consumer_secret = "input your keys"
access_key = "input your keys"
access_secret = "input your keys"

def get_all_tweets(screen_name):
    
    #Twitter only allows access to a users most recent 3240 tweets with this method
    
    #authorize twitter, initialize tweepy
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    
    #initialize a list to hold all the tweepy Tweets
    alltweets = []    
    
    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=10)
    
    #save most recent tweets
    alltweets.extend(new_tweets)
    
    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
    
    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        
        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=10,max_id=oldest)
        
        #save most recent tweets
        alltweets.extend(new_tweets)
        
        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        if(len(alltweets) > 15):
            break
        print ("...%s tweets downloaded so far" % (len(alltweets)))
       
    #write tweet objects to JSON
    file = open('tweet.json', 'w') 
    print ("Writing tweet objects to JSON please wait...")
    for status in alltweets:
        json.dump(status._json,file,sort_keys = True,indent = 4)
    
    #close the file
    print ("Done")
    file.close()
    
    #get images url
    media_files = set()
    for status in alltweets:
        media = status.entities.get('media',[])
        if(len(media) > 0):
            media_files.add(media[0]['media_url'])
            
    #download the images
    print("Downloading images please wait...")
    i = 1
    for media_file in media_files:
        wget.download(media_file,'image'+str(i)+'.jpg')
        i = i + 1
    
    #change images into video
    print("Changing images into video please wait...")
    os.system('ffmpeg -framerate 2 -i image%d.jpg -r 15 video.mp4')
    print("Done")
    
    #google vision analysis
    #Google API credentials
    print("Analysising the content please wait...")
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\\Users\\xieyn\Downloads\\My First Project-a6794e647960.json"
    client = vision.ImageAnnotatorClient()

    img_path = glob.glob('*.jpg') 
    i = 1
    for i in range(len(img_path)):
    # The name of the image file to annotate
        file_name = os.path.join(
            os.path.dirname('__file__'),
            img_path[i])

    # Loads the image into memory
        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()

        image = types.Image(content = content)

    # Performs label detection on the image file
        response = client.label_detection(image = image)
        labels = response.label_annotations

        print('Image Name:'+ img_path[i])

        print('Labels:')
        for label in labels:
            print(label.description)

        i = i + 1
    
if __name__ == '__main__':
    #pass in the username of the account you want to download
    get_all_tweets("@blakelively")

