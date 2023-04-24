from typing import List, Union
from googletrans import Translator
from fastapi import FastAPI
from pydantic import BaseModel


translator = Translator()
app = FastAPI()

class Data(BaseModel):
    text: str
    src: str 
    dest: str

# class Bulkdata(BaseModel):
#     text_arr: List[str] = []
#     src: str 
#     dest: str

@app.get("/")
async def root():
    return {"message": "welcome to translate api"}


@app.post("/translate/")
async def translate(data: Data):
    # 
    print(data)
    translations = translator.translate(data.text, src=data.src, dest=data.dest)
    data = data.dict()
    data["translation"] = translations.text
    return data

# @app.post("/translate/bulk/")
# async def translate_bulk(data: Bulkdata):
    
#     print(data.text_arr)
#     # translations = translator.translate(data.text_arr, dest=data.dest)
#     data = data.dict()
#     return data

text_arrrr = ["what is wrong", "with you"]
translations = translator.translate("this is test", dest="hi")

print(translations)