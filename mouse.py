import cv2
import mediapipe as mp
import pyautogui

cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
# screen_width, screen_height = pyautogui.size()
index_y = 0
l_index_y = 0
middle_y = 0
l_middle_y = 0

_, frame = cap.read()
frame_height, frame_width, _ = frame.shape

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                if id == 4:
                    # NewValue = (((OldValue - OldMin) * (NewMax - NewMin)) / (OldMax - OldMin)) + NewMin
                    thumb_x = ((landmark.x - 0) * (120 + 120)) - 120
                    thumb_y = ((landmark.y - 0) * (90 + 90)) - 90
                
                elif id == 5:
                    l_index_y = landmark.y
                
                elif id == 8:
                    index_y = landmark.y
                
                elif id == 9:
                    l_middle_y = landmark.y
                
                elif id == 12:
                    middle_y = landmark.y
                
        if abs(thumb_x) + abs(thumb_y) > 20:
            try:
                pyautogui.move(thumb_x, thumb_y,0.1)
            except:
                continue
        
        elif index_y > l_index_y :
            pyautogui.click()
            pyautogui.sleep(0.5)
            
        elif middle_y > l_middle_y :
            pyautogui.click(button='right')
            pyautogui.sleep(0.5)
                
    cv2.circle(img=frame, center=(int(frame_width/2),int(frame_height/2)), radius=53, color=(255, 255, 255))
    cv2.imshow('Camera Mouse', frame)
    if cv2.waitKey(10) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()