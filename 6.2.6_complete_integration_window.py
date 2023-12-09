import cv2
import subprocess
import numpy as np

button_clicked = [False] * 4  # Keep track of each button state
subprocs = [None] * 4  # Store subprocesses for each script
scripts = ['D:/btp integration/6.2.5 Hand Nav/hand_nav.py', 'D:/btp integration/6.2.4 Gaze Typing/gaze_typing.py', 'D:/btp integration/6.2.3 Hand Typing/hand_typing.py', 'D:/btp integration/6.2.2 Head Nav/Head_Nav.py']

def on_mouse_click(event, x, y, flags, param):
    global button_clicked, subprocs

    # Define regions for each button (adjust coordinates as needed)
    button_regions = [
        (50, 50, 160, 100),
        (200, 50, 310, 100),
        (50, 150, 160, 200),
        (200, 150, 310, 200)
    ]

    if event == cv2.EVENT_LBUTTONDOWN:
        for i, region in enumerate(button_regions):
            if region[0] < x < region[2] and region[1] < y < region[3]:
                if not button_clicked[i]:
                    subprocs[i] = subprocess.Popen(['python', scripts[i]])
                    button_clicked[i] = True
                else:
                    if subprocs[i]:
                        subprocs[i].terminate()
                    button_clicked[i] = False

window = np.zeros((250, 350, 3), dtype=np.uint8)
cv2.namedWindow('Navigation Options')
cv2.setMouseCallback('Navigation Options', on_mouse_click)

while True:
    cv2.imshow('Navigation Options', window)
    button_regions = [
        (50, 50, 160, 100),
        (200, 50, 310, 100),
        (50, 150, 160, 200),
        (200, 150, 310, 200)
    ]
    colors = [(93, 84, 138), (76, 0, 153), (255, 0, 0), (25, 51, 0)]  # Colors for buttons
    labels = [' Hand Nav', 'Gaze Typing', 'Hand Typing', ' Gaze Nav']  # Labels for buttons

    for i, (region, color, label) in enumerate(zip(button_regions, colors, labels)):
        if button_clicked[i]:
            cv2.rectangle(window, (region[0], region[1]), (region[2], region[3]), (0, 255, 0), -1)
            cv2.putText(window, f' Running', (region[0] + 10, region[1] + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
        else:
            cv2.rectangle(window, (region[0], region[1]), (region[2], region[3]), color, -1)
            cv2.putText(window, label, (region[0] + 10, region[1] + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cv2.destroyAllWindows()