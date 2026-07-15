import asyncio

async def greet():

    print("Hello")

    await asyncio.sleep(2)

    print("Welcome to Async Programming")


asyncio.run(greet())