# DigitRecognition.py
# Jamison Talley
# 2024-04-18

# import necessary modules
import torch
from torch import nn
from torch.utils.data import DataLoader
import torch.nn.functional as F
import torchvision
import torchvision.transforms as transforms
from torchvision import datasets
from torchvision.transforms import ToTensor
import matplotlib.pyplot as plt
import numpy as np
import torch.optim as optim

# initialize data set
transform = transforms.Compose(
    [transforms.ToTensor(),
     transforms.Normalize((0.05), (0.05))])
batch_size = 128
trainset = torchvision.datasets.MNIST(root='./data', train=True,
                                        download=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=batch_size,
                                          shuffle=True, num_workers=2)
testset = torchvision.datasets.MNIST(root='./data', train=False,
                                       download=True, transform=transform)
testloader = torch.utils.data.DataLoader(testset, batch_size=batch_size,
                                         shuffle=False, num_workers=2)
classes = ('zero', 'one', 'two', 'three',
           'four', 'five', 'six', 'seven', 'eight', 'nine')

# specify network hyperparameters
class NetCnnBn(nn.Module):
    def __init__(self):
      super().__init__()
      self.conv_l1 = nn.Conv2d(1,8,3,1,1)
      self.conv_l2 = nn.Conv2d(8,16,3,1,1)
      self.bn1 = nn.BatchNorm2d(16)
      self.mp_l3 = nn.MaxPool2d(2,2)
      self.conv_l4 = nn.Conv2d(16,32,3,1,1)
      self.conv_l5 = nn.Conv2d(32,64,3,1,1)
      self.mp_l6 = nn.MaxPool2d(2,2)
      self.fc7 = nn.Linear(64 * 7 * 7, 50)
      self.bn2 = nn.BatchNorm1d(50)
      self.fc8 = nn.Linear(50, 10)

    def forward(self, x):
      x1 = F.relu(self.conv_l1(x))
      x2 = F.relu(self.conv_l2(x1))
      x2 = self.bn1(x2)
      x3 = F.relu(self.mp_l3(x2))
      x4 = F.relu(self.conv_l4(x3))
      x5 = F.relu(self.conv_l5(x4))
      x6 = F.relu(self.mp_l6(x5))
      x6 = torch.flatten(x6, 1)
      x7 = F.relu(self.fc7(x6))
      x7 = self.bn2(x7)

      output = self.fc8(x7)
      return output
    
# create helper function to train and test the model
class hlp():
  def trainMyModel(net,lr,trainloader,n_epochs):
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    net = net.to(device)

    net.train()
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(net.parameters(), lr)
    for epoch in range(n_epochs):  

      running_loss = 0.0
      for i, data in enumerate(trainloader, 0):
          inputs, labels = data
          inputs = inputs.to(device)
          labels = labels.to(device)

          optimizer.zero_grad()

          outputs = net(inputs)
          loss = criterion(outputs, labels)
          loss.backward()
          optimizer.step()

          running_loss += loss.item()
          if i % 100 == 99:
            print(f'[{epoch + 1}, {i + 1:5d}] loss: {running_loss / 100:.3f}')
            running_loss = 0.0

    print('Finished Training')
    return net

  def testMyModel(trainedNet,testloader):
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    net = trainedNet.to(device)

    correct = 0
    total = 0

    with torch.no_grad():
        for data in testloader:
            images, labels = data
            images = images.to(device)
            labels = labels.to(device)
            outputs = net(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    acc = np.round(correct * 100 / total,4)
    print(f'Accuracy of the network on the 10000 test images: {acc} %')
    return acc

# train and test the model
net = NetCnnBn()
lr = 0.01
n_epochs = 2
trainedNet = hlp.trainMyModel(net,lr,trainloader,n_epochs)
hlp.testMyModel(trainedNet,testloader)