# This line doesn`t work
task = loop.create_task(test())
    
# This line works
loop.create_task(test())