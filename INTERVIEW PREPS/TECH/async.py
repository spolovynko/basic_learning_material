import asyncio

async def fetch_data():
    await asyncio.sleep(1)  # Simulates a long-running operation
    return "Data fetched!"

async def main():
    result = await fetch_data()
    print(result)

asyncio.run(main())  # The program continues during the "sleep".