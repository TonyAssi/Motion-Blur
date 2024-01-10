# Motion Blur
Motion blur module in Python

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
![](https://cdn.discordapp.com/attachments/1120417968032063538/1194676736193998888/image-normal.png?ex=65b13869&is=659ec369&hm=63716ce40a3bc307a8151955393329f81080c1e4d729559ba28be67a3b5fb4fe&)
Basic motion blur
```python
result = motion_blur(img, distance=100, amount=0.75)
```
Background motion blur
```python
result = background_motion_blur(img, distance_blur=100, amount_blur=0.75, amount_subject=1.0)
```
