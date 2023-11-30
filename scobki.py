stroka = input()
stake = []
correct = True
for i in range(0, len(stroka)):
    if stroka[i] == "{" or stroka[i] == "[" or stroka[i] == "(":
        stake.append(stroka[i])
    elif len(stake) != 0:
        if (stroka[i] == ")" and stake[-1] == "(") or (stroka[i] == "]" and stake[-1] == "[") or (stroka[i] == "}" and stake[-1] == "{"):
            stake.pop()
        else:
            correct = False
            break
    else:
        correct = False
        break
if correct and len(stake) == 0 and len(stroka) > 1:
    print("yes")
else:
    print("no")