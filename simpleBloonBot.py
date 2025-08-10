import pyautogui
import pydirectinput
import time
from time import sleep
import keyboard
import numpy
import random
import colorama
from colorama import Fore, Back, Style
from discord_webhook import DiscordWebhook
import os


# TODO
# Go to Medium
# Add Wizard 042
# Logging
# Discord message?
# Per Run
# Embeddi
# Insta Logging - Added / not tested
# Discord message?
colorama.init(autoreset=True)

overtime = 0

path = "pictures/levelup.png"
victory_path = "pictures/victory.png"
defeat_path = "pictures/defeat.png"
menu_path = "pictures/menu.png"
event_path = "pictures/event.png"
obyn_hero_path = "pictures/obyn.png"
next_path = "pictures/next.png"
discord_url = "https://discord.com/api/webhooks/961959326401065000/vuG2h5LRTqCE3I5_Q6wSH7TvQ57N5cHBf98zxSB8lUe013DhtYuNfaiFjH2eHM-kDb9f"
upgrade_path_1 = ','
upgrade_path_2 = '.'
upgrade_path_3 = '/'

monkeys = {
    "DART": "q",
    "BOOMERANG": "w",
    "BOMB": "e",
    "TACK": "r",
    "ICE": "t",
    "GLUE": "y",
    "SNIPER": "z",
    "SUBMARINE": "x",
    "BUCCANEER": "c",
    "ACE": "v",
    "HELI": "b",
    "MORTAR": "n",
    "DARTLING": "m",
    "WIZARD": "a",
    "SUPER": "s",
    "NINJA": "d",
    "ALCHEMIST": "f",
    "DRUID": "g",
    "BANANA": "h",
    "ENGINEER": "l",
    "SPIKE": "j",
    "VILLAGE": "k",
    "HERO": "u"
}

button_positions = {
    "HOME_MENU_START": [1732, 1263],
    "EXPERT_SELECTION": [2219, 1301],
    "RIGHT_ARROW_SELECTION": [2638, 572],
    "DARK_CASTLE": [1144, 763],
    "EASY_MODE": [1277, 541],
    "STANDARD_GAME_MODE": [1283, 793],
    "OVERWRITE_SAVE": [1955, 967],
    'HERO_LOCATION': [1189, 649], # Top Middle Corner
    'SUBMARINE_LOCATION': [1907, 549], # Just above drawbridge
    'NINJA_LOCATION': [2382, 741], # On Castle, centered
    "VICTORY_CONTINUE": [1702, 1210],
    "VICTORY_HOME": [1393, 1112],
    'EVENT_COLLECTION': [1735, 903],
    'FAR_LEFT_INSTA': [1520, 707],
    'FAR_RIGHT_INSTA': [1921, 702],
    'LEFT_INSTA': [1517, 711],
    'RIGHT_INSTA': [1924, 715],
    'MID_INSTA': [1716, 712],
    'EVENT_CONTINUE': [1718, 1335],
    'EVENT_EXIT': [97, 74],
    'HERO_SELECT': [1153, 1278],
    'SELECT_OBYN': [140, 558],
    'CONFIRM_HERO': [1925, 816]
}


REF_WIDTH = 3440
REF_HEIGHT = 1440

NEW_WIDTH, NEW_HEIGHT = pyautogui.size()  # This should be (3440, 1440) for you


def scale_position(pos):
  x, y = pos
  scaled_x = int(x * (NEW_WIDTH / REF_WIDTH))
  scaled_y = int(y * (NEW_HEIGHT / REF_HEIGHT))
  return scaled_x, scaled_y


def click(location):
  pyautogui.click(scale_position(button_positions[location]))
  sleep(0.5)


def move_mouse(location):
  pyautogui.moveTo(location)
  time.sleep(0.5)


def press_key(key):
  pydirectinput.press(key)
  time.sleep(0.5)


