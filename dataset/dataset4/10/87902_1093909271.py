t0 = create_task(task("T0", 10))
print("starting tasks ...")
await t0
t1 = create_task(task("T1", 10))
await t1