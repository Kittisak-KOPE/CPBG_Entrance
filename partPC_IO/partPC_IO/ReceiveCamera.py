import time
import cv2

# rtsp://admin:Sp_123456@192.168.50.145:554
vidcap = cv2.VideoCapture(0)
success,image = vidcap.read()
count = 0

while success:
    cv2.imwrite("frame%d.jpg" % count, image)    
    success,image = vidcap.read()
    print('Read a new frame: ', success)
    count += 1
    time.sleep(3)






# โค้ดเดิม
# import time
# import cv2

# # rtsp://admin:Sp_123456@192.168.50.145:554
# vidcap = cv2.VideoCapture('rtsp://admin:Sp_123456@192.168.50.145:554')
# success,image = vidcap.read()
# count = 0

# while success:
#     cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
#     success,image = vidcap.read()
#     print('Read a new frame: ', success)
#     count += 1
#     time.sleep(3
# )