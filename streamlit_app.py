
# # # # # #
# Imports #
# # # # # #

# Import streamlit
import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import speech_recognition as sr
import pyttsx3
import pyaudio
import nltk





st.set_page_config(
    page_title='(name not decided)',
)

st.title("(name not decided)")
st.caption('Sid Singh; Congressional App Challenge')
st.header('What does ____ do?')
st.markdown('The ____ is able to start up a conversation with the user and provide motivational support when needed.')


r = sr.Recognizer()


def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


n = 0
if n != 1:
    SpeakText("Enter your name.")
    name = str(input("What's your name? "))

SpeakText("Hello " + name)
print("How are you doing? ")
SpeakText("How are you doing?")
with sr.Microphone() as source2:
    r.adjust_for_ambient_noise(source2, duration=0)
    audio2 = r.listen(source2)
    MyText = r.recognize_google(audio2)
    MyText = MyText.lower()
print("You answered: " + MyText)

analyzer = SentimentIntensityAnalyzer()
sentence = MyText
vs = analyzer.polarity_scores(sentence)

print(vs['pos'])

if vs['pos'] >= 0.8:
    SpeakText("That's good to hear " + name + "!")
    print("That's good to hear " + name + "!")
elif vs['pos'] >= 0.5:
    SpeakText("Your day will get better " + name + "!")
elif vs['pos'] >= 0.25:
    SpeakText("Maybe you should go take some rest " + name + ".")
elif vs['pos'] >= 0.0:
    SpeakText("I am so sorry to hear that, your day will get better " + name + ", I promise!")


