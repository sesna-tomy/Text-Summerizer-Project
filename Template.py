import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO,format ='[%(asctime)s]:%(message)s:')


project_name ="textSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"scr/{project_name}/__init__.py",
    f"scr/{project_name}/components/__init__.py",
    f"scr/{project_name}/utils/__init__.py",
    f"scr/{project_name}/utils/common .py",
    f"scr/{project_name}/logging/__init__.py",
    f"scr/{project_name}/config/__init__.py",
    f"scr/{project_name}/config/configuration.py",
    f"scr/{project_name}/pipeline__init__.py",
    f"scr/{project_name}/entity/__init__.py",
    f"scr/{project_name}/constants/__init__.py",
    "config/config.yami",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]



for filepath in list_of_files:                         #Path creates the file path according to the sstem we use
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)        #splits the file path to corresponf=ding file and directore

    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creatinf directory: {filedir} for the file {filename}")

    if (not os.path.exists(filepath) or (os.path.getsize(filepath) == 0)):
        with open(filepath,'w') as f:
            pass
            logging.info(f"creating an empty file {filepath}")
    
    else:
        logging.info(f"{filename} already exist")


