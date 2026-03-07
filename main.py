import os
import asyncio
from cloudlink import server

def main():
    # Porta padrão do Render
    porta = int(os.environ.get("PORT", 10000))
    
    # Criamos o servidor
    cl = server()
    
    # --- CONFIGURAÇÕES DE COMPATIBILIDADE ---
    # 1. Permite que o TurboWarp conecte de qualquer lugar
    cl.conns.check_origin = False 
    
    # 2. Força o servidor a ser menos rígido com o protocolo
    print(f"Servidor subindo na porta {porta}...")
    
    # O Cloudlink 4.0 às vezes precisa que o motor asyncio seja 
    # iniciado de forma que não bloqueie o handshake do Scratch.
    cl.run(ip="0.0.0.0", port=porta)

if __name__ == "__main__":
    main()
