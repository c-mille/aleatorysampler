
"""
#librairies
import speech_recognition
import pyttsx3


recognizer=speech_recognition.Recognizer()

while True:
    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambiant_noise(mic,duration=0.2)
            audio=recognizer.listen(mic)
            text=recognizer.recognize_google(audio, language = 'pt', show_all=True)
            text=text.lower()
            print(f"Recognized {text}")


    except :
        print("pas reconnue")
       
        continue

"""
"""
#speech recognition un peu nul
    
import speech_recognition as sr
import pyttsx3


r = sr.Recognizer()


with sr.Microphone() as source:
    print("parler ici")
    audio=r.listen(source)
    try:
        text=r.recognize_google(audio, language = "fr-FR" )
        print(f'Tu dis {text}')


    except:
        print("non identifié")


#voice recorder

import pyaudio 
import wave

audio=pyaudio.PyAudio()
stream=audio.open(format=pyaudio.paInt16, channels=1, rate=44100,input=True,frames_per_buffer=1024)
frames=[]
try:
    while True:
        data=stream.read(1024)
        frames.append(data)
except KeyboardInterrupt:
    pass

stream.stop_stream()
stream.close()
audio.terminate()
sound_file=wave.open("myrecording.wav","wb")
sound_file.setnchannels(1)
sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
sound_file.setframerate(44100)
sound_file.writeframes(b''.join(frames))
sound_file.close()

#comment maitriser la durée du rec?

"""

import random
import pygame
from pygame import mixer
from pygame.locals import *
import simpleaudio as sa
import numpy as np
import wave
import pyaudio



#voice recorder avec la durée
import pyaudio, wave, sys

def rec_sample(numero_rec,temp_rec):
    CHUNK = 8192
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    RECORD_SECONDS = temp_rec

    WAVE_OUTPUT_FILENAME = 'MonRec'+str(numero_rec)+'.wav'
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                channels = CHANNELS,
                rate = RATE,
                input = True,
                input_device_index = 0,
                frames_per_buffer = CHUNK)

    print("* Ca enregistre")

    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("* Terminé")

    stream.stop_stream()
    stream.close()
    p.terminate()


    #wf wave open

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()



rec_sample(1,2)

rec_sample(2,2)

rec_sample(3,2)



pygame.init()
screen = pygame.display.set_mode((640, 480))
playlist = ['MonRec3.wav','MonRec2.wav','MonRec1.wav']
pygame.mixer.init()
continuer = 1

#définir le temps du changement ?


while continuer:
     
    if pygame.mixer.music.get_busy() != True:
        pygame.mixer.music.load(random.choice(playlist))
            # Jouer avec le volume de la musique
        pygame.mixer.music.set_volume(random.uniform(0, 1)) 

        #génère un nombre entre 0 et 1, ex: 0.65552568842

        pygame.mixer.music.play(0,0,2000)


   

        #pygame.mixer.music.fadeout(2000)


         
    for event in pygame.event.get():     
        if event.type == QUIT:
            continuer = 0 


    

              
pygame.quit()



