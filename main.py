from src.voice_input import listen_for_command
from src.voice_output import speak
from src.post_manager import broadcast_omnichannel

def main():
    print("=== Reddit-Bot (Omnichannel Voice Edition) ===")
    
    speak("Welcome to Reddit Bot. What is the title of your post?")
    title = listen_for_command()
    
    if not title:
        speak("I didn't catch that. Shutting down.")
        return

    speak("Got it. What do you want the body of the post to say?")
    content = listen_for_command()

    if not content:
        speak("I didn't hear the content. Shutting down.")
        return

    speak("Broadcasting your post across all platforms.")
    
    # Target subreddits (Keep to "test" until you are ready for real deployment)
    targets = ["test"]
    
    # Execute the cross-platform blast
    logs = broadcast_omnichannel(title, content, targets)
    
    # Print the logs to the terminal
    print("\n--- Broadcast Report ---")
    for log in logs:
        print(log)
        
    speak("Broadcast complete. Check your terminal for the detailed report.")

if __name__ == "__main__":
    main()
