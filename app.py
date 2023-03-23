import cv2
import mediapipe as mp
import numpy as np
import streamlit as st

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# Initialize the Mediapipe pose model
pose_model = mp_pose.Pose()

# Define a function to process a single video frame
def process_frame(frame):
    # Convert the frame to RGB color space
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Process the frame with the Mediapipe pose model
    results = pose_model.process(frame)
    
    # Draw the pose landmarks on the frame
    mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
    
    # Convert the frame back to BGR color space
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    
    # Return the processed frame and the pose landmarks
    return frame, results.pose_landmarks

# Define functions to calculate body measurements
def get_body_height(pose_landmarks):
    # Calculate the distance between the top of the head and the ground
    head_top = pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE]
    hip = pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP]
    distance = np.sqrt((head_top.x - hip.x)**2 + (head_top.y - hip.y)**2 + (head_top.z - hip.z)**2)
    
    # Convert the distance to meters and return it
    return distance

def get_shoulder_width(pose_landmarks):
    # Calculate the distance between the left and right shoulders
    left_shoulder = pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER]
    right_shoulder = pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER]
    distance = np.sqrt((left_shoulder.x - right_shoulder.x)**2 + (left_shoulder.y - right_shoulder.y)**2 + (left_shoulder.z - right_shoulder.z)**2)
    
    # Convert the distance to meters and return it
    return distance

# Define a function to generate a simple 3D animation
def generate_animation(pose_landmarks):
    # Calculate the position of the left hand
    left_hand = pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST]
    x = left_hand.x - 0.1
    y = left_hand.y + 0.1
    z = left_hand.z
    
    # Create a 3D model of a cube at the position of the left hand
    cube_3d = np.array([[-0.1, -0.1, 0], [0.1, -0.1, 0], [0.1, 0.1, 0], [-0.1, 0.1, 0], [-0.1, -0.1, 0.2], [0.1, -0.1, 0.2], [0.1, 0.1, 0.2], [-0.1, 0.1, 0.2]])
    cube_3d[:, 0] += x
    cube_3d[:, 1] += y
    cube_3d[:, 2] += z
    
    # Project the 3D model onto the 2D image plane
    # Project the 3D model onto the 2D image plane
    camera_matrix = np.array([[1000, 0, 640], [0, 1000, 360], [0, 0, 1]])
    distortion_coeffs = np.zeros((5,))
    projection, _ = cv2.projectPoints(cube_3d, np.zeros((3,)), np.zeros((3,)), camera_matrix, distortion_coeffs)
    projection = projection.reshape((-1, 2)).astype(int)

    # Create a black image to draw the projection on
    image = np.zeros((720, 1280, 3), dtype=np.uint8)

    # Draw the projection on the image
    cv2.fillPoly(image, [projection], (0, 255, 0))

    # Return the image
    return image
def main():
# Create a streamlit window
    st.title("3D Human Modeling with Mediapipe")
    # Define the video capture device
cap = cv2.VideoCapture(0)

# Define a flag to track if the app is running
is_running = True

# Loop until the app is stopped
while is_running:
    # Read a single frame from the video capture device
    ret, frame = cap.read()
    
    # Check if the frame was read successfully
    if ret:
        # Process the frame with the Mediapipe pose model
        frame, pose_landmarks = process_frame(frame)
        
        # Check if pose landmarks were detected
        if pose_landmarks is not None:
            # Calculate body measurements
            body_height = get_body_height(pose_landmarks)
            shoulder_width = get_shoulder_width(pose_landmarks)
            
            # Display the body measurements
            st.write("Body Height:", body_height, "m")
            st.write("Shoulder Width:", shoulder_width, "m")
            
            # Generate a simple 3D animation
            animation = generate_animation(pose_landmarks)
            
            # Display the animation
            st.image(animation, channels="BGR")
        
        # Display the processed frame
        st.image(frame, channels="BGR")
        
        # Check if the user pressed the "Stop" button
        if st.button("Stop"):
            is_running = False
            break
            
# Release the video capture device and close the streamlit window
cap.release()
st.close()

if __name__ == "__main__":
    main()