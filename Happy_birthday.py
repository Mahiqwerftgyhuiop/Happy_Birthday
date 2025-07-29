import time
import sys

def slow_print(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def happy_birthday(SRAVS="You"):
    print("\n🎉🎂🎈 Happy Birthday SRAVS 🎈🎂🎉\n")
    time.sleep(1)

    lyrics = [
        "Happy Birthday to You 🎵",
        "Happy Birthday to You 🎶",
        f"Happy Birthday dear {SRAVS} 🎂",
        "Happy Birthday to You! 🎉"
    ]

    for line in lyrics:
        slow_print(line, delay=0.07)
        time.sleep(0.5)

    print("\n🎊 Wishing you joy, success, and cake! 🎊")
    print("\n Have a Blast and Provide me the Blast")

# Customize the name here
happy_birthday("SRAVS")
