# BloonBot
This is a fork from someone, I have lost the original repo. I have added discord intergration
## How It Works
This program will select the map Dark Castle and beat it on easy difficulty while collecting any levels and event items.  
It will use the Hero OBYN (Which will be selected auto if not), a submarine and a ninja monkey to beat the game.   

## In-Game Requirements
Map: Dark Castle  

Keybinds that need to be changed:  
Keybind         | Key
--------------- | -----
Upgrade path 1	| <ul>, 
Upgrade path 2	|	<ul>. 
Upgrade path 3	|	<ul>/  

Upgrades:  
Monkey        | Upgrade
------------- | -------------
Submarine     | <ul>2-0-4
Ninja         | <ul>4-0-1

Discord Webhook: Add your web hook
## Setup
Run ```pip install -r requirements.txt```
## How to Run without Discord Posting
Run ```python bloonBot.py```<br>
Follow instruction from script

## How to Run with Discord Posting
Prereq:
- Server On Discord
1. Create webhook
    1. In the server settings Go to Integrations
    2. Create Webhook
    3. Copy Webhook URL
2. In `bloonbot_logging.py` add the URL to `discord_url`
3. Run `python bloonbot_logging.py`
  
## Compatibility
#### Resolutions supported:  
* 3440x1440 (But should work for any 1440p)
## ToDo
- [x] Add per run output
- - [x] Used/ Updating embed messages
- [ ] Add Error Recovery Program
- - [ ] Be able to correct bot
- - [ ] Restart bot if needed
- [x] Logging of won instas
- - [x] Discord Message / image

