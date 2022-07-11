import asyncio
import asyncio
import websockets
import random

EVENTS =  ["R", "P", "S"]

def get_results(choice, userChoice):
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

async def hello(websocket):
    while True:
        try:
            response = await websocket.recv()
            # print(f"<<< {response}")
            choice = random.choice(EVENTS)
            result = get_results(choice, response.upper())
            if result == "Invalid Choice":
                await websocket.send(result)
            else:
                # print(result)
                await websocket.send(f"Computer's choice is: {choice} \n |--> {result}")
        except websockets.ConnectionClosedOK:
            print("Connection terminated by client.")
            break
        except websockets.ConnectionClosedError:
            print("Connection closed.")
            break

async def main():
    async with websockets.serve(hello, "localhost", 8765):
        await asyncio.Future()

if __name__ =="__main__":
    asyncio.run(main())