import websocket
import time
import _thread
import argparse
import asyncio
import websockets

class WebsocketServer():

    wsocket = None

    def __init__(self, hostname: str, port: int):
        self.hostname = hostname
        self.port = port

    async def hello(self, websocket, path):
        name = await websocket.recv()
        print(f"< {name}")

        greeting = f"Hello {name}!"

        await websocket.send(greeting)
        print(f"> {greeting}")

    def start(self):
        """Starts the server supporting web socket connections."""
        return websockets.serve(self.hello, self.hostname, self.port)


    #
    # def send_command(self, ws, message: str):
    #     print(message)
    #
    # def send_invalidCommand(self, ws, error: str):
    #     print(error)
    #
    #
    # def on_open(self, ws):
    #     def run(*args):
    #         for i in range(3):
    #             time.sleep(1)
    #             ws.send("Hello %d" % i)
    #         time.sleep(1)
    #         ws.close()
    #         print("thread terminating...")
    #
    #     _thread.start_new_thread(run, ())
    #
    #
    # def run(self):
    #     for i in range(3):
    #         time.sleep(1)
    #         self.wsocket.send("Hello %d" % i)
    #     time.sleep(1)
    #     self.wsocket.close()
    #     print("thread terminating...")
    #
    #
    # def start(self):
    #     self.wsocket.run_forever()


if __name__ == "__main__":
    argsparser = argparse.ArgumentParser(description="Starting server")
    argsparser.add_argument("-host", "--hostname",
                            required=True, help="Hostname is required.")
    argsparser.add_argument("-p", "--port",
                            required=True, help="Port is required.")

    args = argsparser.parse_args()
    wsocket_server = WebsocketServer(args.hostname, args.port)
    socketConnection = wsocket_server.start()
    asyncio.get_event_loop().run_until_complete(socketConnection)
    asyncio.get_event_loop().run_forever()

