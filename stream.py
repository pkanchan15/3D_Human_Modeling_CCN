import streamlit as st
import cv2
import mediapipe as mp

def capture_video():
    mp_drawing = mp.solutions.drawing_utils
    cap = cv2.VideoCapture(0)
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)
    while True:
        ret, frame = cap.read()
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(frame_rgb)

        # Draw the poses on the frame
        mp_drawing.draw_landmarks(
        frame, results.pose_landmarks, 
        mp_pose.POSE_CONNECTIONS)
        st.image(frame, channels="BGR", use_column_width=True)

        # If the 'q' key is pressed, break from the loop
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
st.title("Webcam Pose Detection")
st.write("Press 'q' to quit")
if st.button("quit"):
    cv2.destroyAllWindows()
if st.button("Start"):
    capture_video()
