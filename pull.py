import subprocess as sp
import cv2 as cv
import time

# -------------------------------------------------------------------------------------
# 設定好address就可以運作了
# 值得注意的是，請設定好影片的寬高，不然收下來的影片會無法使用
# 也請注意影片的fps，若是fps不相同，請去編輯result，把20改成你需要的fps
# 若是不想要有超時的error report，請改28行
# -------------------------------------------------------------------------------------
myrtmp_addr = "rtmp://192.168.53.102:1935/myapp/live"

cap = cv.VideoCapture(myrtmp_addr)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 480)


if not cap.isOpened():
    print("Cannot open camera")
    exit()
width  = 640 # int (cap.get(cv.CV_CAP_PROP_FRAME_WIDTH))
height = 480 # int (cap.get(cv.CV_CAP_PROP_FRAME_HEIGHT))
result = cv.VideoWriter('output.mp4', cv.VideoWriter_fourcc(*'MP4V'), 20, (width, height))

while True:
    ret, frame = cap.read()
    # 若是不想要有超時的error report，請把這三行if的內容拔掉
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    # cv.imshow('frame', gray)
    result.write(frame)
    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
result.release()
cv.destroyAllWindows()








# rtmpUrl = "rtmp://192.168.53.127:1935/myapp/live"
# # camera_path = "File.avi"
# cap = cv.VideoCapture(rtmpUrl)

# # Get video information
# fps = int(cap.get(cv.CAP_PROP_FPS))
# width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

# # ffmpeg command
# command = ['ffmpeg',
#         '-y',
#         '-f', 'rawvideo',
#         '-vcodec','rawvideo',
#         '-pix_fmt', 'bgr24',
#         '-s', "{}x{}".format(width, height),
#         '-r', str(fps),
#         '-i', '-',
#         '-c:v', 'libx264',
#         '-pix_fmt', 'yuv420p',
#         '-preset', 'ultrafast',
#         '-f', 'flv', 
#         rtmpUrl]

# # 管道配置
# p = sp.Popen(command, stdin=sp.PIPE)
# size = (width, height)
# result = cv.VideoWriter("File.avi",cv.VideoWriter_fourcc(*'MJPG'), 10, size)

# # read webcamera
# while(cap.isOpened()):
#     ret, frame = cap.read()
#     if not ret:
#         print("Opening camera is failed")
#         break
#     else:
#         result.write(frame)
#         if cv.waitKey(1) & 0xFF == ord('s'):
#             break
#     p.stdin.read()
# # frame.tostring()
# cap.release()
# result.release()
# cv.sdestroyAllWindows()
# print("Success")
#     # process frame
#     # your code
#     # process frame

#     # write to pipe
