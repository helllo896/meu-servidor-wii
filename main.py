import asyncio
import os
from cloudlink import server

async def main():
    # O Render diz qual porta usar através da variável 'PORT'
    # Se não encontrar, ele usa a 8080 por padrão
    port = int(os.environ.get("PORT", 8080))
    
    cl = server()
    print(f"Iniciando servidor na porta {port}...")
    
    # O host 0.0.0.0 é obrigatório para o Render conseguir acessar o código
    await cl.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    asyncio.run(main())
