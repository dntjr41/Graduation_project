### Graduation Project - Re:Mind
***

* ### [Graduation Project Proposal(Youtube) - Re:Mind](https://youtu.be/V59beXzW11Y)
* ### [Graduation Project Implementation(Youtube) - Re:Mind](https://youtu.be/JECVPx8Vpys)
* ### [Graduation Project Faceswap Demo(Youtube) - Re:Mind](https://youtu.be/Powcvba2DL8)
* ### [Graduation Project Faceswap + Wav2Lip Demo(Youtube) - Re:Mind](https://youtu.be/Powcvba2DL8)

***
> Table Of Contents <br>
> [1. Motivation & Objective](#1-motivation) <br>
> [2. Project Overview](#2-project-overview) <br>
> [3. Technologies Used](#3-technologies-used)<br>
> [4. Implementation Detail](#4-implementation-detail)<br>
> [5. Progress](#5-progress)<br>
> [6. Role & Plan](#6-role-and-plan)<br>

***
# 1. Motivation

| For Reminiscence | For Fun |
| ---------------- | ------- |
| [MBC 다큐멘터리 - 너를 만났다](https://www.youtube.com/watch?v=uflTK8c4w0c) <br> ![reminiscence](https://user-images.githubusercontent.com/67234937/146102612-84c809aa-ab8e-4eae-a202-78c0e40be855.PNG) | [나몰라 패밀리 - 일론머스크](https://www.youtube.com/watch?v=hIzuIuVY3XU) <br> ![fun](https://user-images.githubusercontent.com/67234937/146102538-0e4a337b-18c0-4e47-97ee-649ad0effd91.PNG)|

* As technology advances, the possibilities of things that cannot be done in real life and <br>
that can only be done in virtual reality are increasing and people's desires are also increasing. <br>
From changing characters to creating facial expressions, how to add movement to a photo to make it lively <br>
It can give us fun and meaningful memories to reminisce about loved ones.


* Similar Apps

> * Deep Nostalgia
> * ![6](https://user-images.githubusercontent.com/67234937/121906666-4ac95980-cd66-11eb-9cf8-3b79d9cd8fd1.jpg)
> * Not a Smartphone app
> * Paid Service

> * Deepfake Studio
> * ![7](https://user-images.githubusercontent.com/67234937/121906624-3edd9780-cd66-11eb-8484-279e5ede4f1d.png)
> * Vlunerable to security
> * Just face Swapping (Deepfake)
> * Vulnerable to security

> * Wav2Lip
> * ![image](https://user-images.githubusercontent.com/67234937/146102703-4c993f9d-a41f-4c7c-81d9-d8c6ccdfd05c.png)
> * Just Lip-Syncing (DeepVoice)
> * Bad User Experience


* ### Objective
* DeepFake(Face Swap) + Lip-Syncing (+My Voice)
* ![objective](https://user-images.githubusercontent.com/67234937/146103031-fa182c6a-93a5-45d1-a515-746e56e23209.PNG)
* ![11](https://user-images.githubusercontent.com/67234937/121907856-6b45e380-cd67-11eb-9a7d-c037388c0a3c.png) ![ezgif com-gif-maker (6)](https://user-images.githubusercontent.com/67234937/121911056-5e76bf00-cd6a-11eb-8600-1712b0175562.gif) ![10](https://user-images.githubusercontent.com/67234937/121907196-cb885580-cd66-11eb-8655-793108bf9942.png)

* Cross Platform Application (Web + Mobile)
* ![image](https://user-images.githubusercontent.com/67234937/146103129-d687ae3f-a5f6-4b24-adf8-e51eb8f64da1.png)


***
# 2. Project Overview

| | Key Features | 
| ------------ | ----------------------------- |
| ![image](https://user-images.githubusercontent.com/67234937/146103594-bdccf9f2-a624-449c-85c2-427e8ea5a608.png) | For fun & reminiscence <br><br> DeepFake (FaceSwap) + Lip Syncing <br><br> Cross Platform App (Windows, Mac, Android) <br><br> Easy To Use <br><br> Better UI/UX <br><br> Training One-shot (Picture) <br><br> High Quality + Done Quickly <br><br> Various templates |

| Divide into two tracks |
| ---------------------- |
| 1. Gif File (3 ~ 4 Seconds) + No Voice file <br> ![image](https://user-images.githubusercontent.com/67234937/146105153-c384efe7-1c62-49d9-aec2-9da4d98493f1.png) |
| 2. MP4 file (30~60 Seconds) + Voice file <br> ![image](https://user-images.githubusercontent.com/67234937/146105203-0ce68a35-4b91-4922-87a5-e6f4f9742471.png) |

* Sequence Diagram <br> ![image](https://user-images.githubusercontent.com/67234937/146105242-c19ec3b3-878e-4f73-b4e4-488f444c9f5f.png)
* Usecase Diagram <br> ![image](https://user-images.githubusercontent.com/67234937/146105291-4570f9cd-2a40-4ab6-9daa-bb35e4d890a4.png)

### Structure
![image](https://user-images.githubusercontent.com/67234937/146105333-a7c79e6d-f946-42bf-9c28-fa88b0735ddc.png)

***
# 3. Technologies used

| Model |
| ----- |
| ![image](https://user-images.githubusercontent.com/67234937/146105492-b22a91f0-1bcb-43c0-87a1-4e49429cfdb2.png) |
| Requirements - Training Time, Convenience |

| Model - Deep Fake [(Reference.SimSwap)](https://github.com/neuralchen/SimSwap) |
| ------------------------------------- |
| ![image](https://user-images.githubusercontent.com/67234937/146105617-e7dbd0c2-4629-42a3-8366-8797fca0acf9.png) |
| ![image](https://user-images.githubusercontent.com/67234937/146105645-ee015349-e2f3-4c96-ad57-f042ac3787cb.png) <br> Overcome the defects in generalization and attribute preservation <br> Generalization to Arbitrary Identify   +   Preserving the Attributes of the Target | 
| Image To Gif <br> ![image](https://user-images.githubusercontent.com/67234937/146105849-aefaa960-daa8-49b7-b5d6-f99776056886.png) | 

| Model - Lip Syncing [(Reference.Wav2lip)](https://github.com/Rudrabha/Wav2Lip) |
| --------------------------------------- |
| ![image](https://user-images.githubusercontent.com/67234937/146105906-d539f4c8-25fb-43b0-be61-cc0256b83c5a.png) <br> Extraction -> Training -> Converting | 
| Image + Voice To MP4 <br> ![image](https://user-images.githubusercontent.com/67234937/146105994-fa57ec8c-56c6-450e-9d83-3b438e482545.png) |

| Model - Voice Extraction [(Reference.Spleeter)](https://github.com/deezer/spleeter) |
| --------------------------------------------- |
| ![image](https://user-images.githubusercontent.com/67234937/146106122-93256bce-411b-480b-8b20-0e80433b5550.png) <br> Extract only voice from mp3, mp4 or wav file -> Better Quality !! |

| Cross Platform Application (Flask + Flutter) |
| -------------------------------------------- |
| ![image](https://user-images.githubusercontent.com/67234937/146106245-a0371f98-e172-4ecc-baa5-410f9bc6c475.png) <br> Python Application & Cross Platform |

***
# 4. Implementation Detail

* Model - Python Library
* Deepfake (SimSwap) - Insightface, torch, torchVision, Cuda, cv2, tensorflow
* Lip-Syncing (Wav2lip) - Opencv, torch, torchVision, Cuda, librosa, tensorflow
* Voice Extraction (Spleeter) - tensorflow, ffmpeg-python, norbert, librosa, typer

| Model - Deep Fake [(Reference.SimSwap)](https://github.com/neuralchen/SimSwap) |
| ------------------------------------- |
| 1. Set Image Size <br> ![image](https://user-images.githubusercontent.com/67234937/146106901-51add445-9d8b-426f-824c-ec1b724461c7.png) <br> 2. Set Option (Weights) <br> ![image](https://user-images.githubusercontent.com/67234937/146106942-909f9f9a-c086-4423-be69-f834027efa89.png) <br> 3. Convert (Main) <br> ![image](https://user-images.githubusercontent.com/67234937/146107000-31abe34f-fe7e-43de-919f-3325e053fce5.png) |

| Model - Lip Syncing [(Reference.Wav2lip)](https://github.com/Rudrabha/Wav2Lip) |
| --------------------------------------- |
| 1. Data Parse <br> ![image](https://user-images.githubusercontent.com/67234937/146107092-6749e34e-2226-406f-bf88-8501e91f064c.png) <br> 2. Face Detect <br> ![image](https://user-images.githubusercontent.com/67234937/146107118-de057a90-ba69-4fd2-8c04-0182208b607a.png) <br> 3. Data Generation <br> ![image](https://user-images.githubusercontent.com/67234937/146107158-64fc20cd-d5bf-469a-858c-91ae9f76effa.png) <br> 4. Load Model & Weights <br> ![image](https://user-images.githubusercontent.com/67234937/146107183-5b358b3e-894a-4e4b-8a81-41fd9bca1a37.png) <br> 5. Main <br> ![image](https://user-images.githubusercontent.com/67234937/146107230-2a4cf0c0-38be-4256-8a01-a566594f3a9c.png) |

| Model - Voice Extraction [(Reference.Spleeter)](https://github.com/deezer/spleeter) |
| --------------------------------------------- |
| Main (In Lip-Syncing) <br> ![image](https://user-images.githubusercontent.com/77625823/171043328-f360821b-2bd8-4ad9-89b6-caa55fef2e0b.png) |

| Flask (Backend) |
| --------------- |
| 1. Gif transformation <br> ![image](https://user-images.githubusercontent.com/77625823/171043511-d0048e22-f3fb-42a0-bb0a-375a5e5987d0.png) <br> 2. MP4 transformation <br> ![image](https://user-images.githubusercontent.com/77625823/171043785-ce353923-f173-4aa4-8b66-10af79080ca4.png) |

| Flutter (Frontend) |
| ------------------ |
| Modeling -> Return the Result <br> ![image](https://user-images.githubusercontent.com/77625823/171043953-d5896fb2-4466-4165-b8d6-d433dfc30065.png)![image](https://user-images.githubusercontent.com/77625823/171043995-c54d609f-ef07-4308-8923-a2cef0a6c21e.png)
 |

### 1st Mentoring Feedback
* 1. Processing speed, model capacity problem <br> -> Lightweight model
* 2. Wav2lip model is a model tailored to English <br> -> Since the expected user is Korean, <br> training after changing the dataset.

| Lightweight model |
| ----------------- |
| To shorten the learning time, The training file is built in advance <br> ![image](https://user-images.githubusercontent.com/67234937/146107787-76010f38-2b68-48d8-9c83-7e173096a9a4.png) |
| Lightweight - Deepfake |
| Parameter was changed in consideration of Running Time & Quality <br> ![image](https://user-images.githubusercontent.com/67234937/146107928-c2f58c2d-0823-4df5-96aa-ac3f47ff04ca.png) <br> 
| Lightweight - Lip-Syncing |
| Parameter was changed in consideration of Eval model's sync, train loss & fps <br> ![image](https://user-images.githubusercontent.com/67234937/146108047-3d025414-49bc-434b-905a-e252e9f58075.png) <br> ![image](https://user-images.githubusercontent.com/67234937/146108060-321d00f5-36cb-42ac-a440-f9d5b3cfeab4.png) |

| Changing weight dataset |
| ----------------------- |
| Compare them according to the environment of each datset (LRW, LRS2, LRS3) <br> ![image](https://user-images.githubusercontent.com/67234937/146108188-f2d17696-d33e-45c7-9e8e-eee30463f7de.png) <br> Translating sounds from the Eastern Languages: LRS3 -> LRS2 <br> But LRS3 has a lot of artifacts around the face. Use LRS2 |

| Lightweight Result |
| ------------------ |
| ![image](https://user-images.githubusercontent.com/67234937/146108316-b6dd4488-67fe-4117-96c9-bbd92c8048c1.png) |

### 2nd Mentoring Feedback
* 3. Cloud Server Instance & Cost Problems <br> -> We must use CUDA, Need GPU Server. <br> So, Looking for a solution 

| Cloud Server Instance & Cost |
| ---------------------------- |
| Trying to deploy the Cloud GPU Server <br> ![image](https://user-images.githubusercontent.com/67234937/146108582-b3e72af7-779c-4269-8676-9522c899a523.png) |
| Very Expensive Server Cost -> Looking for a Solution <br> ![image](https://user-images.githubusercontent.com/67234937/146108658-b8a4072d-099e-4cbf-b19d-29ff881eb99a.png) |

***
# 5. Progress

| Template (GIF 짤방) | Template (MP4) |
| ------------------ | --------------- |
| ![image](https://user-images.githubusercontent.com/67234937/146108862-acf415a9-259c-4b38-ae52-0fbd0e3d4d2f.png) | ![image](https://user-images.githubusercontent.com/67234937/146108889-eaca6387-6cf8-40a6-a930-7e2cd61a8e58.png) |

| Flutter Demo |
| ------------ |
| ![image](https://user-images.githubusercontent.com/67234937/146108943-b79eecef-bef3-4146-8073-cf1de3172f45.png) |
| ![image](https://user-images.githubusercontent.com/67234937/146108988-04478a20-4a2f-4e28-8e3e-3515ef2bf2df.png) |
| ![image](https://user-images.githubusercontent.com/67234937/146109007-d1033b62-f127-4f9d-9da6-0129e35cda90.png) |
| ![image](https://user-images.githubusercontent.com/67234937/146109024-6a0d5d86-03a6-4453-b58a-9f8cc5665a92.png) |

| Gif Template Demo |
| ----------------- |
| Source - ![image](https://user-images.githubusercontent.com/67234937/146109083-e55e437a-8cf0-4900-8977-138a89fd9b65.png) target - ![그림1](https://user-images.githubusercontent.com/67234937/146109210-5b15ffb9-9623-42a3-8eac-4c17d11e1d16.gif) = Result Gif file - ![ezgif com-gif-maker](https://user-images.githubusercontent.com/67234937/146109353-a72edd45-8c65-42ce-a038-72722eeadd25.gif) |

| MP4 (Video) Template Demo |
| ------------------------- |
| Source - ![image](https://user-images.githubusercontent.com/67234937/146109479-9738f0dd-7f9c-4769-911c-66cd1eb660a5.png) + Source Voice File ![image](https://user-images.githubusercontent.com/67234937/146109518-6608991e-301d-4d0a-95b4-e11cb07186ec.png) <br> = Result MP4 file - https://user-images.githubusercontent.com/67234937/146109628-a4bffe50-59e5-4ec2-adb5-62d9ca995947.mp4 |

***
# 6. Role and Plan
* Plan
* ![plan](https://user-images.githubusercontent.com/67234937/146101634-fbb26b30-3a7d-46a8-a67a-9d8bf08652e4.PNG)

* Role

<table>
<tr> <td>심우석(201636417)</td> <td>Model Lightweight, Server</td> </tr>
<tr> <td>오찬희(201735855)</td> <td>Model Lightweight, Modeling</td> </tr>
<tr> <td>김다혜(201835414)</td> <td>Modeling, Flutter</td> </tr>
<tr> <td>선다혜(201835466)</td> <td>Modeling, Flutter</td> </tr>
</table>
