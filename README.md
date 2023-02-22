# 3D_Human_Modeling_CCN

Team 8: [ 3D- Human Modeling ] CCN [Spring 2023]

## Team Members:

Praneeth Reddy Kanchanakuntla <br>
Akhil Challa <br>
Kousik Varma Dandu <br>
Durga Sri Jonnalagadda<br>

### Introduction <br>

The Aim of the project is to develop a real time 2 D video to 3 D animated Video. 
Initially, the shapes of human bodies are detected, and then specific points on these shapes are recognized. These particular points are then utilized to calculate the body measurements, which are essential for generating a standard 3D model of a person.After the creation of the 3D human model, it becomes possible to view and animate the digital representation of the human.The approach of building 3D human models by using 2D images is straightforward and rational.


#### Working model: 

To create a 3D human model using photographs, it is possible to obtain the silhouette information and the corresponding relationship of the human body from the images. By detecting the shape feature from the body silhouette, it is possible to establish spatial relations between the 2D images and the 3D template model in a coordinate system. This relationship can be used to modify the body shape of the human model. The 3D modeling of the human body can be adjusted based on relevant anthropometric measurements. Since the variation of body shape is connected to anthropometric measurements in different parts of the body, anthropometric data can be used as parameters to alter the body shape with the desired characteristics.

When constructing a 3D human model from 2D images, feature points are extracted from the captured images. However, some crucial feature points such as the neck point, thigh point, knee point, and shank point may not be fully utilized. As a result, the deformation of the body shape with limited feature points can impact the quality and realism of the final 3D body shape. To ensure an accurate representation of the 3D human model, it is necessary to use sufficient feature information.


the image decribes about the feature points that are to be extracted from the 2D video
![](https://github.com/pkanchan15/3D_Human_Modeling_CCN/blob/group_8_proposal/Screenshot%202023-02-22%20at%201.09.45%20PM.png)


There are many Existing Trained Models that provide descent accuarcy and Modeling in a real time speed. Some of them are 

1. Posnet
2. HRNet
3.Mask R-CNN
4.Cascaded Pyramid Network
5. Media Pipe

### Proposed Model:

For this project we are intented to use media pipe library because of its vast resources and apis and ease of use.

In pose detection, the majority of approaches use the COCO topology, which consists of 17 key points. However, the blaze pose detector can detect 33 key points across the human body, including the torso, arms, legs, and face. This increase in key points is important for domain-specific pose estimation models such as those focused on hands, face, and feet. Each key point is predicted with three degrees of freedom, along with a visibility score. The blaze pose model is very fast, taking less than a millisecond to execute, and has better accuracy than many existing models. It is available in two versions: Blaze Pose Lite and Blaze Pose Fully, which provide a trade-off between speed and accuracy.




#### paper reffered:

1. Yueh-Ling Lin, Mao-Jiun J. Wang,
Constructing 3D human model from front and side images,
Expert Systems with Applications,
Volume 39, Issue 5,
2012,
Pages 5012-5018,
ISSN 0957-4174, https://www.sciencedirect.com/science/article/abs/pii/S0957417411014965


2.Bernard Boulay, Francois Brémond, Monique Thonnat,
Applying 3D human model in a posture recognition system,
Pattern Recognition Letters,
Volume 27, Issue 15,
2006,
Pages 1788-1796,
ISSN 0167-8655,

https://www.sciencedirect.com/science/article/pii/S0167865506000389


The following implementation is very use full in Video Games, animation and various other purposes. we as a group are playing to use Computer vision to locate the points of the body and store them to give 3-D model in UNITY frame work.

### Current Project Plan:

<ul>
  <li>
    In the first week we are planing to learn Computer Vision and other specific frame works </li>
  <li> Learn to convert the points of the body to 3 D model <li>
  </ul>
    
