# Motion Blur
Motion blur module in Python

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

Load an image
```python
img = Image.open('image.png')
```
![](https://cdn.discordapp.com/attachments/1120417968032063538/1194679023243120690/image-normal.png?ex=65b13a8b&is=659ec58b&hm=1510b72453dafba78d3068e02e043b0abed6314dd712845d7af6810d8b2a4da4&)
---

Basic motion blur
```python
result = motion_blur(img, distance=100, amount=0.75)
```
![](https://cdn.discordapp.com/attachments/1120417968032063538/1194679612769304717/basic_blur.png?ex=65b13b17&is=659ec617&hm=ebfde91b36e9afb5e6066c44ed01b129c9a573c75f2cb4c74868dabf21cd17a5&)
---

Background motion blur
```python
result = background_motion_blur(img, distance_blur=100, amount_blur=0.75, amount_subject=1.0)
```
![](https://cdn.discordapp.com/attachments/1120417968032063538/1194683576709550080/bg_blur.png?ex=65b13ec8&is=659ec9c8&hm=d7e6b2c543518e7450ac25db5aa222a7f7f8047018ac2cca0df0a0d31468fa4f&)
---
