import speech_recognition as sr 

r=sr.Recognizer()

with sr.Microphone() as source:
    print("speak anything : ")
    audio=r.listen(source)

    def checker(Sliceddata): #checks for the object is there in stored data or not
        StoredData=['pen','pencil','plate','book','phone'] 
        for i in Sliceddata:
            for j in StoredData:
                if(i==j):
                    print('Object is '+i) # now pass that i ( object ) to the image recognition software
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