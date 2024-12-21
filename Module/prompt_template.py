


from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.chat_models import ChatOpenAI

# Configura el modelo LLM
llm = ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo")
# llm = ChatOpenAI(temperature=0.7, model_name="gpt-4")



from langchain.chains import LLMChain, SequentialChain

def generar_reporte(datos, tipo_reporte, llm):
    """
    Genera un reporte o retroalimentación basado en el pipeline definido.
    
    datos: dict
        Diccionario con las claves "competencias", "personalidad" e "inteligencias_multiples".
    tipo_reporte: str
        Tipo de reporte a generar: "retroalimentacion", "reporte_institucional", etc.
    llm: OpenAI
        Instancia del modelo LLM.

    """
    # Paso 0: Definir el tono del reporte
    prompt_tono_retroalimentacion = '''Basado en el análisis de competencias del tutor:
    {json_competencias}
    y personalidad:
    {json_personalidad}
    Escribe una retroalimentación personalizada dirigida a la persona. 
    Debe ser motivadora, clara y profesional.
    Devuelve en formato JSON:
    "fortalezas": "párrafo de fortalezas",
    "oportunidades": "párrafo de áreas de oportunidad",
    "descripcion": "párrafo que describe cómo es la persona".'''

    prompt_tono_reporte = '''Basado en el análisis de competencias del tutor:
    {json_competencias}
    y personalidad:
    {json_personalidad}
    Redacta un reporte dirigido a un superior. El reporte debe tener un tono formal, profesional y centrado en la evaluación global.
    Devuelve en formato JSON:
    "fortalezas": "párrafo de fortalezas relevantes para el tutorado",
    "oportunidades": "párrafo de áreas de oportunidad relevantes para el tutorado",
    "descripcion": "párrafo descriptivo del tutorado basado en sus características generales".'''

    # Paso 1: Generar contexto
    prompt_contexto = '''Los datos se tomaron del tutor que esta participando el PIT en el Tecnológico Nacional de México.
    Definición: 

    El PIT (Programa Institucional de Tutorías) es un programa académico del Tecnológico Nacional de México (TecNM) diseñado para ofrecer un acompañamiento personalizado a los estudiantes, con el fin de fomentar su desarrollo integral. Este programa tiene un enfoque preventivo y formativo, abordando necesidades académicas, personales y sociales, y busca mejorar el rendimiento académico de los estudiantes a través de un seguimiento constante y la intervención de tutores.
    
    El tutor es un docente o mentor asignado dentro del marco del PIT, cuyo papel es guiar y apoyar al estudiante en su formación académica, personal y profesional. El tutor tiene la responsabilidad de identificar las necesidades del tutorado, proporcionarle orientación, y ayudarle a desarrollar competencias clave para su éxito académico y personal. El tutor debe ser un facilitador del aprendizaje, un orientador emocional y un modelo a seguir para el tutorado.'''
    template_contexto = PromptTemplate.from_template(prompt_contexto)
    # cadena_contexto = LLMChain(llm=llm, prompt=template_contexto, output_key="contexto_generado")
    
    # Paso 2: Pipeline de competencias y personalidad
    prompt_competencias = '''Dado el siguiente puntaje en competencias de 0 a 100:
    {competencias}
    Y este contexto:
    {template_contexto}
    Realiza un análisis general:
    1. Describe las principales fortalezas en un párrafo.
    2. Describe las principales áreas de oportunidad en un párrafo.
    Devuelve en formato JSON:
    "fortalezas": "párrafo de fortalezas",
    "oportunidades": "párrafo de áreas de oportunidad".'''
    template_competencias = PromptTemplate.from_template(prompt_competencias)
    cadena_competencias = LLMChain(llm=llm, prompt=template_competencias, output_key="json_competencias")
    
    prompt_personalidad = '''Con los datos de personalidad de 0 a 100:
    {personalidad}
    e inteligencias múltiples:
    {inteligencias_multiples}
    Y este contexto:
    {template_contexto}
    Analisis sobre la personalidad e inteligencias multiples sin mencionar.
    Devuelve en formato JSON:
    "descripcion": "párrafo de analsis de la personalidad e inteligencias multiples".'''
    template_personalidad = PromptTemplate.from_template(prompt_personalidad)
    cadena_personalidad = LLMChain(llm=llm, prompt=template_personalidad, output_key="json_personalidad")
    
    # Paso 3: Generar reporte final basado en el tipo
    if tipo_reporte == "retroalimentacion":
        prompt_tono = prompt_tono_retroalimentacion
    else:
        prompt_tono = prompt_tono_reporte
    
    template_tono = PromptTemplate.from_template(prompt_tono)
    cadena_tono = LLMChain(llm=llm, prompt=template_tono, output_key="reporte_final_json")
    
    # Crear cadena secuencial
    pipeline = SequentialChain(
        chains=[ cadena_competencias, cadena_personalidad, cadena_tono],
        input_variables=["template_contexto","competencias", "personalidad", "inteligencias_multiples"],
        output_variables=["reporte_final_json"],
        verbose=True
    )
    
    # Ejecutar la cadena
    resultado = pipeline.run(
      template_contexto=template_contexto,
        competencias=datos["competencias"],
        personalidad=datos["personalidad"],
        inteligencias_multiples=datos["inteligencias_multiples"]
    )
    return resultado
