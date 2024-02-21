from django.shortcuts import render
from django.http import JsonResponse
from posts.models import InstaData, SearchedUser
from instaloader import Instaloader,Profile
import json
from datetime import datetime

import os

# Create your views here.
def home(request,name):
    
    try:
        queryset = SearchedUser.objects.get(userName=name)
    except SearchedUser.DoesNotExist:
        queryset = SearchedUser(userName=name)
        queryset.save()
    print(queryset.id)
    instaData = InstaData.objects.filter(related_model=queryset.id)
    data = list(instaData.values())
    getDataByUser(name)
    
    return JsonResponse(data, safe=False)



def getDataByUser(username):
   
    try:
        searchedUser = SearchedUser.objects.get(userName=username)
    except SearchedUser.DoesNotExist:
        searchedUser = SearchedUser(userName=username)
        searchedUser.save()
   


    L = Instaloader(compress_json=False)
    
    profile = Profile.from_username(L.context, username)	
    i=0
    for post in profile.get_posts():
        i = i+1
        print(f"i : {i}")
        filename = post.date_utc.strftime(f"{username} %Y-%m-%d %H:%M:%S")
        dateTimeOnly = post.date_utc.strftime("%Y-%m-%d %H:%M:%S")
        print(f"filename : {filename}")
        
        

        
        if post.is_video:
            L.download_post(post,target=filename)
            newFIleName = f"static/{filename}/{fileDateSet(dateTimeOnly)}_UTC.json"
            print(f"newFIleName : {newFIleName}")
            json_data = json_file_to_python(newFIleName)

            filesGet = getAllFiles(f"static/{filename}")

            
            print(f"filesGet : {filesGet}")

            try:
                instaAlreadyData = InstaData.objects.get(file_name=f"static/{filename}/")
            except InstaData.DoesNotExist:
                instaAlreadyData = InstaData(json_data=json_data)
                instaAlreadyData.related_model = searchedUser
                instaAlreadyData.file_name = f"static/{filename}/"
                instaAlreadyData.files_array = filesGet
                InstaData.save(instaAlreadyData)

            
        else:
            L.download_post(post,target=filename)

            newFIleName = f"static/{filename}/{fileDateSet(dateTimeOnly)}_UTC.json"
            print(f"newFIleName : {newFIleName}")
            json_data = json_file_to_python(newFIleName)

            filesGet = getAllFiles(f"static/{filename}")
            print(f"filesGet : {filesGet}")


            try:
                instaAlreadyData = InstaData.objects.get(file_name=f"static/{filename}/")
            except InstaData.DoesNotExist:
                instaAlreadyData = InstaData(json_data=json_data)
                instaAlreadyData.related_model = searchedUser
                instaAlreadyData.file_name = f"static/{filename}/"
                instaAlreadyData.files_array = filesGet
                InstaData.save(instaAlreadyData)
           


def json_file_to_python(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def fileDateSet(date):
    # Original datetime string
    original_datetime_string = date

    # Convert the string to a datetime object
    datetime_object = datetime.strptime(original_datetime_string, "%Y-%m-%d %H:%M:%S")

    # Format the datetime object to the desired format
    formatted_datetime_string = datetime_object.strftime("%Y-%m-%d_%H-%M-%S")

    return formatted_datetime_string


def getAllFiles(folder_path):
   

    # Get all filenames inside the folder
    filenames = os.listdir(folder_path)

    # Filter filenames to include only JPG and MP4 files
    jpg_files = [filename for filename in filenames if filename.lower().endswith('.jpg')]
    mp4_files = [filename for filename in filenames if filename.lower().endswith('.mp4')]


    merged_array = jpg_files + mp4_files
    
    return merged_array
    