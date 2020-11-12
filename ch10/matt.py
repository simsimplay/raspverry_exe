
#-*- coding: utf-8 -*-

import paho.mqtt.client as mqtt
from flask import Flask, render_template, request

app = Flask(__name__)

mqttc = mqtt.Client()
mqttc.connect("localhost", 1883, 60)
mqttc.loop_start()

led = {'name' : 'LED pin', 'state' : 'ON'}

@app.route('/')
def main():
    templateData = {
        'led' : led
    }
    return render_template('main.html', **templateData)


@app.route("/DED/<action>")
def action(action):
    if action == 'on':
        mqttc.publish('inTopic', '1')
        led['state'] = 'ON'
        message = "LED on."

    if action == 'off':
        mqttc.publish('inTopic', '0')
        led['state'] = 'OFF'
        message = "LED off."

    templateData = {
        'message' : message, 
        'led' : led
    }

    return render_template('main.html', **templateData)

if __name__=='__main__':
    app.run(host='0.0.0.0', debug=False)