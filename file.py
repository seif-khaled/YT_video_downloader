from asyncio import streams
# from mysqlx import Column
# from curses import window
from pytube import YouTube
import tkinter as tk
import tkinter.font as tkFont
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
        # self.background=tk.PhotoImage(file="hexagons-patterns-red-background-red-blocks-black-blocks-3d-3840x2160-2276.png")
        # self.text=tk.Text(self.window,height=6).
        self.window.geometry(str(wid)+"x"+str(hei))
        # canvas1 = Canvas( root, width = self.width,height = self.height)
        self.window.title("Video Downloader Pro Max")
        self.label1 = tk.Label(text="Resolution",width=8,font=("Arial", 25)).grid(row=0,column=0)
        self.label2 = tk.Label(text="File path",width=8,font=("Arial", 25)).grid(row=1,column=0)
        self.label3 = tk.Label(text="File Name",width=8,font=("Arial", 25)).grid(row=2,column=0)
        self.label4 = tk.Label(text="URL",width=8,font=("Arial", 25)).grid(row=3,column=0)
        self.entry1 = tk.Entry(width=40,font=("Arial", 25)).grid(row=0,column=1)
        self.entry2 = tk.Entry(width=40,font=("Arial", 25)).grid(row=1,column=1)
        self.entry3 = tk.Entry(width=40,font=("Arial", 25)).grid(row=2,column=1)
        self.entry4 = tk.Entry(width=40,font=("Arial", 25)).grid(row=3,column=1)
        self.button1=tk.Button(text="Click me!",width=10,height=5).grid(row=0,column=2,pady=10)
        self.button2=tk.Button(text="Click me!",width=10,height=5).grid(row=1,column=2,pady=10)
        self.button3=tk.Button(text="Click me!",width=10,height=5).grid(row=2,column=2,pady=10)
        self.button4=tk.Button(text="Click me!",width=10,height=5).grid(row=3,column=2,pady=10)
        self.button5=tk.Button(text="Download",width=50,height=7).grid(row=4,column=1,pady=10)
        self.window.mainloop()
    #    for i in x:
    #         for j in str(i.split()):
    #             print(j)
    
# print(help(filter))
c=download_vidoes(youtube_url,SAVE_PATH,"720p")
# print(c.donwload_video())
# print(tk.TkVersion)
width=1280
height=720
i=interface(width,height)