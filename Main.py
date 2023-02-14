import time
import pyautogui
from pynput.keyboard import Key, Controller
from pynput.mouse import Button, Controller

keyboard = Controller()
mouse = Controller()

def foundImg(img, detail = 0.8):
    return pyautogui.locateOnScreen('./assets/'+img+'.png', confidence=detail) != None

def locateImg(img):
    return pyautogui.locateCenterOnScreen('./assets/'+img+'.png', confidence=0.8)

def isGameOpen():
    return foundImg('game_open') != None or foundImg('game_open2') != None

def isPkmHealthy():
    return pyautogui.locateOnScreen('./assets/died.png', confidence=0.9) == None

# def isInPokeCenter():
#     return foundImg('pokeCenterObj')

def isInPkmCenter():
    return foundImg('pkmCenter')

def isInMtSilverExterior():
    return foundImg('mtSilverMailbox')

def talkWithJoy():
    while not foundImg('pokeCenterUp'):
        keyboard.type('w')
    if foundImg('nurse1'):
        keyboard.type('space')
    if foundImg('nurse2'):
        keyboard.type('1')
    if foundImg('nurse3'):
        keyboard.type('space')

def isInCherryCity():
    return foundImg('cherryCityObj')

def isInDownCherryCity():
    return foundImg('cherryDown') or foundImg('cherryDown2')

def isInRoute29():
    return foundImg('route29lbl')

def isRightRoute29():
    return foundImg('route29right') or foundImg('route29right2')

def isDownRoute29():
    return foundImg('route29down') or foundImg('route29down2')

def isInBattle():
    return foundImg('battle')

def gotoBattle():
    while not isRightRoute29():
        keyboard.type('d')
    while not isDownRoute29():
        keyboard.type('s')
    while not isInBattle():
        keyboard.type('s')
        keyboard.type('s')
        keyboard.type('w')


def gotoBattleCerulean():
    pyautogui.press('a')
    time.sleep(1)
    pyautogui.press('d')

def is_your_turn():
    return foundImg('your_turn')

def attacks_displayed():
    return foundImg('attacks_displayed')

def no_pp_left():
    return foundImg('no_pp_left')

def is_shiny_pkm():
    return foundImg('shiny') or foundImg('shiny2', 0.99) or foundImg('rareEncounter')

def items_displayed():
    return foundImg('choose_item')

def choose_pkm():
    return foundImg('choose_pkm')

def is_evolving():
    return foundImg('no')

def evolve():
    pos = locateImg('no')
    if pos != None:
        pyautogui.moveTo(pos.x/2, pos.y/2)
        mouse.click(Button.left)
        time.sleep(2)
        pyautogui.moveTo(100, 100)

def learn_move():
    print("LEARNING MOVE")
    if foundImg('deny_move'):
        pos = locateImg('deny_move')
        if pos != None:
            pyautogui.moveTo(pos.x/2, pos.y/2)
            mouse.click(Button.left)
            time.sleep(2)
            pyautogui.moveTo(100, 100)
    if foundImg('yes'):
            pos = locateImg('yes')
            pyautogui.moveTo(pos.x/2, pos.y/2)
            mouse.click(Button.left)

def is_learning_move():
    return foundImg('learning_move')

def is_a_shuckle():
    return foundImg('shuckle') or foundImg('shuckle2')

def is_a_wonder_bug():
    return foundImg('chansey')

    # return foundImg('ponytaH') or foundImg('ponytaH2') or foundImg('haunterH') or foundImg('growliteH') or foundImg('hawlucha') or foundImg('charmander') or foundImg('absolH') or foundImg('charmanderH') or foundImg('charmanderH2') or foundImg('gastlyH', 0.98) or foundImg('hawluchaH') or foundImg('torkoalH')
    # return foundImg('shuckle') or foundImg('shuckle2') or foundImg('larvesta') or foundImg('scyther')


def is_a_roggenrola():
    return foundImg('roggenrola')

attack_to_use = 1
def attack_mode():
    global attack_to_use
    if is_your_turn():
        print('YOUR TURN TO ATTACK')
        pyautogui.press('1')
    if attacks_displayed():
        print('ATTACKS DISPLAYED')
        pyautogui.press(str(attack_to_use))
        time.sleep(1)
        attack_to_use +=1
        if attack_to_use == 5:
            attack_to_use = 1

def hunt_mode():
    if is_your_turn():
        print('YOUR TURN')
        pyautogui.press('4')

