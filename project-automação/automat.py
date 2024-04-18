import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

wikipedia.set_lang('pt')

try:
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    for voice in voices:
        if 'portuguese' in voice.languages:
            engine.setProperty('voice', voice.id)
            break
except ModuleNotFoundError:
    print("Error: pyttsx3 requires the 'setuptools' package to be installed.")
    exit(1)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    """
    12:00 - noon
    1:00 pm - morning / 13:00 - afternoon
    18:00 - evening
    """
    if hour >= 0 and hour <= 12:
        speak('Bom dia meu querido amigo')
    elif hour >= 12 and hour <= 18:
        speak("Boa tarde meu querido amigo")
    else:
        speak("Boa noite meu querido amigo")
    speak("Diga-me como o posso ajudar, o que procura?")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('estou te ouvindo, Pedro')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recohecendo sua voz")
        query = r.recognize_google(audio, language = 'pt-BR')
        print(f'Meu amigo, você disse: {query}\n')

    except Exception as e:
        print("Pedro, poderia repetir, por favor? ...")
        speak("Pedro, poderia repetir, por favor? ...")
        return 'None'
    
    return query

#def sendEmail(to, content):
#    server = smtplib.SMTP('smtp.gmail.com', 178)
#    server.ehlo()
#    server.starttls()
#    server.login('blabla@gmail.com','codigo12334')
#    server.sendmail('taltal@gmail.com', to, content)
#    server.close()


if __name__ == '__main__':
    wishme()

    while True:
        query = takecommand().lower()
        if 'abrir wikipédia' in query:
            speak('Pesquisando wikipedia')
            query = query.replace('wikipedia', '')
            try:
                # Buscar títulos de páginas possíveis
                titles = wikipedia.search(query)
                if titles:
                    # Usar o primeiro título para obter o resumo
                    results = wikipedia.summary(titles[0], sentences = 2)
                    speak('De acordo com a wikipedia')
                    print(results)
                    speak(results)
                else:
                    speak('Desculpe, não consegui encontrar uma página da Wikipedia correspondente à sua consulta.')
            except Exception as e:
                speak('Desculpe, ocorreu um erro ao pesquisar na Wikipedia.')

        if 'abrir bloco de notas' in query:
            npath = 'C:\\Windows\\System32\\notepad.exe'
            os.startfile(npath)
        
        elif ' abrir paint' in query:
            npath = 'C:\\Windows\\System32\\mspaint.exe'
            os.startfile(npath)

        elif 'abrir youtube' in query:
            webbrowser.open('youtube.com')

        elif 'abrir google' in query:
            webbrowser.open('google.com')

        elif 'hora atual' in query:
            strtime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'Meu amigo, são exatas: {strtime}')

        elif 'abrir linkedin' in query:
            webbrowser.open('www.linkedin.com/in/pedrohalmeidadev')
