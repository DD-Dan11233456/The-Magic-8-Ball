#Here is the python code for my maic 8 ball project


import random
import time
import sys

def magic_8_ball():
    responses = [
        "It is certain", "Reply hazy, try again", "Don't count on it",
        "It is decidedly so", "Ask again later", "My sources say no",
        "Without a doubt", "Better not tell you now", "Outlook not so good",
        "Yes definitely", "Cannot predict now", "Very doubtful",
        "You may rely on it", "Concentrate and ask again", "Signs point to yes",
        "As I see it, yes", "Most likely", "Outlook good", "Yes"
    ]

    # 1. User Input
    input("Ask the Magic 8-Ball a question: ")
    print("\nSHAKING THE BALL...")

    # 2. The "Spinning" Animation
    # We use \r (carriage return) to keep overwriting the same line
    spinner = ["|", "/", "-", "\\"]
    for _ in range(3): # Shake for 3 cycles
        for char in spinner:
            sys.stdout.write(f"\r  [{char}]  *Spinning* [{char}]")
            sys.stdout.flush()
            time.sleep(0.1)
    
    # 3. The "Settling" Animation (Slows down)
    print("\n\nSettling...")
    time.sleep(1)
    
    # 4. Reveal the Answer
    answer = random.choice(responses)
    
    print("-" * 30)
    print(f"THE 8-BALL SAYS: \033[1;34m{answer}\033[0m") # Added blue color
    print("-" * 30)

if __name__ == "__main__":
    while True:
        magic_8_ball()
        play_again = input("\nWant to ask another? (y/n): ").lower()
        if play_again != 'y':
            print("Goodbye!")
            break
