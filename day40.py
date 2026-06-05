# Day 40 - YouTube Video Downloader

from pytube import YouTube

class YouTubeDownloader:

    def download_video(self, url):

        yt = YouTube(url)

        print(f"\nTitle: {yt.title}")
        print(f"Views: {yt.views}")

        stream = yt.streams.get_highest_resolution()

        print("\nDownloading...")

        stream.download()

        print("Download completed!")


def main():

    print("===== YOUTUBE VIDEO DOWNLOADER =====")

    url = input("Enter YouTube video URL: ")

    downloader = YouTubeDownloader()

    try:
        downloader.download_video(url)

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()