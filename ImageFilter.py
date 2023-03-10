import cv2
import sys
import numpy
PREVIEW=0 #Preview Mode
BLUR=1 #Blurring Filter
FEATURES=2 #corner Feature Detector
CANNY=3 #Canny Edge Detector


feature_params=dict(maxCorners=500,
qualityLevel=0.2,
minDistance=15,
blockSize=9)

s=0
if len(sys.argv)>1:
    s=sys.srgv[1]
source=cv2.VideoCapture(s)
image_filter=PREVIEW
alive=True
win_name='Camera Filters'
cv2.namedWindow(win_name,cv2.WINDOW_NORMAL)
result=None
while alive:
    has_frame,frame=source.read()
    if not has_frame:
        break
    frame=cv2.flip(frame,1)

    if image_filter==PREVIEW:
        result=frame
    elif image_filter==CANNY:
        result=cv2.Canny(frame,145,150)
    elif image_filter==BLUR:
        result=cv2.blur(frame,(13,13))
    elif image_filter==FEATURES:
        result=frame
        frame_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        corners=cv2.goodFeaturesToTrack(frame_gray,**feature_params)
        if corners is not None:
            for x,y in numpy.float32(corners).reshape(-1,2):
                cv2.circle(result,(int(x),int(y)),10,(0,255,0),1)
    cv2.imshow(win_name,result)

    key=cv2.waitKey(1)

    if key==ord('Q') or key ==ord('q') or key ==27:
        alive=False
    elif key==ord('W') or key ==ord('w'):
        image_filter=CANNY
    elif key==ord('E') or key ==ord('e'):
        image_filter=BLUR
    elif key==ord('R') or key ==ord('r'):
        image_filter=FEATURES
    elif key==ord('T') or key ==ord('t'):
        image_filter=PREVIEW

source.release()
cv2.destroyAllWindows(win_name)

