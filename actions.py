import pyautogui
import time
import random


def port_fight():
    while True:
        try:
            port_fight = pyautogui.locateOnScreen(
                image='images/port_fight.png')
            x, y = pyautogui.center(port_fight)

            pyautogui.click(x=x+random.randint(-60, 60), y=y +
                            random.randint(-40, 40), clicks=1, button='left')
            pyautogui.moveTo(1850, 340)
            time.sleep(random.uniform(1, 3))
            break
        except:
            print("port_fight not found")
            time.sleep(1)


def fight():
    while True:
        try:
            fight = pyautogui.locateOnScreen(image='images/fight.png')
            x, y = pyautogui.center(fight)

            pyautogui.click(x=x+random.randint(-110, 110), y=y +
                            random.randint(-200, 50), clicks=1, button='left')
            pyautogui.moveTo(1850, 340)
            time.sleep(random.uniform(1, 3))
            break
        except:
            print("fight not found")
            time.sleep(1)


def back():
    while True:
        try:
            back = pyautogui.locateOnScreen(image='images/back.png')
            x, y = pyautogui.center(back)

            pyautogui.click(x=x+random.randint(-60, 60), y=y +
                            random.randint(-50, 50), clicks=1, button='left')
            pyautogui.moveTo(1850, 340)
            time.sleep(random.uniform(1, 3))
            break
        except:
            print("back not found")
            time.sleep(1)


def check():
    while True:
        try:
            check = pyautogui.locateOnScreen(image='images/check.png')
            x, y = pyautogui.center(check)

            pyautogui.click(x=x+random.randint(-7, 7), y=y +
                            random.randint(-7, 7), clicks=1, button='left')
            pyautogui.moveTo(1850, 340)
            time.sleep(random.uniform(1, 3))
            break
        except:
            print("check not found")
            time.sleep(1)


def compass():
    while True:
        try:
            compass = pyautogui.locateOnScreen(image='images/compass.png')
            x, y = pyautogui.center(compass)

            pyautogui.click(x=630+random.randint(-500, 500), y=540 +
                            random.randint(-300, 300), clicks=1, button='left')
            pyautogui.moveTo(1850, 340)
            time.sleep(random.uniform(1, 3))
            break
        except:
            print("compass not found")
            time.sleep(1)


def confirm():
    while True:
        try:
            confirm = pyautogui.locateOnScreen(image='images/confirm.png')
            x, y = pyautogui.center(confirm)

            pyautogui.click(x=x+random.randint(-150, 150), y=y +
                            random.randint(-30, 30), clicks=1, button='left')
            pyautogui.moveTo(1850, 340)
            time.sleep(random.uniform(1, 3))
            break
        except:
            print("confirm not found")
            time.sleep(1)


def formation_1():
    while True:
        try:
            formation_1 = pyautogui.locateOnScreen(
                image='images/formation_1.png')
            x, y = pyautogui.center(formation_1)

            pyautogui.click(x=x+random.randint(-70, 70), y=y +
                            random.randint(-15, 15), clicks=1, button='left')
            pyautogui.moveTo(1850, 340)
            time.sleep(random.uniform(1, 3))
            break
        except:
            print("formation_1 not found")
            time.sleep(1)


def map_5():
    while True:
        try:
            map_5 = pyautogui.locateOnScreen(image='images/map_5.png')
            x, y = pyautogui.center(map_5)

            pyautogui.click(x=x+random.randint(-35, 35), y=y +
                            random.randint(-15, 15), clicks=1, button='left')
            pyautogui.moveTo(1850, 340)
            time.sleep(random.uniform(1, 3))
            break
        except:
            print("map_5 not found")
            time.sleep(1)


def map_X_2():
    while True:
        try:
            x, y = 920, 450

            pyautogui.click(x=x+random.randint(-130, 130), y=y +
                            random.randint(-90, 90), clicks=1, button='left')
            pyautogui.moveTo(1850, 340)
            time.sleep(random.uniform(1, 3))
            break
        except:
            print("map_X_2 not found")
            time.sleep(1)


def port():
    while True:
        try:
            port = pyautogui.locateOnScreen(image='images/port.png')
            x, y = pyautogui.center(port)

            pyautogui.click(x=x+random.randint(-25, 25), y=y +
                            random.randint(-55, 55), clicks=1, button='left')
            pyautogui.moveTo(1850, 340)
            time.sleep(random.uniform(1, 3))
            break
        except:
            print("port not found")
            time.sleep(1)


def startfight():
    while True:
        try:
            startfight = pyautogui.locateOnScreen(
                image='images/startfight.png')
            x, y = pyautogui.center(startfight)

            pyautogui.click(x=x+random.randint(-120, 120), y=y +
                            random.randint(-20, 20), clicks=1, button='left')
            pyautogui.moveTo(1850, 340)
            time.sleep(random.uniform(1, 3))
            break
        except:
            print("startfight not found")
            time.sleep(1)


def port_supply():
    while True:
        try:
            supply = pyautogui.locateOnScreen(image='images/port_supply.png')
            x, y = pyautogui.center(supply)

            pyautogui.click(x=x+random.randint(-45, 45), y=y +
                            random.randint(-35, 35), clicks=1, button='left')
            pyautogui.moveTo(1850, 340)
            time.sleep(random.uniform(1, 3))
            break
        except:
            print("port_supply not found")
            time.sleep(1)


def next():
    while True:
        try:
            next = pyautogui.locateOnScreen(image='images/next.png')
            x, y = pyautogui.center(next)

            pyautogui.click(x=630+random.randint(-500, 500), y=540 +
                            random.randint(-300, 300), clicks=1, button='left')
            pyautogui.moveTo(1850, 340)
            time.sleep(random.uniform(1, 3))
            break
        except:
            print("next not found")
            time.sleep(1)

def next_ss():
    while True:
        try:
            next = pyautogui.locateOnScreen(image='images/next_ss.png')
            x, y = pyautogui.center(next)

            pyautogui.click(x=630+random.randint(-500, 500), y=540 +
                            random.randint(-300, 300), clicks=1, button='left')
            pyautogui.moveTo(1850, 340)
            time.sleep(random.uniform(1, 3))
            break
        except:
            print("next_ss not found")
            time.sleep(1)

def report():
    #pyautogui.click(x=800, y=600, clicks=1, button='left')
    #time.sleep(random.uniform(4, 5))
    while True:
        try:
            report = pyautogui.locateOnScreen(image='images/report.png')
            x, y = pyautogui.center(report)

            pyautogui.click(x=630+random.randint(-500, 500), y=540 +
                            random.randint(-300, 300), clicks=1, button='left')
            pyautogui.moveTo(1850, 340)
            time.sleep(random.uniform(4, 5))
            break
        except:
            print("report not found")
            # time.sleep(1)
