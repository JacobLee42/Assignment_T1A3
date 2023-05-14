 #!/bin/bash


python3 -m venv kapuut-venv
source Kapuut-venv/bin/activate
pp3 install -r requirements.txt
python3 main.py
