import pyautogui
import time

DEFAULT_SAVE = 'pictures'
IMAGE_SET = {
  'menu': 'Picture of the register on the left of the screen',
  'obyn': 'A picture of the hero obyn selected from the main menu',
  'game_paused': 'Start round arrow',
  'game_slow': 'The game running at normal speed',
  'game_fast': 'The game running at fast speeds',
  'victory': 'The victory text',
  'next': 'The button to move on after victory/defeat',
  'defeat': 'The defeat text',
  'event': 'The collection event text',
  'escape_menu': 'A image only in the escape menu'
}


def remap_images(image_name, prompt):
  # Get positions
  print(f"Taking for {image_name}:")
  print(prompt)
  print('-' * 50)
  top_left = get_position("Hover over the TOP-LEFT corner of the element")
  bottom_right = get_position(
      "Hover over the BOTTOM-RIGHT corner of the element")

  # Calculate width/height
  width = bottom_right.x - top_left.x
  height = bottom_right.y - top_left.y

  # Get filename
  filename = f"./pictures/{image_name}.png"

  # Take screenshot
  pyautogui.screenshot(filename, region=(
    top_left.x, top_left.y, width, height))
  print(f"Saved screenshot as {filename}")

  # Test if it matches
  print("Testing image recognition...")
  match = pyautogui.locateOnScreen(filename, confidence=0.7)
  if match:
    print(f"✅ Match found on screen: {match}")
  else:
    print("❌ No match found. Try lowering confidence or recapturing.")


def get_position(prompt):
  input(f"{prompt} and press Enter...")
  pos = pyautogui.position()
  print(f"Recorded position: {pos}")
  return pos


def remap_pixels():
  button_positions = {  # Creates a dictionary of all positions needed for monkeys (positions mapped to 2160 x 1440 resolution)
      "HOME_MENU_START": [0, 0],
      "EXPERT_SELECTION": [0, 0],
      "RIGHT_ARROW_SELECTION": [0, 0],
      "DARK_CASTLE": [0, 0],
      "EASY_MODE": [0, 0],
      "STANDARD_GAME_MODE": [0, 0],
      "OVERWRITE_SAVE": [0, 0],
      'HERO_LOCATION': [0, 0],  # Top Middle Corner
      'SUBMARINE_LOCATION': [0, 0],  # Just above drawbridge
      'NINJA_LOCATION': [0, 0],  # On Castle, centered
      "VICTORY_CONTINUE": [0, 0],
      "VICTORY_HOME": [0, 0],
      'EVENT_COLLECTION': [0, 0],
      'FAR_LEFT_INSTA': [0, 0],
      'FAR_RIGHT_INSTA': [0, 0],
      'LEFT_INSTA': [0, 0],
      'RIGHT_INSTA': [0, 0],
      'MID_INSTA': [0, 0],
      'EVENT_CONTINUE': [0, 0],
      'EVENT_EXIT': [0, 0],
      'HERO_SELECT': [0, 0],
      'SELECT_OBYN': [0, 0],
      'CONFIRM_HERO': [0, 0],
      'ESCAPE_HOME': [0, 0],
      'DEFEAT_HOME': [0, 0]
  }

  for key in button_positions.keys():
    button_positions[key] = list(get_position(f'Position for {key}'))

  print(button_positions)


if __name__ == '__main__':
  choice = input("ReMap Pixels or Image (P/I)")
  if (choice.lower() == 'p'):
    remap_pixels()
  elif (choice.lower() == 'i'):
    for image, prompt in IMAGE_SET.items():
      remap_images(image, prompt)
  else:
    print("Invalid Option")
