from pygame import mixer
from datetime import datetime
from time import time

def music_on_loop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()

    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 1800
    eyessecs = 2700
    exercisesecs = 3600

    while True:
        if time() - init_water > watersecs:
            print("Water Drinking time. Enter 'drank' to stop the alarm.")
            music_on_loop("water.mp3", "drank")
            init_water = time()
            log_now("Drank water at:")

        if time() - init_eyes > eyessecs:
            print("Eyes rest time. Enter 'done' to stop the alarm.")
            music_on_loop("eyes.mp3", "done")
            init_eyes = time()
            log_now("Eyes rest at:")

        if time() - init_exercise > exercisesecs:
            print("Physical exercise time. Enter 'done' to stop the alarm.")
            music_on_loop("exercise.mp3", "done")
            init_exercise = time()
            log_now("Exercise done at:")