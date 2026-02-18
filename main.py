import asyncio
from cloudlink import server

async def main():
    # Inicializa o servidor Cloudlink
    cl = server()
    # Roda na porta 8080 (padrão de serviços de nuvem)
    await cl.run(host="0.0.0.0", port=8080)

if __name__ == "__main__":
    asyncio.run(main())
