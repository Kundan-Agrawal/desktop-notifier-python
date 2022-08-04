
import time
from win10toast import ToastNotifier
from gtts import gTTS
import os


def textToVoice(text):

    mytext = text

    language = 'en'

    myobj = gTTS(text=mytext, lang=language, slow=False)

    myobj.save("welcome.mp3")

    os.system("welcome.mp3")


# input("Input Time in 24hr format(HH:MM:SS) to set reminder->")
remTime = ["17:47:00", "17:47:15", "17:47:30", "17:47:45"]
# input("Enter your message:>")
remMssg = ["'this is the first reminder of samar feeling good'", "'this is the second reminder of  samar feeling good",
           "this is the third reminder of  samar feeling good'", "this is the fourth reminder of  samar feeling good"]
for i in range(len(remTime)):
    while True:
        current_time = time.strftime("%H:%M:%S")

        if current_time == remTime[i]:
            print(current_time)
            break

    notify = ToastNotifier()
    notify.show_toast("Reminder", remMssg[i])
    textToVoice(remMssg[i])
