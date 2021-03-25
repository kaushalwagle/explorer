import RPi.GPIO as GPIO
import keyboard

GPIO.setmode(GPIO.BCM)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)

def reset():
    GPIO.output(5,GPIO.LOW)
    GPIO.output(6,GPIO.LOW)
    GPIO.output(13,GPIO.LOW)
    GPIO.output(19,GPIO.LOW)
    
def forward():
    GPIO.output(5,GPIO.LOW)
    GPIO.output(6,GPIO.HIGH)
    GPIO.output(13,GPIO.HIGH)
    GPIO.output(19,GPIO.LOW)

def stop_robot():
    GPIO.output(5,GPIO.LOW)
    GPIO.output(6,GPIO.LOW)
    GPIO.output(13,GPIO.LOW)
    GPIO.output(19,GPIO.LOW)
    
def backward():
    GPIO.output(5,GPIO.HIGH)
    GPIO.output(6,GPIO.LOW)
    GPIO.output(13,GPIO.LOW)
    GPIO.output(19,GPIO.HIGH)
    
def left():
    GPIO.output(5,GPIO.HIGH)
    GPIO.output(6,GPIO.LOW)
    GPIO.output(13,GPIO.HIGH)
    GPIO.output(19,GPIO.LOW)

def right():
    GPIO.output(5,GPIO.LOW)
    GPIO.output(6,GPIO.HIGH)
    GPIO.output(13,GPIO.LOW)
    GPIO.output(19,GPIO.HIGH)

#https://qmoki89va7.execute-api.us-east-2.amazonaws.com/test/key?up=h&down=b&left=l&right=r

#camera = PiCamera()
#camera.resolution = (1024,768)
#camera.start_preview()

#sleep(2)

while True:
       
       if keyboard.is_pressed('w'):
           forward()
           stop_robot()
       elif keyboard.is_pressed('s'):
           backward()
           stop_robot()
       elif keyboard.is_pressed('a'):
           left()
           stop_robot()
       elif keyboard.is_pressed('d'):
           right()
           stop_robot()
       elif keyboard.is_pressed('x'):
           stop_robot()
           #camera.stop_preview()
       else:
           stop_robot()

    
    #sth = get('http://ec2-3-80-22-87.compute-1.amazonaws.com:8080/products').json()
        
    #for key in sth[0]:
    #   value= sth[0].get(key,'name')
    #   print(key,value)
        
     
