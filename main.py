from fastapi import FastAPI

from model.DataStructure import getDataStructure
from model.DataStructureType import DataStructureType
from utils.ReponseBuilder import buildResponse
from model.APIStatus import APIStatus

app = FastAPI()


@app.get("/data_structures")
async def getAllDataStructure():
    dataStructures = []
    for dataStructure in DataStructureType:
        dataStructures.append(dataStructure.id)
    return buildResponse(APIStatus.SUCCESS, dataStructures)

@app.get("/data_structure/{name}")
async def data_structure(name: str):
   return buildResponse(APIStatus.SUCCESS, getDataStructure(DataStructureType[name]))