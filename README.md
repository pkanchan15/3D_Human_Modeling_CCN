# 3D_Human_Modeling_CCN

Three-dimensional (3D) human modeling is the process of creating virtual representations of the human body using computer software. 
This technology has seen widespread use in various industries, including film and video game production, medical research, and fashion design.
The use of 3D modeling has revolutionized the way human beings are represented in various media, providing unprecedented levels of realism and detail.

The given video input has taken by frames and the frames are given input to the pose detector of the media pipe and it will return the result that stores the landmarks of the pose from the pose tracker. The landmarks are defined by the Blaze pose which detects around 33 human key points from the body, we have another standard topology called COCO topology which consists of 17 landmarks across the torso, arms, legs, and face. However, the COCO key points only localize to the ankle and wrist points, lacking scale and orientation information for hands and feet, which is vital for practical applications like fitness and dance. The inclusion of more key points is crucial for the subsequent application of domain-specific pose estimation models, like those for hands, faces, or feet.

There are two programs in the project 
1. the first part of the project is app, the file contains the code which display the output where the users can upload the video to transform the 3d video, the function get_in_3d() takes the video as input and takes the frames from the video and takes the landmarks from the video and gets the stream of landmarks and we convert these stream of landmarks points and connect together by connecting the points and convert into video.



