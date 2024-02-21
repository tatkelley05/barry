
import cv2
import numpy as np

def ColorMask(ret, frame):

    if not ret:
        print("Cry")    

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_yellow = np.array([15,50,180])
    upper_yellow = np.array([40,255,255])
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    result = cv2.bitwise_and(frame,frame, mask= mask)

    # cv2.imshow("Result", result)  #APotatoFlewAroundMyRoomBeforeYouCame
    return result

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        quit()
 