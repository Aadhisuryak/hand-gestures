import cv2
import time
import numpy as np
import mediapipe as mp
import pyautogui

wcam, hcam = 580, 320

cap = cv2.VideoCapture(0)
cap.set(3, wcam)
cap.set(4, hcam)
pTime = 0
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
index_y = 0
while True:
    _, frame = cap.read()

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    cv2.putText(frame, f'FPS: {int(fps)}', (90, 120), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1)

    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x*frame_width)
                y = int(landmark.y*frame_height)
                if id == 8:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
                    index_x = screen_width/frame_width*x
                    index_y = screen_height/frame_height*y
                    pyautogui.moveTo(index_x, index_y)
                if id == 4:
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    thumb_x = screen_width / frame_width * x
                    thumb_y = screen_height / frame_height * y
                    print('outside', abs(index_y - thumb_y))
                    if abs(index_y - thumb_y) < 80:
                        pyautogui. click()
                        pyautogui.sleep(1)
                if id == 12:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
                    middle_x = screen_width/frame_width*x
                    middle_y = screen_height/frame_height*y
                    print('outside', abs(middle_y - index_y))
                    if abs(middle_y - index_y) < 60:
                        pyautogui. doubleClick()
                        pyautogui.sleep(1)
                if id == 16:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
                    ring_x = screen_width/frame_width*x
                    ring_y = screen_height/frame_height*y
                    print('outside', abs(ring_y - thumb_y))
                    if abs(ring_y - thumb_y) < 50:
                        pyautogui. rightClick()
                        pyautogui.sleep(1)

    cv2.imshow('hand gesture', frame)
    cv2.waitKey(1)
