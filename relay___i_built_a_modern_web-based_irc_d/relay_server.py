import asyncio
import websockets
from rich import print

class RelayServer:
    def __init__(self):
        self.clients = set()

    async def handle_client(self, websocket, path):
        self.clients.add(websocket)
        try:
            async for message in websocket:
                print(f"Received: {message}")
                await self.broadcast(message)
        except websockets.exceptions.ConnectionClosedError:
            print("Client disconnected abruptly")
        finally:
            self.clients.remove(websocket)

    async def broadcast(self, message):
        for client in self.clients:
            try:
                await client.send(message)
            except websockets.exceptions.ConnectionClosedOK:
                print(f"Removed client {client}")

async def main():
    server = RelayServer()
    start_server = websockets.serve(server.handle_client, "localhost", 6789)
    print("Relay Server started on ws://localhost:6789")
    await start_server

if __name__ == "__main__":
    asyncio.run(main())