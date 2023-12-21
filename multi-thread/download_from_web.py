from concurrent.futures import ThreadPoolExecutor
import random
import threading
import requests
import time

def download(url, filename):
    response = requests.get(url=url, stream=True)
    length = int(response.headers.get('Content-Length'))
    print(length)
    if (response.headers.get('Content-Type') == 'image/jpeg'):
        download_helper(response,filename,'jpeg',length)
    elif (response.headers.get('Content-Type') == 'audio/mp4'):
        download_helper(response,filename,'mp3',length)

    else:
        download_helper(response,filename,'zip',length)


def download_helper(response,file_name,type,length):
    try:
        with open(f"{file_name}.{type}", 'wb') as file:
            for i in response.iter_content(chunk_size=1 * 1024 * 1024):
                dowloaded = ((length - len(i))/1024 ** 2)/100
                print("downloaded{%1.2f}"%dowloaded)
                file.write(i)
                time.sleep(0.1)
    except Exception as e:
        print("error")

    else:
        return True
    
    return False
    


if __name__ == '__main__':
    print("QAt maia")
    music_list = ["https://aac.saavncdn.com/355/5eed3326fb2aa459d06b5ce97f51f368_160.mp4"]
    with ThreadPoolExecutor(max_workers=3) as e:
            for i in music_list:
                filename = str(input(f"Enter the file name for {i} = \n"))
                e.submit(download,i,filename)
                time.sleep(1)
