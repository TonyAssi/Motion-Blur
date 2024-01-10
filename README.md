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
![](https://cdn.discordapp.com/attachments/1120417968032063538/1194678623504973924/image-normal.png?ex=65b13a2b&is=659ec52b&hm=34e2d65c09dc76104e2d1efc61c99cb315ae37a0a69f79e212178b22f9bdc44e&)
Basic motion blur
```python
result = motion_blur(img, distance=100, amount=0.75)
```
Background motion blur
```python
result = background_motion_blur(img, distance_blur=100, amount_blur=0.75, amount_subject=1.0)
```
