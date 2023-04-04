import cv2
import mediapipe as mp


mp_drawing = mp.solutions.drawing_utils


mp_pose = mp.solutions.pose
pose = mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)
cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(frame_rgb)
    mp_drawing.draw_landmarks(
        frame, results.pose_landmarks, 
        mp_pose.POSE_CONNECTIONS)
    cv2.imshow('Pose Estimation', frame)
    landmarks = []
    if results.pose_landmarks is not None:
        for landmark in results.pose_landmarks.landmark:
            landmarks.append([landmark.x, landmark.y, landmark.z])
    print(landmarks)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


