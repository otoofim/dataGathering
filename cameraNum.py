import cv2

def cameranum():

    ids = []
    for i in range(100):
        try:
            cap = cv2.VideoCapture(i)
            if cap is not None and cap.isOpened():
                ids.append(i)
        except:
            pass
    return ids



    #index = 0
    #arr = []
    #while len(arr)<3:
        #cap = cv2.VideoCapture(index)
        #if cap.read()[0] and index != 200:
            #arr.append(index)
            #cap.release()
        #index += 1
    #return arr


if __name__ == '__main__':
    cameranum()
