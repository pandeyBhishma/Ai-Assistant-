import speech_recognition as sr
import webbrowser
import pyaudio
import pyttsx3
import musicliberary

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcmd(txt):
    if 'open youtube' in txt.lower():
        webbrowser.open('https://youtube.com')
        # speak('opened youtube successfully!')

    elif 'open facebook' in txt.lower():
        webbrowser.open('https://facebook.com')
        # speak('opened facebook successfully!')

    elif 'open gpt' in txt.lower():
        webbrowser.open('https://chatgpt.com')
        # speak('opened chatgpt successfully!')

    elif 'open movies' in txt.lower():
        webbrowser.open('https://hdmovie2.bike')  
        # speak('opened hdmovie successfully!') 

    elif txt.lower().startswith('play'):
        song = txt.lower().split(' ')[1]
        link = musicliberary.music[song]  
        webbrowser.open(link)   
        # speak(f'played song {song} successfully')
    print(txt)

if __name__ == '__main__':
    # listining for wake word jarvis 
    speak('initializing william ....')
    while True:
        
        # recognize speech using google
        try:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listining...")
                audio = r.listen(source , timeout=3 , phrase_time_limit=2)

            print('recogniging...')
            word = r.recognize_google(audio)
            print(word)
            if (word.lower() == 'william'):
                speak('yes sir!')
                # listen for command
                with sr.Microphone() as source:
                    speak('Your command sir ')
                    print('Jarvis activated')
                    audio = r.listen(source)

                    command = r.recognize_google(audio)
                    processcmd(command)
 

        except Exception as e:
            print(e)