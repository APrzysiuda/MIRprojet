
def Recherche(self, MainWindow):
    # Remise à 0 de la grille des voisins
    for i in reversed(range(self.gridLayout.count())):
        self.gridLayout.itemAt(i).widget().setParent(None)
    voisins = ""
    if self.algo_choice != 0:
        ##Generer les features de l'images requete
        req = extractReqFeatures(fileName, self.algo_choice)
        ##Definition du nombre de voisins
        self.sortie = 9
        # Aller chercher dans la liste de l'interface la distance choisie
        distanceName = self.comboBox.currentText()
        # Générer les voisins
        voisins = getkVoisins(self.features1, req, self.sortie, distanceName)
        self.path_image_plus_proches = []
        self.nom_image_plus_proches = []
        for k in range(self.sortie):
            self.path_image_plus_proches.append(voisins[k][0])
            self.nom_image_plus_proches.append(os.path.basename(voisins[k][0]))
        # Nombre de colonnes pour l'affichage
        col = 3
        k = 0
        for i in range(math.ceil(self.sortie / col)):
            for j in range(col):
                img = cv2.imread(self.path_image_plus_proches[k], 1)  # load image
                # Remise de l'image en RGB pour l'afficher correctement
                b, g, r = cv2.split(img)  # get b,g,r
                img = cv2.merge([r, g, b])  # switch it to rgb
                # convert image to QImage
                height, width, channel = img.shape
                bytesPerLine = 3 * width
                qImg = QtGui.QImage(img.data, width, height, bytesPerLine ,QtGui.QImage.Format_RGB888)
                pixmap = QtGui.QPixmap.fromImage(qImg)
                label = QtWidgets.QLabel("")
                label.setAlignment(QtCore.Qt.AlignCenter)
                label.setPixmap \
                    (pixmap.scaled(0.3 * width, 0.3 * height, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
                self.gridLayout.addWidget(label, i, j)
                k += 1
    else:
        print("Il faut choisir une méthode !")

def rappel_precision(self):
    rappel_precision = []
    rappels = []
    precisions = []
    filename_req = os.path.basename(fileName)
    num_image, _ = filename_req.split(".")
    classe_image_requete = int(num_image) / 100
    val = 0

    for j in range(self.sortie):
        classe_image_proche = (int(self.nom_image_plus_proches[j].split('.')[0])) / 100
        classe_image_requete = int(classe_image_requete)
        classe_image_proche = int(classe_image_proche)
        if classe_image_requete == classe_image_proche:
            rappel_precision.append(True)  # Bonne classe (pertinant)
            val += 1
        else:
            rappel_precision.append(False)  # Mauvaise classe (non pertinant)
    for i in range(self.sortie):
        j = i
        val = 0
        while (j >= 0):
            if rappel_precision[j]:
                val += 1
            j -= 1
        precision =  (va l /( i +1) ) *100
        rappel = (va l /self.sortie ) *100
        rappels.append(rappel)
        precisions.append(precision)
    # Création de la courbe R/P
    plt.plot(rappels, precisions)
    plt.xlabel("Recall")
    plt.ylabel("Precision")
    plt.title("R/P" + str(self.sortie) + " voisins de l'image n°" + num_image)

    # Enregistrement de la courbe RP
    save_folder = os.path.join(".", num_image)
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)
    save_name = os.path.join(save_folder, num_image + '.png')
    plt.savefig(save_name, format='png', dpi=600)
    plt.close()

    # Affichage de la courbe R/P
    img = cv2.imread(save_name, 1)  # load image in color

    # Remise de l'image en RGB pour l'afficher correctement
    b, g, r = cv2.split(img)  # get b,g,r
    img = cv2.merge([r, g, b])  # switch it to rgb

    # convert image to QImage
    height, width, channel = img.shape
    bytesPerLine = 3 * width
    qImg = QtGui.QImage(img.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
    pixmap = QtGui.QPixmap.fromImage(qImg)
    width = self.label_requete.frameGeometry().width()
    height = self.label_requete.frameGeometry().height()
    self.label_courbe.setAlignment(QtCore.Qt.AlignCenter)
    self.label_courbe.setPixmap(pixmap.scaled(width, height, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))


def extractReqFeatures(fileName ,algo_choice):
    print(algo_choice)
    if fileName :
        img = cv2.imread(fileName)
        resized_img = resize(img, (12 8 *4, 6 4 *4))

        if algo_choic e= =1:  # Couleurs
            histB = cv2.calcHist([img] ,[0] ,None ,[256] ,[0 ,256])
            histG = cv2.calcHist([img] ,[1] ,None ,[256] ,[0 ,256])
            histR = cv2.calcHist([img] ,[2] ,None ,[256] ,[0 ,256])
            vect_features = np.concatenate((histB, np.concatenate((histG ,histR) ,axis=None)) ,axis=None)

        elif algo_choic e= =2: # Histo HSV
            hsv = cv2.cvtColor(img ,cv2.COLOR_BGR2HSV)
            histH = cv2.calcHist([hsv] ,[0] ,None ,[180] ,[0 ,180])
            histS = cv2.calcHist([hsv] ,[1] ,None ,[256] ,[0 ,256])
            histV = cv2.calcHist([hsv] ,[2] ,None ,[256] ,[0 ,256])
            vect_features = np.concatenate((histH, np.concatenate((histS ,histV) ,axis=None)) ,axis=None)

        elif algo_choic e= =3:  # SIFT
            sift = cv2.SIFT_create()  # cv2.xfeatures2d.SIFT_create() pour py < 3.4
            # Find the key point
            kps , vect_features = sift.detectAndCompute(img ,None)

        elif algo_choic e= =4:  # ORB
            orb = cv2.ORB_create()
            # finding key points and descriptors of both images using detectAndCompute() function
            key_point1 ,vect_features = orb.detectAndCompute(img ,None)

        elif algo_choic e= =5:  # HOG
            resized_img = resize(img, (128 * 4, 64 * 4))
            fd, vect_features = hog(resized_img, orientations=9, pixels_per_cell=(8, 8) ,cells_per_block=(2, 2), visualize=True, multichannel=True)

        elif algo_choic e= =6:  # GLCM
            image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            vect_features = greycomatrix(image, distances=[1], angles=[0, np.pi / 4, np.pi / 2], symmetric=True, normed=True)

        elif algo_choic e= =7:  # LBP:
            METHOD = 'uniform'
            radius = 3
            n_points = 8 * radius
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            lbp = local_binary_pattern(gray, n_points, radius, METHOD)
            lpb_feature s =lbp.tolist()
            vect_features = np \
            ;array(lpb_features)

        np.savetxt("Methode_ " +str(algo_choice ) +"_requete.txt" ,vect_features)
        print("saved")
        # print("vect_features", vect_features)
        return vect_features

