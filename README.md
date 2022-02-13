## discord-file-uploader
automates the discord ui to upload files in a channel


### Usage

 - find the discord file upload button [this](images/button.png)

 - set the x and y click position variables in the [init.py](src/__init__.py) file to the x y position of the button

 - set the DIRECTORY variable in the [init.py](src/__init__.py) to the directory containing the files to upload

 - *optional* -> make all the filenames as SHORT as possible, because this script types the filenames into the upload dialog, there is a max limit of 259 characters

 - double click the upload dialog once and navigate to the folder and send 1 file, this ensures next time you open the dialog it is in the same folder

 - run the [main.py](src/__main__.py) script to start the script, this DOES NOT have a stop hotkey, so it's recommended you set the delay long enough to close the script / keep the console window close enough to close

 
