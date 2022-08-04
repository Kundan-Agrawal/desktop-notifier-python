
from gtts import gTTS
import os

mytext = 'hello test one for the good benifits'

language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("welcome.mp3")

os.system("welcome.mp3")
