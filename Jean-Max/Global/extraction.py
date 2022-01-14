from librairie import *


def featureExtraction(image, featureName):
    if featureName == "HOG":
        feature = HOG(image)
    if featureName == "LBP":
        feature = LBP(image)
    if featureName == "GLCM":
        feature = GLCM(image)
    if featureName == "BGR":
        feature = BGR(image)
    if featureName == "HSV":
        feature = HSV(image)
    return feature


def HOG(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.resize(image, winSize)
    hog = cv2.HOGDescriptor(winSize, blockSize, blockStride, cellSize, nBins)
    feature = hog.compute(image)
    return feature


def LBP(image):
    points = 8
    radius = 1
    method = 'default'
    subSize = (70, 70)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.resize(image, (350, 350))
    fullLBPmatrix = local_binary_pattern(image, points, radius, method)
    feature = []
    for k in range(int(fullLBPmatrix.shape[0] / subSize[0])):
        for j in range(int(fullLBPmatrix.shape[1] / subSize[1])):
            subVector = fullLBPmatrix[k * subSize[0]:(k + 1) * subSize[0],
                        j * subSize[1]:(j + 1) * subSize[1]].ravel()
            subHist, edges = np.histogram(subVector, bins=int(2 ** points), range=(0, 2 ** points))
            feature = np.concatenate((feature, subHist), axis=None)
    return feature


def GLCM(image):
    distances = [1, -1]
    angles = [0, np.pi / 4, np.pi / 2, 3 * np.pi / 4]
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = img_as_ubyte(gray)
    glcmMatrix = greycomatrix(gray, distances=distances, angles=angles, normed=True)
    glcmProperties1 = greycoprops(glcmMatrix, 'contrast').ravel()
    glcmProperties2 = greycoprops(glcmMatrix, 'dissimilarity').ravel()
    glcmProperties3 = greycoprops(glcmMatrix, 'homogeneity').ravel()
    glcmProperties4 = greycoprops(glcmMatrix, 'energy').ravel()
    glcmProperties5 = greycoprops(glcmMatrix, 'correlation').ravel()
    glcmProperties6 = greycoprops(glcmMatrix, 'ASM').ravel()
    feature = np.array([glcmProperties1, glcmProperties2, glcmProperties3, glcmProperties4, glcmProperties5,
                        glcmProperties6]).ravel()
    return feature


def BGR(image):
    histB = cv2.calcHist([image], [0], None, [256], [0, 256])
    histG = cv2.calcHist([image], [1], None, [256], [0, 256])
    histR = cv2.calcHist([image], [2], None, [256], [0, 256])
    feature = np.concatenate((histB, np.concatenate((histG, histR), axis=None)), axis=None)
    return feature


def HSV(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    histH = cv2.calcHist([image], [0], None, [180], [0, 180])
    histS = cv2.calcHist([image], [1], None, [256], [0, 256])
    histV = cv2.calcHist([image], [2], None, [256], [0, 256])
    feature = np.concatenate((histH, np.concatenate((histS, histV), axis=None)), axis=None)
    return feature
