import asyncio
import os
from cloudlink import server

async def main():
    # O Render obriga a usar a porta da variável de ambiente PORT
    porta = int(os.environ.get("PORT", 8080))
    
    # Inicializa o motor do Cloudlink
    cl = server()
    
    print(f"Servidor iniciado na porta {porta}")
    
    # No Cloudlink 4, usamos ip="0.0.0.0" para o Render conseguir acessar
    await cl.run(ip="0.0.0.0", port=porta)

if __name__ == "__main__":
    asyncio.run(main())