def generar_reporte_nacional(datos_promedio, llm):
    """
    Genera un reporte nacional basado en el pipeline definido.
    
    datos_promedio: dict
        Diccionario con los promedios nacionales en las claves "competencias", "personalidad" e "inteligencias_multiples".
    llm: OpenAI
        Instancia del modelo LLM.
    """
    # Paso 1: Generar contexto nacional
    prompt_contexto_nacional = '''Crea un contexto enfocado en un reporte nacional:
    Competencias (promedio nacional): {competencias}
    Personalidad (promedio nacional): {personalidad}
    Inteligencias Múltiples (promedio nacional): {inteligencias_multiples}
    Describe las tendencias generales y el enfoque del reporte en un párrafo.'''
    template_contexto_nacional = PromptTemplate.from_template(prompt_contexto_nacional)
    cadena_contexto_nacional = LLMChain(llm=llm, prompt=template_contexto_nacional, output_key="contexto_nacional")

    # Paso 2: Pipeline de análisis nacional
    prompt_competencias_nacional = '''Dado el siguiente promedio nacional en competencias:
    {competencias}
    Y este contexto nacional:
    {contexto_nacional}
    Realiza un análisis general:
    1. Describe las principales fortalezas nacionales en un párrafo.
    2. Describe las principales áreas de oportunidad nacionales en un párrafo.
    Devuelve en formato JSON:
    "fortalezas": "párrafo de fortalezas nacionales",
    "oportunidades": "párrafo de áreas de oportunidad nacionales".'''
    template_competencias_nacional = PromptTemplate.from_template(prompt_competencias_nacional)
    cadena_competencias_nacional = LLMChain(llm=llm, prompt=template_competencias_nacional, output_key="json_competencias_nacional")

    prompt_personalidad_nacional = '''Con los datos promedio nacionales de personalidad:
    {personalidad}
    e inteligencias múltiples:
    {inteligencias_multiples}
    Y este contexto nacional:
    {contexto_nacional}
    Describe cómo son las tendencias generales de las personas en el país en un párrafo general.
    Devuelve en formato JSON:
    "descripcion": "párrafo que describe cómo son las personas en el país".'''
    template_personalidad_nacional = PromptTemplate.from_template(prompt_personalidad_nacional)
    cadena_personalidad_nacional = LLMChain(llm=llm, prompt=template_personalidad_nacional, output_key="json_personalidad_nacional")

    # Paso 3: Generar reporte nacional
    prompt_tono_nacional = '''Usando los siguientes análisis nacionales:
    Competencias: {json_competencias_nacional}
    Personalidad: {json_personalidad_nacional}
    Genera un reporte formal enfocado en tendencias y conclusiones nacionales.
    Devuelve en formato JSON:
    "fortalezas": "párrafo formal de fortalezas nacionales",
    "oportunidades": "párrafo formal de áreas de oportunidad nacionales",
    "descripcion": "párrafo formal con las tendencias nacionales".'''
    template_tono_nacional = PromptTemplate.from_template(prompt_tono_nacional)
    cadena_tono_nacional = LLMChain(llm=llm, prompt=template_tono_nacional, output_key="reporte_nacional_json")

    # Crear cadena secuencial para reporte nacional
    pipeline_nacional = SequentialChain(
        chains=[cadena_contexto_nacional, cadena_competencias_nacional, cadena_personalidad_nacional, cadena_tono_nacional],
        input_variables=["competencias", "personalidad", "inteligencias_multiples"],
        output_variables=["reporte_nacional_json"],
        verbose=True
    )

    # Ejecutar la cadena para el reporte nacional
    resultado_nacional = pipeline_nacional.run(
        competencias=datos_promedio["competencias"],
        personalidad=datos_promedio["personalidad"],
        inteligencias_multiples=datos_promedio["inteligencias_multiples"]
    )
    return resultado_nacional

