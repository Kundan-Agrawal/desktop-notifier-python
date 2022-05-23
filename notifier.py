import time
from win10toast import ToastNotifier

# input("Input Time in 24hr format(HH:MM:SS) to set reminder->")
remTime = ["14:03:00", "14:03:15", "14:03:30", "14:03:45"]
# input("Enter your message:>")
remMssg = ["test 1", "test 2", "test 3", "test 4"]
for i in range(len(remTime)):
    while True:
        current_time = time.strftime("%H:%M:%S")
        if current_time == remTime[i]:
            print(current_time)
            break

    notify = ToastNotifier()
    notify.show_toast("Reminder", remMssg[i])
