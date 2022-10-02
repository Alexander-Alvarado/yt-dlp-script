import os

url = None #enter valid youtube video url here

command = str('yt-dlp.exe ' + url)

os.system(command)