import random

# Task 1: Your Mood Today
def mood_today():
    moods = ["Happy", "Sad", "Energetic", "Calm"]
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    print("Task 1: Your Mood Today\n")
    for i in range(len(days)):
        mood = random.choice(moods)
        print(f"On {days[i]}, you were feeling {mood.lower()}.")

# Task 2: Double Scoop with Nested Loops (Mood Tracker)
def mood_tracker():
    moods = ["Happy", "Sad", "Energetic", "Calm", "Tired", "Excited"]
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    times_of_day = ["morning", "afternoon", "evening"]

    print("\nTask 2: Double Scoop with Nested Loops\n")
    for day in days:
        for time in times_of_day:
            mood = random.choice(moods)
            print(f"On {day} {time} you were {mood.lower()}.")

if __name__ == "__main__":
    mood_today()
    mood_tracker()
