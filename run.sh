 #!/bin/bash

# Creates virtual environment to run packages and quiz
python3 -m venv kapuut-venv
# Activates the virtual environment 
source Kapuut-venv/bin/activate
# Installs all requirements/packages needed to run game
pip3 install -r requirements.txt
# clears the terminal
clear
# Runs the main game program
python3 main.py
