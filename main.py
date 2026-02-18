import asyncio
import os
from cloudlink import server

async def main():
    # O Render exige o uso da variável de ambiente PORT
    port = int(os.environ.get("PORT", 8080))
    
    # Inicializa o servidor Cloudlink
    cl = server()
    
    # O segredo: a versão 4 do Cloudlink usa cl.run() que já abre o websocket.
    # Usamos o ip 0.0.0.0 para o Render conseguir rotear o tráfego.
    print(f"Iniciando Wii Server na porta {port}")
    await cl.run(ip="0.0.0.0", port=port)

if __name__ == "__main__":
    asyncio.run(main())
    # Inicia o servidor web e o Cloudlink juntos
    await asyncio.gather(
        site.start(),
        cl.run(ip="0.0.0.0", port=port)
    )

if __name__ == "__main__":
    asyncio.run(main())
