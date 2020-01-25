import sys
import pandas as pd
import numpy as np

probsT = [None] * 32
probsF = [None] * 32
osT = 0
osF = 0
total = 0


def main():

    dfTrain = 1
    try:
        dfTrain = pd.read_csv("test.csv")
    except Exception as e:
        print("ERROR: CSV FILE NOT FOUND")
        return

    buildProbabilities(dfTrain)

def buildProbabilities(train):

    global osT
    global osF
    global total

    for i in range(0, 31):
        dict1 = {}
        dict2 = {}
        arrTrain = dfTrain[dfTrain.columns[i]].unique()

        for j in range(0, len(arr)):
            d2 = {str(arrTrain[j]): 0}
            d3 = {str(arrTrain[j]): 0}
            dict1.update(d2)
            dict2.update(d3)
        probsT[i] = dict1
        probsF[i] = dict2

    total = len(dfTrain)

    for i in range(0, total):
        if str(dfTrain.iloc[i,31]) == True:
            osT += 1
        else:
            osF += 1

    for i in range(0, 31):
        if len(probsT[i]) == 2:
            for j in range(0, total):
                if str(dfTrain.iloc[j, i]) == 'True' and str(dfTrain.iloc[j, 41]) == 'True':
                    probsT[i]['True'] += 1
                if str(dfTrain.iloc[j, i]) == 'True' and str(dfTrain.iloc[j, 41]) == 'False':
                    probsF[i]['True'] += 1

            #We have to calculate the falses given
            probsT[i]['False'] = osT - probsT[i]['True']
            probsF[i]['False'] = osF - probsF[i]['True']








if __name__ == "__main__":
    main()

