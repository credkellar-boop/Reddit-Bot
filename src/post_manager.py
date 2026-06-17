from src.platforms.reddit_client import post_to_reddit
from src.platforms.discord_client import post_to_discord
from src.platforms.telegram_client import post_to_telegram

def broadcast_omnichannel(title, content, reddit_targets):
    """Broadcasts content across Reddit, Discord, and Telegram."""
    results = []

    # 1. Post to Reddit
    for sub in reddit_targets:
        success, msg = post_to_reddit(sub, title, content)
        status = "✅" if success else "❌"
        results.append(f"{status} Reddit (r/{sub}): {msg}")

    # 2. Post to Discord
    d_success, d_msg = post_to_discord(title, content)
    d_status = "✅" if d_success else "❌"
    results.append(f"{d_status} Discord: {d_msg}")

    # 3. Post to Telegram
    t_success, t_msg = post_to_telegram(title, content)
    t_status = "✅" if t_success else "❌"
    results.append(f"{t_status} Telegram: {t_msg}")

    return results
