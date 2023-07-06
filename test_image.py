import torch
import torch.nn as nn
import torch.optim as optim
from torch.optim import lr_scheduler
import torch.backends.cudnn as cudnn
import numpy as np
import torchvision
from torchvision import datasets, models, transforms
import matplotlib.pyplot as plt
import time
import os
from PIL import Image
import copy

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
data_transforms = {
    'train': transforms.Compose([
        transforms.RandomResizedCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ]),
    'val': transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ]),
}

data_dir = '../ten_classes'
image_datasets = {x: datasets.ImageFolder(os.path.join(data_dir, x),
                                          data_transforms[x])
                  for x in ['train', 'val']}
class_names = image_datasets['train'].classes
id_to_plant_name = {"1355936": "Cirsium arvense (L.) Scop.", 
                    "1357330": "Calendula officinalis L.",
                    "1358752": "Lamium purpureum L.",
                    "1359517": "Trifolium pratense L.",
                    "1359616": "Punica granatum L.",
                    "1359620": "Alcea rosea L.",
                    "1361824": "Lavandula angustifolia Mill.",
                    "1363128": "Papaver rhoeas L.",
                    "1363740": "Trifolium repens L.",
                    "1363991": "Fragaria vesca L.",
                    "1364099": "Centranthus ruber (L.) DC.",
                    "1364164": "Lapsana communis L.",
                    "1364173": "Lactuca serriola L.",
                    "1394460": "Anemone nemorosa L.",
                    "1394994": "Pyracantha coccinea M.Roem.",}

MODEL_PATH = "ten_classes.pt"

def eval_image(path):
    img = Image.open(path)
    model_ft = torch.load(MODEL_PATH)

    mean = [0.485, 0.456, 0.406] 
    std = [0.229, 0.224, 0.225]
    transform_norm = transforms.Compose([transforms.ToTensor(), 
    transforms.Resize((224,224)),transforms.Normalize(mean, std)])
    # get normalized image
    img_normalized = transform_norm(img).float()
    img_normalized = img_normalized.unsqueeze_(0)
    # input = Variable(image_tensor)
    img_normalized = img_normalized.to(device)
    # print(img_normalized.shape)
    with torch.no_grad():
        model_ft.eval()  
        output =model_ft(img_normalized)
        # print(output)
        index = output.data.cpu().numpy().argmax()
        class_name = class_names[index]
        print(class_name)
        print(id_to_plant_name[class_name])

if __name__ == '__main__':

    # Specify a path
    IMAGE_PATH = "C:/Users/olaky/Documents/PlantsAI/python/code/1357330.jpg"
    eval_image(IMAGE_PATH)
    