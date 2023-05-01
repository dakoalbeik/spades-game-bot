import threading

import eventlet
import socketio
from dqn import create_dqn, train_dqn
import sys

# get the parameter value from the terminal
is_testing = sys.argv[1] == "test" if len(sys.argv) > 1 else False

eventlet.monkey_patch()

sio = socketio.Server(cors_allowed_origins='*')
app = socketio.WSGIApp(sio)

games = {}


def send_update(sid, data):
    sio.emit("new-state", data, room=sid)


@sio.event
def connect(sid, environ):
    print('Client connected ', sid)
    # games[sid] = SpadesEnv()
    env, agent = create_dqn(emit=lambda data: send_update(sid, data), is_testing=is_testing)
    # game_thread = threading.Thread(target=games[sid].play_game)
    # Create a new thread to run the game simulation
    game_thread = threading.Thread(target=train_dqn, args=[env, agent, is_testing])
    game_thread.start()
    sio.emit("msg", "game created on connection")


@sio.event
def disconnect(sid):
    print('disconnect ', sid)
    games.pop(sid)


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('localhost', 4000)), app)
