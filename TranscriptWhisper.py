import whisper
import PySimpleGUI as sg
import os
import subprocess

filePath = sg.popup_get_file("ファイルを選択してください",
  file_types = (("mp3 files", ".mp3"), ("mp4 files", ".mp4"))
)
print(filePath)

if(filePath != None) :
    fileName =  "OutTranscript.txt"
    file = open(fileName, mode='w', encoding='utf_8')

    model = whisper.load_model("tiny")
    #model = whisper.load_model("base")
    #model = whisper.load_model("small")
    #model = whisper.load_model("large")

    result = model.transcribe(filePath)
    #print(result["text"])
    file.write(result["text"])
    file.close()
    path = os.getcwd() + '\\' +fileName
    subprocess.Popen(["start", path], shell=True)