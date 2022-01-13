import matplotlib.pyplot as plt

from librairie import *


def evaluate(ordering, requestImageName):
    requestBrand = int(requestImageName.split("_")[0])
    recalls = []
    precisions = []
    RR = 0
    T = 0
    N = len(ordering)
    for i in range(N):
        if int(ordering[i].imageName.split("_")[0]) == requestBrand:
            RR += 1
            T += 1
        recalls.append(RR)
        precisions.append(RR/(i+1))
    if T != 0:
        for i in range(N):
            recalls[i] = recalls[i] / T

    plt.plot(recalls, precisions)
    plt.xlabel("Rappel")
    plt.ylabel("Precision")
    plt.title("Courbe de Rappel/Pecision")
    plt.savefig("recallprecision.jpg", bbox_inches="tight")

    return recalls[20], precisions[20], recalls[50], precisions[50]