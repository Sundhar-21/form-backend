import cv2
import mediapipe as mp

class PoseDetector:
    def __init__(self):
        self.pose = mp.solutions.pose.Pose(
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )

    def detect(self, image):
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        return self.pose.process(rgb)
