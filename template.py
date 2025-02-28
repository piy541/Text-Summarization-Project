import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')


project='Text Summarization Project'


list_of_files=[
     "github/workflow/.gitkeep",
    f"src/Text Summarization Project/__init__.py",
    f"src/Text Summarization Project/conponents/__init__.py",
    f"src/Text Summarization Project/utils/__init__.py",
    f"src/Text Summarization Project/utlis/common.py",
    f"src/Text Summarization Project/logging/__init__.py",
    f"src/Text Summarization Project/config/__init__.py",
    f"src/Text Summarization Project/config/configuration.py",
    f"src/Text Summarization Project/pipeline/configuration.py",
    f"src/Text Summarization Project/__init__.py",
    f"src/Text Summarization Project/__init__.py",
    f"src/Text Summarization Project/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]



for filepath in list_of_files:
    filepath=Path(filepath)

    # Separate the file and folder
    filedir,filename=os.path.split(filepath)

    # Now lets check file directory is empty or not 
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
        logging.info(f"Creating empty file:{filepath}")


    else:
        logging.info(f"{filename} is already exists")