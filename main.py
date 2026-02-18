import asyncio
import os
from cloudlink import server
from aiohttp import web

async def heartbeat(request):
    return web.Response(text="Servidor Wii Online")

async def main():
    port = int(os.environ.get("PORT", 8080))
    
    # Configura o Servidor Cloudlink
    cl = server()
    
    # Cria um servidor web simples para o Render não dar erro de porta
    app = web.Application()
    app.router.add_get("/", heartbeat)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", port)
    
    print(f"Servidor Wii na porta {port}")
    
    # Inicia o servidor web e o Cloudlink juntos
    await asyncio.gather(
        site.start(),
        cl.run(ip="0.0.0.0", port=port)
    )

if __name__ == "__main__":
    asyncio.run(main())
