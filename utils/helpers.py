from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
import time

console = Console()

def print_message(role: str, content: str):
    """Imprime mensajes formateados con Rich"""
    if role == "user":
        panel = Panel(content, title="👤 Usuario", border_style="blue")
    elif role == "assistant":
        panel = Panel(content, title="🤖 Asistente", border_style="green")
    elif role == "system":
        panel = Panel(content, title="⚙️ Sistema", border_style="yellow")
    else:
        panel = Panel(content, title=role.capitalize())
    
    console.print(panel)

def format_conversation(conversation: list) -> str:
    """Formatea una conversación para display"""
    formatted = ""
    for msg in conversation:
        formatted += f"{msg['role'].capitalize()}: {msg['content']}\n\n"
    return formatted

def loading_animation(duration: int = 2):
    """Muestra una animación de carga"""
    with console.status("[bold green]Procesando...") as status:
        time.sleep(duration)