import os
from cloudlink import server

def main():
    # O Render usa a porta 10000 ou o que estiver na variável PORT
    porta = int(os.environ.get("PORT", 8080))
    
    # Inicializa o servidor
    cl = server()
    
    print(f"Servidor Cloudlink iniciando na porta {porta}...")
    
    # No Cloudlink 4, para evitar o erro de 'event loop', 
    # chamamos o run() direto, sem o asyncio.run por fora.
    cl.run(ip="0.0.0.0", port=porta)

if __name__ == "__main__":
    main()
