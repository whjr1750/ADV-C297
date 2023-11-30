from flask import Flask, render_template

from paho.mqtt import client as mqtt_client

app = Flask(__name__)

broker = 'broker.emqx.io'
port = 1883
topic = "topicName/iot"

client_id = 'test'
username = 'emqx'
password = ''

def connect_mqtt():
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.connect(broker, port)
    return client

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main', methods=['POST'])
def main():
    return render_template('main.html')

@app.route('/1', methods=['POST'])
def release(): 
    release_test()
    return render_template('1.html')

def release_test():
    client = connect_mqtt()
    client.loop_start()

@app.route('/2', methods=['POST'])
def engine():
    engine_test()
    return render_template('2.html')

def engine_test():
    client = connect_mqtt()
    client.loop_start()

@app.route('/3', methods=['POST'])
def activate():
    activate_test()
    return render_template('3.html')

def activate_test():
    client = connect_mqtt()
    client.loop_start()

@app.route('/4', methods=['POST'])
def ignite():
    ignite_test()
    return render_template('4.html')

def ignite_test():
    client = connect_mqtt()
    client.loop_start()

@app.route('/5', methods=['POST'])
def vent():
    vent_test()
    return render_template('5.html')

def vent_test():
    client = connect_mqtt()
    client.loop_start()

@app.route('/6', methods=['POST'])
def srb():
    srb_test()
    return render_template('6.html')

def srb_test():
    client = connect_mqtt()
    client.loop_start()

if __name__ == "__main__":
    app.run(port=5001)





