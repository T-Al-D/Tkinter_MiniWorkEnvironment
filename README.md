# Tkinter_MiniWE
A small integrated work environment: A little project with python tkiner.

Unfinished!
This project has no guarantee or liability.


Colorfinder : 
	Google colorpicker

Pixelart    : 
	https://www.pixilart.com/draw?ref=home-page

png to ico converter: 
	https://www.online-convert.com/

Command to covert *.py to *.exe (which did not work succsessfully in this case):
	pyinstaller --onefile --icon="res/icon.ico" -w main.py
	pyinstaller -F -w --icon="res/icon.ico" --hidden-import=tkinter --hidden-import=tkinter.filedialog -import=Tkinter_MiniWorkEnvironment main.py