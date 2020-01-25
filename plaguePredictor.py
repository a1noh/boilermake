import sys
import pandas as pd
import numpy as np

probsT = [None] * 32
probsF = [None] * 32
osT = 0
osF = 0
total = 0


def main():

    testCase = ["True", "False", "True", "True", "True", "False", "True", "True", "True", "False", "True", "False", "True", "False", "False", "True", "True", "False", "False", "True", "True", "False", "True", "True", "False", "False", "True", "False", "True", "False", "True", "True"]

    dfTrain = 1
    try:
        dfTrain = pd.read_csv("Test.csv", header=None)
    except Exception as e:
        print("ERROR: CSV FILE NOT FOUND")
        return


    buildProbabilities(dfTrain)
    finale = testNBC(testCase)
    print(finale)


def buildProbabilities(train):

    global probsT
    global probsF
    global osT
    global osF
    global total

    #print(train)
    #return

    for i in range(0, 31):
        dict1 = {}
        dict2 = {}
        arr = ["True", "False"]

        for j in range(0, len(arr)):
            d2 = {str(arr[j]): 0}
            d3 = {str(arr[j]): 0}
            dict1.update(d2)
            dict2.update(d3)
        probsT[i] = dict1
        probsF[i] = dict2

    total = len(train)

    for i in range(0, total):
        if str(train.iloc[i,31]) == "True":
            osT += 1
        else:
            osF += 1

    for i in range(0, 31):
        if len(probsT[i]) == 2:
            for j in range(0, total):
                if str(train.iloc[j, i]) == 'True' and str(train.iloc[j, 31]) == 'True':
                    probsT[i]['True'] += 1
                if str(train.iloc[j, i]) == 'True' and str(train.iloc[j, 31]) == 'False':
                    probsF[i]['True'] += 1

            #We have to calculate the falses given
            probsT[i]['False'] = osT - probsT[i]['True']
            probsF[i]['False'] = osF - probsF[i]['True']


    for i in range(0, 31):
        for k, v in probsT[i].items():
            probsT[i][k] = (float(v) + float(1)) / (float(osT) + float(len(probsT[i])))

        for k, v in probsF[i].items():
            probsF[i][k] = (float(v) + float(1)) / (float(osF) + float(len(probsF[i])))

def testNBC(dfTest):

    # osT is the number of true labels
    global osT
    # osF is the number of false labels
    global osF
    # total is the number of total number of training data.
    global total


    testResultsT = 0
    testResultsF = 0
    predicted = 0

    # Calculate the probabilities of all the test data
    # Cross reference and calculate the probabilities for all the feature values of this row
    Tmult = 1
    for j in range(0, 31):
        Tmult *= probsT[j][str(dfTest[j])]
    Tmult *= (float(osT) / float(total))

    Fmult = 1
    for j in range(0, 31):
        Fmult *= probsF[j][str(dfTest[j])]
    Fmult *= (float(osF) / float(total))

        # Normalize by the sum
    Tmult = Tmult / (Tmult + Fmult)
    Fmult = 1 - Tmult
    testResultsT = Tmult
    testResultsF = Fmult

    # Fill out the predicted class labels
    #for i in range(0, len(dfTest)):
    if testResultsT >= testResultsF:
        predicted = 'True'
    else:
        predicted = 'False'

    return predicted

if __name__ == "__main__":
    main()

