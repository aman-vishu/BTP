# BTP

6.2.1 Implementation 1:

1. We employed the combined power of CV2, DLIB, and NumPy to detect eyes in real-time video. By utilizing DLIB's facial landmarks detection, we pinpointed 68 specific landmarks on the face. With this, we could isolate the locations for each eye and then detect the eye position on the face.

2. We used advanced filters from the CV2 library for better eye detection. 

3. For detecting blinks, we employed DBLIB, CV2, and NumPy. Here, we used EAR to find whether the eye is closed or not.

4. Tracked gaze in left and right directions using gaze ration (divided the white pixel count between the left and right parts of the eye image).

5. Combining above techniques, we designed a virtual keyboard for text input. This integrated system allows users to type using eye movements and blinking, providing a novel and efficient way to interact.


----------------------------------x-------------------------------------------------------------------------------------------x----------------------------------------------------------

6.2.2 Implementation 2:

1. Facial Landmark Detection and Thresholds:
   - Utilizes Dlib for facial landmark estimation.
   - Defines thresholds for eye and mouth aspect ratios.
   - Calculates ratios and checks differences.

2. Gesture Interpretation and Action Triggering:
   - Tracks eye aspect ratio for blink detection.
   - Identifies left or right clicks based on ratio differences.
   - Monitors mouth aspect ratio for input mode and cursor movement based on nose(as it indicates head movements).

3. Visual Feedback and Display:
   - Visualizes facial landmarks and contours on the frame.
   - Provides textual feedback on the frame for different states.

4. Interaction with PyAutoGUI and Control:
   - Uses PyAutoGUI for mouse and keyboard simulation.
   - Performs actions based on detected gestures and states.



---------------------------------x---------------------------------------------------------------------------------------------------x---------------------------------------------------
6.2.3 Implementation 3:

Demonstrates a real-time interactive interface that combines hand tracking with virtual keyboard functionality.
1. Initialize Key Objects: You create instances of the ‘Key’ class for each keyboard key, specifying their positions, sizes, and corresponding letters or functions.

2. Initialize Hand Tracking: You create an instance of the ‘HandTracker’ class, setting parameters for hand detection confidence.

3. Main Loop:
   - Continuously read frames from the webcam (‘cap.read()’).
   - Resize and flip the frame.
   - Use the hand tracker to find hands and extract hand landmarks.
   - Calculate distances between finger landmarks and determine if the fingers are close, indicating a gesture.
   - Display real-time frames annotated with hand landmarks and other UI elements.
   - Update the FPS counter.

6. Mouse and Keyboard Interaction:
   - Define a function (‘getMousPos’) to handle mouse events.
   - Simulate mouse clicks and movements based on hand gestures.
   - Detect if the sign finger is over a virtual key and handle mouse clicks accordingly.


7. UI Elements:
   - Draw keys on the frame and update their appearance based on mouse and hand interactions.
   - Display the FPS counter, “Show,” and “Exit” buttons.

8. Text Input:
   - Display a text box and update its content based on mouse clicks or hand gestures over virtual keys.
   - Simulate keyboard presses for text input.




