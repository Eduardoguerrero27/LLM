#!/usr/bin/env python3
"""
LLM Client para DeepSeek API
"""

import os
import json
from rich.console import Console
from rich.prompt import Prompt, Confirm
from rich.panel import Panel  # ✅ Importación faltante
from config.settings import Config
from services.deepseek_service import DeepSeekService
from utils.helpers import print_message, loading_animation, format_conversation

console = Console()

class DeepSeekLLMClient:
    """Cliente interactivo para DeepSeek LLM"""
    
    def __init__(self):
        try:
            Config.validate_config()
            self.service = DeepSeekService()
            console.print("✅ [green]Configuración validada correctamente[/green]")
        except Exception as e:
            console.print(f"❌ [red]Error de configuración: {e}[/red]")
            exit(1)
    
    def single_query_mode(self):
        """Modo de consulta única"""
        console.print("\n🎯 [bold]Modo Consulta Única[/bold]")
        console.print("Escribe 'quit' para salir\n")
        
        while True:
            prompt = Prompt.ask("👤 Tu pregunta")
            
            if prompt.lower() in ['quit', 'exit', 'salir']:
                break
            
            if not prompt.strip():
                continue
            
            try:
                with console.status("[bold green]Pensando...[/bold green]"):
                    response = self.service.generate_response(
                        prompt,
                        system_message="Eres un asistente útil y amable. Responde en el mismo idioma del usuario.",
                        temperature=0.7
                    )
                
                print_message("assistant", response)
                
            except Exception as e:
                console.print(f"❌ [red]Error: {e}[/red]")
    
    def conversation_mode(self):
        """Modo conversación continua"""
        console.print("\n💬 [bold]Modo Conversación[/bold]")
        console.print("Escribe 'quit' para salir o 'clear' para limpiar la conversación\n")
        
        conversation = []
        system_message = "Eres un asistente conversacional inteligente. Mantén conversaciones naturales y útiles."
        
        conversation.append({"role": "system", "content": system_message})
        
        while True:
            user_input = Prompt.ask("👤 Tú")
            
            if user_input.lower() in ['quit', 'exit', 'salir']:
                break
            
            if user_input.lower() == 'clear':
                conversation = [conversation[0]]  # Mantener solo el system message
                console.print("🔄 Conversación limpiada")
                continue
            
            conversation.append({"role": "user", "content": user_input})
            
            try:
                with console.status("[bold green]Pensando...[/bold green]"):
                    response = self.service.multi_turn_conversation(
                        conversation,
                        temperature=0.7
                    )
                
                conversation.append({"role": "assistant", "content": response})
                print_message("assistant", response)
                
            except Exception as e:
                console.print(f"❌ [red]Error: {e}[/red]")
                conversation.pop()  # Remove the failed user message
    
    def batch_processing_mode(self):
        """Procesamiento por lotes"""
        console.print("\n📦 [bold]Modo Procesamiento por Lotes[/bold]")
        
        prompts = [
            "Explica la inteligencia artificial en 50 palabras",
            "¿Cuáles son las ventajas de Python?",
            "Dame 3 consejos para aprender programación"
        ]
        
        for i, prompt in enumerate(prompts, 1):
            console.print(f"\n📝 Procesando prompt {i}/3...")
            print_message("user", prompt)
            
            try:
                with console.status("[bold green]Procesando...[/bold green]"):
                    response = self.service.generate_response(prompt)
                
                print_message("assistant", response)
                
            except Exception as e:
                console.print(f"❌ [red]Error en prompt {i}: {e}[/red]")
    
    def run(self):
        """Ejecuta la aplicación principal"""
        console.print(Panel.fit(
            "🤖 [bold blue]DeepSeek LLM Client[/bold blue]\n"
            "Interfaz para interactuar con modelos de lenguaje de DeepSeek",
            title="Bienvenido"
        ))
        
        while True:
            console.print("\n🔍 [bold]Selecciona un modo:[/bold]")
            console.print("1. 🎯 Consulta única")
            console.print("2. 💬 Conversación continua")
            console.print("3. 📦 Procesamiento por lotes (ejemplo)")
            console.print("4. 🚪 Salir")
            
            choice = Prompt.ask("Tu elección", choices=["1", "2", "3", "4"])
            
            if choice == "1":
                self.single_query_mode()
            elif choice == "2":
                self.conversation_mode()
            elif choice == "3":
                self.batch_processing_mode()
            elif choice == "4":
                console.print("👋 ¡Hasta pronto!")
                break

if __name__ == "__main__":
    client = DeepSeekLLMClient()
    client.run()