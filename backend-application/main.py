from config.settings.settings import app





from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from dbs.mongo.queries.user_query import DBQuery
import json



# @app.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     print("connected")
#     while True:
#         data = DBQuery().find(
#             collection='groups'
#         )
#         data = json.dumps(data)
#         print(data)
#         await websocket.send_text(data)



