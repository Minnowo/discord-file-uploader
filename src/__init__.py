
# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.


import os 
import subprocess
from re import compile
from time import sleep 

AHK_PATH     = ".depends\\AutoHotkeyA32.exe" # path to AHK 
CLICK        = "scripts\\click.ahk"          # click script // this is not used
DOUBLE_CLICK = "scripts\\doubleClick.ahk"    # double click script
SEND_TEXT    = "scripts\\send.ahk"           # send text script
SEND_KEY     = "scripts\\sendKey.ahk"        # send key script

DIRECTORY = "X:\\__\\ConvertOut\\"           # directory of files to upload

CLICK_X = 2533                               # x mouse click position
CLICK_Y = 1035                               # y mouse click position 
  
MAX_BUFFER_SIZE   = 8192000                  # max upload files size in bytes
MAX_BUFFER_COUNT  = 10                       # max number of uplaods per message
MAX_BUFFER_LENGTH = 259                      # max character length that can be typed in the upload file dialog

DELAY = 6                                    # delay in seconds between each upload
USE_FULL_PATHS = False                       # are absolute paths being used 



def natural_sort_key(s, _nsre=compile('([0-9]+)')):
    return [int(text) if text.isdigit() else text.lower()
            for text in _nsre.split(s)]


def mouse_click(xpos, ypos, *, AHK = AHK_PATH, script=CLICK):

    subprocess.run([AHK, script, str(xpos), str(ypos)])


def double_mouse_click(xpos, ypos, *, AHK = AHK_PATH, script=DOUBLE_CLICK):

    subprocess.run([AHK, script, str(xpos), str(ypos)])


def send(text, *, AHK = AHK_PATH, script=SEND_TEXT):

    subprocess.run([AHK, script, str(text)])


def send_key(key_name, *, AHK = AHK_PATH, script=SEND_KEY):

    subprocess.run([AHK, script, str(key_name)])


def invoke_upload(buffer : set, click_pos : tuple):

    double_mouse_click(click_pos[0], click_pos[1])
    sleep(1)

    text = []
    for i in buffer:

        text.append(f'"{i}"')

    send("".join(text))
    
    sleep(1)

    send_key("enter")

    sleep(1)

    send_key("enter")


def main():

    buffer = set()
  
    buffer_size   = 0
    buffer_count  = 0
    buffer_length = 0
    
    for file in sorted(os.listdir(DIRECTORY), key=natural_sort_key):

        file = os.path.abspath(os.path.join(DIRECTORY, file))

        if not os.path.isfile(file):
            continue

        try:

            file_size = os.path.getsize(file)
            
            if file_size > MAX_BUFFER_SIZE:
                print("file size is over the limit, cannot upload this file: " + file)
                continue

            if not USE_FULL_PATHS:
                file = os.path.basename(file)

            if len(file) + 2 > MAX_BUFFER_LENGTH:
                print("file path is over the limit, cannot upload this file: " + file)
                continue

            if buffer_count >= MAX_BUFFER_COUNT:
                print(f"sending: {buffer_count} files with a total size of {buffer_size}")
                invoke_upload(buffer, (CLICK_X, CLICK_Y))
                buffer.clear()
                buffer_count  = 0
                buffer_size   = 0
                buffer_length = 0
                sleep(DELAY)

            elif (buffer_size + file_size) >= MAX_BUFFER_SIZE:
                print(f"sending: {buffer_count} files with a total size of {buffer_size}")
                invoke_upload(buffer, (CLICK_X, CLICK_Y))
                buffer.clear()
                buffer_count  = 0
                buffer_size   = 0
                buffer_length = 0
                sleep(DELAY)
            
            elif buffer_length + (2 + len(file)) >= MAX_BUFFER_LENGTH:
                print(f"sending: {buffer_count} files with a total size of {buffer_size}")
                invoke_upload(buffer, (CLICK_X, CLICK_Y))
                buffer.clear()
                buffer_count  = 0
                buffer_size   = 0
                buffer_length = 0
                sleep(DELAY)

            buffer.add(file)
            buffer_size   += file_size
            buffer_count  += 1
            buffer_length += 2 + len(file)

        except:
            pass 
    
    print(f"sending: {buffer_count} files with a total size of {buffer_size}")
    invoke_upload(buffer, (CLICK_X, CLICK_Y))

    input("all done. press enter to exit.")

