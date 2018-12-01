# EC601-HW1
# Definition of the exercise
Build a library (preferable in python) that downloads images from a twitter feed, convert them to a video and describe the content of the images in the video.
# Main process of the exercise
* Twitter API to access the twitter content  
* FFMPEG to convert images to videos  
* Google Vision analysis to describe the content
# Pre-preparation for running the code
* Install Tweepy 
```
pip install tweepy
```
* Install FFMpeg (Because I run the code on windows, we need to change the environment variables.)  
* Install Wget 
```
pip install wget
``` 
* Get your API credentials from [here](https://developer.twitter.com/en/docs/developer-utilities)  
* Install google cloud for python```pip install google-cloud-vision```
* Get your Google Vision API Credentials from [here](https://cloud.google.com/vision/docs/auth)
# About the results
You will get images named image.jpg which downloaded from twitter account you choose, and a video named video.mp4 from these original images. Also, you will get new images with tags on them named new_image.jpg and a video named new_video.mp4.

# EC601-HW3
# Definition of the exercise
Go back to Project 1:  Twitter+FFMPEG+Google Vision  
Do two database implementations with MySQL and MongoDB  
The main requirements are:  
* Detail information of every transaction the user may run using your system  
* Store all relevant information for everytime a user uses your application  
* Add API and develop test program to search for certain words and retrieve which user/session that has this work in it.  For example, search for ‘basketball”, and get results of which user had Basketball in their sessions.  
* Collective statistics about overall usage of the system.  For example
  * number of images per feed  
  * most popular descriptors
# Pre-preparation for running the code
* Install mysql from [here](https://www.mysql.com/downloads/)
* Install pymysql
```
  pip install pymysql
```
* Install mongoDB from [here](https://www.mongodb.com/download-center/community?jmp=nav)
* Install pymongo
```
  pip install pymongo
```
