import os
import asyncio
import logging


async def main():

    logging.basicConfig(level=logging.INFO)

    async def sub_task():
        logging.info('sub_task: enter')    
        try:    
            while True:
                await asyncio.sleep(1)
                logging.info('some_task: action')
        finally:
            logging.info('sub_task: cleanup')    
            await asyncio.sleep(3)
            logging.info('sub_task: cleanup generates exception')    
            raise ValueError()
            logging.info('sub_task: cleanup end')    
    
    task = asyncio.create_task(sub_task())
                         
    try:
        while True:
            await asyncio.sleep(1)
    except Exception as e:
        logging.info(f"Main: exception {repr(e)} received: something went wrong: cancelling sub-task")
        task.cancel()
    finally:
        logging.info("Main: cleanup")
        try:
            await task
        except Exception as e:
            logging.info(f"Main: catched exception {repr(e)} from await sub_task")