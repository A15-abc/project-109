# import cv2
# import mediapipe as mp
# from pynput.keyboard import Key, Controller

# keyboard = Controller()

# cap = cv2.VideoCapture(0)

# width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) 
# height  = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) 

# mp_hands = mp.solutions.hands
# mp_drawing = mp.solutions.drawing_utils

# hands = mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5)

# tipIds = [4, 8, 12, 16, 20]

# state = None

# # Define a function to count fingers
# def countFingers(image, hand_landmarks, handNo=0):

#     global state

#     if hand_landmarks:
#         # Get all Landmarks of the FIRST Hand VISIBLE
#         landmarks = hand_landmarks[handNo].landmark

#         # Count Fingers        
#         fingers = []

#         for lm_index in tipIds:
#                 # Get Finger Tip and Bottom y Position Value
#                 finger_tip_y = landmarks[lm_index].y 
#                 finger_bottom_y = landmarks[lm_index - 2].y

#                 # Check if ANY FINGER is OPEN or CLOSED
#                 if lm_index !=4:
#                     if finger_tip_y < finger_bottom_y:
#                         fingers.append(1)
#                         # print("FINGER with id ",lm_index," is Open")

#                     if finger_tip_y > finger_bottom_y:
#                         fingers.append(0)
#                         # print("FINGER with id ",lm_index," is Closed")

        
#         totalFingers = fingers.count(1)
        
#         # PLAY or PAUSE a Video
#         if totalFingers == 4:
#             state = "Play"

#         if totalFingers == 0 and state == "Play":
#             state = "Pause"
#             keyboard.press(Key.space)

#         # Move Video FORWARD & BACKWARDS    
#         finger_tip_x = (landmarks[8].x)*width
 
#         if totalFingers == 1:
#             if  finger_tip_x < width-400:
#                 print("Play Backward")
#                 keyboard.press(Key.left)

#             if finger_tip_x > width-50:
#                 print("Play Forward")
#                 keyboard.press(Key.right)
        
        
# # Define a function to 
# def drawHandLanmarks(image, hand_landmarks):

#     # Darw connections between landmark points
#     if hand_landmarks:

#       for landmarks in hand_landmarks:
               
#         mp_drawing.draw_landmarks(image, landmarks, mp_hands.HAND_CONNECTIONS)



# while True:
#     success, image = cap.read()

#     image = cv2.flip(image, 1)
    
#     # Detect the Hands Landmarks 
#     results = hands.process(image)

#     # Get landmark position from the processed result
#     hand_landmarks = results.multi_hand_landmarks

#     # Draw Landmarks
#     drawHandLanmarks(image, hand_landmarks)

#     # Get Hand Fingers Position        
#     countFingers(image, hand_landmarks)

#     cv2.imshow("Media Controller", image)

#     # Quit the window on pressing Sapcebar key
#     key = cv2.waitKey(1)
#     if key == 27:
#         break

# cv2.destroyAllWindows()



import pyautogui

screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
screenWidth, screenHeight(2560, 1440)

currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
currentMouseX, currentMouseY(1314, 345)

pyautogui.moveTo(100, 150) # Move the mouse to XY coordinates.

pyautogui.click()          # Click the mouse.
pyautogui.click(100, 200)  # Move the mouse to XY coordinates and click it.
pyautogui.click('button.png') # Find where button.png appears on the screen and click it.

pyautogui.move(400, 0)      # Move the mouse 400 pixels to the right of its current position.
pyautogui.doubleClick()     # Double click the mouse.
pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)  # Use tweening/easing function to move mouse over 2 seconds.

pyautogui.write('Hello world!', interval=0.25)  # type with quarter-second pause in between each key
pyautogui.press('esc')     # Press the Esc key. All key names are in pyautogui.KEY_NAMES

with pyautogui.hold('shift'):  # Press the Shift key down and hold it.
        pyautogui.press(['left', 'left', 'left', 'left'])  # Press the left arrow key 4 times.
 # Shift key is released automatically.

pyautogui.hotkey('ctrl', 'c') # Press the Ctrl-C hotkey combination.

pyautogui.alert('This is the message to display.') # Make an alert box appear and pause the program until OK is clicked.