import cv2
import time
from os import listdir
from os.path import isdir, isfile, join

face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')     

def merge():
    data_path = 'faces/'
    model_dirs = [f for f in listdir(data_path) if isdir(join(data_path,f))]
    
    models = {}
    for model in model_dirs:
        path = model + ".xml"
        if not isfile(path):
            continue
        result = cv2.face.LBPHFaceRecognizer_create()
        result.read(path)

        models[model] = result

    return models

def face_detector(img, size = 0.5):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray,1.3,5)
        if faces is():
            return img,[]
        for(x,y,w,h) in faces:
            cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,255),2)
            roi = img[y:y+h, x:x+w]
            roi = cv2.resize(roi, (200,200))
        return img,roi


def run(models):    
    cap = cv2.VideoCapture(0)
    myTime = 0
    
    while True:

        startTime = time.time()

        ret, frame = cap.read()
        image, face = face_detector(frame)
        try:            
            min_score = 999
            min_score_name = ""
            
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

            for key, model in models.items():
                result = model.predict(face)                
                if min_score > result[1]:
                    min_score = result[1]
                    min_score_name = key
                           
            if min_score < 500:
                confidence = int(100*(1-(min_score)/300))
                display_string = str(confidence)+'% Confidence it is ' + min_score_name
            cv2.putText(image,display_string,(50,120), cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,1),2)
            cv2.putText(image, 'cogn_time='+str(round(myTime, 2)), (40, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            if confidence >= 85:
                if myTime >= 2:
                    cv2.putText(image, "Unlocked : " + min_score_name, (120, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                    print(min_score_name)
                cv2.imshow('Face Cropper', image)

            else:
                cv2.putText(image, "Locked", (120, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                cv2.imshow('Face Cropper', image)
                myTime = 0

        except:
            cv2.putText(image, "Face Not Found", (120, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            cv2.imshow('Face Cropper', image) 
            myTime = 0
            pass
        
        if cv2.waitKey(1)==13:
            break

        endTime = time.time()
        myTime+=endTime-startTime
  
    cap.release()
    cv2.destroyAllWindows()

while True:
    models = merge()
    run(models)