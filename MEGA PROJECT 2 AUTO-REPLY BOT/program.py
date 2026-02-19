import pyautogui
import pyperclip
import time
from openai import OpenAI
client = OpenAI(
base_url="https://openrouter.ai/api/v1",
api_key="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",
)

# Safety delay
time.sleep(3)

def is_last_message_from_sender(chat_text):
    lines = chat_text.strip().split("\n")
    
    # Last non-empty line lo
    last_line = lines[-1].strip()
    
    # Name extract karo ('] ' ke baad aur ':' se pehle)
    try:
        sender = last_line.split("] ")[1].split(":")[0]
    except IndexError:
        return False
    
    return sender == "Home Minister 🏡"


    # Step 1: Click on icon
pyautogui.click(1290, 1041)
time.sleep(1)

while True:

    # Step 1: Click on icon
    pyautogui.click(1290, 1041)
    time.sleep(1)

    # Step 2: Select text by dragging
    pyautogui.moveTo(1354, 197, duration=0.5)
    pyautogui.dragTo(1727, 951, duration=1, button='left')
    time.sleep(0.5)

    # Step 3: Copy selected text
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click(1710, 957)
    time.sleep(1)

    # Step 4: Get clipboard text into variable
    chat_history = pyperclip.paste()


    print(chat_history)

    if is_last_message_from_sender(chat_history):
      completion = client.chat.completions.create(
      model="arcee-ai/trinity-large-preview:free",
      messages=[
        {"role": "system", "content": "You are a person named kashish who speaks hindi as well as english she is from India, Delhi     and is a coder , You analyze chat history and respond (text message only)"},
        {"role": "user", "content": chat_history}
  ]
)

      response = completion.choices[0].message.content
      pyperclip.copy(response)

      # Click at new location
      pyautogui.click(1694, 960)
      time.sleep(1)

      # Paste
      pyautogui.hotkey('ctrl', 'v')
      time.sleep(1)

      # Press Enter
      pyautogui.press('enter')

      print("Text pasted successfully!")
       

