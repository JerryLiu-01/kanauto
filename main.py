import functions
import time
import os
from os import system
import win32gui
import win32con
import random


def wait(seed):
    t = -1
    if seed >= 0 and seed <= 6:
        t = random.uniform(2, 5)
        print("等待"+str(round(t, 2))+"秒")
        time.sleep(t)
    elif seed >= 7 and seed <= 8:
        t = random.uniform(5, 9)
        print("等待"+str(round(t, 2))+"秒")
        time.sleep(t)
    elif seed == 9:
        t = random.uniform(9, 20)
        print("等待"+str(round(t, 2))+"秒")
        time.sleep(t)


def menu():
    os.system('cls')
    while True:
        mode = -1
        print("K☆A☆N☆A☆U☆T☆O")
        print("")
        print("[1] 肝5-2（CV）")
        print("[2] 肝5-2（SS）")
        print("")
        mode = eval(input("请选择模式:"))

        if mode == 1:
            r = int(input("请输入出击次数:"))
            os.system('cls')
            functions.supply()
            print("补给完成")
            time.sleep(random.uniform(2, 9))
            s = random.randint(15, 17)  # 在出击s+1次后补给（ss2-4）
            print("第"+str(s+1)+"次出击完成后补给")
            for i in range(r):
                system("title 出击次数:%d/%d" % (i+1, r))
                functions.run_5_2()
                print("第"+str(i+1)+"次出击完成")
                wait(random.randint(0, 9))  # 等待随机时间
                # 出击s次后补给
                if i == s:
                    functions.supply()
                    print("补给完成")
                    s += random.randint(16, 18)  # 出击间隔 次补给(ss3-5)
                    print("第"+str(s+1)+"次出击完成后补给")
                    time.sleep(random.uniform(2, 9))
            system("title K☆A☆N☆A☆U☆T☆O")
            os.system('cls')
            continue
        elif mode == 2:
            r = int(input("请输入出击次数:"))
            os.system('cls')
            functions.supply()
            print("补给完成")
            time.sleep(random.uniform(2, 9))
            s = random.randint(3, 4)  # 在出击s+1次后补给（ss2-4）
            print("第"+str(s+1)+"次出击完成后补给")
            for i in range(r):
                system("title 出击次数:%d/%d" % (i+1, r))
                functions.run_5_2()
                print("第"+str(i+1)+"次出击完成")
                wait(random.randint(0, 9))  # 等待随机时间
                # 出击s次后补给
                if i == s:
                    functions.supply()
                    print("补给完成")
                    s += random.randint(4, 5)  # 出击间隔 次补给(ss3-5)
                    print("第"+str(s+1)+"次出击完成后补给")
                    time.sleep(random.uniform(2, 9))
            system("title K☆A☆N☆A☆U☆T☆O")
            os.system('cls')
            continue


system("title K☆A☆N☆A☆U☆T☆O")
time.sleep(1)
hwnd = win32gui.FindWindow(None, "K☆A☆N☆A☆U☆T☆O")
win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 1320,
                      10, 600, 400, win32con.SWP_SHOWWINDOW)
menu()
