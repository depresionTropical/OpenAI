from dotenv import load_dotenv
import os
# Eliminar la variable de entorno si existe
if "OPENAI_API_KEY" in os.environ:
    del os.environ["OPENAI_API_KEY"]
# Ruta completa al archivo .env
dotenv_path = "/home/hugo/Documents/Projects/OpenAI/.env"
load_dotenv(dotenv_path=dotenv_path)

# Verificar la clave cargada
openai_api_key = os.getenv("OPENAI_API_KEY")
if openai_api_key:
    print("Clave API cargada correctamente:", openai_api_key[:5] + "..." + openai_api_key[-5:])
else:
    print("Error: No se pudo cargar la clave API.")
