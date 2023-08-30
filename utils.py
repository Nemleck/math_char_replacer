import json
import keyboard
from time import sleep

def load_keys():
    with open("keys.json", "r", encoding="utf-8") as f:
        data = json.loads(f.read())
    
    # Add necessary things
    for key in data["keys"]:
        if not "params" in key:
            key["params"] = []
    
    return data

def is_written(text: str | list[str], last_keys: list[str], lower_case=False):
    if type(text) is str:
        last_text = "".join(last_keys)

        if lower_case:
            return last_text.lower().endswith(text.replace(" ", "").lower())
        else:
            return last_text.endswith(text.replace(" ", ""))
    else:
        check = True
        for key in text:
            if not keyboard.is_pressed(key):
                check = False
        
        return check

def write(text: list[str] | str):
    if type(text) is str:
        keyboard.write(text)
    
    else:
        for key in text:
            keyboard.press(key)
        
        for key in text:
            keyboard.release(key)

def remove(num):
    for i in range(num):
        keyboard.press_and_release("backspace")