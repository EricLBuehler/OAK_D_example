  # -*- coding: utf-8 -*-


from webcam import webcam as webc
from matplotlib import pyplot as plt
import cv2
import time
import torch
from PIL import Image
import torchvision.transforms as transforms


transform = transforms.Compose([transforms.ToTensor()])

to_pil=transforms.ToPILImage()

webcam=webc()
img=webcam.read()

webcam.saveread(img, "img.jpg")

tensor=transform(img)
print(tensor.max(), tensor.min())
print(tensor.size())

plt.imshow(img, cmap='gray')
plt.show()

webcam.kill()