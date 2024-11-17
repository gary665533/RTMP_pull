RTMP Video Recording and Streaming
This program is designed to receive video streams from an RTMP server and save them to local files. It supports frame processing with OpenCV and efficient streaming with FFmpeg.

Features:
Receive video streams from an RTMP address and process the frames.
Save processed frames as local MP4 files.
Switch to FFmpeg for efficient streaming.
Customize video resolution and FPS settings to avoid format issues.


Installation and Environment Requirements:
Dependencies
Python 3.7
OpenCV (cv2)
FFmpeg

Usage:
Setting the RTMP Address
Locate the following code in the program and modify myrtmp_addr with your RTMP address:
	myrtmp_addr = "rtmp://192.168.53.102:1935/myapp/live"


Video Resolution:
Adjust the following lines to set the video width and height:
	cap.set(cv.CAP_PROP_FRAME_WIDTH, 640)
	cap.set(cv.CAP_PROP_FRAME_HEIGHT, 480)

FPS Configuration
If you need to customize the FPS, modify the following parameters:
	result = cv.VideoWriter('output.mp4', cv.VideoWriter_fourcc(*'MP4V'), 20, (width, height))
