import schedule
import time
from plyer import notification

def send_notification():
    notification.notify(
        title="Take A Break!!!",
        message="Your 35 minutes are up. Time to stretch!",
        timeout=10
    )

# Schedule the notification to run every 35 minutes
schedule.every(10).minutes.do(send_notification)

while True:
    schedule.run_pending()
    time.sleep(2)