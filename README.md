# Motion Blur
Motion blur module in Python. Supports Basic Motion Blur and a special Background Motion Blur where only the background is blurred. Try the [demo](https://huggingface.co/spaces/tonyassi/motion-blur).

![](https://cdn.discordapp.com/attachments/1120417968032063538/1194679612769304717/basic_blur.png?ex=65b13b17&is=659ec617&hm=ebfde91b36e9afb5e6066c44ed01b129c9a573c75f2cb4c74868dabf21cd17a5&)
![](https://cdn.discordapp.com/attachments/1120417968032063538/1194683576709550080/bg_blur.png?ex=65b13ec8&is=659ec9c8&hm=d7e6b2c543518e7450ac25db5aa222a7f7f8047018ac2cca0df0a0d31468fa4f&)

## Installation
```bash
pip install -r requirements.txt
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

![](https://cdn.discordapp.com/attachments/1120417968032063538/1194683576709550080/bg_blur.png?ex=65b13ec8&is=659ec9c8&hm=d7e6b2c543518e7450ac25db5aa222a7f7f8047018ac2cca0df0a0d31468fa4f&)
