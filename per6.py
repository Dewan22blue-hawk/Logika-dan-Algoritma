
from pytube import YouTube
"""for a in range(2, 9):
    a = a+1
    print(a)"""

# ask for the link from user
link = input("Masukkan tautan/link video YouTube yang ingin anda unduh :  ")
yt = YouTube(link)

# Showing details dengan menggunakan 
print("Title: ", yt.title)
print("Number of views: ", yt.views)
print("Length of video: ", yt.length)
print("Rating of video: ", yt.rating)
# Getting the highest resolution possible
ys = yt.streams.get_highest_resolution()

# Starting download
print("Mendownload...")
ys.download()
print("Download Selesai!!")