def generar_reporte_programa_educativo(datos_promedio_programa, llm):
    """
    Genera un reporte basado en el promedio de puntajes dentro de un programa educativo.
    
    datos_promedio_programa: dict
        Diccionario con los promedios del programa educativo en las claves "competencias", "personalidad" e "inteligencias_multiples".
    llm: OpenAI
        Instancia del modelo LLM.
    """
    # Paso 1: Generar contexto para el reporte del programa educativo
    prompt_contexto_programa = '''Crea un contexto enfocado en un reporte para un programa educativo:
    Competencias (promedio del programa educativo): {competencias}
    Personalidad (promedio del programa educativo): {personalidad}
    Inteligencias Múltiples (promedio del programa educativo): {inteligencias_multiples}
    Describe las tendencias generales y el enfoque del reporte en un párrafo.'''
    template_contexto_programa = PromptTemplate.from_template(prompt_contexto_programa)
    cadena_contexto_programa = LLMChain(llm=llm, prompt=template_contexto_programa, output_key="contexto_programa")

    # Paso 2: Pipeline de análisis del programa educativo
    prompt_competencias_programa = '''Dado el siguiente promedio en competencias para el programa educativo:
    {competencias}
    Y este contexto para el programa educativo:
    {contexto_programa}
    Realiza un análisis general:
    1. Describe las principales fortalezas en el programa educativo en un párrafo.
    2. Describe las principales áreas de oportunidad en el programa educativo en un párrafo.
    Devuelve en formato JSON:
    "fortalezas": "párrafo de fortalezas del programa educativo",
    "oportunidades": "párrafo de áreas de oportunidad del programa educativo".'''
    template_competencias_programa = PromptTemplate.from_template(prompt_competencias_programa)
    cadena_competencias_programa = LLMChain(llm=llm, prompt=template_competencias_programa, output_key="json_competencias_programa")

    prompt_personalidad_programa = '''Con los datos promedio del programa educativo en personalidad:
    {personalidad}
    e inteligencias múltiples:
    {inteligencias_multiples}
    Y este contexto para el programa educativo:
    {contexto_programa}
    Describe cómo son las tendencias generales de las personas dentro del programa en un párrafo.
    Devuelve en formato JSON:
    "descripcion": "párrafo que describe cómo son las personas dentro del programa educativo".'''
    template_personalidad_programa = PromptTemplate.from_template(prompt_personalidad_programa)
    cadena_personalidad_programa = LLMChain(llm=llm, prompt=template_personalidad_programa, output_key="json_personalidad_programa")

    # Paso 3: Generar reporte final del programa educativo
    prompt_tono_programa = '''Usando los siguientes análisis del programa educativo:
    Competencias: {json_competencias_programa}
    Personalidad: {json_personalidad_programa}
    Genera un reporte formal enfocado en tendencias y conclusiones del programa educativo.
    Devuelve en formato JSON:
    "fortalezas": "párrafo formal de fortalezas del programa educativo",
    "oportunidades": "párrafo formal de áreas de oportunidad del programa educativo",
    "descripcion": "párrafo formal con las tendencias del programa educativo".'''
    template_tono_programa = PromptTemplate.from_template(prompt_tono_programa)
    cadena_tono_programa = LLMChain(llm=llm, prompt=template_tono_programa, output_key="reporte_programa_json")

    # Crear cadena secuencial para reporte del programa educativo
    pipeline_programa = SequentialChain(
        chains=[cadena_contexto_programa, cadena_competencias_programa, cadena_personalidad_programa, cadena_tono_programa],
        input_variables=["competencias", "personalidad", "inteligencias_multiples"],
        output_variables=["reporte_programa_json"],
        verbose=True
    )

    # Ejecutar la cadena para el reporte del programa educativo
    resultado_programa = pipeline_programa.run(
        competencias=datos_promedio_programa["competencias"],
        personalidad=datos_promedio_programa["personalidad"],
        inteligencias_multiples=datos_promedio_programa["inteligencias_multiples"]
    )
    return resultado_programa

