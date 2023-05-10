import actions
import time
import random


def supply():
    actions.port_supply()
    actions.check()
    actions.port()


def run_5_2():
    actions.port_fight()
    actions.fight()
    actions.map_5()
    actions.map_X_2()
    actions.confirm()
    actions.startfight()
    time.sleep(random.uniform(4, 6))
    actions.compass()
    #time.sleep(random.uniform(17, 30))
    #actions.formation_1()
    time.sleep(random.uniform(40, 45))  # 等待战斗结束
    actions.next_ss()
    time.sleep(random.uniform(3, 4))
    actions.next()
    actions.back()
