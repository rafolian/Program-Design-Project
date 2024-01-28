# *********************************************************
# Program: playsound.py
# Course: PSP0101 PROBLEM SOLVING AND PROGRAM DESIGN
# Class: TL11-13
# Year: 2023/2024 Trimester 1
# Name: AMIRAH NAILOFAR BINTI MUHAMAD HAFIDZ
# ID: 1231102231
# Email: 1231102231@student.mmu.edu.my
# Phone: 011-1001-8080
# *********************************************************

# reference for use of sound using pygame: https://stackoverflow.com/questions/63449184/playing-sound-using-pygame-python
import pygame

# function to play sound
def music_play(sound_file):
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()

# function to stop sound
def music_stop():
    pygame.mixer.music.stop()