def generar_reporte_institucion(datos_promedio_institucion, llm):
    """
    Genera un reporte basado en el promedio de puntajes dentro de una institución.
    
    datos_promedio_institucion: dict
        Diccionario con los promedios de la institución en las claves "competencias", "personalidad" e "inteligencias_multiples".
    llm: OpenAI
        Instancia del modelo LLM.
    """
    # Paso 1: Generar contexto para el reporte de la institución
    prompt_contexto_institucion = '''Crea un contexto enfocado en un reporte para una institución:
    Competencias (promedio de la institución): {competencias}
    Personalidad (promedio de la institución): {personalidad}
    Inteligencias Múltiples (promedio de la institución): {inteligencias_multiples}
    Describe las tendencias generales y el enfoque del reporte en un párrafo.'''
    template_contexto_institucion = PromptTemplate.from_template(prompt_contexto_institucion)
    cadena_contexto_institucion = LLMChain(llm=llm, prompt=template_contexto_institucion, output_key="contexto_institucion")

    # Paso 2: Pipeline de análisis de la institución
    prompt_competencias_institucion = '''Dado el siguiente promedio en competencias para la institución:
    {competencias}
    Y este contexto para la institución:
    {contexto_institucion}
    Realiza un análisis general:
    1. Describe las principales fortalezas en la institución en un párrafo.
    2. Describe las principales áreas de oportunidad en la institución en un párrafo.
    Devuelve en formato JSON:
    "fortalezas": "párrafo de fortalezas de la institución",
    "oportunidades": "párrafo de áreas de oportunidad de la institución".'''
    template_competencias_institucion = PromptTemplate.from_template(prompt_competencias_institucion)
    cadena_competencias_institucion = LLMChain(llm=llm, prompt=template_competencias_institucion, output_key="json_competencias_institucion")

    prompt_personalidad_institucion = '''Con los datos promedio de la institución en personalidad:
    {personalidad}
    e inteligencias múltiples:
    {inteligencias_multiples}
    Y este contexto para la institución:
    {contexto_institucion}
    Describe cómo son las tendencias generales de las personas dentro de la institución en un párrafo.
    Devuelve en formato JSON:
    "descripcion": "párrafo que describe cómo son las personas dentro de la institución".'''
    template_personalidad_institucion = PromptTemplate.from_template(prompt_personalidad_institucion)
    cadena_personalidad_institucion = LLMChain(llm=llm, prompt=template_personalidad_institucion, output_key="json_personalidad_institucion")

    # Paso 3: Generar reporte final de la institución
    prompt_tono_institucion = '''Usando los siguientes análisis de la institución:
    Competencias: {json_competencias_institucion}
    Personalidad: {json_personalidad_institucion}
    Genera un reporte formal enfocado en tendencias y conclusiones de la institución.
    Devuelve en formato JSON:
    "fortalezas": "párrafo formal de fortalezas de la institución",
    "oportunidades": "párrafo formal de áreas de oportunidad de la institución",
    "descripcion": "párrafo formal con las tendencias de la institución".'''
    template_tono_institucion = PromptTemplate.from_template(prompt_tono_institucion)
    cadena_tono_institucion = LLMChain(llm=llm, prompt=template_tono_institucion, output_key="reporte_institucion_json")

    # Crear cadena secuencial para reporte de la institución
    pipeline_institucion = SequentialChain(
        chains=[cadena_contexto_institucion, cadena_competencias_institucion, cadena_personalidad_institucion, cadena_tono_institucion],
        input_variables=["competencias", "personalidad", "inteligencias_multiples"],
        output_variables=["reporte_institucion_json"],
        verbose=True
    )

    # Ejecutar la cadena para el reporte de la institución
    resultado_institucion = pipeline_institucion.run(
        competencias=datos_promedio_institucion["competencias"],
        personalidad=datos_promedio_institucion["personalidad"],
        inteligencias_multiples=datos_promedio_institucion["inteligencias_multiples"]
    )
    return resultado_institucion

# Datos de entrada
datos_entrada = {
    "competencias": "Habilidad para resolver problemas: 85, Trabajo en equipo: 70, Liderazgo: 65",
    "personalidad": "Introversión: alta, Apertura: media, Responsabilidad: alta",
    "inteligencias_multiples": "Inteligencia lingüística: 90, Inteligencia lógica-matemática: 75, Inteligencia interpersonal: 60"
}

