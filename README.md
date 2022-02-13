## Discord-File-Uploader
automates the discord ui to upload files in a channel

### About / Info

 - this program violates the [Discord Community Guidelines](https://discord.com/guidelines) USE AT OWN RISK I'm not responsible if anything happens

 - this program is WINDOWS ONLY because it uses [AutoHotkey](https://www.autohotkey.com/) for user inputs. it also relies on the [choose file dialog](images/fileDialog.png) where typing the filenames into the textbox in the format "name1.png""name2.png""name3.png" will select them to be uploaded, limitations being the max character length of 259

 - you're gonna want to set the delay based off how long it takes you to upload files because discord rate limits file uploads if they're consistent and fast, i haven't had any problems with 15 seconds or more 

 - this script doesn't have a pause/close hotkey so BE CARFUL as it uses the mouse and keyboard to simulate user input, it's recommended that you use command prompt or something that kills the script when it closes to allow easy closing paired with a high enough delay that you can move the mouse

### Usage

 - find the discord file upload button [this](images/button.png)

 - set the x and y click position variables in the [init.py](src/__init__.py) file to the x y position of the button. you can use the [mouseLocation.ahk](src/scripts/mouseLocation.ahk)

 - set the DIRECTORY variable in the [init.py](src/__init__.py) to the directory containing the files to upload

 - *optional* -> make all the filenames as SHORT as possible, because this script types the filenames into the upload dialog, there is a max limit of 259 characters

 - double click the upload dialog once and navigate to the folder and send 1 file, this ensures next time you open the dialog it is in the same folder

 - run the [main.py](src/__main__.py) script to start the script, this DOES NOT have a stop hotkey, so it's recommended you set the delay long enough to close the script / keep the console window close enough to close
