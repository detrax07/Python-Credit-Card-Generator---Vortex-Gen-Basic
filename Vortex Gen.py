import random
import pygame
import os 
import time 
import gratient 
import fade
from colorama import init, Fore, Back, Style 

pygame.mixer.init()

pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play()

os.system("title Vortex Card Generator - Basic Version by Detarx.")

caracters = ['1','2','3','4','5','6','7','8','9','0']

print(fade.purpleblue("""


    ▄   ████▄ █▄▄▄▄    ▄▄▄▄▀ ▄███▄      ▄      ▄█▄    ██   █▄▄▄▄ ██▄         ▄▀  ▄███▄      ▄   
     █  █   █ █  ▄▀ ▀▀▀ █    █▀   ▀ ▀▄   █     █▀ ▀▄  █ █  █  ▄▀ █  █      ▄▀    █▀   ▀      █  
█     █ █   █ █▀▀▌      █    ██▄▄     █ ▀      █   ▀  █▄▄█ █▀▀▌  █   █     █ ▀▄  ██▄▄    ██   █ 
 █    █ ▀████ █  █     █     █▄   ▄▀ ▄ █       █▄  ▄▀ █  █ █  █  █  █      █   █ █▄   ▄▀ █ █  █ 
  █  █          █     ▀      ▀███▀  █   ▀▄     ▀███▀     █   █   ███▀       ███  ▀███▀   █  █ █ 
   █▐          ▀                     ▀                  █   ▀                            █   ██ 
   ▐                                                   ▀                                        

b  y         d       e       t       r        a        x
                      
"""))

time.sleep(2)

print(gratient.purple("[@] This generator is only for education ! im not responsable of your actions "))
time.sleep(1)
print(gratient.purple("[@] This generator has been coded by https://github.com/detrax07 , all rights reserved."))
time.sleep(1)
print(gratient.purple("[@] This generator generate unchecked credit cards !"))
time.sleep(1)
print(gratient.purple("[@] This generator can not generate user name's card, please use a realistic one !"))
time.sleep(1)
print(gratient.purple("[@] Vortex Gen contains also a premium variant that can generate valid credit card for trial subscriptions."))
time.sleep(1)
print(gratient.purple("[@] Contact me on discord for the premium variant, or if u need any help: chahine07."))
time.sleep(1)
print(gratient.purple("[@] This code will be updated in 2030, Enjoy !"))


time.sleep(3)

while True:
        cardcode = ''.join(random.choice(caracters) for _ in range(16))
        ccv = ''.join(random.choice(caracters) for _ in range(3))

        init(autoreset=True)

        print(Fore.RED + f"[$] SUCCESSFULLY GENERATED | UNCHECKED :{cardcode} |3|2030 - {ccv}")

        with open("Vortex gen log.txt", "a+") as cardFile:

            cardFile.write(f"{cardcode} |3|2030 - {ccv}\n")

            cardFile.close()
