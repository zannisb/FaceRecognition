import cv2
import numpy as np
from os import listdir
from os.path import isdir, isfile, join

def train(model,path):
    data_path = 'faces/' + model + '/'
    face_pics = [f for f in listdir(data_path) if isfile(join(data_path,f))]
    
    Training_Data, Labels = [], []
    
    for i, files in enumerate(face_pics):
        image_path = data_path + face_pics[i]
        images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        if images is None:
            continue    
        Training_Data.append(np.asarray(images, dtype=np.uint8))
        Labels.append(i)

    if len(Labels) == 0:
        print("There is no data to train.")
        return None

    Labels = np.asarray(Labels, dtype=np.int32)
    result = cv2.face.LBPHFaceRecognizer_create()
    result.train(np.asarray(Training_Data), np.asarray(Labels))
    path = model + ".xml"
    result.write(path)
    print("Model Training Complete! : " + model)
    return 0

def trains():
    data_path = 'faces/'
    model_dirs = [f for f in listdir(data_path) if isdir(join(data_path,f))]

    for model in model_dirs:
        print('Model : ' + model)
        path = model + ".xml"
        if isfile(path):
            print("Facial data of " + model + " already exists.")
            continue
        train(model,path)

    return 0  

while True:
    trains()
    exit()


