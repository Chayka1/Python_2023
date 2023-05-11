import os
import threading
import time
import requests

# CPU-bound task (heavy computation)
def encrypt_file(path: str):
    start_time = time.perf_counter()
    print(f"Processing image from {image_url} in process {os.getpid()}")
    # Simulate heavy computation by sleeping for a while
    _ = [i for i in range(100_000_000)]
    end_time = time.perf_counter()
    print(f"{end_time - start_time:.4f} секунд")

# I/O-bound task (downloading image from URL)
def download_image(image_url):
    start_time = time.perf_counter()
    print(f"Downloading image from {image_url} in thread {threading.current_thread().name}")
    response = requests.get(image_url)
    with open("image.jpg", "wb") as f:
        f.write(response.content)
    end_time = time.perf_counter()
    print(f"{end_time - start_time:.4f} секунд")

try:
    encrypt_file("rockyou.txt")
    download_image("https://picsum.photos/1000/1000")
    print(f"Time taken for encryption task: {encryption_counter}, I/O-bound task: {download_counter}, Total: {total} seconds")
except Exception as e:
    print(f"Error occurred: {e}")
