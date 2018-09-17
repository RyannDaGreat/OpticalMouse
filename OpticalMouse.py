#DEMO: https://youtu.be/wpeRlaDJNc0
#Trying to create an optical mouse from an iPhone Slow-Mo cam and light using OpenCv and Python3. It tries to use optical flow from a video I recorded on my phone. Its also stored in my RPY.
from rp import *
#MOUSETEST
path='/Users/Ryan/Desktop/movie.AVI'
#path='/Users/Ryan/Desktop/Untitled.mov'
path='/Users/Ryan/Downloads/IMG_9305.MOV'
import cv2
s=64*2**2
_get_gray=lambda:cv2.resize(cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2GRAY),(s,)*2)#get image, make it grayscale, and resize it to 100,100
def get_gray():
    #ans=grayscale_to_rgb(_get_gray())
    #return (gauss_blur(full_range(ans.astype(float)/256-gauss_blur(ans.astype(float)/256,10,1)),5,1)*256).astype(np.uint8)[:,:,0]
    ans=_get_gray()
    #exec(mini_terminal)
    blur=lambda ans,s=10,S=60:cv2.GaussianBlur(ans,(S+(not S%2),)*2,s,ans,s)
    contrast=10
    return blur(((ans.astype(float)-blur(ans).astype(float))*contrast+128).astype(np.uint8))


cap=cv2.VideoCapture(path)
old_gray=get_gray()
gray=get_gray()
def update_gray():
    global gray,old_gray
    old_gray=gray
    gray=get_gray()
lk_params = dict(winSize = (s-10,)*2,maxLevel = 122,criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,  20,.00000))# Lucas kanade params
pps=[(s//2,s//2)]
while 0:
 update_gray()
 p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, gray, np.array([(s//2,)*2],np.float32), None, **lk_params)
 gray1=gray+0
 pp=p1[0]
 pps.append(pp)
 if len(pps)>10:
     del pps[0]
 pp=sum(np.array(pps))/len(pps)

 cv2.arrowedLine(gray1,tuple(np.array([s//2,s//2]).astype(int)), tuple(((np.array(pp)-[s//2,s//2])*5+[s//2,s//2]).astype(int)), (0,0,255), 2)


 cv_imshow(grayscale_to_rgb(gray1))
 print(p1)
