import keyboard
from time import sleep
import json
from utils import *

# Import the settings
params = load_keys()

last_keys = []
on = True

stop = False
while not stop:
    key = keyboard.read_key()

    # Normal key
    if len(key) == 1:
        # Append to last_key
        last_keys.append(key)

        # Keep last_key 50 lenght
        if len(last_keys) > params["global_params"]["max_keys"]:
            del last_keys[0]
    
    elif key == "backspace" and len(last_keys) >= 1:
        # Remove letters
        del last_keys[-1]
    
    else:
        continue
    
    print(last_keys)

    # If on, analyse last keys
    if on:
        for event in params["keys"]:
            input_text = event["input"]
            output_text = event["output"]

            # Input ? Output.
            if is_written(input_text, last_keys, "accept_lower_and_upper_case" in event["params"]):
                if not "keep_text" in event["params"]:
                    remove(len(input_text))

                write(output_text)

                # Remove keys
                if len(last_keys) >= len(input_text):
                    del last_keys[-1 * len(input_text):]
    
    # Analyse all special keys
    for event in params["special_keys"].keys():
        if type(params["special_keys"][event]) is list:
            check = True
            for letter in event:
                if not keyboard.is_pressed(letter):
                    check = False
                    break
        else:
            check = is_written(params["special_keys"][event], last_keys)
        
        if check:
            # Events
            if event == "end":
                stop = True
                msg = "Programm ending !"

            elif event == "reload":
                params = load_keys()
                msg = "Reloaded !"
            
            elif event == "on":
                if on:
                    msg = "I'm already activated !"
                else:
                    on = True
                    msg = "Activating !"

            elif event == "off":
                if not on:
                    msg = "Already off !"
                else:
                    on = False
                    msg = "Goodbye !"
            
            else:
                msg = "What is supposed to be this event ?"

            remove(len(event))
            write(msg)

            sleep(0.5)
            remove(len(msg))
    
    # Avoid double keys
    keyboard.read_key()