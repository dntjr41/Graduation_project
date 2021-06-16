### Graduation Project - Re:Mind
***

* ### [Graduation Project Proposal(Youtube) - Re:Mind](https://youtu.be/V59beXzW11Y)

***
> Table Of Contents <br>
> [1. Motivation](#1-motivation) <br>
> [2. Key features](#2-key-features) <br>
> [3. Technologies Used](#3-technologies-used)<br>
> [4. Progress](#4-progress)<br>
> [5. Development plan](#5-development-plan)<br>
> [6. Role & Plan](#6-role-and-plan)<br>

***
# 1. Motivation

| IF ???           |                                                                                                           |
|------------------|-----------------------------------------------------------------------------------------------------------|
| I'M Actor        |![1](https://user-images.githubusercontent.com/67234937/121903590-6e3ed500-cd63-11eb-87e2-c8efdc664bc8.png)|
| My Parents Alive |![2](https://user-images.githubusercontent.com/67234937/121904566-41d78880-cd64-11eb-9987-90c366aded0c.png)|

* [MBC 다큐멘터리 - 너를 만났다](https://www.youtube.com/watch?v=uflTK8c4w0c)
* ![3](https://user-images.githubusercontent.com/67234937/121905155-ce824680-cd64-11eb-8710-8691d96ed31d.png)
* As technology advances, the possibilities of things that cannot be done in real life and <br>
that can only be done in virtual reality are increasing and people's desires are also increasing. <br>
From changing characters to creating facial expressions, how to add movement to a photo to make it lively <br>
It can give us fun and meaningful memories to reminisce about loved ones.

| For Fun | For Reminiscence |
|------------------|-----------------------------------------------------------------------------------------------------------|
| ![4](https://user-images.githubusercontent.com/67234937/121905650-5700e700-cd65-11eb-9aa8-09f547fd1b5a.png)|![5](https://user-images.githubusercontent.com/67234937/121905674-5ff1b880-cd65-11eb-81cf-eafc58f268a4.png) ![2](https://user-images.githubusercontent.com/67234937/121905811-7b5cc380-cd65-11eb-8550-8b5d12e2658a.png)|

* Similar Apps
> * Deepfake Studio
> * ![7](https://user-images.githubusercontent.com/67234937/121906624-3edd9780-cd66-11eb-8484-279e5ede4f1d.png)
> * Vlunerable to security
> * Just face Swapping
> * Inconvenient use

> * Deep Nostalgia
> * ![6](https://user-images.githubusercontent.com/67234937/121906666-4ac95980-cd66-11eb-9cf8-3b79d9cd8fd1.jpg)
> * Not a Smartphone app
> * Paid Service

* ### Re:Mind
* ![8](https://user-images.githubusercontent.com/67234937/121906887-83693300-cd66-11eb-8079-d0be0d8f5e04.png)
* Smartphone App
* Remind Person in memory
* Make my own deep fake video

***
# 2. Key features

| DeepFake(Face Swap) +  Speech To Text(Lip Sync) |
|----------------------------------------------|
| ![9](https://user-images.githubusercontent.com/67234937/121907150-c0cdc080-cd66-11eb-98ae-7e89fca66dfa.jpg) ![10](https://user-images.githubusercontent.com/67234937/121907196-cb885580-cd66-11eb-8655-793108bf9942.png) |
| ![11](https://user-images.githubusercontent.com/67234937/121907856-6b45e380-cd67-11eb-9a7d-c037388c0a3c.png) ![ezgif com-gif-maker (6)](https://user-images.githubusercontent.com/67234937/121911056-5e76bf00-cd6a-11eb-8600-1712b0175562.gif) |

| Hard to Use + You need to install the program |
| ------------------------------------------------|
| <img width="353" alt="faceSwap" src="https://user-images.githubusercontent.com/67234937/121908248-c546a900-cd67-11eb-96d3-e13994ccb599.PNG"> <img width="332" alt="deepfacelab" src="https://user-images.githubusercontent.com/67234937/121908479-02ab3680-cd68-11eb-90db-74504c13aadd.PNG"> <img width="325" alt="libsync" src="https://user-images.githubusercontent.com/67234937/121908598-1f476e80-cd68-11eb-83ea-30c1ca3b0e25.png"> |
| ![13](https://user-images.githubusercontent.com/67234937/121908668-2cfcf400-cd68-11eb-8525-e0a64ef40cdb.png) |

| Do you want Quality? or Time? |
| ----------------------------- |
| ![ezgif com-gif-maker](https://user-images.githubusercontent.com/67234937/121912528-9f230800-cd6b-11eb-8a77-96dc51d1022b.jpg) |

* ### Re:Mind
* Easy to Use
* DeepFake + Speech To Text(Lip Sync)
* High Quality + Done Quickly Or <br>
Low Quality + Done Slowly

***
# 3. Technologies used

* [Deep Fake(Face Swap)](https://en.wikipedia.org/wiki/Deepfake)
* A deep learning – based technique able to create fake images/videos.
* Swapping the face of a person in an image or video by the face of another person.
* To create an image or video, it has to go through 3 processes.
* A. Extraction -> B. Training -> C. Converting
<br>

* A. Extraction

| To generate a set of faces, and optionally <br> on alignments file and mask, for training. <br><br> To generate an alignments file and <br> mask for converting your final frames. |
| ---------------------------------------------------- |
| ![23](https://user-images.githubusercontent.com/67234937/121984519-12f5fc80-cdce-11eb-98b8-95d2b753491d.png) ![22](https://user-images.githubusercontent.com/67234937/121984564-2903bd00-cdce-11eb-8c6a-27f5da667433.png) |
<br>

* B. Training
* ![24](https://user-images.githubusercontent.com/67234937/121984928-d080ef80-cdce-11eb-843f-eb193c802413.png)
* Few-Shot - 3 ~ 5 images, Multi-shot - 2000 > images

* B. Training(Few-Shot)
* ![25](https://user-images.githubusercontent.com/67234937/121985241-5a30bd00-cdcf-11eb-817f-ffd88b9382e7.png)
* [FUNIT(Few-Shot Unsupervised Image-to-Image Translation)](https://github.com/NVlabs/FUNIT)
* In the case of a Few shot, you need to create a dataset first because there are few datasets. <br> 
So, we are considering two approaches in this section. First up is Funit. <br>
With just a few example images during testing, Funit can create photos of various <br>
expressions and angles with technology applied to the target layer that has never been seen before. <br>
It has the advantage of being fast, but it is an algorithm that was originally applied to animals, <br> 
so the result is a bit disappointing for humans. <br>

* ![26](https://user-images.githubusercontent.com/67234937/121985447-b562af80-cdcf-11eb-904c-9eee171cf308.png)
* [StyleGAN(A Style-Based Generator Architecture for GANs](https://www.youtube.com/watch?v=eaW_P85wQ9k)
* The second method is the method using styleGAN. <br>
StyleGAN sees the image as a combination of styles, and synthesizes the image <br>
by applying style information to each layer of the generator.<br>
At this time, the style added in each layer can control different levels of visual attributes <br>
from coarse features (gender, pose, etc.) of the image to fine details (hair color, skin tone, etc.). <br>
Using this styleGAN, it is possible to generate photos of various angles and expressions through the learned 3D architecture. <br>
In the case of styleGAN, it produces very stable and high-quality images, but the time is a bit slow. <br>
So, we decided to decide one of the two methods through the consumer requirement research and development process. <br>

* ![27](https://user-images.githubusercontent.com/67234937/121985620-0ffc0b80-cdd0-11eb-89c5-32908cd03292.png)
* [AdaIN (Adaptive Instance Normalization)](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=tlqordl89&logNo=221536378926)
* AdaIN is a normalization method for style conversion, and when you input a content image and a style image, <br>
the content image is changed to the style of the style image.<br>
Therefore, we can change the semantic map of the face extracted earlier to the face of the person we want to change, <br>
that is, the style of the photorealistic. <br>

* ![28](https://user-images.githubusercontent.com/67234937/121985741-52254d00-cdd0-11eb-8517-03eff2efe592.png)
* [SPADE (Spatially-Adaptive Normalization)](https://github.com/NVlabs/SPADE)
* However, it cannot be said that it is a perfect live-action painting <br> 
because the style of painting remains with the result of Adain alone. So what we're going to use here is SPADE. <br>
The conv process (conv → normalize → activation) is commonly used in the image-to-image translation process. <br>
In this case, the normalization layer has the disadvantage of “losing” the information of the input image. <br>
However, in SPADE, element-wise affine transformation operation proceeds <br>
through the form of a tensor, not through the average variance value in the semantic image. <br>
This allows you to change the style while maximizing the information in the semantic image. <br>
Through this SPADE, photo-realization processing will take place. <br>

* ![29](https://user-images.githubusercontent.com/67234937/121985922-a03a5080-cdd0-11eb-8981-c39d0e5c5468.png)
* Few-Shot -> FUNIT or StylerGAN + AdaIN + SPADE
<br>

* B. Training - Multi-Shot
* ![30](https://user-images.githubusercontent.com/67234937/121986055-dbd51a80-cdd0-11eb-8c8d-97da892ac2b1.png) + ![31](https://user-images.githubusercontent.com/67234937/121986075-e2639200-cdd0-11eb-86d9-0e160202cf65.png)
* [AutoEncoder – For troubleshooting](https://en.wikipedia.org/wiki/Autoencoder)
* Training in multi-shot <br>
Image training will be done using autoencoders based on Keras and TensorFlow. <br>
In general, the autoencoder is used to convert the original data into compressed information through the encoder, <br>
and then go through the decoder to restore the original image.<br><br>
But here the encoder part of A and B will be shared. Therefore, similar features can be learned from two photos, <br>
and a latent layer can be visualized that only visualizes these features, such as the outline <br>
of the body excluding the identity, and the location of the eyes, nose and mouth. <br>
Through this process, you can learn the identity of features such as <br>
eye shape and nose size through learning in the decoder part.<br>

* ![32](https://user-images.githubusercontent.com/67234937/121986377-5aca5300-cdd1-11eb-975b-691f226a23b8.png)
* [GAN (Generative adversarial networks)](https://en.wikipedia.org/wiki/Generative_adversarial_network)
* Through these autoencoders, we will form a generative network of GANs to drive the results.
<br>

* C. Converting
* ![33](https://user-images.githubusercontent.com/67234937/121986495-8f3e0f00-cdd1-11eb-8f97-1c3cdfdf3496.png) ->
* ![34](https://user-images.githubusercontent.com/67234937/121986513-96651d00-cdd1-11eb-905f-acdcd7e60b85.png) ![ezgif com-gif-maker (7)](https://user-images.githubusercontent.com/67234937/121986729-04a9df80-cdd2-11eb-8197-cf6bd55f56e7.gif)
<br>

* [Speech-to-Lip Sync](https://github.com/Rudrabha/LipGAN)
* A deep learning – based technique able to change the sound to lib sync.
* Technology that converts acoustic speech signals obtained through sound sensors such as voice recordings and microphones into lib sync.
* In order to achieve recognized results, it has to go through 3 processes.
* A. Extraction -> B. Tranining -> C. Converting
<br>

* A. Extraction
* The extraction of the intonation, voice size, etc. of a voice signal in numerical form is called a characteristic vector.
* SST use characteristic vectors to generate criteria to determine the meaning of voice signals.
<br>

* B. Training
* ![35](https://user-images.githubusercontent.com/67234937/121987047-a16c7d00-cdd2-11eb-967f-d40ab82a31d8.png)
* In this way, we encode the voice signal, and in the case of the face encoder, <br>
we proceed with the encoding through face recognition as described earlier in face swap. <br>
It then decodes using both encoders, compares the result with the speech encoder, calculates and adjusts the sync. <br>
<br>

* C. Converting
* Audio -> ![36](https://user-images.githubusercontent.com/67234937/121987122-ca8d0d80-cdd2-11eb-945b-0780b9c66a3d.jpg) -> ![1](https://user-images.githubusercontent.com/67234937/121987151-d973c000-cdd2-11eb-999e-54e68750d1ab.gif) ![2](https://user-images.githubusercontent.com/67234937/121987158-ded10a80-cdd2-11eb-8b01-5af1c7083260.gif) ![3](https://user-images.githubusercontent.com/67234937/121987172-e690af00-cdd2-11eb-9236-04e361ccc2d6.gif) 
* ![ezgif com-gif-maker (9)](https://user-images.githubusercontent.com/67234937/121988044-a6323080-cdd4-11eb-855b-8871eb8fa7f6.gif)
<br>

* Framework

| Modeling  | Mobile Implementation + Server | Version Control |
|---------|------------------------------|---------------|
| PyCharm + TensorFlow, Keras | Android Studio + AWS, Firebase | Github |


***
# 4. Progress

| Sequence diagram | Usecase diagram |
|----------------- |-----------------|
| ![14](https://user-images.githubusercontent.com/67234937/121909576-04c1c500-cd69-11eb-9228-c1f63aee7716.png) | ![15](https://user-images.githubusercontent.com/67234937/121909608-0d1a0000-cd69-11eb-9834-e3da05537157.png) |

* Agile Development
* ![16](https://user-images.githubusercontent.com/67234937/121910012-70a42d80-cd69-11eb-84fd-e03da2a3d153.png)

***
# 5. Development Plan

* Focus Direction
<table>
<tr><th>Distinction</th><th>Effective</th></tr>
<tr><td>DeepFake + Lip-synching</td><td>If a person who wants to remember has only <br>
 a picture and a voice left, the prospect is that <br>
it can be provided as if he or she is speaking the voice.</td></tr>
<tr><td>Existing <br>
-> cover only human face <br>
-> My image or base image requires mouth shape to move</td>
<td>User can synthesize your own face and <br> say your own lines in the best scenes of the movie.
</td></tr>
</table>

* Application Screen

| Screen | Description |
| --- | ---- |
|![18](https://user-images.githubusercontent.com/67234937/121983731-c2ca6a80-cdcc-11eb-9e82-1000824508d9.png) | [Home Screen]<br><br> Provides a list of application <br> self-recommended base images. <br><br> Home / Search / Settings Search can use <br> base images and search functions <br> divided by tags |
|![19](https://user-images.githubusercontent.com/67234937/121983997-2e143c80-cdcd-11eb-84b0-08d5fe564cd4.png) | [Choice Fabrication Mode]<br><br> First screen available when <br> base image is selected.<br><br> Quick: fast time, low quality<br>Quality: slow time, high quality |
|![20](https://user-images.githubusercontent.com/67234937/121984092-58fe9080-cdcd-11eb-8504-b60fea79366a.png) | [Voice Input]<br><br> Enter a voice for the <br> lip-syncing function. <br><br> Select files that have already <br> been recorded, Proceeding to a live<br> recording |
|![21](https://user-images.githubusercontent.com/67234937/121984186-80555d80-cdcd-11eb-97d2-a8c4905f5177.png) | [Result]<br><br> Download and share <br><br> Using voice function -> mp4 <br> If not ->  gif or jpg |

***
# 6. Role and Plan
* Plan
* <img width="600" alt="17" src="https://user-images.githubusercontent.com/67234937/121911176-7ea67e00-cd6a-11eb-8d9d-544f76e1bf19.PNG">

* Role

<table>
<tr> <td>심우석(201636417)</td> <td>DeepFake Research, GAN, SPADE, AdaIN, Tensorflow, Keras Study</td> </tr>
<tr> <td>오찬희(201735855)</td> <td>DeepFake Research, GAN, SPADE, AdaIN, Tensorflow, Keras Study</td> </tr>
<tr> <td>김다혜(201835414)</td> <td>Speech To text Research, Server Study</td> </tr>
<tr> <td>선다혜(201835466)</td> <td>Speech To text Research, Development Environment Study</td> </tr>
</table>
