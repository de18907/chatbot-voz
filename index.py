#Importar librerías
import pygame
import pyworld as pw
from gtts import gTTS
from tempfile import TemporaryFile
from pygame import mixer

tts = gTTS(text='Hola. ¿Cómo estás?', lang='es')
ficheroMP3='tts.mp3'
tts.save(ficheroMP3)

mixer.init()
mixer.music.load(ficheroMP3)
print("Reproduciendo {0}".format(ficheroMP3))
mixer.music.play()
while mixer.music.get_busy(): 
    pygame.time.Clock().tick(10)
mixer.quit()