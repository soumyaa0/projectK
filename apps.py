import time

def alarm_clock():
    alarm_time = input("Set the alarm (HH:MM): ")
    print("Alarm is set. Waiting...")
    
    while True:
        current_time = time.strftime("%H:%M")
        if current_time == alarm_time:
            print("Alarm ringing! Time to wake up!")
            break
        time.sleep(60)  # Check every minute

alarm_clock()

