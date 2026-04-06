# MLLearning

Pytorch, OpenCV in python

Pytorch:
Learning: Tensors, Autograd, Building a Model, Loading Data, Training Models, Deplying with Torch Script
(Following PyTorch Beginner Series: https://www.youtube.com/watch?v=IC0_FRiX-sw&list=PL_lsbAsL_o2CTlGHgMxNrKhzP97BaG9ZN&index=3)
-From April 2021
Signifcant updates since then: torch.compile, 

Additional Notes:
Has: deep learning primitives, nn layer types, activation & loss functions, optimizers (on NVIDIA chips)

Overview Plan:
OpenCV to find keypoints.
Going to use keypoint-RCNN because there's more manual processing to be done. Nevermind - its not 3D

PyTorch and YOLOv8 Pose, ViTPose, MMPose to find keypoints based on human. (filter keypoints to keyratios/angles) 
    Find out which options for keypoint detection are best
    Note: Looking for monocoular 3D  (YOLOv8 Pose -> PoseFormer or MotionBERT?)
Train small NN or logistic regression classifier to determine good/bad posture.
Add Backend then deploy.


Todo:
Look for preexisting sitting posture datasets

Activation functions of Pytorch: (have to figure out which one is the best) 
https://docs.pytorch.org/docs/stable/nn.html#non-linear-activations-weighted-sum-nonlinearity

Actual Notes:
Link: https://docs.google.com/document/d/1U5abbSzZvI6JGDtnuu2W8OisjzJU-0dkfZh0DvNB4Uo/edit?tab=t.0
Automatic Differentiation Engine:
    Computation as a graph built at run time
    Example with: recurrent neural network (RNN)
    

(consideration for single training pass)

For visualization:
https://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=circle&regDataset=reg-plane&learningRate=0.03&regularizationRate=0&noise=0&networkShape=4,2&seed=0.609198&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false


Paper's of existing projects + potential datasets:
https://ethanweber.me/documents/posturepal.pdf
^Interesting way of classifying and calculating data - vectors relative to chest vector and posture types (https://ethanweber.me/ one of the guys who was part of it - maybe can contact him with questions and stuff maybe hes a helpful guy)


