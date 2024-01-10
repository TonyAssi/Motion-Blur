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
Basic motion blur
```python
result = motion_blur(img)
```
Background motion blur
```python
result = background_motion_blur(img)
```
