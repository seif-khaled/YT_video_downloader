from pytube import YouTube


SAVE_PATH="D:/donwloaded_videos"


youtube_url="https://www.youtube.com/watch?v=JGulAZnnTKA"

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
       x= self.yt.streams.get_highest_resolution().download(self.savepath,filename=input("Enter file name (without extension): "))
       print(x)
    #    y=x.filter(res=self.reso,progressive=True,file_extension="mp4").first().download(self.savepath)
    #    print(y)
    #    for i in x:
    #         for j in str(i.split()):
    #             print(j)
    

c=download_vidoes(youtube_url,SAVE_PATH,"1080p")
print(c.donwload_video())