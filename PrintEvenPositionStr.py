def PrintEvenPositionStr(str):
    string = ""
    for i in range(len(str)):
        if(i%2==0):
            string += str[i];
    return string;

print(PrintEvenPositionStr("NagengraChaudhari"));
