import schedule
import time

def remind(habit_name):
    print(f"🔔 Reminder: Complete your habit — {habit_name}!")

def schedule_habit(habit_name, time_str):
    schedule.every().day.at(time_str).do(remind, habit_name)

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(60)
