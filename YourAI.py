# This Python Project is created by James Esparrago
# This is an open source project you can modify it if you want
# Simple thanks is very much welcome

import speech_recognition as sr
import pyttsx3
import openai

openai.api_key = "" # Insert your Open AI API here

# initialize recognizer and engine
r = sr.Recognizer()
#use of voice, set property and all
def using_voice(response):
  engine = pyttsx3.init()
  ru_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
  engine.setProperty('rate', 150)    # Speed percent (can go over 100)
  engine.setProperty('volume', 1)
  voice = engine.getProperty('voices')
  engine.setProperty('voice', ru_voice_id)  # Volume 0-1
  engine.say(response)
  engine.runAndWait()

#generate response from openai
def response_user(prompt):
  response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens = 2000,
    stop=None,
    temperature=0.5,
  )
  return response["choices"][0]["text"]
#using the microphone as source of the input
def listening():
  with sr.Microphone() as source:
      
      print("Speak now....")
      using_voice("I'm listening...")
      audio_text = r.listen(source)
      # recognize speech using Google Speech Recognition
      try:
          text = r.recognize_google(audio_text)
          print("Audio Text: " + text)
          text = text.lower()
          return text
      except sr.UnknownValueError:
          print("Google Speech Recognition could not understand audio")
      except sr.RequestError as e:
          print("Could not request results from Google Speech Recognition service; {0}".format(e))
          text = ''
def greeting_user():
  using_voice("Hi Name, What can i do for you?")

print("Hi Name, What can i do for you?")
greeting_user()

while True:
  command = listening()
  response = response_user(command)
  print(response)
  using_voice(response)