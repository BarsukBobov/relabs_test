from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    i=0
    while True:
        data = await websocket.receive_json()
        i+=1
        await websocket.send_json(
            {
                "id": i,
                "message": data["message"],
            }
        )