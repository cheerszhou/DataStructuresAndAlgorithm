import asyncio
import websockets

async def hello():
    async with websockets.connect('ws://124.222.224.186:8800') as websocket:
        await websocket.send('Hello Server!')
        response = await websocket.recv()
        print('Received from server:', response)

# 运行异步任务
if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(hello())