def catch_mode():
    if is_your_turn():
        print('YOUR TURN TO CATCH')
        pyautogui.press('3')
    if items_displayed():
        pyautogui.press('1')

team_defeated = 0
def useEscapeRope():
    global team_defeated
    time.sleep(1)
    pyautogui.press('4')
    if(foundImg('escapeRopeWindow')):
        pos = locateImg('yes')
        time.sleep(1)
        if pos != None:
            pyautogui.moveTo(pos.x/2, pos.y/2)
            mouse.click(Button.left)
            time.sleep(2)
            pyautogui.moveTo(100, 100)
            team_defeated = 0


def automaticBattle():
    global team_defeated
    while not isInBattle() and isInCeruleanCave2F():
        pyautogui.keyDown('a')
        time.sleep(2)
        pyautogui.keyUp('a')
        pyautogui.keyDown('d')
        time.sleep(0.5)
        pyautogui.keyUp('d')

    if is_shiny_pkm():
        print("IS A SHINY!!!-----------------------------------")
        time.sleep(2)
        while foundImg('ok'):
            pos = locateImg('ok')
            time.sleep(2)
            if pos != None:
                pyautogui.moveTo(pos.x/2, pos.y/2)
                mouse.click(Button.left)
                time.sleep(2)
                pyautogui.moveTo(100, 100)
        catch_mode()
    else:
        if is_a_wonder_bug():
            print("IS THE PKM LOOKED!!!--------------------------------")
            catch_mode()
        else:
            print("IN BATTLE")
            if not teamDefeated():
                attack_mode()
            else:
                print("TEAM DEFEATED -----> GO TO HEAL")
                team_defeated = 1
                hunt_mode()

def isInMtSilverDown():
    return foundImg('mtSilverDown')

def isInMtSilverLeft():
    return foundImg('mtSilverLeft')

def isInMtSilver():
    return foundImg('mtSilver') or foundImg('mtSilver2')

def isInCeruleanCave2F():
    return foundImg('ceruleanCave2F')

def isInCeruleanCave1F():
    return foundImg('ceruleanCave1F')

def talkNurseJoy():
    global team_defeated
    pyautogui.press('space')
    time.sleep(2)
    if foundImg('healBy5000'):
        pyautogui.press('1')
    time.sleep(2)
    pyautogui.press('space')
    time.sleep(2)
    pyautogui.press('space')
    team_defeated = 0

def gotoHealPkmns():
    global team_defeated
    while not isInCeruleanCave1F() and not is_not_logged():
        if isInBattle():
            hunt_mode()
        pyautogui.press('d')
    pyautogui.press('d')
    talkNurseJoy()

def teamDefeated():
    return foundImg('teamDefeated', 0.98)

def goToBattleMtSilver():
    while isInPkmCenter():
        pyautogui.press('s')
    if isInMtSilverExterior():
        pyautogui.press('1')
        while not isInMtSilverLeft():
            hunt_mode()
            pyautogui.press('a')
        while not isInMtSilver():
            hunt_mode()
            pyautogui.press('w')

def is_not_logged():
    return foundImg('login')

def login():
    pos = locateImg('login_btn')
    if pos != None:
        pyautogui.moveTo(pos.x/2, pos.y/2)
        mouse.click(Button.left)
        time.sleep(2)
        pyautogui.moveTo(100, 100)

time.sleep(2)
while isGameOpen():
#     if isPkmHealthy():
#         if isInPokeCenter():
#             keyboard.type('s')
#         if isInCherryCity():
#             print("IN CHERRY CITY")
#             while not isInDownCherryCity():
#                 keyboard.type('s')
#             while isInDownCherryCity():
#                 keyboard.type('d')
#         if isInRoute29():
#             print("IN ROUTE 29")
#             gotoBattle()

        if is_not_logged():
            login()

        if choose_pkm():
            print("CHOOSING A POKMN")
            pyautogui.press('2')
            pyautogui.press('3')
            pyautogui.press('4')
            pyautogui.press('5')
            pyautogui.press('6')

        if (team_defeated == 1):
            gotoHealPkmns()
            # useEscapeRope()

        if is_learning_move():
            learn_move()

        if is_evolving():
            evolve()

        if not isInCeruleanCave2F():
            gotoBattleCerulean()
        else:
            print("LOOKING A BATTLE")
            automaticBattle()

print("GOOD BYE!")