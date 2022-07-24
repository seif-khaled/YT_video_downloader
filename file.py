from asyncio import streams
from fileinput import filename
# from mysqlx import Column
# from curses import window
from pytube import YouTube
import tkinter as tk
import sys
import os.path
from os import path
import tkinter.font as tkFont



class interface:
    def __init__(self,wid,hei):
        self.width=wid
        self.height=hei
        self.window=tk.Tk()
        self.stringvar1=tk.StringVar(self.window)
        self.stringvar2=tk.StringVar(self.window)
        self.stringvar3=tk.StringVar(self.window)
        self.stringvar4=tk.StringVar(self.window)

        # self.background=tk.PhotoImage(file="hexagons-patterns-red-background-red-blocks-black-blocks-3d-3840x2160-2276.png")
        # self.text=tk.Text(self.window,height=6).
        self.window.geometry(str(wid)+"x"+str(hei))
        # canvas1 = Canvas( root, width = self.width,height = self.height)
        self.window.title("Video Downloader Pro Max")
        self.drawing_labels()
        self.window.mainloop()
    def drawing_labels(self):

        self.label1 = tk.Label(text="Resolution",width=8,font=("Arial", 25)).grid(row=0,column=0)
        self.label2 = tk.Label(text="File path",width=8,font=("Arial", 25)).grid(row=1,column=0)
        self.label3 = tk.Label(text="File Name",width=8,font=("Arial", 25)).grid(row=2,column=0)
        self.label4 = tk.Label(text="URL",width=8,font=("Arial", 25)).grid(row=3,column=0)
        self.entry1 = tk.Entry(width=40,font=("Arial", 25),textvariable=self.stringvar1).grid(row=0,column=1)
        self.entry2 = tk.Entry(width=40,font=("Arial", 25),textvariable=self.stringvar2).grid(row=1,column=1)
        self.entry3 = tk.Entry(width=40,font=("Arial", 25),textvariable=self.stringvar3).grid(row=2,column=1)
        self.entry4 = tk.Entry(width=40,font=("Arial", 25),textvariable=self.stringvar4).grid(row=3,column=1)
        self.button1=tk.Button(text="Click me!",width=10,height=5,command=self.assign_variable1).grid(row=0,column=2,pady=10)
        self.button2=tk.Button(text="Click me!",width=10,height=5,command=self.assign_variable2).grid(row=1,column=2,pady=10)
        self.button3=tk.Button(text="Click me!",width=10,height=5,command=self.assign_variable3).grid(row=2,column=2,pady=10)
        self.button4=tk.Button(text="Click me!",width=10,height=5,command=self.assign_variable4).grid(row=3,column=2,pady=10)
        self.button5=tk.Button(text="Download",width=50,height=7,command=self.download_video).grid(row=4,column=1,pady=10)
        # self.get_textvar1=lambda:self.stringvar1.get()
        # self.get_textvar2=lambda:self.stringvar2.get()s
        # self.get_textvar3=lambda:self.stringvar3.get()
        # self.get_textvar4=lambda:self.stringvar4.get()
        self.resolution=None
        self.File_path=None
        self.File_Name=None
        self.URL=None
        # self.yt=None
    def assign_variable1(self):
        self.resolution=self.stringvar1.get()
        if(self.resolution not in ["144p","240p","360p","480p","720p"]):
            sys.exit()

    def assign_variable2(self):
        try:
            path.isdir(self.stringvar2.get())
            self.File_path=self.stringvar2.get()
        except:
            sys.exit()
    
    def assign_variable3(self):
        self.File_Name=self.stringvar3.get()
    def assign_variable4(self):
        try:
            self.URL=self.stringvar4.get()
        except:
            sys.exit()
    def download_video(self):
        try:
            self.yt=YouTube(self.URL)
            self.x=self.yt.streams
            self.y=self.x.filter(res=self.resolution,progressive=True,file_extension="mp4")
            if(len(self.y)>0):
                self.y=self.x.filter(res=self.resolution,progressive=True,file_extension="mp4").first().download(self.File_path,filename=self.File_Name)
            else:
                sys.exit()
        except:
            sys.exit()

    #    for i in x:
    #         for j in str(i.split()):
    #             print(j)
    
# print(help(filter))

# print(c.donwload_video())
# print(tk.TkVersion)
width=1920
height=1080
i=interface(width,height)
# x=["" for i in range(5)]
# print(x)