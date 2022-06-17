import speech_recognition as sr

from gpiozero import AngularServo
from time import sleep
servo1 =AngularServo(14, min_angle=0, max_angle=180,min_pulse_width=0.0004, max_pulse_width=0.0026)
servo2 =AngularServo(15, min_angle=0, max_angle=180,min_pulse_width=0.0004, max_pulse_width=0.0026)
servo3 =AngularServo(18, min_angle=0, max_angle=180,min_pulse_width=0.0004, max_pulse_width=0.0026)
servo4 =AngularServo(23, min_angle=-180, max_angle=200,min_pulse_width=0.0004, max_pulse_width=0.0026)
servo5 =AngularServo(24, min_angle=-180, max_angle=200,min_pulse_width=0.0004, max_pulse_width=0.0026)


def left():
    print("lifting the left object")
    servo1.angle=115
    sleep(1)
    servo2.angle=10
    sleep(1)
    servo5.angle=0
    sleep(1)
    servo4.angle=190
    sleep(1)
    servo3.angle=20
    sleep(1)
    servo5.angle=-180
    sleep(1)
    servo3.angle=40
    sleep(1)
    servo4.angle=0
    sleep(1)
    servo1.angle=0
    sleep(1)
    servo5.angle=0
    
def right():
    print("lifting the right object")
    servo1.angle=75
    sleep(1)
    servo2.angle=10
    sleep(1)
    servo5.angle=0
    sleep(1)
    servo4.angle=190
    sleep(1)
    servo3.angle=20
    sleep(1)
    servo5.angle=-180
    sleep(1)
    servo3.angle=40
    sleep(1)
    servo4.angle=0
    sleep(1)
    servo1.angle=170
    sleep(1)
    servo5.angle=0
    


def mapper(otf):
        
        with open("testop.txt") as txt:
            lines = [line for line in txt]
        process_names = [line.split()[-1] for line in lines[1:]]
        #print(process_names)
        for i in range(9,len(process_names),13):
           a = process_names[i][1:-1]

           if a == otf:
            co = process_names[i-8]
            
            if(int(co)>200):
                left()
            else:
                right()
        
        




 r=sr.Recognizer()
 
 with sr.Microphone() as source:
     print("speak anything : ")
     audio=r.listen(source)
 
     def checker(Sliceddata): #checks for the object is there in stored data or not
         StoredData=['bottol','cup'] 
         for i in Sliceddata:
             for j in StoredData:
                 if(i==j):
                     #print('Object is '+i)
                     # now pass that i ( object ) to the image recognition software
                     mapper(i)
         else:
             print("sorry i am not trained for that yet!!!!!!!!!!1")
     try:
         text=r.recognize_google(audio)
         print(type(text))
         print('You said: {}'.format(text))
         Sliceddata=text.split()
         # print(Sliceddata)
         checker(Sliceddata) # passing the sliced tts to the checker function
     except:
         print("sorry cout not recognize you voice ")

object_name=input('Enter the object name');
mapper(object_name)
