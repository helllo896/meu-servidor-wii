import asyncio
import os
import websockets

async def handler(websocket):
    # Lógica simples de repetidor (o que um recebe, o outro na sala lê)
    async for message in websocket:
        # Envia a mensagem de volta para todos os conectados (broadcast)
        for conn in connected:
            if conn != websocket:
                await conn.send(message)

connected = set()

async def main():
    # Pega a porta do Render
    port = int(os.environ.get("PORT", 8080))
    
    # Registra quem entra e sai
    async with websockets.serve(handler, "0.0.0.0", port):
        print(f"Servidor Wii rodando na porta {port}")
        await asyncio.Future()  # Mantém o servidor vivo para sempre

if __name__ == "__main__":
    asyncio.run(main())