def menu_check():
  while True:  # Not doing anything until menu screen is open
    menu_on = pyautogui.locateOnScreen(
      menu_path, grayscale=True, confidence=0.9)
    if menu_on != None:
      print(f'{Fore.RED}Menu screen found. Continuing...')
      break
    else:
      print(f'{Fore.GREEN}Menu screen not found. Trying again...')
      sleep(2)


def hero_obyn_check():

  menu_check()

  print(f'{Fore.CYAN}Checking for OBYN...')
  found = pyautogui.locateOnScreen(
    obyn_hero_path, grayscale=True, confidence=0.9)

  if found == None:
    print(f'{Fore.CYAN}Not found. Selecting OBYN...')
    click("HERO_SELECT")
    click("SELECT_OBYN")
    click("CONFIRM_HERO")
    press_key("esc")
    print(f'{Fore.CYAN}OBYN selected.')


def place_tower(tower, location):

  Level_Up_Check(1)
  print(f'{Fore.CYAN}Placing ' + tower + '...')
  move_mouse(button_positions[location])
  press_key(monkeys[tower])
  pyautogui.click()
  print(f'{Fore.CYAN}' + tower + ' placed.')
  sleep(0.5)


def upgrade_tower(path, location):

  Level_Up_Check(1)
  print(f'{Fore.CYAN}Upgrading tower path ' + path + '...')
  click(location)
  press_key(path)
  time.sleep(1)
  press_key("esc")
  print(f'{Fore.CYAN}Path ' + path + ' upgraded.')
  sleep(0.5)


def Level_Up_Check(seconds):  # Just a timer that checks if you ahve leved up
  global overtime
  overtime = 0

  t_end = time.time() + seconds
  found = None
  while time.time() < t_end:
    try:
      found = pyautogui.locateOnScreen(path, grayscale=True, confidence=0.9)
    except:
      pass

    if found != None:
      print(f'{Fore.RED}Level Up notification detected. Getting rid of it...')
      click("LEFT_INSTA")  # Accept lvl
      time.sleep(1)
      click("LEFT_INSTA")  # Accept knoledge
      time.sleep(1)
      press_key("space")  # Start the game
      print(f'{Fore.GREEN}Notification kyssed.')
    else:
      sleep(0.2)

  overtime = time.time() - t_end


def send_event_loot():
  named_tuple = time.localtime()  # get struct_time
  time_string = time.strftime("%Y-%m-%d-%H-%M", named_tuple)
  loot_img = time_string + ".png"  # Creates image file name of 'time.png'
  im1 = pyautogui.screenshot(loot_img)  # Takes the screenshot
  try:
    webhook = DiscordWebhook(
        url=discord_url,
        username='Event Looot'
    )
    with open(loot_img, "rb") as f:
      webhook.add_file(file=f.read(), filename=loot_img)
    response = webhook.execute()
    if os.path.exists(loot_img):
      os.remove(loot_img)
    else:
      print("The file does not exist")
  except:
    print("An exception occurred")
    print("Waiting 20 seconds to continue")
    sleep(20)
    global error_status
    error_status += 1


def event_check():

  found = pyautogui.locateOnScreen(event_path, grayscale=True, confidence=0.9)

  if found != None:
    print(f"{Fore.RED}Event notification detected. Getting rid of it...")
    click("EVENT_COLLECTION")  # DUE TO EVENT:
    time.sleep(1)
    click("LEFT_INSTA")  # unlock insta
    time.sleep(1)
    click("LEFT_INSTA")  # collect insta
    time.sleep(1)
    click("RIGHT_INSTA")  # unlock r insta
    time.sleep(1)
    click("RIGHT_INSTA")  # collect r insta
    time.sleep(1)
    # send_event_loot()  # Send discord message
    time.sleep(1)
    click("FAR_LEFT_INSTA")
    time.sleep(1)
    click("FAR_LEFT_INSTA")
    time.sleep(1)
    click("MID_INSTA")  # unlock insta
    time.sleep(1)
    click("MID_INSTA")  # collect insta
    time.sleep(1)
    click("FAR_RIGHT_INSTA")
    time.sleep(1)
    click("FAR_RIGHT_INSTA")
    time.sleep(1)
    # send_event_loot()  # Send discord message
    time.sleep(1)
    click("EVENT_CONTINUE")

    # awe try to click 3 quick times to get out of the event mode, but also if event mode not triggered, to open and close profile quick
    click("EVENT_EXIT")
    print(f'{Fore.GREEN}Event notification kyssed.')
    time.sleep(1)


