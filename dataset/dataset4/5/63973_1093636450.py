from datetime import datetime
for i in range(0,53):
    if i == 0:
        yr=input("Enter a valid year: ")
        print("Wk#\tBeginning of week\tEnd of week")
    BegWk = datetime.strptime((yr + "-" + str(i) + "-0"),"%Y-%W-%w")
    EndWk = datetime.strptime((yr + "-" + str(i) + "-6"),"%Y-%W-%w")
    print(str(i) + "\t" + str(BegWk) + "\t" +str(EndWk))