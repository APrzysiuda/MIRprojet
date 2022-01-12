import os
import cv2
import numpy as np
from skimage import io, color, img_as_ubyte
from skimage.feature import hog, greycomatrix, greycoprops, local_binary_pattern

def generateHistogramme_HSV(input,output):
    if not os.path.isdir(output+"/HSV"):
        os.mkdir(output+"/HSV")

    for path in os.listdir(input):
        img = cv2.imread(input+"/"+path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        histH = cv2.calcHist([img],[0],None,[180],[0,180])
        histS = cv2.calcHist([img],[1],None,[256],[0,256])
        histV = cv2.calcHist([img],[2],None,[256],[0,256])
        feature = np.concatenate((histH, np.concatenate((histS,histV),axis=None)),axis=None)

        num_image, _ = path.split(".")
        np.savetxt(output+"/HSV/"+str(num_image)+".txt" ,feature)

    print("indexation Hist HSV terminée !!!!")
        
def generateHistogramme_Color(input,output):
    if not os.path.isdir(output+"/BGR"):
        os.mkdir(output+"/BGR")

    for path in os.listdir(input):
        img = cv2.imread(input+"/"+path)
        histB = cv2.calcHist([img],[0],None,[256],[0,256])
        histG = cv2.calcHist([img],[1],None,[256],[0,256])
        histR = cv2.calcHist([img],[2],None,[256],[0,256])
        feature = np.concatenate((histB, np.concatenate((histG,histR),axis=None)),axis=None)

        num_image, _ = path.split(".")
        np.savetxt(output+"/BGR/"+str(num_image)+".txt" ,feature)

    print("indexation Hist Couleur terminée !!!!")

def generateSIFT(input,output):
    if not os.path.isdir(output+"/SIFT"):
        os.mkdir(output+"/SIFT")

    for path in os.listdir(input):
        img = cv2.imread(input+"/"+path)
        featureSum = 0
        sift = cv2.SIFT_create()  
        kps , des = sift.detectAndCompute(img,None)

        num_image, _ = path.split(".")
        np.savetxt(output+"/SIFT/"+str(num_image)+".txt" ,des)

        featureSum += len(kps)

    print("Indexation SIFT terminée !!!!")    

def generateORB(input,output):
    if not os.path.isdir(output+"/ORB"):
        os.mkdir(output+"/ORB")

    for path in os.listdir(input):
        img = cv2.imread(input+"/"+path)
        orb = cv2.ORB_create()
        key_point1,descrip1 = orb.detectAndCompute(img,None)
        
        num_image, _ = path.split(".")
        np.savetxt(output+"/ORB/"+str(num_image)+".txt" ,descrip1 )

    print("indexation ORB terminée !!!!")

def generateGLCM(input,output):
    if not os.path.isdir(output+"/GLCM"):
        os.mkdir(output+"/GLCM")

    distances=[1,-1]
    angles=[0, np.pi/4, np.pi/2, 3*np.pi/4]

    for path in os.listdir(input):
        image = cv2.imread(input+"/"+path)
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        gray = img_as_ubyte(gray)
        glcmMatrix = greycomatrix(gray, distances=distances, angles=angles, normed=True)
        glcmProperties1 = greycoprops(glcmMatrix,'contrast').ravel()
        glcmProperties2 = greycoprops(glcmMatrix,'dissimilarity').ravel()
        glcmProperties3 = greycoprops(glcmMatrix,'homogeneity').ravel()
        glcmProperties4 = greycoprops(glcmMatrix,'energy').ravel()
        glcmProperties5 = greycoprops(glcmMatrix,'correlation').ravel()
        glcmProperties6 = greycoprops(glcmMatrix,'ASM').ravel()
        feature = np.array([glcmProperties1,glcmProperties2,glcmProperties3,glcmProperties4,glcmProperties5,glcmProperties6]).ravel()
        num_image, _ = path.split(".")
        np.savetxt(output+"/GLCM/"+str(num_image)+".txt" ,feature)

    print("indexation GLCM terminée !!!!")

def generateLBP(input,output):
    if not os.path.isdir(output+"/LBP"):
        os.mkdir(output+"/LBP")

    for path in os.listdir(input):
        img = cv2.imread(input+"/"+path)
        points=8
        radius=1
        method='default'
        subSize=(70,70)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.resize(img,(350,350))
        fullLBPmatrix = local_binary_pattern(img,points,radius,method)
        histograms = []
        for k in range(int(fullLBPmatrix.shape[0]/subSize[0])):
            for j in range(int(fullLBPmatrix.shape[1]/subSize[1])):
                subVector = fullLBPmatrix[k*subSize[0]:(k+1)*subSize[0],j*subSize[1]:(j+1)*subSize[1]].ravel()
                subHist,edges =np.histogram(subVector,bins=int(2**points),range=(0,2**points))
                histograms = np.concatenate((histograms,subHist),axis=None)
        num_image, _ = path.split(".")
        np.savetxt(output+"/LBP/"+str(num_image)+".txt" ,histograms)

    print("indexation LBP terminé !!!!")

def generateHOG(input,output):
    if not os.path.isdir(output+"/HOG"):
        os.mkdir(output+"/HOG")

    cellSize = (25,25)
    blockSize = (50,50)
    blockStride = (25,25)
    nBins = 9
    winSize = (350,350)
    for path in os.listdir(input):
        img = cv2.imread(input+"/"+path)
        image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        image = cv2.resize(image,winSize)
        hog = cv2.HOGDescriptor(winSize,blockSize,blockStride,cellSize,nBins)
        feature = hog.compute(image)
        num_image, _ = path.split(".")
        np.savetxt(output+"/HOG/"+str(num_image)+".txt" ,feature )

    print("indexation HOG terminée !!!!")