import cv2
import requests
from ultralytics import YOLO

model = YOLO('yolov8n.pt')
cap = cv2.VideoCapture(0)
API_URL = "http:localhost:8000/explain"

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    results = model(frame, stream=True)
    detected_objects = set()
    
    for result in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            label = model.names[cls]
            detected_objects.add(label)

            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
            cv2.putText(frame, label, (x1, y1-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)
            
    if detected_objects:
        requests.post(API_URL, json={"objects": list(detected_objects)})
        
    cv2.imshow("YOLO Realtime", frame)
    if cv2.waitKey(1) == 27:
        break
    
cap.release()
cv2.destroyAllWindows()