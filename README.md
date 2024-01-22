# Motion Blur
Motion blur module in Python. Supports Basic Motion Blur and a special Background Motion Blur where only the background is blurred. Try the [demo](https://huggingface.co/spaces/tonyassi/motion-blur).

![](https://cdn.discordapp.com/attachments/1120417968032063538/1194679612769304717/basic_blur.png?ex=65b13b17&is=659ec617&hm=ebfde91b36e9afb5e6066c44ed01b129c9a573c75f2cb4c74868dabf21cd17a5&)
![](https://cdn.discordapp.com/attachments/1120417968032063538/1199042638926598184/bg_blur_2.png?ex=65c11a7a&is=65aea57a&hm=6c3957e11e0fdcdb58c94e7bdfbc0fc13dd95ab3dca2eceb2ecebbad04164efb&)

## Installation
```bash
pip install -r requirements.txt
```
If your getting ffmpeg errors when importing then try installing ffmpeg with conda or try one of these [solutions](https://github.com/Zulko/moviepy/issues/1158)
```bash
conda install ffmpeg
```

## Usage
Import PIL
```python
from PIL import Image
```
Import the motion blur module
```python
from Blur import motion_blur, background_motion_blur
```

Load an image using the PIL library
```python
img = Image.open('image.png')
```
![](https://cdn.discordapp.com/attachments/1120417968032063538/1194679023243120690/image-normal.png?ex=65b13a8b&is=659ec58b&hm=1510b72453dafba78d3068e02e043b0abed6314dd712845d7af6810d8b2a4da4&)
---

**Basic Motion Blur**
```python
result = motion_blur(img, distance=100, amount=0.75)
```
- **distance** the distance of the motion blur
- **amount** the amount of motion blur where 0.0 is none and 1.0 is full
  
![](https://cdn.discordapp.com/attachments/1120417968032063538/1194679612769304717/basic_blur.png?ex=65b13b17&is=659ec617&hm=ebfde91b36e9afb5e6066c44ed01b129c9a573c75f2cb4c74868dabf21cd17a5&)
---

**Background Motion Blur** 

Only the background is motion blurred and the subject is unaffected
```python
result = background_motion_blur(img, distance_blur=100, amount_blur=0.75, amount_subject=1.0)
```
- **distance_blur** the distance of the motion blur
- **amount_blur** the amount of motion blur where 0.0 is none and 1.0 is full
- **amount_subject** the opacity of the subject where 0.0 is no subject and 1.0 is full opacity

![](https://cdn.discordapp.com/attachments/1120417968032063538/1199042638926598184/bg_blur_2.png?ex=65c11a7a&is=65aea57a&hm=6c3957e11e0fdcdb58c94e7bdfbc0fc13dd95ab3dca2eceb2ecebbad04164efb&)

## Video
Import the video motion blur module
```python
from Blur import video_motion_blur
```
**Video Motion Blur** 
```python
video_motion_blur(video_path='video.mp4', export_video_path= 'export-video.mp4', distance_blur=100, amount_blur=0.75, amount_subject=1.0)
```
- **video_path** source video
- **export_video_path** path where the final video will be exported to
- **distance_blur** the distance of the motion blur
- **amount_blur** the amount of motion blur where 0.0 is none and 1.0 is full
- **amount_subject** the opacity of the subject where 0.0 is no subject and 1.0 is full opacity
