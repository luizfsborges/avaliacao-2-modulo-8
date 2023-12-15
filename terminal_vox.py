from gtts import gTTS
from pygame import mixer
from time import sleep

mixer.init(buffer=512)

def vox_maker(text, lang='pt-br'):
    tts = gTTS(text=text, lang=lang)
    audio_file = "temp_vox.mp3"
    tts.save(audio_file)
    return 

def vox_talk(file_path):
    audio_object = mixer.Sound(file_path)
    audio_duration = audio_object.get_length()
    audio_object.play()
    sleep(audio_duration)
    return

def main():
    print("\n TERMINAL VOX: Sistema de conversão de texto em vox")
    print("\n Para sair, digite 'sair'")
    vox_maker("Terminal Vox inicializado com sucesso!")
    vox_talk("temp_vox.mp3")

    scripta_manent = ""
    while scripta_manent != "sair":
        scripta_manent = input("\nFalar: ")
        vox_maker(scripta_manent)
        vox_talk("temp_vox.mp3")

    print("\nPrograma encerrado.")
    

if __name__ == "__main__":
    main()