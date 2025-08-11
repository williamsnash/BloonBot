# BloonBot
This is a fork from someone; I have lost the original repo.
## How It Works
This program will select the map Dark Castle and beat it on easy difficulty while collecting all levels and event items.  
It will use the Hero OBYN (Which will be selected auto if not), a submarine, and a ninja monkey to beat the game.   

## In-Game Requirements
### Map: 
- Dark Castle  

### Monkeys * Upgrades:  
Monkey        | Upgrade
------------- | -------------
Submarine     | <ul>2-0-4
Ninja         | <ul>4-0-1

~~Discord Webhook: Add your webhook~~
## Setup
Run ```pip install -r requirements.txt```

### Config File
Run the setup.py to generate images and then to generate the button positions (For examples of the images see the [images folder](https://github.com/williamsnash/BloonBot/tree/main/imgs))
```
discord_url = "" #NOT CURRENTLY FUNCTIONAL
upgrade_path_1 = ','
upgrade_path_2 = '.'
upgrade_path_3 = '/'

monkeys = {
    "SUBMARINE": "x",
    "NINJA": "d",
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
    'HERO_LOCATION': [1189, 649],  # Top Middle Corner
    'SUBMARINE_LOCATION': [1907, 549],  # Just above drawbridge
    'NINJA_LOCATION': [2382, 741],  # On Castle, centered
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
```
## How to Run without Discord Posting
Run ```python bloonBot.py```<br>
Follow the instructions from the script

## ~~How to Run with Discord Posting~~
Prereq:
- Server On Discord
1. Create a webhook
    1. In the server settings, go to Integrations
    2. Create Webhook
    3. Copy Webhook URL
2. In `bloonbot_logging.py` add the URL to `discord_url`
3. Run `python bloonbot_logging.py`



