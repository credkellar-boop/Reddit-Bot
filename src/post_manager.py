from src.platforms.reddit_client import post_to_reddit
from src.platforms.discord_client import post_to_discord

def broadcast_message(title, content, subreddit_list):
    # 1. Post to the Reddit communities seen in image.png
    for sub in subreddit_list:
        try:
            post_to_reddit(sub, title, content)
            print(f"Successfully posted to r/{sub}")
        except Exception as e:
            print(f"Failed to post to r/{sub}: {e}")

    # 2. Simultaneously push the update to your Discord Community
    try:
        post_to_discord(title, content)
        print("Successfully posted to Discord")
    except Exception as e:
        print(f"Failed to post to Discord: {e}")
