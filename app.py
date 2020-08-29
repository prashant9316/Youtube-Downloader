from pytube import YouTube, Playlist
import time
playlist = False

def intro():
    print("Welcome to Youtube Video Downloader!!")
    time.sleep(0.5)
    print("I am here to download youtube videos for you!")
    print("")
    time.sleep(0.5)
    print("press 1 if you want to download a youtube video")
    print("press 2 if you want to download a playlist!")
    time.sleep(1)
    error = True
    while(error):
        choice = input("Enter your choice: ")
        if int(choice) == 2:
            playlist = True
            error = False
            return 2
            print("Playlist selected!")
        elif int(choice) != 1:
            print("invalid choice")
        else:
            error = False
            return 1
            print("Single youtube video selected!")



def print_info():
    print(" ")
    print(" ")
    print("-------------------------------------------------------------------------------")
    print("----------------------             INFO               -------------------------")
    print("-------------------------------------------------------------------------------")
    print("There are two types of video streaming services used by youTube: ")
    print("Progressive and Dashed")
    print("1. Progressive: the video and audio are combined in a single file.")
    print("----- progressive are used for low quality file i.e., 360p and sometimes 720p")
    print("")
    print("2. Dashed: Separate Video and Audio files for high quality streaming")
    print("----- this app will automatically combine these two files for you!!")
    print("Created by Prashant Mishra ")
    print("-------------------------------------------------------------------------------")
    print("-------------------------------------------------------------------------------")
    choice = input("Enter 1 or 2 depending upon video stream type: ")
    return int(choice)

def input_url(playlist):
    if playlist == 2:
        video_link = input("Enter a youtube playlist URL: ")
    else:
        video_link = input("Enter a youtube video URL: ")

    return video_link

def print_video_details(yt_obj):
    print("Youtube Video/Playlist Details of the URL: ")
    print(" ")
    print("Title: ", yt_obj.title)
    print("Video Length: ", yt_obj.length/60, " minutes")
    print("Description: ", yt_obj.description)
    print("Rating: ", yt_obj.rating)

def init():

    # Introduction of our chatbot
    choice = intro()
    print(choice)

    # Inputting the URL from the user
    video_link = input_url(playlist)

    # Creating an object to access the video url


    # Showing the user some information regarding download options
    if choice == 1:

        yt_obj = YouTube(video_link)
        time.sleep(1)

        # Printing the details of the video
        print_video_details(yt_obj)

        choice = print_info()

        if choice == 1:
            filters = yt_obj.streams.filter(progressive = True)
            print("Fetching all the available progressive streams: ")
            time.sleep(1)
            for filter in filters:
                print(filter)
                print("")

            output_path = input("Enter output Path: ")
            filename = input("Enter filename: ")

            input("Press Enter to start downloading ...")
            print("Downloading the highest quality of the available Progressive video!! ")
            # download the highest quality video
            filters.get_highest_resolution().download(output_path = output_path, filename=filename)
            print('Video Downloaded Successfully')

        elif choice == 2:
            print("Fetching all the available dashed streams: ")
            filters = yt_obj.streams.filter(progressive = False)
            time.sleep(2)
            for filter in filters:
                print(filter)
                print("")

            video_tag = input("Select a video stream, Enter the itag: ")
            audio_tag = input("Select a audio stream, Enter the itag: ")

            output_path = input("Enter output Path: ")
            filename = input("Enter filename: ")
            if filename is None:
                filename = 'video_1'

            video_download = yt_obj.streams.get_by_itag(video_tag)
            audio_download = yt_obj.streams.get_by_itag(audio_tag)

            print("Donwloading separate Video and Audio files: ")
            video_download.download(output_path = output_path, filename = "video"+filename)
            audio_download.download(output_path = output_path, filename = "audio"+filename)
            print("completed downloading!!")
            time.sleep(1)
            print("time to combine both the files together!!")


            print("Development Not completed!")
        else:
            print("Wrong Input")

    else:
        print("Playlist downloader not completed!")


init()