from django.shortcuts import render
from django.contrib.auth.models import User
from pytube import YouTube
from django.http import FileResponse
from io import BytesIO
import os
import datetime
import requests
import json

URL = None
year = datetime.datetime.now()
buffer = BytesIO()
def Index(request):
    if request.method == 'POST':
        URL = request.POST["URL"]
        ext = request.POST.getlist('extention')
        if ext ==['mp3']:
            print('start downloading audio!')
            yt = YouTube(URL)
            video = yt.streams.filter(only_audio=True).first()
            video.stream_to_buffer(buffer)
            buffer.seek(0)
            filename = video.title + '.mp3'
            return FileResponse(
                buffer,
                filename = filename,
                as_attachment=True,
                content_type="audio/mp3"
               )
        else:
            print('vedio hd downloading wait .....')
            video = YouTube(URL).streams.get_highest_resolution()
            video.stream_to_buffer(buffer)
            buffer.seek(0)
            filename = video.title + '.mp4'
            return FileResponse(
                buffer,
                filename = filename,
                as_attachment=True,
                content_type="video/mp4"
               )
               
              

     

    response = render(request, 'index.html',{"year":year.year})
    response.set_cookie('Vedio','YouTube')
    response.set_cookie('date', datetime.datetime.now())
    return response



def entry_not_found(request, exception, template_name='404.html'):
    return render(request, template_name)

