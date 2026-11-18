from pynput.keyboard import Controller
import time
import random

keyboard = Controller()

# Contagem regressiva
print("Você tem 5 segundos para clicar no campo de texto do SITE...")
for i in range(5, 0, -1):
    print(f"{i}...")
    time.sleep(1)

# Texto formatado corretamente com r""" e fechado com """
texto = r"""TEXTOAQUI."""

# Digitação caractere por caractere
for char in texto:
    keyboard.type(char)
    time.sleep(random.uniform(0.03, 0.07))
