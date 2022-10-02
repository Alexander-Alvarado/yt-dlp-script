import os

url = str(input("Enter url of the stream you want to download (live or archived), press enter to start download: \n"))

command = str('yt-dlp.exe ' + url)

print(command + "\n")

os.system(command)