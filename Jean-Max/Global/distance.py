from librairie import *

def distance(l1, l2, distanceName):
    if distanceName == "Euclidienne":
        distance = euclidean(l1, l2)
    elif distanceName == "Chicarre":
        distance = chiSquareDistance(l1, l2)
    elif distanceName == "Bhattacharyya":
        distance = bhatta(l1, l2)
    elif distanceName == "Brute force":
        distance = bruteForceMatching(l1, l2)
    elif distanceName == "Flann":
        distance = flann(l1, l2)
    elif distanceName =="Random":
        distance = np.random.rand()
    return distance

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