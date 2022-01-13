from function import *

input="D:/MIR/Data"
output="D:/MIR/DeepLearning"

listRequestName=[
    "0_1_BMW_X3_279",
    "0_0_BMW_Serie3Berline_45",
    "0_2_BMW_i8_407",
    "2_0_Volkswagen_Touareg_2839",
    "2_4_Volkswagen_Polo_3471",
    "2_9_Volkswagen_T-Roc_4322",
    "4_2_Opel_vivarofourgon_5982",
    "4_4_Opel_Insignatourer_6351",
    "4_8_Opel_GrandlandX_6805",
    "6_0_Hyundai_Nexo_8397",
    "6_3_Hyundai_i10_8736",
    "6_4_Hyundai_i30fastback_9021",
    "8_1_Ford_Puma_11198",
    "8_5_Ford_Explorer_11890",
    "8_7_Ford_Fiesta_12211"
]

distanceName="Euclidienne"

listFeatureName=os.listdir(output)
featureNumber = len(listFeatureName)

for featureName in listFeatureName:
    print("---> " + featureName)

    featurePath = os.path.join(output, featureName)

    finalTotal = 0

    listRappel20 = []
    listPrecision20 = []
    listRappel50 = []
    listPrecision50 = []
    listRappel100 = []
    listPrecision100 = []
    listRappel500 = []
    listPrecision500 = []

    for requestName in listRequestName:
        requestBrand=int(requestName.split('_')[0])
        listDistance=getDistance(featurePath,requestName,distanceName)
        eval=evaluation(requestName, listDistance, requestBrand)
        listRappel20.append(eval.rappel20)
        listPrecision20.append(eval.precision20)
        listRappel50.append(eval.rappel50)
        listPrecision50.append(eval.precision50)
        listRappel100.append(eval.rappel100)
        listPrecision100.append(eval.precision100)
        listRappel500.append(eval.rappel500)
        listPrecision500.append(eval.precision500)
        finalTotal += eval.total

    print("Total :" + str(finalTotal))
    print("20 :")
    print("   Rappel : ")
    print("      Min :" + str(min(listRappel20)))
    print("      Moy :" + str(np.mean(listRappel20)))
    print("      Max :" + str(max(listRappel20)))
    print("   Precision : ")
    print("      Min :" + str(min(listPrecision20)))
    print("      Moy :" + str(np.mean(listPrecision20)))
    print("      Max :" + str(max(listPrecision20)))
    print("50 :")
    print("   Rappel : ")
    print("      Min :" + str(min(listRappel50)))
    print("      Moy :" + str(np.mean(listRappel50)))
    print("      Max :" + str(max(listRappel50)))
    print("   Precision : ")
    print("      Min :" + str(min(listPrecision50)))
    print("      Moy :" + str(np.mean(listPrecision50)))
    print("      Max :" + str(max(listPrecision50)))
    print("100 :")
    print("   Rappel : ")
    print("      Min :" + str(min(listRappel100)))
    print("      Moy :" + str(np.mean(listRappel100)))
    print("      Max :" + str(max(listRappel100)))
    print("   Precision : ")
    print("      Min :" + str(min(listPrecision100)))
    print("      Moy :" + str(np.mean(listPrecision100)))
    print("      Max :" + str(max(listPrecision100)))
    print("500 :")
    print("   Rappel : ")
    print("      Min :" + str(min(listRappel500)))
    print("      Moy :" + str(np.mean(listRappel500)))
    print("      Max :" + str(max(listRappel500)))
    print("   Precision : ")
    print("      Min :" + str(min(listPrecision500)))
    print("      Moy :" + str(np.mean(listPrecision500)))
    print("      Max :" + str(max(listPrecision500)))