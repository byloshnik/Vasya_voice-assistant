import time
import speech_recognition as sr
import pyttsx3
import os
from fuzzywuzzy import fuzz
def speak(what):
    print( what )
    print(os.system("say"+what))
    # speak_engine.say( what )
    # speak_engine.runAndWait()
    # speak_engine.stop()

opts = {
    "alias": ('вася','васечка','васюня','василий','василиса'),
    "tbr": ('скажи','расскажи','покажи','сколько','произнеси'),
    "calc": ('сколько будет','посчитай'),
    "load": ('открой','запусти','включи'),
    "cmds": {
        "ctime": ('текущее время','сейчас времени','который час'),
        "radio": ('включи музыку','воспроизведи радио','включи радио'),
        "stupid1": ('расскажи анекдот','рассмеши меня','ты знаешь анекдоты'),

    }
}
def callback(recognizer, audio):
    try:
        voice = recognizer.recognize_google(audio, language = "ru-RU").lower()
        print("[log] Распознано: " + voice)
        if voice.startswith(opts["alias"]):
            cmd = voice

            for x in opts['alias']:
                cmd = cmd.replace(x, "").strip()
            if cmd.startswith(opts["load"]):
                for x in opts['load']:
                    cmd = cmd.replace(x, "").strip()
                if cmd == 'калькулятор':
                    os.startfile("C:\\Users\\gusev\\OneDrive\\Рабочий стол\\Калькулятор")
            if cmd.startswith(opts["calc"]):
                for x in opts['calc']:
                    cmd = cmd.replace(x, "").strip()
                c=1
                a = ''
                b = ''
                oper = 1
                for i in cmd:
                    if oper != 1 and i!=' ':
                        b +=i
                    if c==2:
                        oper=i
                        c=3
                    if i == ' ' and c==1:
                        c=2
                    if c == 1:
                        a +=i
                if oper=='x':
                    result=int(a)*int(b)
                    print('ответ: ',str(result) )
                if oper=='/':
                    result=int(a)/int(b)
                    print('ответ: ',str(result) )
                if oper=='+':
                    result=int(a)+int(b)
                    print('ответ: ',str(result) )
                if oper=='-':
                    result=int(a)-int(b)
                    print('ответ: ',str(result) )
        # speak_engine.say('ответ: %s' %result )
        # speak_engine.runAndWait()
        # speak_engine.stop()
        speak('привет')
    except sr.UnknownValueError:
        print("[log] Голос не распознан!")
    except sr.RequestError as e:
        print("[log] Неизвестная ошибка, проверьте интернет!")

r = sr.Recognizer()
m = sr.Microphone(device_index = 1)

with m as source:
    r.adjust_for_ambient_noise(source)

speak_engine = pyttsx3.init()

voices = speak_engine.getProperty('voices')
speak_engine.setProperty('voice', voices[0].id)


speak("Добрый день, повелитель")
speak("Вася слушает")

stop_listening = r.listen_in_background(m, callback)
while True: time.sleep(0.1)