from services.deepseek_service import DeepSeekService
from utils.helpers import print_message

service = DeepSeekService()

def mi_funcion_llm(pregunta):
    respuesta = service.generate_response(pregunta)
    return respuesta