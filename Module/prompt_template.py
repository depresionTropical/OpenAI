from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.chat_models import ChatOpenAI

# Configura el modelo LLM
llm = ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo")

# prompt de contexto 

prompt_contexto = '''Dado que se necesita analizar a una persona en relación con estas características:
- Habilidades de liderazgo efectivas.
- Alta colaboración.
- Equilibrio entre inteligencia emocional y analítica.
Genera una descripción clara y profesional del contexto que deben seguir los análisis.'''
template_contexto = PromptTemplate.from_template(prompt_contexto)
cadena_contexto = LLMChain(llm=llm, prompt=template_contexto, output_key="contexto_generado")

# Análisis de Competencias
prompt_competencias = '''Dado el siguiente puntaje en competencias:
{competencias}
Y este contexto:
{contexto_generado}
Realiza un análisis general:
1. Describe las principales fortalezas de manera integral en un párrafo.
2. Describe las principales áreas de oportunidad en un párrafo.
Devuelve el análisis en formato JSON con las claves:
"fortalezas": "párrafo de fortalezas",
"oportunidades": "párrafo de áreas de oportunidad".'''
template_competencias = PromptTemplate.from_template(prompt_competencias)
cadena_competencias = LLMChain(llm=llm, prompt=template_competencias, output_key="json_competencias")


# Análisis de Personalidad e Inteligencias Múltiples
prompt_personalidad = '''Con los datos de personalidad:
{personalidad}
e inteligencias múltiples:
{inteligencias_multiples}
Y este contexto:
{contexto_generado}
Describe cómo es la persona en un párrafo general, considerando las características más destacadas.
Devuelve el análisis en formato JSON con la clave:
"descripcion": "párrafo que describe cómo es la persona".'''
template_personalidad = PromptTemplate.from_template(prompt_personalidad)
cadena_personalidad = LLMChain(llm=llm, prompt=template_personalidad, output_key="json_personalidad")

prompt_tono = '''Revisa los siguientes análisis:
1. {json_competencias}
2. {json_personalidad}
Asegúrate de que el tono sea consistente, profesional y adecuado para un reporte.
Devuelve todo en un único JSON con las claves:
"oportunidad": "párrafo revisado de áreas de oportunidad",
"fortalezas": "párrafo revisado de fortalezas",
"descripcion": "párrafo descriptivo revisado".'''
template_tono = PromptTemplate.from_template(prompt_tono)
cadena_tono = LLMChain(llm=llm, prompt=template_tono, output_key="reporte_final_json")




# Crear la cadena secuencial
cadenas = SequentialChain(
    chains=[cadena_contexto, cadena_competencias, cadena_personalidad, cadena_tono],
    input_variables=["competencias", "personalidad", "inteligencias_multiples"],
    output_variables=["reporte_final_json"],
    verbose=True
)

# Datos de entrada
datos_entrada = {
    "competencias": "Habilidad para resolver problemas: 85, Trabajo en equipo: 70, Liderazgo: 65",
    "personalidad": "Introversión: alta, Apertura: media, Responsabilidad: alta",
    "inteligencias_multiples": "Inteligencia lingüística: 90, Inteligencia lógica-matemática: 75, Inteligencia interpersonal: 60"
}

# Ejecutar la cadena
resultados = cadenas(datos_entrada)

# Imprimir el JSON final
import json
print(json.dumps(resultados["reporte_final_json"], indent=4, ensure_ascii=False))
