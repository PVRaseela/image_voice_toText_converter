# Importing necessary modules required
from re import T
import speech_recognition as sr
# from googletrans import Translator
from gtts import gTTS
import os


# Creating Recogniser() class object
recog1 = sr.Recognizer()

# Creating microphone instance
mc = sr.Microphone()


# Capture Voice
with mc as source:
    print("Speak 'hello' to initiate the Translation !")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    recog1.adjust_for_ambient_noise(source, duration=0.5)
    audio = recog1.listen(source)
    MyText = recog1.recognize_google(audio)
    MyText = MyText.lower()

# Here initialising the recorder with
# hello, whatever after that hello it
# will recognise it.
if 'hello' in MyText:

    lang= 'en'

    with mc as source:

        print("Speak Now...")
        recog1.adjust_for_ambient_noise(source, duration=0.5)

        # Storing the speech into audio variable
        audio = recog1.listen(source)

        # Using recognize_google() method to
        # convert audio into text
        get_sentence = recog1.recognize_google(audio, language=lang,)


        print(get_sentence)

        speak = gTTS(text=get_sentence, lang=lang, slow=False, tld='co.in')
        f = open("captured_text.txt", "w", encoding="utf_8")
        f.write(get_sentence+'\n')
        f.close()

       

    