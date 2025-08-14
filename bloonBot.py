import pyautogui
import pydirectinput
import time
from time import sleep
from datetime import datetime
import keyboard
import numpy
import random
import colorama
from colorama import Fore, Back, Style
from discord_webhook import DiscordWebhook
import os

import config

colorama.init(autoreset=True)

overtime = 0

path = "pictures/levelup.png"
victory_path = "pictures/victory.png"
defeat_path = "pictures/defeat.png"
menu_path = "pictures/menu.png"
event_path = "pictures/event.png"
obyn_hero_path = "pictures/obyn.png"
next_path = "pictures/next.png"
escape_menu = "pictures/escape_menu.png"


class RecoveryRestart(Exception):
    pass


def save_screenshot(file_name):
    screenshot = pyautogui.screenshot()
    screenshot.save(file_name)


def locate_on_screen(image_path, grayscale=True, confidence=0.9, capture_error=False, recover_on_fail=False):
    try:
        return pyautogui.locateOnScreen(
          image_path, grayscale=grayscale, confidence=confidence)
    except:
        if capture_error:
            date = datetime.now().strftime("%H_%M_%S_%m_%d_%Y")
            file_name = f'./errors/{date}-{image_path.split('/')[-1]}'
            print(f"Saving error image - {file_name}")
            save_screenshot(file_name)

        if recover_on_fail:
            try_recover(reason=f"Failed to locate {image_path}")


def click(location):
    pyautogui.click(config.button_positions[location])
    sleep(0.5)


def move_mouse(location):
    pyautogui.moveTo(location)
    time.sleep(0.5)


def press_key(key):
    pydirectinput.press(key)
    time.sleep(0.5)


def menu_check():
    while True:  # Not doing anything until menu screen is open
        menu_on = locate_on_screen(
          menu_path, grayscale=True, confidence=0.9, recover_on_fail=True)
        if menu_on != None:
            print(f'{Fore.RED}Menu screen found. Continuing...')
            break


def hero_obyn_check():

    menu_check()

    print(f'{Fore.CYAN}Checking for OBYN...')
    found = locate_on_screen(
      obyn_hero_path, grayscale=True, confidence=0.9, recover_on_fail=True)

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
    move_mouse(config.button_positions[location])
    press_key(config.monkeys[tower])
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
        found = locate_on_screen(
            path,
            grayscale=True,
            confidence=0.9,
        )

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

        defeat = locate_on_screen(
            defeat_path,
            grayscale=True,
            confidence=0.9
        )
        if defeat != None:
            print(f'{Fore.RED}Defeat - Reason: Unknow | Attempting Recovery')
            try_recover('Defeated')

    overtime = time.time() - t_end