def Start_Select_Map():
  menu_check()
  print(f'{Fore.CYAN}Selecting map...')
  click("HOME_MENU_START")  # Move Mouse and click from Home Menu, Start
  click("EXPERT_SELECTION")  # Move Mouse to expert and click
  click("RIGHT_ARROW_SELECTION")  # Move Mouse to arrow and click
  click("DARK_CASTLE")  # Move Mouse to Dark Castle
  click("EASY_MODE")  # Move Mouse to select easy mode
  click("STANDARD_GAME_MODE")  # Move mouse to select Standard mode
  click("OVERWRITE_SAVE")  # Move mouse to overwrite save if exists
  print(f'{Fore.CYAN}Map selected.')


def Main_Game():

  sleep(2)
  # sub_path_1 = 0
  # sub_path_3 = 0
  # ninja_path_1 = 0
  # ninja_path_3 = 0
  print(f'{Fore.CYAN}Game started.')

  place_tower("HERO", "HERO_LOCATION")
  press_key("space")  # Start the game
  press_key("space")  # Fast forward the game
  Level_Up_Check(20 - overtime)
  place_tower("SUBMARINE", "SUBMARINE_LOCATION")  # 8.5
  Level_Up_Check(8.5 - overtime)
  upgrade_tower(upgrade_path_1, "SUBMARINE_LOCATION")  # 18
  # sub_path_1 += 1
  print(f'{Fore.GREEN}Sub upgrade')
  # print(f" Sub Path 1: {sub_path_1}")
  # print(f" Sub Path 3: {sub_path_3}")
  Level_Up_Check(18 - overtime)
  upgrade_tower(upgrade_path_3, "SUBMARINE_LOCATION")  # 45
  # sub_path_3 += 1
  print(f'{Fore.GREEN}Sub upgrade')
  # print(f" Sub Path 1: {sub_path_1}")
  # print(f" Sub Path 3: {sub_path_3}")
  Level_Up_Check(45 - overtime)
  upgrade_tower(upgrade_path_3, "SUBMARINE_LOCATION")  # 24
  # sub_path_3 += 1
  print(f'{Fore.GREEN}Sub upgrade')
  # print(f" Sub Path 1: {sub_path_1}")
  # print(f" Sub Path 3: {sub_path_3}")
  Level_Up_Check(24 - overtime)
  upgrade_tower(upgrade_path_1, "SUBMARINE_LOCATION")  # 15
  # sub_path_1 += 1
  print(f'{Fore.GREEN}Sub upgrade')
  # print(f" Sub Path 1: {sub_path_1}")
  # print(f" Sub Path 3: {sub_path_3}")
  Level_Up_Check(15 - overtime)
  place_tower("NINJA", "NINJA_LOCATION")  # 11.5
  Level_Up_Check(11.5 - overtime)
  upgrade_tower(upgrade_path_1, "NINJA_LOCATION")  # 11.5
  # ninja_path_1 += 1
  print(f'{Fore.GREEN}Ninja upgrade')
  # print(f" Ninja Path 1: {ninja_path_1}")
  # print(f" Ninja Path 3: {ninja_path_3}")
  Level_Up_Check(11.5 - overtime)
  upgrade_tower(upgrade_path_1, "NINJA_LOCATION")  # 4
  # ninja_path_1 += 1
  print(f'{Fore.GREEN}"Ninja upgrade')
  # print(f" Ninja Path 1: {ninja_path_1}")
  # print(f" Ninja Path 3: {ninja_path_3}")
  Level_Up_Check(4 - overtime)
  upgrade_tower(upgrade_path_3, "NINJA_LOCATION")  # 12
  # ninja_path_3 += 1
  print(f'{Fore.GREEN}Ninja upgrade')
  # print(f" Ninja Path 1: {ninja_path_1}")
  # print(f" Ninja Path 3: {ninja_path_3}")
  Level_Up_Check(12 - overtime)
  upgrade_tower(upgrade_path_1, "NINJA_LOCATION")  # 23
  # ninja_path_1 += 1
  print(f'{Fore.GREEN}Ninja upgrade')
  # print(f" Ninja Path 1: {ninja_path_1}")
  # print(f" Ninja Path 3: {ninja_path_3}")
  Level_Up_Check(23 - overtime)
  upgrade_tower(upgrade_path_3, "SUBMARINE_LOCATION")  # 39
  # sub_path_3 += 1
  print(f'{Fore.GREEN}Sub upgrade')
  # print(f" Sub Path 1: {sub_path_1}")
  # print(f" Sub Path 3: {sub_path_3}")
  Level_Up_Check(39 - overtime)
  upgrade_tower(upgrade_path_3, "SUBMARINE_LOCATION")  # 40
  # sub_path_3 += 1
  print(f'{Fore.GREEN}Sub upgrade')
  # print(f" Sub Path 1: {sub_path_1}")
  # print(f" Sub Path 3: {sub_path_3}")
  Level_Up_Check(20 - overtime)
  upgrade_tower(upgrade_path_1, "NINJA_LOCATION")
  # ninja_path_1 += 1
  print(f'{Fore.GREEN}Ninja upgrade')
  # print(f" Ninja Path 1: {ninja_path_1}")
  # print(f" Ninja Path 3: {ninja_path_3}")
  # print(f"inal Monkey Levels:")
  # print(f" Sub Path 1: {sub_path_1}\nSub Path 3: {sub_path_3}\n Ninja Path 1: {ninja_path_1}\n Ninja Path 3: {ninja_path_3}")
  Level_Up_Check(20 - overtime)


