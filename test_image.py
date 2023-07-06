import torch
import matplotlib.pyplot as plt

if __name__ == '__main__':

    # Specify a path
    PATH = "ten_classes.pt"

    #load
    model_ft = torch.load(PATH)
    model_ft.eval()
    #visualize_model(model_ft)

    plt.ioff()
    plt.show()