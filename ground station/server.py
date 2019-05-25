import io
import socket
import struct
#from PIL import Image
import cv2
import numpy as np


def show_text(text, img, coord, color=(255, 255, 255)):
    """
    Prints text in location for image img
    """
    if coord[2] > 30:
        location = (coord[1], coord[2] - 5)
    else:
        location = (coord[1], coord[4] + 25)
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 0.7
    fontColor = color
    lineType = 2

    cv2.putText(img, text, location, font,
                fontScale, fontColor, lineType)

# Start a socket listening for connections on 0.0.0.0:8000 (0.0.0.0 means
# all interfaces)
server_socket = socket.socket()
server_socket.bind(('0.0.0.0', 8000))
server_socket.listen(0)
print('Initialising Server')
# Accept a single connection and make a file-like object out of it
connection = server_socket.accept()[0].makefile('rb')
print('Connection Established')

try:
    cv2.namedWindow('PiCam', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('PiCam', 480, 360)
    cv2.resizeWindow('PiCam', 960, 720)
    while True:
        print('Listening')
        # Read the length of the image as a 32-bit unsigned int. If the
        # length is zero, quit the loop
        image_len = struct.unpack('<L', connection.read(struct.calcsize('<L')))[0]
        if not image_len:
            break
            
        # Construct a stream to hold the image data and read the image
        # data from the connection
        image_stream = io.BytesIO()
        image_stream.write(connection.read(image_len))
        
        # Rewind the stream, open it as an image with PIL and do some
        # processing on it
        image_stream.seek(0)
        
        #image = Image.open(image_stream)
        # image = cv2.imdecode(, 1)
        image = cv2.imdecode(np.fromstring(image_stream.getvalue(), dtype=np.uint8), 1)
        show_text(str(fps), image, [0,0])
        
        cv2.imshow('PiCam', image)
        # print('Image is %dx%d' % image.size)
        # image.verify()
        # print('Image is verified')
        
        keyPressed = cv2.waitKey(1)
        if keyPressed == 113:
            break  # q to next
finally:
    connection.close()
    server_socket.close()
    cv2.destroyAllWindows()
