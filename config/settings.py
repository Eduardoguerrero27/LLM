import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Configuración de la aplicación"""
    
    DEEPSEEK_API_KEY = os.getenv('DEEPSEEK_API_KEY')
    DEEPSEEK_API_BASE = os.getenv('DEEPSEEK_API_BASE', 'https://api.deepseek.com/v1')
    DEEPSEEK_MODEL = os.getenv('DEEPSEEK_MODEL', 'deepseek-chat')
    
    @classmethod
    def validate_config(cls):
        """Valida que la configuración sea correcta"""
        if not cls.DEEPSEEK_API_KEY:
            raise ValueError("❌ DEEPSEEK_API_KEY no encontrada. Verifica tu archivo .env")
        
        if cls.DEEPSEEK_API_KEY.startswith('tu_api_key_aqui'):
            raise ValueError("❌ Reemplaza 'tu_api_key_aqui' con tu API key real")
        
        return True