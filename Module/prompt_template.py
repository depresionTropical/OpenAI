from langchain.chains import LLMChain, SequentialChain
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
  # Prompt para analizar competencias
def prompt(flag = False, data = None, type_report = None): 
  llm = ChatOpenAI(temperature=0.3, model="gpt-4")
  if flag: 
    competence_prompt = ChatPromptTemplate.from_template(
        """
        Actúa como experto en análisis de competencias. Con base en los puntajes proporcionados (de 0 a 100), identifica las fortalezas y áreas de oportunidad.

        Datos:
        {data}

        Genera la respuesta en formato JSON con las claves:
        - "fortaleza": Detalla las competencias más altas y su impacto.
        - "oportunidad": Describe las competencias más bajas y cómo mejorarlas.
        """
    )
    final_report_prompt = ChatPromptTemplate.from_template(
        """
        Combina los siguientes análisis en un informe estructurado para {type_report}:

        - Fortalezas y áreas de oportunidad de competencias: {competence_analysis}

        Devuelve la respuesta en formato JSON con las claves:
        - "fortaleza": Incluye fortalezas combinadas de los análisis.
        - "oportunidad": Incluye áreas de oportunidad combinadas.
        """
    )
    # Cadena para análisis de competencias
    competence_chain = LLMChain(llm=llm, prompt=competence_prompt)
    # Cadena final para generar el reporte completo
    final_chain = SequentialChain(
        chains=[competence_chain],
        input_variables=["data", "type_report"],
        output_variables=["competence_analysis"],
        llm=llm,
        final_prompt=final_report_prompt
    )
    competence_data = data
    competence_analysis = competence_chain.run(data=competence_data)
    report = final_chain.run(
        data=data,
        type_report=type_report,
        competence_analysis=competence_analysis,
    )
  else:
    competence_prompt = ChatPromptTemplate.from_template(
        """
        Actúa como experto en análisis de competencias. Con base en los puntajes proporcionados (de 0 a 100), identifica las fortalezas y áreas de oportunidad.

        Datos:
        {data}

        Genera la respuesta en formato JSON con las claves:
        - "fortaleza": Detalla las competencias más altas y su impacto.
        - "oportunidad": Describe las competencias más bajas y cómo mejorarlas.
        """
    )
  # Prompt para analizar personalidad
    personality_prompt = ChatPromptTemplate.from_template(
        """
        Actúa como psicólogo especializado en análisis de personalidad. Con base en los puntajes proporcionados (de 0 a 100), genera un resumen profesional sobre las características predominantes de la persona.

        Datos de personalidad:
        {data}

        Devuelve un resumen breve en formato texto.
        """
    )
    

    # Prompt para analizar inteligencias múltiples
    intelligence_prompt = ChatPromptTemplate.from_template(
        """
        Actúa como experto en teorías de inteligencias múltiples. Con base en los puntajes proporcionados (de 0 a 100), describe cuáles son las inteligencias más desarrolladas y las menos evidentes de la persona.

        Datos:
        {data}

        Devuelve un resumen breve en formato texto.
        """
    )

    # Prompt para combinar todos los análisis
    final_report_prompt = ChatPromptTemplate.from_template(
        """
        Combina los siguientes análisis en un informe estructurado para {type_report}:

        - Fortalezas y áreas de oportunidad de competencias: {competence_analysis}
        - Resumen de personalidad: {personality_analysis}
        - Resumen de inteligencias múltiples: {intelligence_analysis}

        Devuelve la respuesta en formato JSON con las claves:
        - "fortaleza": Incluye fortalezas combinadas de los análisis.
        - "oportunidad": Incluye áreas de oportunidad combinadas.
        """
    )
    # **3. Define las cadenas**
    # Cadena para análisis de competencias
    competence_chain = LLMChain(llm=llm, prompt=competence_prompt)
    personality_chain = LLMChain(llm=llm, prompt=personality_prompt)
    intelligence_chain = LLMChain(llm=llm, prompt=intelligence_prompt)

    # Cadena final para generar el reporte completo
    final_chain = SequentialChain(
        chains=[competence_chain, personality_chain, intelligence_chain],
        input_variables=["data", "type_report"],
        output_variables=["competence_analysis", "personality_analysis", "intelligence_analysis"],
        llm=llm,
        final_prompt=final_report_prompt
    )
        # Análisis de competencias
    competence_data = data
    competence_analysis = competence_chain.run(data=competence_data)

    # Análisis de personalidad
    personality_data = data
    personality_analysis = personality_chain.run(data=personality_data)

    # Análisis de inteligencias múltiples
    intelligence_data = data
    intelligence_analysis = intelligence_chain.run(data=intelligence_data)

    # Generación del reporte final
    report = final_chain.run(
        data=data,
        type_report=type_report,
        competence_analysis=competence_analysis,
        personality_analysis=personality_analysis,
        intelligence_analysis=intelligence_analysis
    )

  return report