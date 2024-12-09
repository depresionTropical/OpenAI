from Module.openAI import make_analysis

data = {
        "Comunicación efectiva": 100,
        "Dominio del contenido": 80,
        "Habilidad para motivar": 40,
        "Capacidad de evaluación": 35,
        "Innovación en la enseñanza": 86
    }
respont = make_analysis(data= data, report = 'nacional', referencia = 'constructo')

print(respont)