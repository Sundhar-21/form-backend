from fastapi import FastAPI, UploadFile, File
import cv2
import numpy as np

from pose_detector import PoseDetector
from rules import bicep_curl_rule, lateral_raise_rule, back_posture_rule

app = FastAPI()
detector = PoseDetector()

MP = {
    "shoulder": 11,
    "elbow": 13,
    "wrist": 15,
    "hip": 23
}

@app.post("/analyze")
async def analyze_image(file: UploadFile = File(...)):
    image_bytes = await file.read()
    np_img = np.frombuffer(image_bytes, np.uint8)
    frame = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

    results = detector.detect(frame)

    if not results.pose_landmarks:
        return {"success": False, "message": "No pose detected"}

    lm = results.pose_landmarks.landmark

    shoulder = (lm[MP["shoulder"]].x, lm[MP["shoulder"]].y)
    elbow = (lm[MP["elbow"]].x, lm[MP["elbow"]].y)
    wrist = (lm[MP["wrist"]].x, lm[MP["wrist"]].y)
    hip = (lm[MP["hip"]].x, lm[MP["hip"]].y)

    curl_msg, angle, _ = bicep_curl_rule(shoulder, elbow, wrist)
    lat_msg, _ = lateral_raise_rule(shoulder, wrist)
    back_msg, _ = back_posture_rule(shoulder, hip)

    return {
        "success": True,
        "bicep_curl": {"message": curl_msg, "angle": round(angle, 1)},
        "lateral_raise": lat_msg,
        "back_posture": back_msg
    }
