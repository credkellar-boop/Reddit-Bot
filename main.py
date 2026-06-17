from src.post_manager import broadcast_message

def main():
    print("=== Reddit-Bot (Omnichannel Orchestrator) ===")
    
    # 1. Simulate the Voice Input (We will replace this with SpeechRecognition later)
    print("\n[Simulating Voice Input...]")
    title = input("What is the title of your post? \n> ")
    content = input("What do you want the post to say? \n> ")
    
    # 2. Define your target communities (from your image)
    # NOTE: Always use 'test' to ensure your bot works without getting banned!
    targets = ["test"] 
    
    # 3. Hand the data to the manager
    broadcast_message(title, content, targets)

if __name__ == "__main__":
    main()
