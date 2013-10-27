binm = "01110011"

def getBin(bin):
    total = 0
    for i in range(len(bin)):
        if bin[i]=="1":
            total += 2**i
    return total

print bin(binm)