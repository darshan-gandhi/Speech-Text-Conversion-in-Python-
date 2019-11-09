import speech_recognition as sr
from gtts import gTTS
import playsound

r=sr.Recognizer()
mic=sr.Microphone()

with mic as source:
    r.adjust_for_ambient_noise (source)
    print("please speak")
    audio=r.listen(source)
    transcript=r.recognize_google(audio)
    print(transcript)

    language="en"

    myobj=gTTS(text=transcript,lang=language, slow=False)
    myobj.save("repeat.mp3")

    playsound.playsound('repeat.mp3')

