from pytube import YouTube
import pyfiglet

print(pyfiglet.figlet_format("YT Downloader"))

print("=" * 15, "Silahkan Pilih Opsi Dari Downloader Dewan", "=" * 15)
print("""[1] Download Video\n[2] Download Audio\n\n""")

opsi = int(input("Masukkan Opsi Anda [1/2]: "))
if opsi == 1:
    link = input("Masukkan Link YouTube Yang Ingin Anda Download : ")
    youtube_a = YouTube(link)

    def yt():
        video = youtube_a.streams.all()
        vidd = list(enumerate(video))
        for x in vidd:
            print(x)

        resolusi = int(
            input("Masukkan resolusi video yang ingin anda download : "))
        video[resolusi].download()
        print("Download Telah Selesai")
    yt()

elif opsi == 2:
    link = input("Masukkan Link YouTube Yang Ingin Anda Download : ")
    youtube_a = YouTube(link)

    def audio():
        video = youtube_a.streams.filter(only_audio=True)
        vidd = list(enumerate(video))
        for x in vidd:
            print(x)

        resolusi = int(
            input("Masukkan ukuran video yang ingin anda download : "))
        video[resolusi].download()
        print("Download Telah Selesai")
    audio()
else:
    print("Maaf opsi Yang anda masukkan salah !")
