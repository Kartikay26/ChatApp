from flask import *
from flask_socketio import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route("/")
def homepage():
    print("Accessing homepage")
    return render_template("index.html")

@socketio.on('m')
def handle_message(name,message):
    print('received message: \"'+message+"\" from",name)
    emit("c", (name, message), broadcast=True)

@socketio.on('connect')
def test_connect():
    print("Client connected")

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')

socketio.run(app)