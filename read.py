import cv2 as cv

# This code opens the image in a new window when code is ran, image will not rescale currently, and will open across multiple monitors

#img = cv.imread('Photos/cat.jpg') # Takes in path to image and returns image as matrix of pixels

#cv.imshow('Cat', img) #Displays the image as a new window, first pass window, then pass image matrix

#cv.waitKey(0) #Keybind function, waits for time for key to be presed. 0 waits forever



# Reading videos

capture = cv.VideoCapture('Videos/dog.mp4') # takes int or a path to a video, int is used for webcam in most cases, int 0. multiple cams connected will reference assigned camera

# Create a while loop and read the video frame by frame

while True:
    isTrue, frame = capture.read() # returns the frame, and a boolean saying wether the fram was succesfully read
    cv.imshow('Video', frame) #passes  individual frame

    if cv.waitKey(20) & 0xFF==ord('d'): #if letter d is pressed break
        break
    #keeps video from running indefinitly
capture.release()
cv.destroyAllWindows()