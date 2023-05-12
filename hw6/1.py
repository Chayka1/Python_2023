import multiprocessing
import threading
import time
import requests


def encrypt_file(path: str):
    _ = [i for i in range(100_000_000)]


def download_image(image_url):
    print(f"Downloading image from {image_url} in thread {threading.current_thread().name}")
    response = requests.get(image_url)
    with open("image.jpg", "wb") as f:
        f.write(response.content)


if __name__ == "__main__":
    try:
        encrypt_file("rockyou.txt")
        download_image("https://picsum.photos/1000/1000")

        encryption_process = multiprocessing.Process(target=encrypt_file, args=("rockyou.txt",))
        download_thread = threading.Thread(target=download_image, args=("https://picsum.photos/1000/1000",))

        start_encrypt_file = time.perf_counter()
        encryption_process.start()
        encryption_process.join()
        end_time_encrypt_file = time.perf_counter() - start_encrypt_file

        start_download_image = time.perf_counter()
        download_thread.start()
        download_thread.join()
        end_time_download_image = time.perf_counter() - start_download_image
        
        total = end_time_download_image + end_time_encrypt_file
        
        print(f"\nTime taken for encryption task: {end_time_encrypt_file:.4f}, I/O-bound task: {end_time_download_image:.4f}, Total: {total:.4f} seconds")
    except Exception as e:
        print(f"Error occurred: {e}")