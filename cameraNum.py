import cv2

def cameranum():
    index = 0
    arr = []
    while len(arr)<4:
        cap = cv2.VideoCapture(index)
        if cap.read()[0] and index != 200:
            arr.append(index)
            cap.release()
        index += 1
    return arr


if __name__ == '__main__':
    cameranum()