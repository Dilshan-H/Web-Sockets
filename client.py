import asyncio
import websockets


async def handler():
    """Handle user input and server requests/responses"""
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        print("-" * 25)
        print("Hello! Welcome User...")
        print("Select choice: R | P | S or Q to quit")
        print("-" * 25)
        while True:
            choice = input("Your choice is...? ")
            choice = choice.strip()
            if choice.lower() == "q":
                break
            await websocket.send(choice)
            result = await websocket.recv()
            print(result)
            print("-" * 25)
        print("Thank You!")

if __name__ == "__main__":
    asyncio.run(handler())
