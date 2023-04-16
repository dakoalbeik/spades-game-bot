import threading

import eventlet
import socketio

from src.spades_env import SpadesEnv

eventlet.monkey_patch()

sio = socketio.Server(cors_allowed_origins='http://127.0.0.1:5173')
app = socketio.WSGIApp(sio)

games = {}


def send_update(sid, data):
    sio.emit("new-state", data, room=sid)


@sio.event
def connect(sid, environ):
    print('Client connected ', sid)
    games[sid] = SpadesEnv(emit=lambda data: send_update(sid, data))
    # Create a new thread to run the game simulation
    game_thread = threading.Thread(target=games[sid].play_game)
    game_thread.start()
    sio.emit("msg", "game created on connection")


@sio.event
def disconnect(sid):
    print('disconnect ', sid)
    games.pop(sid)


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('localhost', 4000)), app)
