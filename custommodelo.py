from ultralytics import YOLO
import cv2



#load model
model = YOLO('clash.pt')

#load video
video_path = 'testvideo.mp4'
cap = cv2.VideoCapture(video_path)

ret = True
# read frames
while ret:
    ret, frame = cap.read()


    #detec objects 
    #track objects 
    results = model.track(frame, persist=True)

    #plot results
    frame_ = results[0].plot()

    # visualize
    cv2.imshow('frame', frame_)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

