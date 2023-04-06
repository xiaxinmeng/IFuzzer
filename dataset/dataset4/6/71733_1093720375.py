async def display_date(interval, end_time, loop=ai.get_event_loop()):
    label = tk.Label(root)
    label.pack()
    async for tick in timer(interval, end_time, loop):
         label['text'] = datetime.datetime.now()