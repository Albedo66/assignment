import jetson_inference
import jetson_utils
from jetson_inference import detectNet
from jetson_utils import videoSource, videoOutput
net = detectNet("ssd-mobilenet-v2", threshold=0.5)
camera = videoSource("/dev/video0") # '/dev/video0' for V4L2
display = videoOutput("display://0") # 'my_video.mp4' for file
while display.IsStreaming():
 img = camera.Capture()
 if img is None: # capture timeout
   continue
 detections = net.Detect(img)
 for i,detection in enumerate(detections):
   print(f"Detection{i}:")
   print(f"-ClassID:{detection.ClassID}")
   print(f"-Confidence:{detection.Confidence:.6f}")
   print(f"-Left:{detection.Left}")
   print(f"-Top:{detection.Top}")
   print(f"-Right:{detection.Right}")
   print(f"-Bottom:{detection.Bottom}")
   print(f"-Width:{detection.Width}")
   print(f"-Height:{detection.Height}")
   print(f"-Area:{detection.Area}")
   print(f"-Center:{detection.Center[0]},{detection.Center[1]}")
   print()

 display.Render(img)
 display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))
