import asyncio

async def prepare_order(order):

    print(f"Preparing Order {order}")

    await asyncio.sleep(2)

    print(f"Order {order} Ready")


async def main():

    task1 = asyncio.create_task(
        prepare_order(1)
    )

    task2 = asyncio.create_task(
        prepare_order(2)
    )

    await task1
    await task2
