import websockets
import ssl
import pathlib
import argparse
import asyncio


class WebsocketClient():

    def __init__(self, uri: str):
        self.uri = uri

    async def connect(self):
        self.wsocket = await websockets.connect(self.uri)
        return self.wsocket

    async def send(self, name):
        print("Sending 'hello' from client")
        await self.wsocket.send(name)
        print(f"Sent: {name}")

        print("Receiving...")
        resp = await self.wsocket.recv()
        print(f"Received: {resp}")


if __name__ == "__main__":
    argsparser = argparse.ArgumentParser(description="Started Client")
    argsparser.add_argument("-u", "--uri",
                            required=True, help="Hostname is required!")

    args = argsparser.parse_args()
    wsocket_client = WebsocketClient(args.uri)
    asyncio.get_event_loop().run_until_complete(wsocket_client.connect())
    asyncio.get_event_loop().run_until_complete(wsocket_client.send("GGWPPP"))

    while True:
        print("Enter input: ")
        wsocket_client.send()
        wsocket_client.wsocket
