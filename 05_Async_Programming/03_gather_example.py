import asyncio

async def prepare_order(order):

    print(f"Preparing Order {order}")

    await asyncio.sleep(2)

    print(f"Order {order} Ready")


async def main():

    await asyncio.gather(
        prepare_order(1),
        prepare_order(2),
        prepare_order(3)
    )


asyncio.run(main())