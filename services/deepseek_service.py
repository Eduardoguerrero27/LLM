import requests
import json
from typing import List, Dict, Any, Optional
from config.settings import Config

class DeepSeekService:
    """Servicio para interactuar con la API de DeepSeek"""
    
    def __init__(self):
        self.api_key = Config.DEEPSEEK_API_KEY
        self.api_base = Config.DEEPSEEK_API_BASE
        self.model = Config.DEEPSEEK_MODEL
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
    
    def chat_completion(
        self,
        messages: List[Dict[str, str]],
        max_tokens: int = 1000,
        temperature: float = 0.7,
        stream: bool = False
    ) -> Dict[str, Any]:
        """
        Envía mensajes a la API de DeepSeek y obtiene una respuesta
        
        Args:
            messages: Lista de mensajes en formato [{"role": "user", "content": "mensaje"}]
            max_tokens: Máximo número de tokens en la respuesta
            temperature: Creatividad (0.0-1.0)
            stream: Si se desea streaming de respuesta
        
        Returns:
            Dict con la respuesta de la API
        """
        url = f"{self.api_base}/chat/completions"
        
        payload = {
            "model": self.model,
            "messages": messages,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "stream": stream
        }
        
        try:
            response = requests.post(
                url,
                headers=self.headers,
                json=payload,
                timeout=30
            )
            
            response.raise_for_status()
            return response.json()
            
        except requests.exceptions.RequestException as e:
            raise Exception(f"❌ Error en la API: {str(e)}")
    
    def generate_response(
        self,
        prompt: str,
        system_message: Optional[str] = None,
        **kwargs
    ) -> str:
        """
        Genera una respuesta para un prompt dado
        
        Args:
            prompt: Texto de entrada del usuario
            system_message: Mensaje del sistema para configurar el comportamiento
        
        Returns:
            Respuesta generada por el LLM
        """
        messages = []
        
        if system_message:
            messages.append({"role": "system", "content": system_message})
        
        messages.append({"role": "user", "content": prompt})
        
        response = self.chat_completion(messages, **kwargs)
        
        return response['choices'][0]['message']['content']
    
    def multi_turn_conversation(
        self,
        conversation_history: List[Dict[str, str]],
        **kwargs
    ) -> str:
        """
        Continúa una conversación existente
        
        Args:
            conversation_history: Historial completo de la conversación
        
        Returns:
            Nueva respuesta del asistente
        """
        response = self.chat_completion(conversation_history, **kwargs)
        return response['choices'][0]['message']['content']