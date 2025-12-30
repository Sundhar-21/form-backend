import cv2
from mediapipe.python.solutions import pose
from mediapipe.python.solutions import drawing_utils

class PoseDetector:
    def __init__(self):
        self.pose = pose.Pose(
            static_image_mode=False,
            model_complexity=1,
            smooth_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5,
        )
        self.drawer = drawing_utils

    def detect(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return self.pose.process(rgb)

    def draw(self, frame, results):
        if results.pose_landmarks:
            self.drawer.draw_landmarks(
                frame,
                results.pose_landmarks,
                pose.POSE_CONNECTIONS,
            )
        return frame
