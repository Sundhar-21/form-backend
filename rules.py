from angle_utils import calculate_angle

def bicep_curl_rule(shoulder, elbow, wrist):
    angle = calculate_angle(shoulder, elbow, wrist)

    if angle < 30:
        return "Curl Up More", angle, False
    elif angle > 160:
        return "Extend Fully", angle, False
    else:
        return "Good Curl", angle, True

def lateral_raise_rule(shoulder, wrist):
    if abs(wrist[1] - shoulder[1]) < 0.05:
        return "Good Alignment", True
    return "Adjust Wrist Height", False

def back_posture_rule(shoulder, hip):
    slope = abs((shoulder[0] - hip[0]) / (shoulder[1] - hip[1] + 1e-6))
    if slope < 0.1:
        return "Back Straight", True
    return "Do Not Lean", False
