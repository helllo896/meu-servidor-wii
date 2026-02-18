import asyncio
import os
from cloudlink import server

# O comando 'await' SÓ pode funcionar aqui dentro
async def iniciar():
    porta = int(os.environ.get("PORT", 8080))
    cl = server()
    print(f"Servidor ligado na porta {porta}")
    await cl.run(ip="0.0.0.0", port=porta)

# Isso aqui embaixo chama a função acima do jeito certo
if __name__ == "__main__":
    asyncio.run(iniciar())
