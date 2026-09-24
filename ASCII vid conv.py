import cv2
import os
import time


# PUT YOUR VIDEO PATH HERE
VIDEO_PATH = r"C:\Users\aura9\Downloads\Chico lachowski I'll do it [edit]#chicolachowski #lookmaxxing.mp4"

# ASCII characters from darkest to brightest
ASCII_CHARS = " .:-=+*#%@"
#Width of ASCII output
WIDTH = 100

# CONVERT FRAME TO ASCII

def frame_to_ascii(frame): 

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Get original dimensions
    height, width = gray.shape
    # Characters are taller than they are wide,so we reduce the height.
    aspect_ratio = height / width
    new_height = int(WIDTH * aspect_ratio * 0.32)

    # Resize frame
    gray = cv2.resize(gray, (WIDTH, new_height))

    ascii_frame = ""

    for row in gray:

        for pixel in row:

            # Convert brightness to ASCII character
            index = int(pixel / 256 * len(ASCII_CHARS))

            ascii_frame += ASCII_CHARS[index]

        ascii_frame += "\n"

    return ascii_frame
    # OPEN VIDEO

video = cv2.VideoCapture(VIDEO_PATH)

if not video.isOpened():
    print("Could not open the video.")
    exit()


# Get video's FPS
fps = video.get(cv2.CAP_PROP_FPS)

# Time between frames
frame_delay = 1 / fps

# PLAY VIDEO
while True:

    success, frame = video.read()

    if not success:
        break

    # Convert frame to ASCII
    ascii_frame = frame_to_ascii(frame)

    # Clear terminal
    os.system("cls" if os.name == "nt" else "clear")

    # Print ASCII frame
    print(ascii_frame, end="")

    # Maintain original FPS
    time.sleep(frame_delay)


video.release()