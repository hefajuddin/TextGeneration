import os, sys
from pathlib import Path
import logging

listOfFiles=[
    f"data/prompts.json",
    f"models/llm_model.py",
    f"utils/data_loader.py",
    f"utils/text_generator.py",
    "config.py",
    "generate.py",
    "requirements.txt"
]

for path in listOfFiles:
    filepath=Path(path)
    filedir, filename=os.path.split(path)

    if filedir!="":
        os.makedirs(filedir, exist_ok=True)

    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass

    else:
        logging.info("file is already present at :{filepath}" )

