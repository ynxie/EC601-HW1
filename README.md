# EC601-HW1
# Definition of the exercise
Build a library (preferable in python) that downloads images from a twitter feed, convert them to a video and describe the content of the images in the video.
# Main process of the exercise
1.Twitter API to access the twitter content  
2.FFMPEG to convert images to videos  
3.Google Vision analysis to describe the content
# Pre-preparation for running the code
1.Install Tweepy (pip install tweepy)  
2.Install FFMpeg (Because I run the code on windows, we need to change the environment variables.)  
3.Install Wget (pip install wget)  
4.Get your API credentials from here: https://developer.twitter.com/en/docs/developer-utilities  
5.Install google cloud for python(pip install google-cloud-vision)  
6.Get your Google Vision API Credentials from here: https://cloud.google.com/vision/docs/auth
# About the results
You will get images named image.jpg which downloaded from twitter account you choose, and a video named video.mp4 from these original images. Also, you will get new images with tags on them named new_image.jpg and a video named new_video.mp4.
