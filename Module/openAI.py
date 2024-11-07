import os
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from Module.prompt_template import prompt


os.environ["OPENAI_API_KEY"]

model = ChatOpenAI(
    model="gpt-4")

parser = StrOutputParser()


def translate() -> str:
    
    tipo_de_reporte = ['una retroalimentación hacia la persona','un reporte']
    nivel_de_analisis = ['tutor','coordinador programa educativo','coordinador institución educativa','coordinador region','coordinador pais']

    detalles_especificos = ['','los datos son la media, desviación estandar, moda']

    objetivos_informe = ['una retroalimentación','un reporte']
    promptTemplate = prompt()

    datos = {
      "Comunicación efectiva":100,
      "Dominio del contenido":80,
      "Habilidad para motivar":40,
      "Capacidad de evaluación":35,
      "Innovación en la enseñanza":86
    }
    chain = promptTemplate | model | parser
    
    
    return chain.invoke({
        "tipo_de_reporte": tipo_de_reporte[0],
        "lector": nivel_de_analisis[0],
        "nivel_de_analisis": nivel_de_analisis[0],
        "detalles_especificos": detalles_especificos[0],
        "objetivo_informe": objetivos_informe[0],
        "datos": datos
    })