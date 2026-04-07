
from jnius import autoclass
import vosk

# Initialize Vosk model
model = vosk.Model("model")
recognizer = vosk.KaldiRecognizer(model, 16000)

# Initialize Android AudioRecord
AudioRecord = autoclass('android.media.AudioRecord')
BUFFER_SIZE = 4000
audio_record = AudioRecord(1, 16000, 16, 1, BUFFER_SIZE)
audio_record.startRecording()

# Initialize pyttsx3 for text-to-speech
engine = autoclass('android.speech.tts.TextToSpeech')
engine.init()

# Define speak function
def speak(command):
    engine.speak(command, 1, None)

# Define commands function
def commands():
    try:
        # Read audio data from microphone
        data = audio_record.read(BUFFER_SIZE)
        
        # Recognize speech
        if recognizer.AcceptWaveform(data):
            my_text = recognizer.Result()
            my_text = my_text.lower()
            print(my_text)
            
            # Play song
            if 'play' in my_text:
                my_text = my_text.replace('play', '')
                speak('Playing ' + my_text)
                pywhatkit.playonyt(my_text)
                
            # Get information
            elif 'what is' in my_text:
                information = my_text.replace('what is', '')
                info = wikipedia.summary(information,2)
                speak(info)
                
            # Get information about person
            elif 'tell about' in my_text:
                person = my_text.replace('tell about', '')
                info = wikipedia.summary(person,2)
                speak(info)
               #date
            elif 'date' in my_text:
                today = datetime.date.today()
                speak(today)

            #time
            elif 'time' in my_text:
                timenow = datetime.datetime.now().strftime('%H:%M')
                speak(timenow)

            else:
                speak('Please ask correct question...')    


    except:
        print('Error in capturing microphone...')
        

while True:
    commands()