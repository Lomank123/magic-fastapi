from enum import Enum
from fastapi import FastAPI


class ModelName(str, Enum):
    name1 = "name11"
    name2 = "name22"
    name3 = "name33"


app = FastAPI()


@app.get("/")
async def root():
    return {"msg": "This is root."}


@app.get("/magic")
async def magic():
    return {"msg": "magic!"}


# This must be placed before current_magic method because of almost same path
# https://fastapi.tiangolo.com/tutorial/path-params/#order-matters
@app.get("/magic/my")
async def my_magic():
    return {"message": "my magic"}


@app.get("/magic/{magic_id}")
async def current_magic(magic_id: int):
    return {"magic_id": magic_id}


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.name1:
        return {"model_name": f"That's model name: {model_name}"}
    return {"model_name": model_name}


# Path is somehow looks like this:
# http://127.0.0.1:8000/files/%2Fhome%2Ffiles%2Fmt.txt
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
