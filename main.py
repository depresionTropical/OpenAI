from Module.openAI import make_analysis
import json

data = {
    "informacion_personal": {
        "first_name": "Alexander",
        "last_name": "Knapp",
        "fecha_nacimiento": "1994-03-31",
        "email": "svalentine@example.com",
        "carrera": "Ingenier??a en Sistemas Computacionales"
    },
    "indicador": [
        {
            "nombre": "Interacci??n social",
            "constructos": [
                {
                    "constructo": {
                        "cve_const": 1,
                        "descripcion": "Madurez",
                        "acronimo": "MAD"
                    },
                    "score": 74
                },
                {
                    "constructo": {
                        "cve_const": 2,
                        "descripcion": "Responsabilidad",
                        "acronimo": "RES"
                    },
                    "score": 82
                },
                {
                    "constructo": {
                        "cve_const": 3,
                        "descripcion": "Empat??a",
                        "acronimo": "EMP"
                    },
                    "score": 0
                },
                {
                    "constructo": {
                        "cve_const": 4,
                        "descripcion": "Respeto",
                        "acronimo": "RES"
                    },
                    "score": 2
                },
                {
                    "constructo": {
                        "cve_const": 5,
                        "descripcion": "Compasi??n",
                        "acronimo": "COM"
                    },
                    "score": 22
                },
                {
                    "constructo": {
                        "cve_const": 6,
                        "descripcion": "Tolerancia",
                        "acronimo": "TOL"
                    },
                    "score": 4
                },
                {
                    "constructo": {
                        "cve_const": 7,
                        "descripcion": "Valoraci??n",
                        "acronimo": "VAL"
                    },
                    "score": 5
                },
                {
                    "constructo": {
                        "cve_const": 8,
                        "descripcion": "Discreci??n",
                        "acronimo": "DIS"
                    },
                    "score": 68
                },
                {
                    "constructo": {
                        "cve_const": 9,
                        "descripcion": "Adaptabilidad",
                        "acronimo": "ADA"
                    },
                    "score": 46
                },
                {
                    "constructo": {
                        "cve_const": 10,
                        "descripcion": "Altruismo",
                        "acronimo": "ALT"
                    },
                    "score": 28
                },
                {
                    "constructo": {
                        "cve_const": 11,
                        "descripcion": "Humildad",
                        "acronimo": "HUM"
                    },
                    "score": 90
                },
                {
                    "constructo": {
                        "cve_const": 12,
                        "descripcion": "Habilidades interpersonales",
                        "acronimo": "HAB"
                    },
                    "score": 20
                },
                {
                    "constructo": {
                        "cve_const": 13,
                        "descripcion": "Manejo de grupo",
                        "acronimo": "MAN"
                    },
                    "score": 33
                }
            ],
            "prom_score": 36
        },
        {
            "nombre": "Toma de decisiones",
            "constructos": [
                {
                    "constructo": {
                        "cve_const": 14,
                        "descripcion": "Orientaci??n a la soluci??n",
                        "acronimo": "ORI"
                    },
                    "score": 97
                },
                {
                    "constructo": {
                        "cve_const": 15,
                        "descripcion": "Compromiso",
                        "acronimo": "COM"
                    },
                    "score": 66
                },
                {
                    "constructo": {
                        "cve_const": 16,
                        "descripcion": "Integridad",
                        "acronimo": "INT"
                    },
                    "score": 27
                },
                {
                    "constructo": {
                        "cve_const": 17,
                        "descripcion": "Credibilidad",
                        "acronimo": "CRE"
                    },
                    "score": 73
                },
                {
                    "constructo": {
                        "cve_const": 18,
                        "descripcion": "Proactividad",
                        "acronimo": "PRO"
                    },
                    "score": 59
                },
                {
                    "constructo": {
                        "cve_const": 19,
                        "descripcion": "Planificaci??n",
                        "acronimo": "PLA"
                    },
                    "score": 60
                },
                {
                    "constructo": {
                        "cve_const": 20,
                        "descripcion": "Aptitudes organizativas",
                        "acronimo": "APT"
                    },
                    "score": 81
                }
            ],
            "prom_score": 66
        },
        {
            "nombre": "Autorregulaci??n emocional y afectiva",
            "constructos": [
                {
                    "constructo": {
                        "cve_const": 21,
                        "descripcion": "Flexibilidad",
                        "acronimo": "FLE"
                    },
                    "score": 57
                },
                {
                    "constructo": {
                        "cve_const": 22,
                        "descripcion": "Observaci??n",
                        "acronimo": "OBS"
                    },
                    "score": 57
                },
                {
                    "constructo": {
                        "cve_const": 23,
                        "descripcion": "Resiliencia",
                        "acronimo": "RES"
                    },
                    "score": 12
                },
                {
                    "constructo": {
                        "cve_const": 24,
                        "descripcion": "Autenticidad",
                        "acronimo": "AUT"
                    },
                    "score": 98
                },
                {
                    "constructo": {
                        "cve_const": 25,
                        "descripcion": "Optimismo",
                        "acronimo": "OPT"
                    },
                    "score": 96
                },
                {
                    "constructo": {
                        "cve_const": 26,
                        "descripcion": "Curiosidad",
                        "acronimo": "CUR"
                    },
                    "score": 4
                },
                {
                    "constructo": {
                        "cve_const": 27,
                        "descripcion": "Manejo de afectividad",
                        "acronimo": "MAN"
                    },
                    "score": 37
                },
                {
                    "constructo": {
                        "cve_const": 28,
                        "descripcion": "Mentalidad de crecimiento",
                        "acronimo": "MEN"
                    },
                    "score": 57
                }
            ],
            "prom_score": 52
        },
        {
            "nombre": "Desarrollo personal y aprendizaje",
            "constructos": [
                {
                    "constructo": {
                        "cve_const": 29,
                        "descripcion": "Inter??s",
                        "acronimo": "INT"
                    },
                    "score": 72
                },
                {
                    "constructo": {
                        "cve_const": 30,
                        "descripcion": "Promover desarrollo aut??nomo",
                        "acronimo": "PRO"
                    },
                    "score": 69
                },
                {
                    "constructo": {
                        "cve_const": 31,
                        "descripcion": "Habilidades de pensamiento reflexivo",
                        "acronimo": "HAB"
                    },
                    "score": 44
                }
            ],
            "prom_score": 61
        },
        {
            "nombre": "Inteligencia m??ltiples",
            "constructos": [
                {
                    "constructo": {
                        "cve_const": 32,
                        "descripcion": "L??gico-matem??tico",
                        "acronimo": "L??G"
                    },
                    "score": 86
                },
                {
                    "constructo": {
                        "cve_const": 33,
                        "descripcion": "Intrapersonal",
                        "acronimo": "INT"
                    },
                    "score": 96
                },
                {
                    "constructo": {
                        "cve_const": 34,
                        "descripcion": "Ling????stico",
                        "acronimo": "LIN"
                    },
                    "score": 83
                },
                {
                    "constructo": {
                        "cve_const": 35,
                        "descripcion": "Espacial",
                        "acronimo": "ESP"
                    },
                    "score": 82
                },
                {
                    "constructo": {
                        "cve_const": 36,
                        "descripcion": "Musical",
                        "acronimo": "MUS"
                    },
                    "score": 82
                },
                {
                    "constructo": {
                        "cve_const": 37,
                        "descripcion": "Interpersonal",
                        "acronimo": "INT"
                    },
                    "score": 78
                },
                {
                    "constructo": {
                        "cve_const": 38,
                        "descripcion": "Corporal-cinest??sico",
                        "acronimo": "COR"
                    },
                    "score": 8
                }
            ],
            "prom_score": 73
        },
        {
            "nombre": "Personalidad",
            "constructos": [
                {
                    "constructo": {
                        "cve_const": 39,
                        "descripcion": "Escrupulosidad",
                        "acronimo": "ESC"
                    },
                    "score": 28
                },
                {
                    "constructo": {
                        "cve_const": 40,
                        "descripcion": "Neuroticismo",
                        "acronimo": "NEU"
                    },
                    "score": 38
                },
                {
                    "constructo": {
                        "cve_const": 41,
                        "descripcion": "Extroversi??n",
                        "acronimo": "EXT"
                    },
                    "score": 23
                },
                {
                    "constructo": {
                        "cve_const": 42,
                        "descripcion": "Intelecto",
                        "acronimo": "INT"
                    },
                    "score": 25
                },
                {
                    "constructo": {
                        "cve_const": 43,
                        "descripcion": "Imaginaci??n",
                        "acronimo": "IMA"
                    },
                    "score": 98
                },
                {
                    "constructo": {
                        "cve_const": 44,
                        "descripcion": "Amabilidad",
                        "acronimo": "AMA"
                    },
                    "score": 28
                },
                {
                    "constructo": {
                        "cve_const": 45,
                        "descripcion": "Extraversi??n",
                        "acronimo": "EXT"
                    },
                    "score": 96
                },
                {
                    "constructo": {
                        "cve_const": 46,
                        "descripcion": "Intelecto,Imaginaci??n",
                        "acronimo": "INT"
                    },
                    "score": 3
                }
            ],
            "prom_score": 42
        },
        {
            "nombre": "Inteligencias Multiples",
            "constructos": [
                {
                    "constructo": {
                        "cve_const": 33,
                        "descripcion": "Intrapersonal",
                        "acronimo": "INT"
                    },
                    "score": 96
                },
                {
                    "constructo": {
                        "cve_const": 34,
                        "descripcion": "Ling????stico",
                        "acronimo": "LIN"
                    },
                    "score": 83
                },
                {
                    "constructo": {
                        "cve_const": 35,
                        "descripcion": "Espacial",
                        "acronimo": "ESP"
                    },
                    "score": 82
                },
                {
                    "constructo": {
                        "cve_const": 36,
                        "descripcion": "Musical",
                        "acronimo": "MUS"
                    },
                    "score": 82
                },
                {
                    "constructo": {
                        "cve_const": 37,
                        "descripcion": "Interpersonal",
                        "acronimo": "INT"
                    },
                    "score": 78
                },
                {
                    "constructo": {
                        "cve_const": 38,
                        "descripcion": "Corporal-cinest??sico",
                        "acronimo": "COR"
                    },
                    "score": 8
                },
                {
                    "constructo": {
                        "cve_const": 47,
                        "descripcion": "L??gico-matematico",
                        "acronimo": "L??G"
                    },
                    "score": 23
                },
                {
                    "constructo": {
                        "cve_const": 48,
                        "descripcion": "Spatial",
                        "acronimo": "SPA"
                    },
                    "score": 42
                },
                {
                    "constructo": {
                        "cve_const": 49,
                        "descripcion": "Logical-mathematical",
                        "acronimo": "LOG"
                    },
                    "score": 39
                }
            ],
            "prom_score": 59
        }
    ],
    "retrochatgpt": [
        {
            "texto1": "- *Desarrollo personal y aprendizaje: Este es el área de mayor fortaleza, con una puntuación perfecta de 100. Esto indica que el individuo está altamente motivado para aprender y crecer personalmente.\n  - **Autorregulación emocional y afectiva: Con una puntuación de 94, este individuo muestra una excelente capacidad para manejar sus emociones y afectos de manera efectiva.\n  - **Inteligencias múltiples*: La puntuación de 80 indica una capacidad bastante fuerte en el área de inteligencias múltiples, incluyendo habilidades lingüísticas, lógico-matemáticas, espaciales, entre otras.",
            "texto2": "- *Interacción social: Con una puntuación de 26, esta es un área que requiere atención y esfuerzo para mejorar. El individuo puede necesitar trabajar en habilidades como la comunicación, la empatía y la colaboración.\n  - **Toma de decisiones: Aunque la puntuación de 51 no es necesariamente baja, todavía hay margen de mejora en esta área. El individuo puede beneficiarse de la práctica y el aprendizaje en la toma de decisiones informada y razonada.\n  - **Inteligencias múltiples*: Aunque esta área fue listada como una fortaleza, hay una puntuación adicional de 8 en 'Inteligencias Multiples'. Esto puede ser un error en los datos o puede indicar una puntuación baja en una subcategoría de inteligencias múltiples, lo cual sería una oportunidad de mejora."
        }
    ]
}
response = make_analysis(data= data, report = 'nacional')

with open('salida.json', 'w', encoding='utf-8') as file:
    json.dump(response, file, indent=2, ensure_ascii=False)
print(response)