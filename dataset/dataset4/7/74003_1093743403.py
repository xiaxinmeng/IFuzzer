import os 
testPath = r"myTestFile.txt"

## Make sure the file exists and its empty
with open(testPath,"w") as tFile:
    tFile.write("")