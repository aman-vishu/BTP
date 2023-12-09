# BTP

6.2.1 Implementation 1 (Virtual keyboard initial implementations):

1. We employed the combined power of CV2, DLIB, and NumPy to detect eyes in real-time video. By utilizing DLIB's facial landmarks detection, we pinpointed 68 specific landmarks on the face. With this, we could isolate the locations for each eye and then detect the eye position on the face.

2. We used advanced filters from the CV2 library for better eye detection. 

3. For detecting blinks, we employed DBLIB, CV2, and NumPy. Here, we used EAR to find whether the eye is closed or not.

4. Tracked gaze in left and right directions using gaze ration (divided the white pixel count between the left and right parts of the eye image).

5. Combining above techniques, we designed a virtual keyboard for text input. This integrated system allows users to type using eye movements and blinking, providing a novel and efficient way to interact.


----------------------------------x-------------------------------------------------------------------------------------------x----------------------------------------------------------

6.2.2 Implementation 2 (Navigation using Head Movements and Gestures):

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


6.2.3 Implementation 3 (Typing using Hand Gestures):

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

---------------------------------x---------------------------------------------------------------------------------------------------x---------------------------------------------------

6.2.4 Implementation 4 (Gaze Typing):

Camera & Frame Handling:
- Initialization: Sets up the camera and configures frame properties.
- Frame Processing: Retrieves frames and applies necessary adjustments.

Face Detection:
- Facial Landmark Detection: Uses Dlib to identify facial features.
- Bounding Box Highlighting: Draws rectangles around detected faces.

Eye Movement Detection:
- Blink Identification: Determines blinks based on eye landmark positions.
- Pupil Tracking: Tracks pupil movement for gaze interaction.

Calibration:
- Guided Process: Helps define the interaction area through user actions.
- Data Collection: Collects and analyzes calibration data for accurate
setup.

Keyboard Projection:
- Virtual Keyboard Generation: Creates a keyboard based on calibration.
- Visual Feedback: Provides interactive visual alignment cues.

Simulated Typing:
- Eye-Guided Input: Interprets eye movements for keyboard selection.
- Input Interpretation: Translates eye interactions into meaningful input.


---------------------------------x---------------------------------------------------------------------------------------------------x---------------------------------------------------

6.2.5 Implementation 5 (Navigation Hand Gestures):

Initialization: Establishes camera connection and initializes the HandTrackingModule for subsequent processing, configuring essential parameters for tracking accuracy and video feed.

Video Processing Loop: Manages an iterative process to capture live video frames, ensuring continuous analysis of hand movements and gestures in real-time from the camera feed.

Hand Detection: Utilizes the HandTrackingModule, leveraging MediaPipe's capabilities, to precisely locate and track hands within each video frame, identifying specific landmarks for subsequent gesture analysis.

Gesture Analysis: Analyzes finger positions and configurations, interpreting gestures for diverse interactions, enabling actions like pointing, clicking, and movement based on recognized hand poses.

Mouse Control and Clicking: Translates hand movements into cursor actions, enabling precise control of the mouse pointer, and executes clicking actions in response to recognized finger gestures, facilitating interactive control.

HandTrackingModule:
Hand Detection and Landmark Tracking: Implements MediaPipe's hand tracking solutions to locate and track hand landmarks.
Finger Gesture Recognition: Detects finger poses and uses them for different interactions.
Distance Calculation: Measures distances between specific landmarks for gesture-based actions, like clicking.

---------------------------------x---------------------------------------------------------------------------------------------------x---------------------------------------------------


6.2.6 Implementation 6 (Integration):
Button Initialization: Defines regions on the window as buttons, associating each region with a corresponding script to execute.
Mouse Click Handling: Monitors mouse clicks within the window and triggers actions based on the clicked region.
Button States: Maintains states for each button to track if a script is running or stopped.
Window Display: Renders the graphical window using OpenCV, showcasing interactive buttons with different colors and labels.
Script Execution: Initiates subprocesses to run specific Python scripts associated with each button when clicked.
Dynamic Updates: Updates button appearances based on script execution states, indicating whether a script is running or stopped.
User Interaction: Allows users to start or stop scripts by clicking the corresponding buttons.
