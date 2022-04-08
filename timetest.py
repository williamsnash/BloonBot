import pyautogui
import time
from discord_webhook import DiscordWebhook, DiscordEmbed

webhookM = 'https://discord.com/api/webhooks/961635444024565860/OuPLMdsmv5Zf96Yk9yYooUIXpC7QCU9UeNZE1SPMebPF2kZ75_MHR_7NfzWgQGOQR3Eq'
def imageSend():
    named_tuple = time.localtime() # get struct_time
    time_string = time.strftime("%Y-%m-%d-%H-%M", named_tuple)
    loot_img = time_string + ".png" # Creates image file name of 'time.png'
    im1 = pyautogui.screenshot(loot_img) # Takes the screenshot

    webhook = DiscordWebhook(
                url= webhookM,
                username='Event Looot',
                )
    with open(loot_img, "rb") as f:
        webhook.add_file(file=f.read(), filename=loot_img)
    response = webhook.execute()

error_check = "Button Not Found"
if(error_check != "None"):
    print("Error ")