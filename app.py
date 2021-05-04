#!/usr/bin/env python3
import praw
import os
import sys
import argparse
import random
import json
from dotenv import load_dotenv

load_dotenv()

reddit = praw.Reddit(
    username=os.getenv('REDDIT_USERNAME'),
    password=os.getenv('REDDIT_PASSWORD'),
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent="reddit-autopost (https://github.com/ThalusA/reddit-autopost)"
)

nsfw_mode = os.getenv('NSFW_MODE')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("json", "json help")
    args = parser.parse_args()
    with open(args.json, "r") as f:
        data = json.load(f)
        for subreddit, info in data.items():
            subreddit = reddit.subreddit(subreddit.lstrip("r/"))
            titles = info.get('titles')
            titles = titles if isinstance(titles, str) else random.choice(titles)
            attachments = info.get('attachments')
            attachments = attachments if isinstance(attachments, str) else random.choice(attachments)
            subreddit.submit_image(title=titles, image_path=attachments, nsfw=nsfw_mode)