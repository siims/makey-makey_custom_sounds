import cv2
import subprocess
import glob
import sys

ESC = 27
UP = 65362
DOWN = 65364
LEFT = 65361
RIGHT = 65363
CLICK_AND_UP = 16842578
CLICK_AND_DOWN = 16842580
CLICK_AND_LEFT = 16842577
CLICK_AND_RIGHT = 16842579
SPACE = 32
NO_KEY_PRESSED = -1

WINDOW_NAME = 'img'

def showImage(filename):
    img = cv2.imread(filename)
    cv2.imshow(WINDOW_NAME, img)

def playSound(filename):
    try:
        subprocess.Popen(["cvlc", "--play-and-exit", filename], stdout=False, stderr=False)
    except:
        print("Vlc cannot play", filename)


def initializeWindow():
    cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(WINDOW_NAME, 1000, 1000);
    _, images = initializeData()
    showImage(images[0])


def readAllFilesFromFolder(sounds):
    files = []
    for filename in glob.glob(sounds + "/*"):
        files.append(filename)
    return files

def initializeData():
    sounds = readAllFilesFromFolder("sounds")
    images = readAllFilesFromFolder("images")
    return sounds, images

def reinitializeData():
    return initializeData()

if __name__ == '__main__':
    
    print("""
Small python program to be used with makey-makey (http://makeymakey.com/). Just add image files to folder images and audio files to folder sounds. Add files on the run.

Press arrow keys and space. Exist with ESC key.
""")

    initializeWindow()  # need to initialize window for opencv eventloop

    while(1):
        k = cv2.waitKey(33)
        if k == ESC:
            break
        elif k == NO_KEY_PRESSED:
            continue

        # single button presses
        sounds, images = reinitializeData()

        if k == UP:
            playSound(sounds[0])
            showImage(images[0])
        elif k == DOWN:
            playSound(sounds[1])
            showImage(images[1])
        elif k == LEFT:
            playSound(sounds[2])
            showImage(images[2])
        elif k == RIGHT:
            playSound(sounds[3])
            showImage(images[3])
        elif k == SPACE:
            pass

        # combination buttons
        elif k == CLICK_AND_UP:
            pass
        elif k == CLICK_AND_DOWN:
            pass
        elif k == CLICK_AND_LEFT:
            pass
        elif k == CLICK_AND_RIGHT:
            pass
        else:
            print("Key", k, "is not mapped to an action.")
