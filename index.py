import os
from wakepy import keepawake

with keepawake(keep_screen_awake=False):
    
    #User input URL
    url = str(input("Enter url of the stream you want to download (live or archived), press enter to start download: \n"))
    
    print("\nThis window will close automatically when the download is complete\n")

    command = str('yt-dlp.exe -S "ext,res,proto" "' + url + '" --live-from-start --no-playlist --cookies-from-browser opera:"C:\\Users\\Alex\\AppData\\Roaming\\Opera Software\\Opera GX Stable" --wait-for-video 30 --downloader aria2c -N 400 -R 30')

    print(command + "\n")

    os.system(command)
