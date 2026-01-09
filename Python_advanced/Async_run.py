import asyncio
import time

async def async_task():
    print("Async start")
    await asyncio.sleep(2)
    print("Async end")

def sync_task():
    print("Sync start")
    time.sleep(2)
    print("Sync end")

async def main():
    start = time.time()
    await asyncio.gather(async_task(), async_task())
    print("Async total:", time.time() - start)

start = time.time()
sync_task()
sync_task()
print("Sync total:", time.time() - start)

asyncio.run(main())
