import speech_recognition as sr
import os

# Função para ouvir e reconhecer a fala
def ouvir_microfone():
    # Inicializa o Recognizer
    microfone = sr.Recognizer()

    # Utilizando o microfone
    with sr.Microphone() as source:
        # Chama o algoritmo de redução de ruídos do som
        microfone.adjust_for_ambient_noise(source)

        # Pede para o usuário dizer alguma coisa
        print("Diga alguma coisa... ")

        # Armazena o que foi dito em uma variável
        audio = microfone.listen(source)

    try:
        # Passa a variável para o algoritmo reconhecedor de padrões
        frase = microfone.recognize_google(audio, language='pt-BR')

        if "navegador" in frase:
            os.system("start chrome.exe")
            return False
        elif "Excel" in frase:
            os.system("start excel.exe")
        
        print("Você disse: " + frase)

    except sr.UnknownValueError:
        print("Não entendi o que foi dito")
    except sr.RequestError:
        print("Não foi possível fazer a solicitação ao serviço de reconhecimento de fala")

# Chama a função para ouvir o microfone
ouvir_microfone()


