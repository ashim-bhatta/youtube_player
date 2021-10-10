import sys
import subprocess
from youtubesearchpython import ChannelsSearch
from tabulate import tabulate
import requests
import scrapetube

def main():
    print("Search for video:")
    chanel_name = input()
    channels_search = ChannelsSearch(chanel_name, limit = 20)

    chanel_result = channels_search.result().get("result")
    tabulate_table = []
    headers = ['S.N', "Chanel Name", "Subscribers"]
    chanel_count = 1
    for chanel in chanel_result:
        table = [chanel_count, chanel.get("title"), chanel.get("subscribers")]
        tabulate_table.append(table)
        chanel_count = chanel_count + 1

    print(tabulate(tabulate_table, headers, tablefmt="orgtbl"))

    print("____________________________________________________________________")

    print("Please, Enter the index of chanel.")

    user_selected_chanel_number = int(input()) - 1
    selected_chanel = chanel_result[user_selected_chanel_number]
    print(f'{selected_chanel.get("title")} is selected.')

    chanel_url = f"{selected_chanel.get('link')}/videos"
    videos =  get_chanel_videos(selected_chanel.get("id"))
    print("Enter 0 for audio only and 1 for video")
    user_format_choice = int(input())
    isVideo = True
    if user_format_choice == 0:
        isVideo = False
    print("Playing...")
    for video in videos:
        play_video(video['videoId'], isVideo)




def get_chanel_videos(url):
    return  scrapetube.get_channel(url)
    
    

def play_video(videoId, isVideo):
    # url = f"mpv --no-video https://www.youtube.com/watch?v={videoId}"
    # if isVideo:
    #     url = f"mpv https://www.youtube.com/watch?v={videoId}"
    # subprocess.call(url, shell=True)
    if sys.platform.startswith('linux'):
        cmd = []
        cmd.append("mpv")
        if not isVideo:
            cmd.append(' --no-video')
        cmd.append(f"https://www.youtube.com/watch?v={videoId}")
        subprocess.call(cmd)

    elif sys.platform.startswith('win32'):
        cmd = ""
        cmd= cmd + "mpv"
        if not isVideo:
            cmd=cmd+' --no-video'
        cmd= cmd + f" https://www.youtube.com/watch?v={videoId}"
        subprocess.call(cmd, shell=True)



if __name__ == "__main__":
  main()
