import asyncio
 import os
 from cloudlink import server

 async def main():
     # Pega a porta que o Render exige
     port = int(os.environ.get("PORT", 8080))
     
     # Inicializa o servidor Cloudlink 4
     cl = server()
     
     print(f"Servidor Cloudlink com Salas ativo na porta {port}")
     
     # O comando cl.run inicia o protocolo que o TurboWarp reconhece
     # O ip 0.0.0.0 permite que o Render direcione o tráfego para o código
     await cl.run(ip="0.0.0.0", port=port)

 if __name__ == "__main__":
     asyncio.run(main())
