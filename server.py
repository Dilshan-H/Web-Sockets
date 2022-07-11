import asyncio
import asyncio
import websockets
import random

EVENTS = ["R", "P", "S"]


def get_results(choice, userChoice):
    """Return the result of the game round based on user choice and computer choice"""
    if userChoice == choice:
        return "DRAW"
    if userChoice == "R":
        if choice == "P":
            return "Paper covers Rock -- YOU LOSE!"
        else:
            return "Rock smashes Scissor -- YOU WIN!"
    elif userChoice == "P":
        if choice == "S":
            return "Scissor cuts Paper -- YOU LOSE!"
        else:
            return "Paper covers Rock -- YOU WIN!"
    elif userChoice == "S":
        if choice == "R":
            return "Rock smashes Scissor -- YOU LOSE!"
        else:
            return "Scissor cuts Paper -- YOU WIN!"
    else:
        return "Invalid Choice"


async def handler(websocket):
    """Handle client requests and send results to the client"""
    while True:
        try:
            response = await websocket.recv()
            choice = random.choice(EVENTS)
            result = get_results(choice, response.upper())
            if result == "Invalid Choice":
                await websocket.send(result)
            else:
                await websocket.send(f"Computer's choice is: {choice} \n |--> {result}")
        except websockets.ConnectionClosedOK:
            print("Connection terminated by client.")
            break
        except websockets.ConnectionClosedError:
            print("Connection closed.")
            break


async def main():
    async with websockets.serve(handler, "localhost", 8765):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
