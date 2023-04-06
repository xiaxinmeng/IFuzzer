import asyncio

import sys


async def run_stockfish():
    STOCKFISH_PATH = r'C:\root\chess\stockfish\stockfish 9\stockfish_9_x64_bmi2.exe'

    stockfish = await asyncio.subprocess.create_subprocess_exec(
        STOCKFISH_PATH,
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

    stockfish.stdin.write('uci'.encode())

    while True:
        # BUG? - blocks at this line - no output
        line = await stockfish.stdout.read()
        print(line)