# Llamar a la función para generar retroalimentación
retroalimentacion = generar_reporte(datos_entrada, tipo_reporte="retroalimentacion", llm=llm)
print(retroalimentacion)

# Llamar a la función para generar un reporte institucional
reporte_institucional = generar_reporte(datos_entrada, tipo_reporte="reporte_institucional", llm=llm)
print(reporte_institucional)

# Generar reporte nacional
reporte_nacional = generar_reporte_nacional(datos_entrada, llm=llm)
print(reporte_nacional)

# # Generar reporte de programa educativo
# reporte_programa = generar_reporte_programa_educativo(datos_entrada, llm=llm)
# print(reporte_programa)

# # Generar reporte de institución
# reporte_institucion = generar_reporte_institucion(datos_entrada, llm=llm)
# print(reporte_institucion)



# # prompt de contexto 

# prompt_contexto = '''Dado que se necesita analizar a una persona en relación con estas características:
# - Habilidades de liderazgo efectivas.
# - Alta colaboración.
# - Equilibrio entre inteligencia emocional y analítica.
# Genera una descripción clara y profesional del contexto que deben seguir los análisis.'''
# template_contexto = PromptTemplate.from_template(prompt_contexto)
# cadena_contexto = LLMChain(llm=llm, prompt=template_contexto, output_key="contexto_generado")

# # Análisis de Competencias
# prompt_competencias = '''Dado el siguiente puntaje en competencias:
# {competencias}
# Y este contexto:
# {contexto_generado}
# Realiza un análisis general:
# 1. Describe las principales fortalezas de manera integral en un párrafo.
# 2. Describe las principales áreas de oportunidad en un párrafo.
# Devuelve el análisis en formato JSON con las claves:
# "fortalezas": "párrafo de fortalezas",
# "oportunidades": "párrafo de áreas de oportunidad".'''
# template_competencias = PromptTemplate.from_template(prompt_competencias)
# cadena_competencias = LLMChain(llm=llm, prompt=template_competencias, output_key="json_competencias")


# # Análisis de Personalidad e Inteligencias Múltiples
# prompt_personalidad = '''Con los datos de personalidad:
# {personalidad}
# e inteligencias múltiples:
# {inteligencias_multiples}
# Y este contexto:
# {contexto_generado}
# Describe cómo es la persona en un párrafo general, considerando las características más destacadas.
# Devuelve el análisis en formato JSON con la clave:
# "descripcion": "párrafo que describe cómo es la persona".'''
# template_personalidad = PromptTemplate.from_template(prompt_personalidad)
# cadena_personalidad = LLMChain(llm=llm, prompt=template_personalidad, output_key="json_personalidad")

# prompt_tono = '''Revisa los siguientes análisis:
# 1. {json_competencias}
# 2. {json_personalidad}
# Asegúrate de que el tono sea consistente, profesional y adecuado para un reporte.
# Devuelve todo en un único JSON con las claves:
# "oportunidad": "párrafo revisado de áreas de oportunidad",
# "fortalezas": "párrafo revisado de fortalezas",
# "descripcion": "párrafo descriptivo revisado".'''
# template_tono = PromptTemplate.from_template(prompt_tono)
# cadena_tono = LLMChain(llm=llm, prompt=template_tono, output_key="reporte_final_json")




# # Crear la cadena secuencial
# cadenas = SequentialChain(
#     chains=[cadena_contexto, cadena_competencias, cadena_personalidad, cadena_tono],
#     input_variables=["competencias", "personalidad", "inteligencias_multiples"],
#     output_variables=["reporte_final_json"],
#     verbose=True
# )

# # Datos de entrada
# datos_entrada = {
#     "competencias": "Habilidad para resolver problemas: 85, Trabajo en equipo: 70, Liderazgo: 65",
#     "personalidad": "Introversión: 90, Apertura: 55, Responsabilidad: 92",
#     "inteligencias_multiples": "Inteligencia lingüística: 90, Inteligencia lógica-matemática: 75, Inteligencia interpersonal: 60"
# }

# # Ejecutar la cadena
# resultados = cadenas(datos_entrada)

# # Imprimir el JSON final
# import json
# print(json.dumps(resultados["reporte_final_json"], indent=4, ensure_ascii=False))

# # print(resultados)