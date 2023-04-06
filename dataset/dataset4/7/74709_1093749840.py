from datetime import datetime
from asyncio import Task

next(iter(datetime.now, None))
next(iter(Task.all_tasks, None))