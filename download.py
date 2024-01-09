from pytube import YouTube

def main():
    link = input('Enter YouTube Video URL ')
    yt = YouTube(link)
    yt.streams.get_highest_resolution().download()
    print('Downloaded')

if __name__ == "__main__":
    main()