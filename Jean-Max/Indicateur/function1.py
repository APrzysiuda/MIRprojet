import numpy as np
import cv2
import os


class Distance:
    def __init__(self, featurePath, requestName, imageName, distanceName):
        self.imageName = imageName
        self.requestName = requestName
        self.imageFeature = np.loadtxt(featurePath + "/" + imageName)
        self.requestFeature = np.loadtxt(featurePath + "/" + requestName)
        self.distanceName = distanceName
        self.distance = float(distance_f(self.imageFeature, self.requestFeature, distanceName))
        self.brand = int(imageName.split('_')[0])

    def __str__(self):
        return self.imageName + ' - ' + self.requestName + ' - ' + self.distanceName + ' - ' + str(
            self.distance) + ' - ' + str(self.brand)


class Evaluation:
    def __init__(self, name, RT, RR50, RR100, RR500,total):
        self.name = name

        self.total = total

        self.rappel50 = RR50 / RT
        self.precision50 = RR50 / 50

        self.rappel100 = RR100 / RT
        self.precision100 = RR100 / 100

        self.rappel500 = RR500 / RT
        self.precision500 = RR500 / 500

    def __str__(self):
        string = "--> " + self.name

        string += "\nTotal :" + str(self.total)

        string += "\n50 :"
        string += "\n   Rappel : " + str(self.rappel50)
        string += "\n   Precision : " + str(self.precision50)

        string += "\n100 :"
        string += "\n   Rappel : " + str(self.rappel100)
        string += "\n   Precision : " + str(self.precision100)

        string += "\n500 :"
        string += "\n   Rappel : " + str(self.rappel500)
        string += "\n   Precision : " + str(self.precision500)

        return string


def evaluation(name, listDistance, requestBrand):
    RR50 = 0
    RR100 = 0
    RR500 = 0
    RT = 0
    total = 0
    T = len(listDistance)
    for i in range(T):
        if listDistance[i].brand == requestBrand:
            total += i
            RT += 1
            if i < 500:
                RR500 += 1
                if i < 100:
                    RR100 += 1
                    if i < 50:
                        RR50 += 1
    eval = Evaluation(name, RT, RR50, RR100, RR500,total)
    return eval


def euclidean(l1, l2):
    s = 0.0
    for i, j in zip(l1, l2):
        if i == j == 0.0:
            continue
        s += (i - j) ** 2
    return s


def chiSquareDistance(l1, l2):
    s = 0.0
    for i, j in zip(l1, l2):
        if i == j == 0.0:
            continue
        s += (i - j) ** 2 / (i + j)
    return s


def bhatta(l1, l2):
    l1 = np.array(l1)
    l2 = np.array(l2)
    num = np.sum(np.sqrt(np.multiply(l1, l2, dtype=np.float64)), dtype=np.float64)
    den = np.sqrt(np.sum(l1, dtype=np.float64) * np.sum(l2, dtype=np.float64))
    return np.sqrt(1 - num / den)


def flann(l1, l2):
    l1 = np.float32(np.array(l1))
    l2 = np.float32(np.array(l2))
    if l1.shape[0] == 0 or l2.shape[0] == 0:
        return np.inf
    index_params = dict(algorithm=1, trees=5)
    sch_params = dict(checks=50)
    flannMatcher = cv2.FlannBasedMatcher(index_params, sch_params)
    matches = list(map(lambda x: x.distance, flannMatcher.match(l1, l2)))
    return np.mean(matches)


def bruteForceMatching(l1, l2):
    l1 = np.array(l1).astype('uint8')
    l2 = np.array(l2).astype('uint8')
    if l1.shape[0] == 0 or l2.shape[0] == 0:
        return np.inf
    bf = cv2.BFMatcher(cv2.NORM_HAMMING)
    matches = list(map(lambda x: x.distance, bf.match(l1, l2)))
    return np.mean(matches)


def distance_f(l1, l2, distanceName):
    l1=np.ndarray.flatten(l1)
    l2=np.ndarray.flatten(l2)
    if distanceName == "Euclidienne":
        distance = euclidean(l1, l2)
    elif distanceName == "Correlation":
        methode = cv2.HISTCMP_CORREL
        distance = cv2.compareHist(np.float32(l1), np.float32(l2), methode)
    elif distanceName == "Chicarre":
        distance = chiSquareDistance(l1, l2)
    elif distanceName == "Intersection":
        methode = cv2.HISTCMP_INTERSECT
        distance = cv2.compareHist(np.float32(l1), np.float32(l2), methode)
    elif distanceName == "Bhattacharyya":
        distance = bhatta(l1, l2)
    elif distanceName == "Brute force":
        distance = bruteForceMatching(l1, l2)
    elif distanceName == "Flann":
        distance = flann(l1, l2)
    return distance


def getDistance(featurePath, requestName, distanceName):
    listDistance = []
    for imageName in os.listdir(featurePath):
        listDistance.append(Distance(featurePath, requestName, imageName, distanceName))

    if distanceName in ["Correlation", "Intersection"]:
        ordre = True
    else:
        ordre = False

    listDistance.sort(key=lambda x: x.distance, reverse=ordre)
    return listDistance