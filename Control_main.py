from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BCM)

def GPIO_setup():
    GPIO.setup(5, GPIO.OUT)
    GPIO.setup(6, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(19, GPIO.OUT)
    GPIO.setup(12, GPIO.OUT)
    
def forward():
    GPIO.output(5, GPIO.HIGH)
    GPIO.output(6, GPIO.LOW)
    GPIO.output(13, GPIO.HIGH)
    GPIO.output(19, GPIO.LOW)

def turn_right():
    GPIO.output(5, GPIO.HIGH)
    GPIO.output(6, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(19, GPIO.HIGH)

def turn_left():
    GPIO.output(5, GPIO.LOW)
    GPIO.output(6, GPIO.HIGH)
    GPIO.output(13, GPIO.HIGH)
    GPIO.output(19, GPIO.LOW)
    

def backward():
    GPIO.output(5, GPIO.LOW)
    GPIO.output(6, GPIO.HIGH)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(19, GPIO.HIGH) 

def stop():
    GPIO.output(5, GPIO.LOW)
    GPIO.output(6, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(19, GPIO.LOW)

class SimpleEcho(WebSocket):

    def handleMessage(self):
        # echo message back to client
        self.sendMessage(self.data)
        # print(self.data)

        if self.data == 'w':
            forward()
        elif self.data == 's':
            backward()
        elif self.data == 'a':
            turn_left()
        elif self.data == 'd':
            turn_right()
        else: 
            stop()

    def handleConnected(self):
        print(self.address, 'connected')

    def handleClose(self):
        print(self.address, 'closed')

GPIO_setup()
server = SimpleWebSocketServer('', 8765, SimpleEcho)
server.serveforever()