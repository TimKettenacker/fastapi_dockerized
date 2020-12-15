#!/usr/bin/env python3
# if you want to work with virtualenv, you need to initially follow the steps outlined in
# https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/
# to create a virtualenv, navigate to the project directory and put "python3 -m venv env" in cmd,
# effectively creating a folder "env" containing the environment that can be activated using
# "source env/bin/activate", you can "pip install" packages into that. "pip freeze > requirements.txt"
# creates and stores a list of all packages and their dependencies into the project folder.
# "uvicorn main:app" starts up the server, specifically looking for file named "main" and object "app"
# in it. It can be reached under "http://127.0.0.1:8000" and its OpenAPI description under "/docs".

from enum import Enum
from fastapi import FastAPI

app = FastAPI()


@app.get("/multiply_by_itself/{number}")
# the function right below is in charge of of handling requests that go to path "/" using a GET
# "pydantic" makes sure programmed type hints are validated
def read_item(number: int):
    return {"your input multiplied with itself": number * number}


class BoardgameName (str, Enum):
    catan = "Catan"
    root = "Root"
    wingspan = "wingspan"


@app.get("/enums/{boardgame_name}")
async def get_model(boardgame_name: BoardgameName):
    if boardgame_name == BoardgameName.catan:
        return {"selected game ": boardgame_name, "message": "Hey fellow Catanian!"}

    if boardgame_name.value == "Root":
        return {"selected game ": boardgame_name, "message": "Hey, a war-fox"}

    return {"selected game": boardgame_name, "message": "Have some birds!"}