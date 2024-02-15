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
    music_list = ["https://aac.saavncdn.com/713/fc91c79b27d14206d9f9f08b2a289519_160.mp4",
                  "https://aac.saavncdn.com/591/0e32e462747a3b7b4378e5ef972bc3bd_96.mp4","https://aac.saavncdn.com/896/ad19c4a75775ccdef32905de23fc10c5_96.mp4"]
    with ThreadPoolExecutor(max_workers=3) as e:
            for i in music_list:
                filename = str(input(f"Enter the file name for {i} = \n"))
                e.submit(download,i,filename)
                time.sleep(1)
