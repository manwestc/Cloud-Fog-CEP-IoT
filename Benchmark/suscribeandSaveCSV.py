import paho.mqtt.client as mqtt
import threading
import json
import datetime
from threading import Thread, Lock
import sys

mutex = Lock()
talarmas=0
Lalarmas = int(sys.argv[1])

def on_connect(client, userdata, flags, rc):
    print("GIO Connected with result code "+str(rc))
    client.subscribe("Alarma/Alarma/+")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    llego = str(datetime.datetime.now())
    mtopic = (msg.topic).split("/")
    mutex.acquire()
    nmsg = str(msg.payload, 'utf-8')
    try:
        global talarmas
        global Lalarmas
        mjson = json.loads(nmsg)
        f = open("latencymobile/"+mtopic[2]+str(Lalarmas)+".csv", "a")
        f.write(str(mjson['timestamp1'])+','+mjson['timestamp2']+","+llego+"\n")
        talarmas = talarmas + 1
        f.close()
        if talarmas == (Lalarmas*10) :
            print ("Cambio archivo "+str(talarmas)+" "+str(datetime.datetime.now()))
            Lalarmas = Lalarmas + 25
            talarmas = 0
    except ValueError as error:
        print("exp json "+str(error))
    mutex.release()


def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    username   = "CTIC-SMARTCITY"
    password   = "YTICTRAMS-CITC"
    # set username and password
    client.username_pw_set(username, password)
    client.connect("localhost", 1883, 60)

    client.loop_forever()

if __name__ == "__main__":
    main()
