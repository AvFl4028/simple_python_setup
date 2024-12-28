# Simple Python Setup
This is a simple script of python that makes a simple setup for projects
## What this script do
- A virtual python enviroment (venv)
- A simple main.py file in a src folder
- Initialize a git repository
## Systax
From Python
~~~bash
python ./src/main.py {path}
~~~
From exe
~~~bash
main.exe {path}
~~~
## Compile .exe
This script use PyInstaller to create the .exe file, you can compile yourself with this command:
~~~bash
pyinstaller --onefile .\src\main.py
~~~