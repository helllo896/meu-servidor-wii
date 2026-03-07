import asyncio
import os
import cloudlink

async def main():
    port = int(os.environ.get("PORT", 8080))
    
    # Inicializa o servidor
    server = cloudlink.server()
    
    print(f"Servidor Cloudlink iniciando na porta {port}")
    
    # Tenta rodar com 'ip', se falhar tenta com 'host' (para cobrir todas as versões)
    try:
        await server.run(ip="0.0.0.0", port=port)
    except TypeError:
        await server.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    asyncio.run(main())
