# sjp-assistant

## Description

The module answers questions about the meaning of words. Information about the meaning of words is taken from the dictionary of the Polish language, and more precisely from the website sjp.pl. The module searches for and reads word definitions contained in the dictionary.

## Instalation

The Mosquitto broker must be installed and running for the program to work. Additionally, the following modules should be installed in the environment using pip: SpeechRecognition, Pyttsx3, paho-mqtt, pipwin, pyaudio, urllib, beautifulsoup4.

### Steps

    • Download and install Mosquitto (you can use the website: https://mosquitto.org/download/)
    • pip install SpeechRecognition
    • pip install pyttsx3
    • pip install paho-mqtt
    • pip install pipwin
    • pipwin install pyaudio
    • pip install urllib3
    • pip install beautifulsoup4
    
Note: It is important to start the Mosquitto broker first before running python files in terminals


## Run
  • Run Mosquitto applications in the background
  
  • Run programs in separate terminals: module.py, mic.py, spk.py
  
  • In the mic.py terminal, press the Enter key and ask the assistant
  
  • The program will read the answer and display it in the terminal meaning.py and spk.py
  
### This program only understands questions asked like: 

     'co oznacza {}', 'znaczenie słowa {} ', 'co znaczy słowo {}', 'jakie jest znaczenie słowa {}', 
     'co to {}', 'co znaczy {}', 'co oznacza słowo {}', 'jaki jest znaczenie słowa {}', 'kto to {}', 
     'kim jest {}','jakie znaczenie ma słowo {}','jakie znaczenie ma {}'
        
   where {} means the word that you are looking for meaning
   
   
   
## Usage examples

<img width="599" alt="Zrzut ekranu 2022-05-7 o 12 06 36" src="https://user-images.githubusercontent.com/92359411/167249664-db9d7b01-3883-48a1-850a-eb384c3ba939.png">
