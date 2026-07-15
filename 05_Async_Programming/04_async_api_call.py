import asyncio

async def fetch_user():
    print("Fetching User Data...")
    await asyncio.sleep(2)
    return "User Data"

async def fetch_orders():
    print("Fetching Orders...")
    await asyncio.sleep(3)
    return "Order Data"

async def main():

    user = asyncio.create_task(fetch_user())
    orders = asyncio.create_task(fetch_orders())

    print("Waiting for API responses...")

    user_data = await user
    order_data = await orders

    print(user_data)
    print(order_data)

asyncio.run(main())