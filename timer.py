import time
import datetime
import random
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def time_remaining(target):
    now = datetime.datetime.now()
    delta = target - now
    days = delta.days
    hours, remainder = divmod(delta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return days, hours, minutes, seconds


def number_guessing_game():
    print("\nMINI-GAME: Guess the number between 1 and 10!")
    number = random.randint(1, 10)
    attempts = 3
    while attempts > 0:
        try:
            guess = int(input("Your guess: "))
            if guess == number:
                print("Correct! You win!")
                return
            elif guess < number:
                print("Too low!")
            else:
                print("Too high!")
            attempts -= 1
            print(f"Attempts left: {attempts}")
        except ValueError:
            print("Please enter a number.")
    print(f"Out of attempts! The number was {number}")

def reaction_time_game():
    print("\nREACTION MINI-GAME: Press ENTER as fast as you can after 'GO'!")
    input("Press ENTER to start...")
    time.sleep(random.uniform(1, 5))
    start = time.time()
    input("GO! Press ENTER now!")
    reaction = time.time() - start
    print(".2f")


def countdown_timer():
    target = datetime.datetime(2026, 1, 1, 0, 0, 0)
    game_count = 0

    print("*** New Year 2026 Countdown Timer ***")
    print("Get ready for 2026! With mini-games to keep you entertained.\n")

    while True:
        days, hours, minutes, seconds = time_remaining(target)

        if days < 0 or (days == 0 and hours == 0 and minutes == 0 and seconds <= 0):
            print("\n*** HAPPY NEW YEAR 2026! ***")
            print("Wishing you a fantastic year ahead! - Yrashka ^^")
            break

        clear_screen()
        print("*** New Year 2026 Countdown Timer ***")
        print("Get ready for 2026! With mini-games to keep you entertained.\n")
        print("┌─────────────────────────────────────┐")
        print("│                                     │")
        print("│          DAYS    HOURS   MINUTES    │")
        print("│                                     │")
        print("│                                     │")
        print("└─────────────────────────────────────┘")
        print(f"         {days:>3}      {hours:>2}       {minutes:>2}        ")
        print("┌─────────────────────────────────────┐")
        print("│                                     │")
        print("│                                     │")
        print("│                                     │")
        print("│                                     │")
        print("└─────────────────────────────────────┘")
        print(f"              SECONDS                 ")
        print(f"                {seconds:>2}                   ")
        print("\nPress Ctrl+C to exit or wait for mini-games...")

    
        if seconds % 10 == 0 and seconds != 0 and game_count < 3:
            print("\nWould you like to play a mini-game? (y/n)")
            try:
                choice = input().strip().lower()
                if choice == 'y':
                    game = random.choice([number_guessing_game, reaction_time_game])
                    game()
                    game_count += 1
                    input("Press ENTER to continue countdown...")
            except KeyboardInterrupt:
                break

        time.sleep(1)

if __name__ == "__main__":
    try:
        countdown_timer()
    except KeyboardInterrupt:
        print("\n\nCountdown interrupted. Happy New Year!")
