import os
from typing import Literal
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from Module.prompt_template import prompt
import json
import time

os.environ["OPENAI_API_KEY"]

model = ChatOpenAI(
    model="gpt-4",
    temperature=0,)

parser = StrOutputParser()


def make_analysis(
        data:dict, 
        report:Literal['retroalimentación','individual','departamento','institucional','regional','nacional'])-> dict:
    
    if not isinstance(data, dict):
        raise TypeError("El parámetro 'data' debe ser un diccionario.")
    
    if report not in ['retroalimentación','individual','departamento','institucional','regional','nacional']:
        raise ValueError("El parámetro 'report' debe ser 'reporte' o 'retroalimentación'.")

    type_report={
        'retroalimentación':'retroalimentación',
        'individual': 'reporte individual',
        'departamento':'reporte departamento',
        'institucional':'reporte institucional',
        'regional':'reporte regional',
        'nacional':'reporte nacional'
    }

    data = {indicador["nombre"]: indicador["prom_score"] for indicador in data.get("indicador", [])}
    return prompt(flag=True, data=data, type_report=type_report[report])
