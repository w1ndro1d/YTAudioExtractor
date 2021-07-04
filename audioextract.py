try:
    import os
    from pytube import YouTube
    from pytube import Playlist
    from moviepy.editor import *
except Exception as e:
    print("Some Modules are missing.",format(e))

vidlink= input("Enter URL of the video: ") #this vidlink is used in YouTube function

try:
    ytobj= YouTube(vidlink).streams.first().download() #YouTube object to download video
    head,tail=os.path.split(ytobj) #splitting pathname and filename of the ytobj
    mp4_file=tail #tail gives just the filename excluding path while head gives pathname excluding the filename
    mp3_file=str(ytobj.title()+".mp3") #save downloaded audio as titlename.mp3
    VideoClip=VideoFileClip(mp4_file) #specify the downloaded mp4 as VideoClip
    AudioClip=VideoClip.audio #specify AudioClip as audio file, extracting audio from VideoClip. MAIN WORKING LINE
    AudioClip.write_audiofile(mp3_file) #using the filename, create mp3 from AudioClip
    AudioClip.close()
    VideoClip.close()
    os.remove(mp4_file) #No need of downloaded mp4 file
    print ("Success! Your downloaded audio has been saved as",ytobj)
except Exception as e1:
    print("Audio couldn't be downloaded.",format(e1))


