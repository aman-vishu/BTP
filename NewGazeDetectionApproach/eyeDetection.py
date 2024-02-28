import cv2
import numpy as np
import dlib

cap = cv2.VideoCapture(0)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("D:/btp project/keyboard_using_gaze/shape_predictor_68_face_landmarks.dat")

def midpoint(p1, p2):
    return int((p1.x + p2.x) / 2), int((p1.y + p2.y) / 2)

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply histogram equalization to increase contrast
    gray = cv2.equalizeHist(gray)

    # Apply adaptive histogram equalization to enhance local contrast
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    gray = clahe.apply(gray)

    faces = detector(gray)
    for face in faces:
        landmarks = predictor(gray, face)

        # Gaze detection
        right_eye_region = np.array([(landmarks.part(42).x, landmarks.part(42).y),
                                     (landmarks.part(43).x, landmarks.part(43).y),
                                     (landmarks.part(44).x, landmarks.part(44).y),
                                     (landmarks.part(45).x, landmarks.part(45).y),
                                     (landmarks.part(46).x, landmarks.part(46).y),
                                     (landmarks.part(47).x, landmarks.part(47).y)], np.int32)

        # Extract right eye region
        height, width, _ = frame.shape
        mask = np.zeros((height, width), np.uint8)
        cv2.polylines(mask, [right_eye_region], True, 255, 2)
        cv2.fillPoly(mask, [right_eye_region], 255)
        #right_eye = cv2.bitwise_and(gray, gray, mask=mask)
        # Apply the mask to the grayscale image using cv2.bitwise_and()
        # Set all other pixels to white (255) instead of black (0)
        right_eye = cv2.bitwise_and(gray, gray, mask=mask)
        right_eye[mask == 0] = 255  # Set pixels outside the mask to white (255)

        # Find coordinates of pixels with intensity less than 20
        low_intensity_pixels = np.argwhere(right_eye < 20)

        # Convert coordinates to list of tuples
        low_intensity_pixels_list = [(row, col) for row, col in low_intensity_pixels]

        # Print the list of coordinates
        print("Coordinates of pixels with intensity less than 20:")
        print(low_intensity_pixels_list)

        # Find coordinates of pixels with intensity less than 20
        # low_intensity_pixels = np.argwhere(right_eye < 20)

        # # Calculate centroid
        # centroid = np.mean(low_intensity_pixels, axis=0)

        # # Print centroid coordinates
        # print("Centroid of low intensity pixels:", centroid)

        # Find coordinates of pixels with intensity less than 20
        low_intensity_pixels = np.argwhere(right_eye < 20)

        # Calculate centroid
        centroid = np.mean(low_intensity_pixels, axis=0).astype(int)

        # Draw a red dot at the location of the centroid
        red_color = (255,255, 255)  # BGR format for red color
        radius = 3
        # Draw a red dot at the location of the centroid
        cv2.circle(right_eye, (centroid[1], centroid[0]), radius, red_color, -1)

        #cv2.circle(right_eye, tuple(centroid), radius, red_color, -1)

        # Print centroid coordinates
        print("Centroid of low intensity pixels:", centroid)

        # Apply Hough Circle Transform to detect circles (pupils)
        circles = cv2.HoughCircles(right_eye, cv2.HOUGH_GRADIENT, dp=1, minDist=50, param1=50, param2=20, minRadius=5,
                                   maxRadius=30)
        # circles = None

        if circles is not None:
            circles = np.round(circles[0, :]).astype("int")
            for (x, y, r) in circles:
                cv2.circle(right_eye, (x, y), r, (0, 255, 0), 4)  # Draw circle around pupil
                cv2.circle(right_eye, (x, y), 2, (0, 0, 255), 3)  # Draw red dot at pupil center
                pupil_center = (x, y)
                print("Pupil coordinates:", pupil_center)

        cv2.imshow("Right Eye", right_eye)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
