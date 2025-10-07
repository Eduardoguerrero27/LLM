"""
Ejemplos de uso del servicio DeepSeek
"""

from config.settings import Config
from services.deepseek_service import DeepSeekService
from utils.helpers import print_message

def ejemplo_consulta_simple():
    """Ejemplo de consulta simple"""
    print("🔍 Ejemplo 1: Consulta Simple")
    
    service = DeepSeekService()
    respuesta = service.generate_response(
        "Explica qué es machine learning en un párrafo",
        temperature=0.5
    )
    
    print_message("user", "Explica qué es machine learning en un párrafo")
    print_message("assistant", respuesta)

def ejemplo_conversacion():
    """Ejemplo de conversación multi-turno"""
    print("\n💬 Ejemplo 2: Conversación")
    
    service = DeepSeekService()
    
    conversacion = [
        {"role": "system", "content": "Eres un experto en tecnología helpful."},
        {"role": "user", "content": "¿Qué es Python?"},
        {"role": "assistant", "content": "Python es un lenguaje de programación interpretado, de alto nivel y de propósito general."},
        {"role": "user", "content": "¿Y qué frameworks web populares tiene?"}
    ]
    
    respuesta = service.multi_turn_conversation(conversacion)
    print_message("user", "¿Y qué frameworks web populares tiene?")
    print_message("assistant", respuesta)

def ejemplo_creativo():
    """Ejemplo con alta temperatura para creatividad"""
    print("\n🎨 Ejemplo 3: Modo Creativo")
    
    service = DeepSeekService()
    respuesta = service.generate_response(
        "Escribe un poema corto sobre la inteligencia artificial",
        temperature=0.9,
        max_tokens=150
    )
    
    print_message("user", "Escribe un poema corto sobre la inteligencia artificial")
    print_message("assistant", respuesta)

if __name__ == "__main__":
    # Validar configuración primero
    try:
        Config.validate_config()
        print("✅ Configuración validada")
        
        # Ejecutar ejemplos
        ejemplo_consulta_simple()
        ejemplo_conversacion()
        ejemplo_creativo()
        
    except Exception as e:
        print(f"❌ Error: {e}")