import speech_recognition as sr
import os
from pydub import AudioSegment
import sys

def main():
     path = "C:\\RPA\\SolveReCaptcha\\Data"
     filePath="C:\\RPA\\SolveReCaptcha\\Data\\audio.wav"
     os.chdir(path)
     audio_files = os.listdir()
     name, ext = os.path.splitext(filePath)
     if ext == ".mp3":
          mp3_sound = AudioSegment.from_file(filePath)
          mp3_sound.export("{0}.wav".format(name), format="wav")


     r = sr.Recognizer()

     harvard_audio = sr.AudioFile(name+".wav")

     with harvard_audio as source:
          audio = r.record(source)

     try:
          #sys.stdout = open('stdout.txt', 'w') #-- 텍스트 저장시 사용
          text = r.recognize_google(audio)
          #sys.stdout.close() 
          return(text)

     except:
          return("Error")

