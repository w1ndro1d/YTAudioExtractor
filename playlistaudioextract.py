try:
    import os,errno,shutil
    from pytube import YouTube
    from pytube import Playlist
    from moviepy.editor import *
except Exception as e:
    print("Some Modules are missing.",format(e))

vidlink= input("Enter URL of the playlist: ") #this vidlink is used in YouTube function

playlist=Playlist(vidlink)
count=len(playlist.video_urls) #get number of videos in the playlist. just for info nothing else
print(count,"songs found in the playlist!")

try:
    os.mkdir("MyPlaylist") #containter for all downloaded mp3s
    for vidlink in playlist.video_urls:
        ytobj= YouTube(vidlink).streams.first().download() #YouTube object to download video
        head,tail=os.path.split(ytobj) #splitting pathname and filename of the ytobj
        mp4_file=tail #tail gives just the filename excluding path while head gives pathname excluding the filename
        mp3_file=str(ytobj.title()+".mp3") #save downloaded audio as titlename.mp3
        VideoClip=VideoFileClip(mp4_file) #specify the downloaded mp4 as VideoClip
        AudioClip=VideoClip.audio #specify AudioClip as audio file, extracting audio from VideoClip. MAIN WORKING LINE

        print("Extracted audio stream from", ytobj)

        AudioClip.write_audiofile(mp3_file) #using the filename, create mp3 from AudioClip
        AudioClip.close()
        VideoClip.close()
        os.remove(mp4_file) #No need of downloaded mp4 file

        source_dir = os.getcwd() #current working directory path
        target_dir = "MyPlaylist" #to move audio clip to MyPlaylist, set target directory
        file_names = os.listdir(source_dir) #list all contents of working directory
        for file_name in file_names:
            if file_name.endswith('.mp3'): #only when it is a .mp3
                shutil.move(os.path.join(source_dir, file_name), target_dir) #move .mp3s to MyPlaylist

    print("Successfully extracted audio from all videos!")

except OSError as e1:
    if e1.errno == errno.EEXIST:
        print('You already have an existing playlist. Remove the folder "MyPlaylist" and retry.')

except Exception as e2:
    print("Audio couldn't be downloaded.",format(e2))


