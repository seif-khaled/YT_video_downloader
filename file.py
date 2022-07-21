from asyncio import streams
from curses import window
from pytube import YouTube
import tkinter as tk
SAVE_PATH="D:/donwloaded_videos"


youtube_url="https://www.youtube.com/watch?v=yoj2I6ZJLx8"

yt=YouTube(youtube_url)

class download_vidoes:
    def __init__(self,youtubelink,savepath,resolution):
        self.youtube_url= youtubelink
        self.savepath=savepath
        self.reso=resolution
        self.yt=YouTube(youtube_url)

    def get_title(self):
        return self.yt.title
    def donwload_video(self):
       x= self.yt.streams
    #    print(x)
       
       y=x.filter(res=self.reso,progressive=True,file_extension="mp4")
    #    .download(self.savepath,filename=input("Enter file name (without extension): "))
       if(len(y)>0):
            y=x.filter(res=self.reso,progressive=True,file_extension="mp4").first().download(self.savepath)
       else:
            return "couldnt find supported extension/file",x.filter(res=self.reso,progressive=True,file_extension="mp4")



class interface:
    def __init__(self,wid,hei):
        self.width=wid
        self.height=hei
        self.window=tk.Tk()
        self.window.geometry(str(wid)+"x"+str(hei))
        self.window.title("Video Downloader Pro Max")
        self.label = tk.Label(text="File path")
        self.entry = tk.Entry()
        self.window.mainloop()
    #    for i in x:
    #         for j in str(i.split()):
    #             print(j)
    
# print(help(filter))
c=download_vidoes(youtube_url,SAVE_PATH,"720p")
# print(c.donwload_video())
# print(tk.TkVersion)
i=