def send_event_loot():
    named_tuple = time.localtime()  # get struct_time
    time_string = time.strftime("%Y-%m-%d-%H-%M", named_tuple)
    loot_img = time_string + ".png"  # Creates image file name of 'time.png'
    im1 = pyautogui.screenshot(loot_img)  # Takes the screenshot
    try:
        webhook = DiscordWebhook(
            url=config.discord_url,
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

    found = locate_on_screen(
        event_path,
        grayscale=True,
        confidence=0.9,
    )

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
        save_screenshot(
            f"./collections/{datetime.now().strftime('%H_%M_%S_%m_%d_%Y')}.png")
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
        save_screenshot(
            f"./collections/{datetime.now().strftime('%H_%M_%S_%m_%d_%Y')}.png")
        time.sleep(1)
        # save_screenshot(f"./collections/{datetime.now().strftime('%H_%M_%S_%m_%d_%Y')}.png")
        click("EVENT_CONTINUE")
        # awe try to click 3 quick times to get out of the event mode, but also if event mode not triggered, to open and close profile quick
        click("EVENT_EXIT")
        print(f'{Fore.GREEN}Event notification closed.')
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
    print(f'{Fore.CYAN}Game started.')

    place_tower("HERO", "HERO_LOCATION")

    press_key("space")  # Start the game
    press_key("space")  # Fast forward the game

    Level_Up_Check(20 - overtime)

    place_tower("SUBMARINE", "SUBMARINE_LOCATION")  # 8.5

    Level_Up_Check(8.5 - overtime)
    upgrade_tower(config.upgrade_path_1, "SUBMARINE_LOCATION")  # 18
    print(f'{Fore.GREEN}Sub upgrade')

    Level_Up_Check(18 - overtime)
    upgrade_tower(config.upgrade_path_3, "SUBMARINE_LOCATION")  # 45
    print(f'{Fore.GREEN}Sub upgrade')

    Level_Up_Check(45 - overtime)
    upgrade_tower(config.upgrade_path_3, "SUBMARINE_LOCATION")  # 24
    print(f'{Fore.GREEN}Sub upgrade')

    Level_Up_Check(24 - overtime)
    upgrade_tower(config.upgrade_path_1, "SUBMARINE_LOCATION")  # 15
    print(f'{Fore.GREEN}Sub upgrade')

    Level_Up_Check(15 - overtime)
    place_tower("NINJA", "NINJA_LOCATION")  # 11.5

    Level_Up_Check(11.5 - overtime)
    upgrade_tower(config.upgrade_path_1, "NINJA_LOCATION")  # 11.5
    print(f'{Fore.GREEN}Ninja upgrade')

    Level_Up_Check(11.5 - overtime)
    upgrade_tower(config.upgrade_path_1, "NINJA_LOCATION")  # 4
    print(f'{Fore.GREEN}"Ninja upgrade')

    Level_Up_Check(4 - overtime)
    upgrade_tower(config.upgrade_path_3, "NINJA_LOCATION")  # 12
    print(f'{Fore.GREEN}Ninja upgrade')

    Level_Up_Check(12 - overtime)
    upgrade_tower(config.upgrade_path_1, "NINJA_LOCATION")  # 23
    print(f'{Fore.GREEN}Ninja upgrade')

    Level_Up_Check(23 - overtime)
    upgrade_tower(config.upgrade_path_3, "SUBMARINE_LOCATION")  # 39
    print(f'{Fore.GREEN}Sub upgrade')

    Level_Up_Check(39 - overtime)
    upgrade_tower(config.upgrade_path_3, "SUBMARINE_LOCATION")  # 40
    print(f'{Fore.GREEN}Sub upgrade')

    Level_Up_Check(20 - overtime)
    upgrade_tower(config.upgrade_path_1, "NINJA_LOCATION")
    print(f'{Fore.GREEN}Ninja upgrade')

    Level_Up_Check(20 - overtime)


def Exit_Game():

    Level_Up_Check(1)

    found = locate_on_screen(
        next_path,
        grayscale=True,
        confidence=0.9,
    )
    error_loop_count = 0
    while found == None:
        sleep(2)
        print('Next button not found.')
        error_loop_count += 1
        found = locate_on_screen(
            next_path, grayscale=True,
            sconfidence=0.9)
        if (error_loop_count == 3):  # Error Detection
            try_recover('Next Button not found')

    print(f'{Fore.CYAN}Game ended. Going back to homescreen...')
    pyautogui.click(config.button_positions['VICTORY_CONTINUE'])
    time.sleep(2)
    pyautogui.click(config.button_positions['VICTORY_HOME'])
    time.sleep(4)
    print(f'{Fore.CYAN}Back in homescreen. Checking for event notification...')
    event_check()
    sleep(2)
    tries = 0
    for x in range(0, 4):  # checking for menu screen
        menu_on = locate_on_screen(
          menu_path, grayscale=True, confidence=0.9, recover_on_fail=True)
        if menu_on != None:
            print(f'{Fore.CYAN}Menu screen found. Continuing...')
            break
        else:
            click("EVENT_EXIT")
            sleep(3)


def try_recover(reason):
    print(f"{Fore.RED}[RECOVERY] Attempting recovery...\n {reason}")

    # Step 1: Hit escape 3 times
    for _ in range(3):
        press_key("esc")
        sleep(0.5)

    defeat = locate_on_screen(
        defeat_path,
        grayscale=True,
        confidence=0.9
    )
    if defeat != None:
        print(f'{Fore.RED}Defeat - Reason: Unknow | Attempting Recovery')
        click('DEFEAT_HOME')
        sleep(3)
        menu_check()
        raise RecoveryRestart()
    else:
        # Step 2: Check for escape menu
        esc_menu = locate_on_screen(
            "pictures/escape_menu.png",
            grayscale=True,
            confidence=0.9
        )

        if esc_menu is not None:
            print(
                f"{Fore.YELLOW}[RECOVERY] Escape menu found. Exiting to home...")
            # Button mapping must exist in config
            click('ESCAPE_HOME')
            sleep(3)
            menu_check()
            raise RecoveryRestart()
        else:
            print(
                f"{Fore.YELLOW}[RECOVERY] Escape menu not found. Trying again...")
            press_key("esc")
            sleep(1)
            esc_menu = locate_on_screen(
                "pictures/escape_menu.png",
                grayscale=True,
                confidence=0.9
            )
            if esc_menu is not None:
                print(
                    f"{Fore.YELLOW}[RECOVERY] Escape menu found after retry. Exiting to home...")
                click("ESC_MENU_EXIT_HOME")
                sleep(3)
                menu_check()
                raise RecoveryRestart()
            else:
                save_screenshot(
                    f'./errors/{datetime.now().strftime('%H_%M_%S_%m_%d_%Y')}_recovery_failed.png')
                raise ('Recovery Failed to Return to menu - Exiting')

    # Step 3: Check for event notification
    event_check()

    # Step 4: Restart loop (this just means return to main while loop)
    print(f"{Fore.GREEN}[RECOVERY] Recovery complete. Restarting run...\n")
    sleep(1)


if __name__ == '__main__':
    time_string = time.strftime("%Y-%m-%d-%H-%M", time.localtime())
    game_win_Count = 1
    error_status = 0
    game_status = 'Running'
    print(f'{Fore.CYAN}Starting in 5 seconds... move to BTD6 homescreen.')
    sleep(5)

    runs = f"Run {game_win_Count} started at {time_string}"

    hero_obyn_check()

    print(f'{Fore.CYAN}Starting loop.')
    while True:
        try:
            time_string = time.strftime("%Y-%m-%d-%H-%M", time.localtime())
            runs = f"Run {game_win_Count} started at {time_string}"
            Start_Select_Map()
            Main_Game()
            Exit_Game()
            game_win_Count += 1
        except RecoveryRestart:
            sleep(2)
            event_check()
            sleep(1)
            continue
