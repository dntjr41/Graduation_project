### Graduation Project - Re:Mind
***

* ### [Graduation Project Proposal(Youtube) - Re:Mind](https://youtu.be/V59beXzW11Y)
* ### [Graduation Project Implementation(Youtube) - Re:Mind](https://youtu.be/JECVPx8Vpys)

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

| Model - Deep Fake [Reference.SimSwap](https://github.com/neuralchen/SimSwap) |
| ------------------------------------- |
| ![image](https://user-images.githubusercontent.com/67234937/146105617-e7dbd0c2-4629-42a3-8366-8797fca0acf9.png) |
| ![image](https://user-images.githubusercontent.com/67234937/146105645-ee015349-e2f3-4c96-ad57-f042ac3787cb.png) <br> Overcome the defects in generalization and attribute preservation <br> Generalization to Arbitrary Identify   +   Preserving the Attributes of the Target | 
| Image To Gif <br> ![image](https://user-images.githubusercontent.com/67234937/146105849-aefaa960-daa8-49b7-b5d6-f99776056886.png) | 

| Model - Lip Syncing [Reference.Wav2lip](https://github.com/Rudrabha/Wav2Lip) |
| --------------------------------------- |
| ![image](https://user-images.githubusercontent.com/67234937/146105906-d539f4c8-25fb-43b0-be61-cc0256b83c5a.png) <br> Extraction -> Training -> Converting | 
| Image + Voice To MP4 <br> ![image](https://user-images.githubusercontent.com/67234937/146105994-fa57ec8c-56c6-450e-9d83-3b438e482545.png) |

| Model - Voice Extraction [Reference.Spleeter](https://github.com/deezer/spleeter) |
| --------------------------------------------- |
| ![image](https://user-images.githubusercontent.com/67234937/146106122-93256bce-411b-480b-8b20-0e80433b5550.png) <br> Extract only voice from mp3, mp4 or wav file -> Better Quality !! |

| Cross Platform Application (Flask + Flutter) |
| -------------------------------------------- |
| ![image](https://user-images.githubusercontent.com/67234937/146106245-a0371f98-e172-4ecc-baa5-410f9bc6c475.png) <br> Python Application & Cross Platform |

***
# 4. Implementation Detail












***
# 5. Progress

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
* ![plan](https://user-images.githubusercontent.com/67234937/146101634-fbb26b30-3a7d-46a8-a67a-9d8bf08652e4.PNG)

* Role

<table>
<tr> <td>심우석(201636417)</td> <td>Model Lightweight, Server</td> </tr>
<tr> <td>오찬희(201735855)</td> <td>Model Lightweight, Modeling</td> </tr>
<tr> <td>김다혜(201835414)</td> <td>Modeling, Flutter</td> </tr>
<tr> <td>선다혜(201835466)</td> <td>Modeling, Flutter</td> </tr>
</table>
