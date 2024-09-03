from pathlib import Path
import requests
import threading
import multiprocessing
import asyncio
import time
import os
import argparse

fin_async = 0.0
fin_thread = 0.0
fin_multiproc = 0.0

data_images = []
with open('images.txt', 'r') as img:
    for i in img.readlines():
        data_images.append(i.strip())


image_path = Path('images')

def download_img(url):
    start_time = time.time()
    response = requests.get(url, stream=True)
    filename = image_path.joinpath(os.path.basename(url))
    with open (filename, 'wb') as f:
        for ch in response.iter_content(chunk_size=1024):
            if ch:
                f.write(ch)
    end_time = time.time() - start_time
    print(f"Загрузка {filename} завершена за {end_time:.2f} секунд")



def download_img_thread(urls):
    start_time = time.time()
    threads = []
    for url in urls:
        t = threading.Thread(target=download_img, args=(url, ))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    end_time = time.time() - start_time
    print(f"Загрузка {urls} завершена за {end_time:.2f} секунд")


def download_img_multiproc(urls):
    start_time = time.time()
    processes = []
    for url in urls:
        p = multiprocessing.Process(target=download_img, args=(url, ))
        p.start()
        processes.append(p)
    for p in processes:
        p.join()
    end_time = time.time() - start_time
    print(f"Загрузка {urls} завершена за {end_time:.2f} секунд")

async def download_im_async(url):
    start_time = time.time()
    response = await asyncio.get_event_loop().run_in_executor(None, requests.get, url, {'stream': True})
    filename = image_path.joinpath('async_' + os.path.basename(url))
    with open (filename, 'wb') as f:
        for ch in response.iter_content(chunk_size=1024):
            if ch:
                f.write(ch)
    end_time = time.time() - start_time
    print(f"Загрузка {filename} завершена за {end_time:.2f} секунд")


async def download_img_async(urls):
    start_time = time.time()
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(download_im_async(url))
        tasks.append(task)
    await asyncio.gather(*tasks)
    end_time = time.time() - start_time
    print(f"Загрузка {urls} завершена за {end_time:.2f} секунд")





if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Прасер изображений по url')
    parser.add_argument('--urls', nargs='+', help='Список URL для загрузки изображений')
    args = parser.parse_args()

    urls = args.urls
    if not urls:
        urls = data_images
    
    
    download_img_thread(urls)

    download_img_multiproc(urls)

    asyncio.run(download_img_async(urls))


    # python flask_lesson_4_homework.py --urls