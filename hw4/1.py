from datetime import datetime, timedelta
from abc import ABC, abstractmethod

class SocialMedia(ABC):
    @abstractmethod
    def post(self, message):
        pass

class Youtube(SocialMedia):
    def __init__(self, followers):
        self.followers = followers

    def post(self, message):
        print(f"Публікація на YouTube: {message}")

class Facebook(SocialMedia):
    def __init__(self, followers):
        self.followers = followers

    def post(self, message):
        print(f"Публікація на Facebook: {message}")

class Twitter(SocialMedia):
    def __init__(self, followers):
        self.followers = followers

    def post(self, message):
        print(f"Публікація на Twitter: {message}")

def post_a_message(channel: SocialMedia, message: str):
    channel.post(message)

def process_schedule(posts, channels):
    for post in posts:
        message, timestamp = post
        for channel in channels:
            if timestamp <= datetime.now().timestamp():
                post_a_message(channel, message)

youtube = Youtube(1_000_000)
facebook = Facebook(5_000_000)
twitter = Twitter(2_000_000)

channels = [youtube, facebook, twitter]

posts = [
    ("Це повідомлення для YouTube", (datetime.now() + timedelta(minutes=1)).timestamp()),
    ("Це повідомлення для Facebook", (datetime.now() + timedelta(minutes=2)).timestamp()),
    ("Це повідомлення для Twitter", (datetime.now() + timedelta(minutes=3)).timestamp()),
]

process_schedule(posts, channels)
