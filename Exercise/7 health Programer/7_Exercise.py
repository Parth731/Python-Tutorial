
#healthy programer
# 9am - 5pm (total 17.5glass== 3500mil, 1glass == 200mil)
#
# water => water.mp3 => (3.5 litres) - drank - log time
# eyes    => eye.mp3   -> every 30min EyDone - log time
# physical activity => physical.mp3  every 45min - exDone - log

# rules
# pygame module to play audio


from pygame import mixer
from datetime import datetime
from time import time

import time as t


def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    mixer.music.rewind()
    while True:
        a = input().lower()
        if a == stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open("mylogs.txt","a") as fop:
        fop.write(f"{msg}: {datetime.now()}\n")
        print(f"{msg}: {datetime.now()}")




def IsOfficeTime(currenttime):
    if currenttime > '09:00:00' and currenttime < '19:00:01':
        return True
    else:
        return False

if __name__ == '__main__':
    # musiconloop("water.mp3","stop")

    input_name = input("Please input your name:")
    print(f"{input_name.capitalize()} welecome to the office")
    print(t.asctime(t.localtime()))

    init_water = time()
    print("water :", t.strftime("%H:%M:%S"))
    init_eyes = time()
    print("eye :", t.strftime("%H:%M:%S"))
    init_Exercise = time()
    print("exercise :", t.strftime("%H:%M:%S"))

    currenttime = t.strftime("%H:%M:%S")
    print(currenttime)
    NumberofWaterRemaining = 18
    SleepTime = 60
    watersecs = 40*60
    exercisesecs = 30*60
    eyesecs = 45*60

    while IsOfficeTime(currenttime):

        # print("Punching done")

        if NumberofWaterRemaining > 0:
            if time() - init_water > watersecs:
                print("water Drinking Time. Enter 'done' to stop the alarm.")
                while True:
                    musiconloop('water.mp3','done')
                    init_water = time()
                    log_now("Drank water Done At :")
                    NumberofWaterRemaining -= 1
                    print("Number of Water Remaining",NumberofWaterRemaining)
                    break

        elif time() - init_eyes > eyesecs:
            print("Eye exercise Time. Enter 'done' to stop the alarm.")
            while True:
                musiconloop('eyes.mp3','done')
                init_eyes = time()
                log_now("eyes Relaxed Done At :")
                break

        elif time() - init_Exercise > exercisesecs:
            print("Physical activity Time. Enter 'done' to stop the alarm.")
            while True:
                musiconloop('physical.mp3','done')
                init_Exercise = time()
                log_now("Physical activity Done At :")
                break

        currenttime = t.strftime('%H:%M:%S')
        if currenttime == '19:00:00':
            break

    # t.sleep(SleepTime)
    currenttime = t.strftime('%H:%M:%S')
    print("You can go to home, now time is :", end=" ")
    print(currenttime)
