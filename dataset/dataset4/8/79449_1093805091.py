import asyncio

import sys


async def process_line_reader(process, on_line=None, on_eof=None):
    while not process.stdout.at_eof():
        # BUG? after first line it becomes dead
        line = await process.stdout.readline()
        if on_line is not None:
            on_line(line.decode())
    if on_eof is not None:
        on_eof()
        print('eof')


async def run_stockfish():
    STOCKFISH_PATH = r'C:\root\chess\stockfish\stockfish 10\stockfish_10_x64_bmi2.exe'

    stockfish = await asyncio.subprocess.create_subprocess_exec(
        STOCKFISH_PATH,
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

    stockfish.stdin.write('uci'.encode())

    task = asyncio.create_task(process_line_reader(
        process=stockfish, on_line=lambda line: print(f'{line}')
    ))