async def _preconfigure(app: web.Application) -> None:
    setup_db()
    # asyncio.create_task(WeightSource.listen_scales('/dev/ttyACM0', 9600)
    asyncio.create_task(handle_weight_event_creation()) # coroutine prints WEIGHT <int>
    await create_track_tasks()

async def create_track_tasks():
    asyncio.create_task(track_scales_availability())
    asyncio.create_task(track_crm_availability())

async def track_scales_availability():
    async for weight in WeightSource():
        print(weight)