import asyncio
import websockets
import ast
import time
import json

# websocket address for the cryptocurrency exchange OKEx
url = "wss://ws.okex.com:8443/ws/v5/public"

# function to download orderbook data, using websocket asynchronously
async def ws_orderbook5(crypto_pair):
    while True:
            try:
                async with websockets.connect(url) as ws:
                    channels = [{'channel': 'books5', 'instId': f'{crypto_pair}'}]
                    sub_param = {"op": "subscribe", "args": channels}
                    sub_str = json.dumps(sub_param)
                    await ws.send(sub_str)
                    print(f"send: {sub_str}")
                    res = await asyncio.wait_for(ws.recv(), timeout=25)

                    while True:
                        try:
                            res = await asyncio.wait_for(ws.recv(), timeout=25)
                            res = ast.literal_eval(res) 
                            print(f"{crypto-pair} : Most favorable ask price is {res['data'][0]['asks'][0][0]}")
                            
                            time.sleep(1)

                        except (asyncio.TimeoutError, websockets.exceptions.ConnectionClosed) as e:
                            try:
                                await ws.send('ping')
                                print("")
                                print("ping")
                                res = await ws.recv()
                                continue
                            except Exception as e:
                                print("Failure due to an unknown error. Stopped working")
                                break
            except Exception as e:
                print("Failure due to an unknown error. Try working again")
                continue