def Exit_Game():

  Level_Up_Check(1)

  found = pyautogui.locateOnScreen(next_path, grayscale=True, confidence=0.9)
  error_loop_count = 0
  while found == None:
    sleep(2)
    print('Next button not found.')
    error_loop_count += 1
    found = pyautogui.locateOnScreen(next_path, grayscale=True, confidence=0.9)
    if (error_loop_count == 3):  # Error Detection
      global game_status, error_status
      error_status = 1
      game_status = "Next Button Not Found"
  print(f'{Fore.CYAN}Game ended. Going back to homescreen...')
  pyautogui.click(button_positions['VICTORY_CONTINUE'])
  time.sleep(2)
  pyautogui.click(button_positions['VICTORY_HOME'])
  time.sleep(4)
  print(f'{Fore.CYAN}Back in homescreen. Checking for event notification...')
  # event_check()
  sleep(2)
  tries = 0
  for x in range(0, 4):  # checking for menu screen
    menu_on = pyautogui.locateOnScreen(
      menu_path, grayscale=True, confidence=0.9)
    if menu_on != None:
      print(f'{Fore.CYAN}Menu screen found. Continuing...')
      break
    else:
      click("EVENT_EXIT")
      sleep(3)

# Main


time_string = time.strftime("%Y-%m-%d-%H-%M", time.localtime())
game_win_Count = 1
error_status = 0
game_status = 'Running'
print(f'{Fore.CYAN}Starting in 5 seconds... move to BTD6 homescreen.')
sleep(5)
# -----------------------------------------
runs = f"Run {game_win_Count} started at {time_string}"
content = f"{runs}\n----------------------\nErrors : {0}\nStatus : {game_status}"
hero_obyn_check()
print(f'{Fore.CYAN}Starting loop.')
while True:
  time_string = time.strftime("%Y-%m-%d-%H-%M", time.localtime())
  runs = f"Run {game_win_Count} started at {time_string}"
  Start_Select_Map()
  Main_Game()
  Exit_Game()
  game_win_Count += 1
