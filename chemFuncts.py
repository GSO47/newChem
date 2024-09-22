import random, math, sympy as sp, numpy as np
from chemData import *

def getAnswer(answer):
    temp = input("Get answer? ")
    if temp == "break":
        return "break"
    else:
        print("\n" + str(answer) + "\n\n")

chanceList = [3,3,3,1,0]
#chanceList = [0,0,0,0,1]

def getRandomCompound(polyChance=chanceList[0], acidChance=chanceList[1], biChance=chanceList[2], diChance = chanceList[3], hChance = chanceList[4]):
    chanceList = []
    p = 0
    a = 0
    b = 0
    d = 0
    h =0
    while p < int(polyChance):
        chanceList.append("p")
        p +=1
    while a < int(acidChance):
        chanceList.append("a")
        a +=1
    while b < int(biChance):
        chanceList.append("b")
        b +=1
    while d < int(diChance):
        chanceList.append("d")
        d += 1
    while h < int(hChance):
        chanceList.append("h")
        h += 1

    if chanceList == []:
        chanceList = ["p","a","b", "d", "h"]
    compoundType = random.choice(chanceList)

    bad = True
    while bad:
        if compoundType == "p": #ternary ionic
            pIonList = list(polyatomicIons.items())
            pIon = list(pIonList[random.randint(0, len(pIonList) -1)])
            if pIon[0] == "ammonium":
                if random.randint(0,5) == 1:
                    otherIon = list(pIonList[random.randint(0, len(pIonList) -1)])
                    if otherIon == "ammonium":
                        bad = True
                    else:
                        bad = False
                        mIndex = 99
                        pIndex = 1
                else:
                    otherIon = elements[random.randint(1,108)]
                    if (otherIon[4] == "m" or otherIon[4] == "tm") or otherIon[6] == "Noble Gas":
                        bad = True
                    elif otherIon[6] == "Actinide" or otherIon[6] == "Lanthanide" :
                        bad = True
                    else:
                        bad = False
                        mIndex = 99
                        pIndex = 0
            else:
                otherIon = elements[random.randint(1,108)]
                if (otherIon[4] == "s" or otherIon[4] == "n") or otherIon[6] == "Noble Gas":
                    bad = True
                elif otherIon[6] == "Actinide" or otherIon[6] == "Lanthanide" :
                    bad = True
                else:
                    bad = False
                    mIndex = 99
                    pIndex = 0
        elif compoundType == "a": #acids
            if random.randint(0,2) == 2:
                pIonList = list(polyatomicIons.items())
                pIon = list(pIonList[random.randint(0, len(pIonList) -1)])
                if pIon[0] == "ammonium" or pIon[0] == "peroxide" or pIon[0] == "hydroxide":
                    bad = True
                else:
                    bad = False
                    mIndex = 99
                    pIndex = 2
            else:
                otherIon = elements[random.randint(1,108)]
                if (otherIon[4] == "m" or otherIon[4] == "tm") or otherIon[6] == "Noble Gas" or (otherIon[2] == "O" or otherIon[2] == "H" or otherIon[2] == "Po"):
                    bad = True
                elif otherIon[6] == "Actinide" or otherIon[6] == "Lanthanide" :
                    bad = True
                else:
                    bad = False
                    mIndex = 99
                    pIndex = 3
        elif compoundType == "d": #diatomic
            pIndex = 99
            mIndex = 99
            diatomicAtoms = ["H", "N", "O", "F", "Cl", "Br", "I"]
            atom = random.choice(diatomicAtoms)
            diatomicNames = ["Hydrogen", "Nitrogen", "Oxygen", "Flourine", "Chlorine", "Bromine", "Iodine"]
            index = diatomicAtoms.index(atom)
            return [diatomicNames[index] + " Gas", atom + "2", "diatomic"]
        elif compoundType == "h": # hydrocarbons
            derivative = bool(random.getrandbits(1))
            if derivative:
                Cn1 = random.randint(1,3)
                O = random.choice(["CO", "COO"])
                Cn2 = random.randint(1,3)
                eq = f"C{Cn1 if Cn1 != 1 else ''}H{2*Cn1+1}{O}C{Cn2 if Cn2 != 1 else ''}H{Cn2*2+1}"
                return [eq, eq, "hydrocarbon"]
            
            Cn = random.randint(1,5)
            if Cn == 1: Hn = 4
            else: Hn = random.choice([2 * Cn + 2, 2 * Cn, 2 * Cn - 2])
            eq = f"C{Cn if Cn != 1 else ''}H{Hn}"
            return [eq, eq, "hydrocarbon"]
        else: # binary
            num1 = random.randint(1,108)
            el1 = elements[num1]
            num2 = random.randint(1,108)
            el2 = elements[num2]
            if (el1[4] == "m" or el1[4] == "tm") and (el2[4] == "m" or el2[4] == "tm") or el1[6] == "Noble Gas" or el2[6] == "Noble Gas" or el1 == el2:
                bad = True
            elif el1[6] == "Actinide" or el1[6] == "Lanthanide" or el2[6] == "Actinide" or el2[6] == "Lanthanide":
                bad = True
            else:
                bad = False
            if el1[4] == "s" and el2[4] == "s":
                mIndex = 0
            elif el1[4] == "m" or el1[4] == "tm":
                mIndex = 1
            elif el2[4] == "m" or el2[4] == "tm":
                mIndex = 2
            else: mIndex = 0
            # I am assuming that the combination of a nonmetal and semimetal is always molecular (cause idk what determines it)
            pIndex = 99
        
    if mIndex == 0:
        if int(el2[3][0]) < 4:
            amount1 = int(el2[3][0])
        else: amount1 = 8-int(el2[3][0])
        if int(el1[3][0]) < 4:
            amount2 = int(el1[3][0])
        else: amount2 = 8-int(el1[3][0])

        amount1 = amount1 // math.gcd(amount1, amount2)
        amount2 = amount2 // math.gcd(amount1,amount2)

        prefix1 = prefixes.get(amount1)
        prefix2 = prefixes.get(amount2)
        if prefix1 == "mono":
            prefix1 = ""


        name = prefix1 + el1[1].lower() + " " + prefix2 + (ionNames.get(el2[2])).lower()
        name = name.replace("ao", "o")
        name = name.replace("oo", "o")
        name = name.replace("aa","a")

        if int(amount1) == 1:
            amount1 = ""
        if int(amount2) == 1:
            amount2 = ""

        equation = el1[2] + str(amount1) + el2[2] + str(amount2)

        return [name, equation, "Binary Molecular"]
    elif mIndex == 1 or mIndex == 2:
        if mIndex == 1:
            mElement = el1
            nElement = el2
        elif mIndex == 2:
            mElement = el2
            nElement = el1
        else: print("mIndexing error")
        if mElement[4] == "tm":
            if mElement[2] in tmcharges:
                if len(tmcharges.get(mElement[2]))-1 != 0:
                    index = random.randint(1,len(tmcharges.get(mElement[2]))-1)
                else: index = 0
                mCharge = tmcharges.get(mElement[2])[index]
                mName = mElement[1] + " (" + str(mCharge) + ") / " + str(tmNames.get(mElement[2] + str(mCharge)))
            else:
                mCharge = random.randint(1,4)
                mName = mElement[1] + "(" + str(mCharge) + ")"
        else:
            mCharge = int(mElement[3][0])
            mName = mElement[1]

        nName = ionNames.get(nElement[2])
        if int(nElement[3][0]) < 4:
            nCharge = int(nElement[3][0])
        else: nCharge = 8-int(nElement[3][0])

        mNum = nCharge // math.gcd(nCharge, int(mCharge))
        nNum = int(mCharge) // math.gcd(nCharge, int(mCharge))

        if mNum == 1:
            mNum = ""
        if nNum == 1:
            nNum = ""

        name = str(mName) + " " + str(nName)
        equation = mElement[2] + str(mNum) + nElement[2] + str(nNum)
        return [name, equation, "Binary Ionic"]
    elif pIndex == 0:
        mElement = otherIon

        if mElement[4] == "tm" or mElement[0] == 50 or mElement[0] == 83:
            if mElement[2] in tmcharges:
                if len(tmcharges.get(mElement[2]))-1 != 0:
                    index = random.randint(1,len(tmcharges.get(mElement[2]))-1)
                else: index = 0
                mCharge = int(tmcharges.get(mElement[2])[index])
                mName = mElement[1] + " (" + str(mCharge) + ") / " + str(tmNames.get(mElement[2] + str(mCharge)))
            else:
                mCharge = int(random.randint(1,4))
                mName = mElement[1] + "(" + str(mCharge) + ")"
        elif mElement[4] == "m":
            mCharge = int(mElement[3][0])
            if mCharge > 4 and mCharge != 8: mCharge = 8- mCharge
            mName = mElement[1]
        else:
            mCharge = int(mElement[3][0])
            mName = (ionNames.get(mElement[2])).lower()
            if int(mCharge) > 4 and mCharge != 8:
                mCharge = 8 - mCharge

        pName = pIon[0]
        pCharge = int(pIon[1][-1])

        pSymbol = pIon[1].split(" ")[0]

        mNum = pCharge // math.gcd(pCharge, int(mCharge))
        pNum = int(mCharge) // math.gcd(pCharge, int(mCharge))

        if mNum == 1:
            mNum = ""
        if int(pNum) == 1:
            pNum = ""
        elif int(mCharge) != 1:
            pSymbol = "(" + pSymbol + ")"

        if mElement[4] == "tm" or mElement[4] == "m":
            name = mName + " " + pName
        else:
            name = pName + " " + mName

        if pSymbol in ["NH4", "(NH4)"]:
            equation = pSymbol + str(pNum) + otherIon[2]
        else:
            equation = otherIon[2] + str(mNum) + pSymbol + str(pNum)
        return [name, equation, "Ternary Ionic"]
    elif pIndex == 1:
        pName = pIon[0]
        pCharge = int(pIon[1][-1])
        pSymbol = pIon[1].split(" ")[0]

        oName = otherIon[0]
        oCharge = int(otherIon[1][-1])
        oSymbol = otherIon[1].split(" ")[0]

        oNum = pCharge // math.gcd(pCharge, int(oCharge))
        pNum = int(oCharge) // math.gcd(pCharge, int(oCharge))

        if oNum == 1:
            oNum = ""
        if pNum == 1:
            pNum = ""
        else:
            pSymbol = "(" + pSymbol + ")"

        name = pName + " " + oName
        equation = pSymbol + str(pNum) + oSymbol + str(oNum)
        return [name, equation, "Ternary Ionic"]
    elif pIndex == 2:
        pName = pIon[0]
        pCharge = int(pIon[1][-1])
        pSymbol = pIon[1].split(" ")[0]

        if "dihydrogen" in pName:
            pSymbol = pSymbol[2:]
            pName = pName.replace("dihydrogen", "")
            pCharge += 2
        elif "hydrogen" in pName:
            pSymbol = pSymbol[1:]
            pCharge += 1
            pName = pName.replace("hydrogen","")

        pName = pName.replace("ite", "ous")
        pName = pName.replace("ate","ic")
        pName = pName.replace("sulf", "sulfur")
        pName = pName.replace("sulfuride","sulfide")
        pName = pName.replace("phosph","phosphor")
        pName = pName.replace("cynanide","hydrocyanic")
        pName = pName.replace("azide", "hydroazoic")

        if pCharge == 1:
            pCharge = ""

        equation = "H" + str(pCharge) + pSymbol
        equation = equation.replace("HH2", "H3")
        equation = equation.replace("HH", "H2")
        name = pName + " acid"
        return [name, equation, "Acid"]
    elif pIndex == 3:
        mElement = otherIon
        if int(otherIon[3][0]) < 4:
            mCharge = int(otherIon[3][0])
        else: mCharge = 8-int(otherIon[3][0])
        mName = otherIon[1]

        if mCharge == 1:
            mCharge = ""

        name = "hydro" + acidNames.get(otherIon[2]) + " acid"
        equation = "H" + str(mCharge) + otherIon[2]

        return [name, equation, "Acid"]

def atomsInCompoundBasic(myCompound):
    atomList = []
    chargeList = []
    for n, i in enumerate(list(myCompound)):
        if i.isdigit():
            if myCompound[n-1].isdigit():
                testVar = False
            elif myCompound[n-1].islower():
                newElement = myCompound[n-2:n]
                testVar = True
            else:
                newElement = myCompound[n-1] 
                testVar = True 
            if n != (len(myCompound) -1) and myCompound[n+1].isdigit():
                atomList.append(newElement)
                chargeList.append(int(myCompound[n:n+2]))
            elif testVar:
                atomList.append(newElement)
                chargeList.append(int(i))
        elif n == len(myCompound)-1:
            if i.islower():
                newElement = myCompound[n-1:n+1]
                atomList.append(newElement)
                chargeList.append(1)
            else:
                newElement = myCompound[-1]
                atomList.append(newElement)
                chargeList.append(1)
        elif i.islower() and not myCompound[n+1].isdigit():
            newElement = myCompound[n-1:n+1]
            atomList.append(newElement)
            chargeList.append(1)
        elif not myCompound[n+1].islower() and not myCompound[n+1].isdigit():
            newElement = myCompound[n]
            atomList.append(newElement)
            chargeList.append(1)
    returnList = []
    for n, i in enumerate(atomList):
        returnList.append([i, chargeList[n]])

    return returnList

def combineCompounds(compound1, compound2):
    atoms1 = []
    charges1 = []
    atoms2 = []
    charges2 = []
    for i in compound1:
        atoms1.append(i[0])
        charges1.append(i[1])
    for i in compound2:
        atoms2.append(i[0])
        charges2.append(i[1])
    returnList = []
    for n, i in enumerate(atoms1):
        if i in atoms2:
            j = atoms2.index(i)
            iCharge = charges1[n] + charges2[j]
        else:
            iCharge = charges1[n]
        returnList.append([i, iCharge])
    for n, i in enumerate(atoms2):
        if i not in atoms1:
            iCharge = charges2[n]
            returnList.append([i, iCharge])

    elList = []
    dupeList = []

    for i in returnList:
        for j in elList:
            if i[0] == j[0]:
                dupeList.append(i)
            else:
                elList.append(i)
    for i in dupeList:
        for j in elList:
            if i[0] == j[0]:
                j[1] += i[1]
    return returnList

def atomsInCompound(myCompound):
    myCompound = str(myCompound)
    if "(NH4)" in myCompound:
        index = myCompound.find(")")
        otherPart = myCompound[index+2:]
        otherAtoms = atomsInCompoundBasic(otherPart)
        try:
            ammoniumNum = int(myCompound[index+1])
        except ValueError:
            ammoniumNum = 1
        ammoniumAtoms = [["N",ammoniumNum], ["H",4*ammoniumNum]]
        return combineCompounds(otherAtoms, ammoniumAtoms)
    elif "NH4" in myCompound:
        insideAtoms = [["N",1],["H",4]]
        outsideCompound = myCompound[3:]
        outsideAtoms = atomsInCompoundBasic(outsideCompound)
        return combineCompounds(outsideAtoms, insideAtoms)
    elif "(" not in myCompound:
        return atomsInCompoundBasic(myCompound)
    else:
        index1 = myCompound.find("(")
        index2 = myCompound.find(")")
        insideCompound = myCompound[index1+1:index2]
        insideAtoms = atomsInCompoundBasic(insideCompound)
        i = 1
        while i < len(insideAtoms) +1:
            try:
                insideAtoms[i-1][1] = insideAtoms[i-1][1] * int(myCompound[index2+1])
            except: raise Exception(f"error handling compound: {myCompound}")
            i +=1
        outsideCompound = myCompound[:index1]
        outsideAtoms = atomsInCompoundBasic(outsideCompound)
        return combineCompounds(outsideAtoms, insideAtoms)

def getAtomMass(symbol):
    for i in elements:
        if symbol == i[2]:
            if i[2] == "Cl":
                return 35.5
            else:
                return round(float(i[8]))

typeList = []

def randElement(type = ""):
    if type not in ["b", "m", "tm", "s", "n", "", "ntm"]: raise Exception("enter a valid type. " + type)
    if type == "b": 
        good = [6,7,8,9,17,35,53]
        return elements[random.choice(good)]
    if typeList == []:
        typeList.append(None)
        for i in elements:
            if i != "n/a":
                typeList.append(i[4])
    if type == "m":
        metals = [3, 4, 11, 12, 19, 20, 37, 38, 55, 56, 87, 88]
        el = elements[random.choice(metals)]
        return el
    if type == "ntm":
        type = ""
        while True:
            el = random.choice(elements)
            if el != "n/a" and int(el[0]) < 108 and (el[4] == type or type == "") and el[6] != "Noble Gas" and el[4] not in ["tm", "n/a"]:
                return el

    while True:
        el = random.choice(elements)
        if el != "n/a" and int(el[0]) < 108 and (el[4] == type or type == "") and el[6] != "Noble Gas":
            return el

def findElement(el = "Input an element!"):
    if el == "HNH": raise Exception("Error: HNH")
    for i in elements:
        if i[2] == el:
            return i
    raise Exception("Error: Element not found: " + el)

def randPolyatomic():
    ion = random.choice(list(polyatomicIons.values()))
    return [ion[:ion.index(" ")], int(ion[-1])]

def findCharge(el):
    el = findElement(el)
    if el[4] in ["n", "s", "m"]:
        group = el[3]
        charge = int(group[0])
        if charge > 4 and charge != 8:
            charge = 8 - charge
    else:
        tmChoices = []
        for i in tmNames:
            if el[2] in i:
                tmChoices.append(int(i[-1]))
        if tmChoices != []:
            charge = random.choice(tmChoices)
        else: charge = random.randint(1,4)

    return charge

def compoundToString(compound):
    returnString = ""
    for i in compound:
        num = str(i[1])
        if num == "1": num = ""
        returnString += i[0] + num
    return returnString

def randomRx(typeRx = "n/a"):
    # chooose the type of the reaction
    rxTypes = ["synthesis", "decomposition", "combustion", "single replacement", "double replacement", "special"]
    rxType = random.choice(rxTypes)
    bond = False
    if typeRx != "n/a" and typeRx in rxTypes or type(typeRx) == list: 
        if type(typeRx) == list:
            i = 0
            while (rxType := random.choice(typeRx)) not in rxTypes: 
                if (i := i + 1) == 10: raise Exception("bad rx type: " + str(typeRx))
        else: rxType = typeRx
    if typeRx == "bond":
        rxType = random.choice(["synthesis", "decomposition", "combustion", "special"])
        bond = True
    if rxType == "synthesis":
        case = random.randint(1,5)
        if bond: case = 3
        if case == 1 or case == 2:
            tmChoice = random.randint(0,1)
            if tmChoice == 0:
                mElement = randElement("m")
                m = [mElement[2], int(mElement[3][0])]
            else:
                mElement = randElement("tm")
                m = [mElement[2], random.randint(1,4)]
            nElement = randElement("n")
            ncharge = int(nElement[3][0])
            if ncharge > 4 and ncharge != 8:
                ncharge = 8-ncharge
            diatomicAtoms = ["H", "N", "O", "F", "Cl", "Br", "I"]
            if nElement[2] in diatomicAtoms:
                n = [nElement[2] + "2", ncharge]
            else:
                n = [nElement[2], ncharge]
            return [[m,n], "s1"]
        if case == 3:
            options = ["SO2", "SO3", "CO2", "N2O3", "N2O5", "P2O3", "P2O5", "As2O3", "As2O5", "NH3"]
            if bond: options = ["SO2", "SO3", "CO2", "NH3"]
            return [[[random.choice(options), 0], ["H2O",0]],"s2"]
        if case == 4 or case == 5:
            tmChoice = random.randint(0,1)
            if tmChoice == 0:
                mElement = randElement("m")
                m = [mElement[2], int(mElement[3][0])]
            else:
                mElement = randElement("tm")
                if mElement[2] in tmNames:
                    tmChoices = list(tmNames.keys())
                    tmChoice = random.choice(tmChoices)
                    while mElement[2] not in tmChoice:
                        tmChoice = random.choice(tmChoices)
                    m = [tmChoice[:-1], int(tmChoice[-1])]
                else: m = [mElement[2], random.randint(1,4)]
            oCharge = int(m[1] / math.gcd(2, m[1]))
            mCharge = str(int(2 * oCharge / m[1]))
            if oCharge == 1:
                oCharge = ""
            if mCharge == "1":
                mCharge = ""
            mOxide = m[0] + mCharge + "O" + str(oCharge)
            return [[[mOxide,0], ["H2O",0]], "s3"]
    elif rxType == "decomposition":
        case = random.randint(1,5)
        if bond: case = 3
        if case == 1:
            mElement = randElement("m")
            m = [mElement[2], int(mElement[3][0])]
            if m[1] == 1:
                eq = m[0] + "ClO3"
            else:
                eq = m[0] + "(ClO3)" + str(m[1])
            return [[eq,0], "d2"]
        elif case == 2:
            mElement = randElement("m")
            m = [mElement[2], int(mElement[3][0])]
            pCharge = m[1] / math.gcd(2, m[1])
            mCharge = str(int(2 * pCharge / m[1]))
            if pCharge == 1:
                pCharge = ""
            if mCharge == "1":
                mCharge = ""
            if pCharge == "":
                eq = m[0] + mCharge + "CO3"
            else:
                eq = m[0] + mCharge + "(CO3)" + str(pCharge)
            return [[eq,0], "d3"]
        else: #maybe add smth about decomposing hydroxides
            if bond: 
                return [[randBMForBonds(), 0], "d1"]

            cmpd = getRandomCompound(0,0,1,0,0)
            return [[cmpd[1],0], "d1"]
    elif rxType == "combustion":
        case = random.randint(1,2)
        if bond: case = 2
        if case == 1:
            tmChoice = random.randint(0,1)
            if tmChoice == 0:
                mElement = randElement("m")
                m = [mElement[2], int(mElement[3][0])]
            else:
                mElement = randElement("tm")
                m = [mElement[2], random.randint(1,4)]
            return [[m, ["O2",2]], "c1"]
        elif case == 2:
            if bond:
                cmpd = getRandomCompound(0,0,0,0,1)
                return [[cmpd[0], 0], random.choice(["complete combustion", "incomplete combustion"]) ]
            cNum = random.randint(1,10)
            hNum = random.randint(1,20)
            oNum = random.randint(0,5)
            if cNum == 1:
                cNum = ""
            if hNum == 1:
                hNum = ""
            if oNum == 1:
                oNum = ""
            cmpd = f"C{cNum}H{hNum}"
            if oNum != 0:
                cmpd += "O" + str(oNum)
            return [[cmpd,0], random.choice(["complete combustion", "incomplete combustion"])]
    elif rxType == "single replacement":
            case = random.randint(1,2)
            if case == 1:
                mActivitySeries = ["Ag", "Hg", "Cu", "H", "Pb", "Fe", "Zn", "Al", "Mg", "Na", "Ca", "K", "Li"]
                m1 = random.choice(mActivitySeries)
                m2 = m1
                while m2 == m1:
                    m2 = random.choice(mActivitySeries)
                m1Charge = findCharge(m1)
                m2Charge = findCharge(m2)

                if m1 == "Hg" and m1Charge == 1:
                    m1 = "Hg2"
                    m1Charge = 2
                if m2 == "Hg" and m2Charge == 1:
                    m2 = "Hg2"
                    m2Charge = 2

                polyatomic = random.randint(0,1)
                if polyatomic == 1:
                    n = randPolyatomic()
                    nIons = n[1]
                else:
                    nElement = randElement("n")
                    n = [nElement[2], int(nElement[3][0])]
                    nIons = n[1]
                    if nIons > 4 and nIons != 8:
                        nIons = 8 - nIons
                nCharge = int(m2Charge / math.gcd(nIons, m2Charge))
                m2Charge = int(nIons / math.gcd(nIons, m2Charge))
                if nCharge == 1: 
                    nCharge = ""
                    nName = n[0]
                elif polyatomic == 1:
                    nName = f"({n[0]})"
                else: nName = n[0]
                if m2Charge == 1: m2ch = ""
                else: m2ch = m2Charge
                return [[[f"{m2}{m2ch}{nName}{nCharge}",0], [m1, m1Charge]], "sr1", [m2, findCharge(m2[0:2])], [n[0], nIons]]
            elif case == 2:
                nActivitySeries = ["I2", "Br2", "Cl2", "F2"]
                n1 = random.choice(nActivitySeries)
                n2 = n1
                while n1 == n2:
                    n2 = random.choice(nActivitySeries)

                tmChoice = random.randint(0,1)
                if tmChoice == 0:
                    mElement = randElement("m")
                    m = [mElement[2], int(mElement[3][0])]
                else:
                    mElement = randElement("tm")
                    m = [mElement[2], random.randint(1,4)]

                mCharge = m[1]
                if mCharge == 1: mCharge = ""

                return [[[f"{m[0]}{n2[:-1]}{mCharge}",0], [n1[:-1], 1]], "sr2", m, [n2[:-1],1]]
    elif rxType == "double replacement":
        repeat = True
        while repeat or (product1.isSoluable() == "inconclusive") or (product2.isSoluable() == "inconclusive"):
            repeat = False
            cmpd1 = getRandomCompound()
            while cmpd1[2] != "Ternary Ionic":
                cmpd1 = getRandomCompound()
            cmpd2 = getRandomCompound()
            while cmpd2[2] != "Ternary Ionic":
                cmpd2 = getRandomCompound()
            cmpd1 = cmpd1[1]
            cmpd2 = cmpd2[1]
            ionized1 = ionizeTernaryIonic(cmpd1)
            ionized2 = ionizeTernaryIonic(cmpd2)
            if ionized1[0] == ionized2[0]:
                repeat = True
            if ionized2[1] == ionized1[1]:
                repeat = True
            product1 = compound(ionicCompoundFromElements(m = ionized1[0], n = ionized2[1]))
            product2 = compound(ionicCompoundFromElements(m = ionized2[0], n = ionized1[1]))
        return [[[cmpd1[1],0], [cmpd2[1], 0]], "dr", [[compound(cmpd1), compound(cmpd2)], [product1, product2]]]
    elif rxType == "special":
        if bond:
            Cn = random.randint(1,6)
            Hn = 2 * Cn - 2 * random.randint(0,2) + 2
            if Cn == 1: 
                Cn = ""
                Hn = 4
            if Hn == 0: Hn = 2
            other = random.choice(["F2", "Cl2", "Br2", "I2"])
            return [[[compound(f"C{Cn if Cn != 1 else ''}H{Hn}"), 0], [compound(other)]], "special", "hydrocarbon replacement"]
        specialList = [[[[compound("Cu"),0], [compound("HNO3"),0]], "special", "dilute", [[compound("Cu(NO3)2"),0], [compound("NO"), 0], [compound("H2O"),0]]],
                       [[[compound("Cu"),0], [compound("HNO3"),0]], "special", "concentrated", [[compound("Cu(NO3)2"),0], [compound("NO2"), 0], [compound("H2O"),0]]]]
        return random.choice(specialList)


    # this should include: synthesis, decomposition, combustion (hydrocarbon stuff), single replacement, double replacement, 
    # based on that, get the elements
    # return [reactionList, type]

def ionicCompoundFromElements(**inputElements):
    for key, value in inputElements.items():
        if key == "m":
            m = value
        else:
            n = value
        
    mCharge = int(m[1])
    nCharge = int(n[1])

    mNum = int(nCharge / math.gcd(mCharge, nCharge))
    nNum = int(mCharge / math.gcd(nCharge, mCharge))

    polyatomic = False
    caps = False
    for i in n[0]:
        tempCaps = False
        if i.isdigit():
            polyatomic = True
        if i.isupper():
            tempCaps = True
        if caps and tempCaps:
            polyatomic = True
        elif tempCaps:
            caps = True

    if mNum == 1: mNum = ""
    if nNum == 1: nNum = ""
    elif polyatomic:
        n[0] = f"({n[0]})"

    return f"{m[0]}{mNum}{n[0]}{nNum}"

def polyatomicCharge(polyatomicIon = "Enter a polyatomic ion!"):
    for i in list(polyatomicCharges.keys()):
        if polyatomicIon == i:
            return int(polyatomicCharges.get(i))
    raise Exception(f"Enter a valid polyatomic ion: {polyatomicIon}")

def ionizeTernaryIonic(el):
    if el[1].isupper(): index = 1
    elif el[2].isupper(): index = 2
    else: index = 3
    if "NH4" in el:
        if "(NH4)" in el:
            index = el.index(")")
            metal = ["NH4", 1]
            pCharge = int(el[index+1])
            polyatomicIon = el[index+2:]
            return [metal, [polyatomicIon, pCharge]]
        else:
            index = el.index("4")
            metal = ["NH4",1]
            polyatomicIon = [el[index+1:], 1]
            return [metal, polyatomicIon]
    elif "(" in el:
        index = el.index("(")
        # ) will have the index -2
        polyatomicIon = el[index+1:-2]
        try: mNum = int(el[index-1])
        except ValueError: mNum = 1
        pNum = int(el[-1])
        if el[index-1].isdigit():
            metal = el[:index-1]
        else: metal = el[:index]
    else:
        polyatomicIon = el[index:]
        pNum = 1
        try: mNum = int(el[index-1])
        except ValueError: mNum = 1
        if el[index-1].isdigit():
            metal = el[:index-1]
        else: metal = el[:index]
    pCharge = polyatomicCharge(polyatomicIon)
    mCharge = int(pCharge / mNum) * pNum
    return [[metal, mCharge], [polyatomicIon, pCharge]]

def findPolyatomicIon(ion, charge) -> str:
    if ion == "MnO4":
        if charge == 1:  return "permanganate"
        else: return "manganate"
    ion += " " + str(charge)
    name = [k for k, v in polyatomicIons.items() if v == ion]
    try: name = name[0]
    except IndexError: raise Exception(f"enter a valid ion: {ion}")
    return str(name)

def findHeatOfFormation(cmpd) -> list:
    small = False
    if cmpd == "Br2":
        cmpd = random.choice(["Br2 (g)", "Br2 (l)"])
        small = True
    elif cmpd == "C":
        cmpd = random.choice(["C (s, diamond)" , "C (s, graphite)"])
        small = True
    elif cmpd == "H2O":
        cmpd = random.choice(["H2O (g)", "H2O (l)"])
        small = True
    elif cmpd == "I2":
        cmpd = random.choice(["I2 (g)", "I2 (s)"])
        small = True
    elif cmpd == "P":
        cmpd = random.choice(["P (s, white)", "P (s, red)"])
        small = True
    elif cmpd == "S":
        cmpd = random.choice([ "S (s, rhombic)", "S (s, monoclinic)"])
        small = True

    if cmpd in heatOfFormationsSmall:
        typeCmpd = "small"
        if small: typeCmpd = "special"
        return [cmpd, heatOfFormationsSmall.get(cmpd), typeCmpd]
    

    if cmpd in heatOfFormationsLarge:
        return [cmpd, heatOfFormationsLarge.get(cmpd), "large"]
    else: 
        value = 0
        while value == 0:
            value = random.choice(list(heatOfFormationsLarge.values()))
        return [cmpd, value, "random"]

def randUnit(cmpd, moles): # cmpd must be a compound object; returns [value, unit]
    try: 
        values = [moles, moles * 22.4, moles * 6.02e23, cmpd.getAtoms(moles), cmpd.getMass(moles)]
    except: 
        raise Exception(f"{cmpd} must be a compound object")
    
    units = ["moles", "L", "particles", "atoms", "g"]

    i = random.randint(0,4)

    return [values[i], units[i], moles]

def getUnit(powerList = []):
    if powerList == []:
        for unit in units:
            p = random.randrange(-2,3)
            powerList.append((unit, p))

    for i, unit in enumerate(units):
        p = powerList[i][1]
        if p == 0: continue
        complexUnits = []
        factor = 0
        n  = random.randrange(1,15)
        prefix = prefixNumbers.get(n)
        complexUnit = prefix + unit + "^" + str(p)
        complexUnits.append(complexUnit)
        prefixFactor = prefixes.get(prefix)
        factor = factor + prefixFactor * p

    finalUnit = " * ".join(complexUnits)
    output = [finalUnit, factor]
    return output

def randTemp():
    return randTempUnit(random.randint(100,450))

def randPressure():
    return randPressureUnit(round(4 * random.random(), 3))

def randVolume():
    return randVolumeUnit(.5 * random.randint(1,200))

def getPressure(pressureAtm, unit):
    if unit == "atm":
        return pressureAtm
    if unit == "kPa":
        return pressureAtm * 101.3
    if unit == "torr":
        return pressureAtm * 760
    
    raise Exception(f"Error: getPressure({pressureAtm}, {unit})")

def getVolume(volumeL, unit):
    if unit == "L":
        return volumeL
    if unit == "m^3":
        return volumeL / 1000
    if unit == "mL":
        return volumeL * 1000
    
    raise Exception(f"Error: getPressure({volumeL}, {unit})")

def getTemp(tempK, unit):
    if unit == "K":
        return tempK
    if unit == "degrees C":
        return tempK - 273
    if unit == "degrees F":
        return (tempK-273) * 9 / 5 + 32
    
    raise Exception(f"Error: getTemp({tempK}, {unit})")

def randTempUnit(tempK):
    temps = ["K", "C", "F"]

    temp = tempK

    unit = random.choice(temps)

    if unit == "K":
        return [temp, unit, temp]
    elif unit == "C":
        return [temp - 273, "degrees " + unit, temp]
    else:
        return [(temp-273) * 9 / 5 + 32, "degrees " + unit, temp]

def randPressureUnit(pressureAtm):
    pressures = ["atm", "kPa", "torr"]

    pressure = pressureAtm

    unit = random.choice(pressures)

    if unit == "atm":
        return [pressure, unit, pressure]
    
    if unit == "kPa":
        return [pressure * 101.3, unit, pressure]
    
    if unit == "torr":
        return [pressure * 760, unit, pressure]    

def randVolumeUnit(volumeL):
    volumes = ["L", "m^3", "mL"]

    volume = volumeL

    unit = random.choice(volumes)

    if unit == "L":
        return [volume, unit, volume]
    
    if unit == "m^3":
        return [volume / 1000, unit, volume]
    
    if unit == "mL":
        return [volume * 1000, unit, volume]    

def solveForVolume(pressure: float, moles: float, temp: int):
    volume = moles * Ratm * temp / pressure
    return volume

def findPeriod(el):
    if el <= 2: return 1
    if el <= 10: return 2
    if el <= 18: return 3
    if el <= 36: return 4
    if el <= 54: return 5
    if el <= 86: return 6
    return 7

def electronConfig(number = 0):
    if number == 0: el = randElement()
    else: el = elements[number]
    numElectrons = int(el[0])
    rList = [el[1]]
    match numElectrons:
        case 1: return ["H", "1s1","1s1"] # H
        case 2: return ["He", "1s2", "1s2"] # He
        case 24: return ["Cr", "[Ar] 4s1 3d5", "1s2 2s2 2p6 3s2 3p6 4s1 3d5"] # Cr
        case 29: return ["Cu", "[Ar] 4s1 3d9", "1s2 2s2 2p6 3s2 3p6 4s1 3d9"] # Cu
        case 57: return ["La", "[Xe] 6s2 5d1", "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d1"] # La
        case 89: return ["Ac", "[Rn] 7s2 6d1", "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 6s2 4f14 5d10 6p6 7s2 6d1"] # Ac

    ngConfigs = {"He" : "1s2",
                  "Ne" : "1s2 2s2 2p6",
                  "Ar" : "1s2 2s2 2p6 3s2 3p6",
                  "Kr" : "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6",
                  "Xe" : "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10",
                  "Rn" : "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 6s2 4f14 5d10 6p6",
                  "Og" : "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 6s2 4f14 5d10 6p6 7s2 5f14 6d10 7p6"}
    
    nobleGasses = [(-1,""), (2, "He"), (10, "Ne"), (18, "Ar"), (36, "Kr"), (54, "Xe"), (86, "Rn"), (118, "Og"), {999, ""}]

    period = findPeriod(numElectrons)

    string = f"[{nobleGasses[period-1][1]}] "
    numElectrons -= nobleGasses[period-1][0]

    level = period // 2 # 1 is <= Ar (sp), 2 is <= Xe (spd), 3 is <= Og (spdf)

    if numElectrons == 0:
        return ngConfigs.get(nobleGasses[period-2][1])

    if level == 1:
        if numElectrons <= 2:
            string += f" {period}s{numElectrons}"
        else:
            string += f" {period}s2 {period}p{numElectrons - 2}"
    if level == 2:
        if numElectrons <= 2:
            string += f" {period}s{numElectrons}"
        elif numElectrons <= 12:
            string += f" {period}s2 {period-1}d{numElectrons - 2}"
        else:
            string += f" {period}s2 {period -1}d10 {period}p{numElectrons - 12}"
    if level == 3:
        if numElectrons <= 2:
            string += f" {period}s{numElectrons}"
        elif numElectrons <= 16:
            string += f" {period}s2 {period - 2}f{numElectrons - 3} {period - 1}d1"
        elif numElectrons <= 26:
            string += f" {period}s2 {period - 2}f14 {period - 1}d{numElectrons - 16}"
        else:
            string += f" {period}s2 {period - 2}f14 {period - 1}d10 {period}p{numElectrons - 26}"

    rList.append(string)
    ng = string[1:3]
    rList.append(ngConfigs.get(ng) + string[4:])
    return rList

def isParamagnetic(el = 0):
    if el == 0: el = random.randint(1,118)
    if el == 1: return True
    if el == 2: return False
    try:
        eConfig = electronConfig(el)[1]
    except: pass
    eConfig = eConfig.split("]")[1]
    nums = []
    for i in range(len(eConfig)):
        if eConfig[i-1].isalpha():
            if i == len(eConfig) - 1 or not eConfig[i+1].isdigit(): nums.append(eConfig[i-1:i+1])
            else: nums.append(eConfig[i-1:i+2])
    
    letterToNum = {"s" : 2, "p" : 6, "d" : 10, "f" : 10}
    for i in nums: 
        n = letterToNum.get(i[0])
        if int(i[1:]) != n:
            return True
    return False

def round_sig(x, sig=4):
   return round(x, sig-int(math.floor(math.log10(abs(x))))-1)

def quantumNumbers(num):
    # assume that the first electron in each orbital has positive spin
    eConfig = electronConfig(num)[1]
    last = eConfig.split(" ")[-1]
    n = int(last[0])
    l = {"s" : 0, "p" : 1, "d" : 2, "f" : 3}.get(last[1])
    electronsInLast = int(last[2])
    ml = -l
    ms = 1/2
    while electronsInLast > 1:
        electronsInLast -= 1
        ml += 1
        if ml == l+1: 
            ms *= -1
            ml = -l
    
    return [n, l, ml, ms]

class element:
    def __init__(self, eq = None, elData = None, charge = 0) -> None:
        if elData == None:
            if eq == None: eq = randElement()[2]
            self.eq = eq
            try:
                self.elData = findElement(self.eq)
            except: raise Exception("Invalid elemnt: " + self.eq)
        else:
            self.elData = elData
            self.eq = elData[2]

        # should only be the magnitude of the charge, the sign will be decided later
        self.charge = charge

    def getCharge(self):
        if self.isMetal(): return self.charge

        return -self.charge

    def isMetal(self):
        number = self.getAtomicNumber()
        return number in [3, 4, 11, 12, 19, 20, 37, 38, 55, 56, 87, 88]
    
    def isSemimetal(self):
        number = self.getAtomicNumber()
        return number in [5, 14, 32, 33, 51, 52, 84, 85]

    def getGroup(self):
        group = self.elData[3]
        if group in ["1a", "2a"]: return float(group[0])
        if "b" in group: return float(group[0]) + 2
        if "n" in group:
            num = self.getAtomicNumber()

            if num in [58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]:
                return 3 + (num - 57) / 15
            if num in [90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103]:
                return 3 + (num - 89) / 15
            
            raise Exception("bad tm, num: " + str(num))
        return float(group[0]) + 10
    
    def getAtomicNumber(self):
        return int(self.elData[0])

    def getPeriod(self):
        return int(findPeriod(self.getAtomicNumber()))

    def getEN(self):
        return electronegativities.get(self.eq)

    def compareSize(self, other): # return self's size - other's size (+ if self is bigger, 0 if its the same, - if self is smaller)
        if other.getCharge() > self.getCharge(): return 1
        if other.getCharge() < self.getCharge(): return -1

        return -self.compareIE(other)

    def compareEN(self, other): # + if self is more electronegative, 0 if its the same, - if self is less electronegative
        myEN = self.getEN()
        otherEN = self.getEN()

        if myEN == None or otherEN == None:
            return self.compareIE(other)
        else:
            diff = myEN - otherEN
            if diff == 0: return 0
            return diff // abs(diff)

    def compareIE(self, other): # + if self has more IE, 0 if its the same, - if self has less IE
        if self.eq == "He" and other.eq == "He": return 0
        if self.eq == "He": return 1
        if other.eq == "He": return -1

        if self.eq == "H" and other.eq == "H": return 0
        if self.eq == "H": return 1
        if other.eq == "He": return -1

        if self.isMetal() and not other.isMetal(): return -1
        if other.isMetal() and not self.isMetal(): return 1

        if self.isSemimetal() and not other.isSemimetal(): return -1
        if other.isSemimetal() and not self.isSemimetal(): return 1

        if self.getGroup() > other.getGroup(): return 1
        if self.getGroup() < other.getGroup(): return -1

        if self.getPeriod() > other.getPeriod(): return -1
        if self.getPeriod() < other.getPeriod(): return 1

        return 0
    
    def compareEA(self, other): # + if self's EA is more exothermic (more negative), 0 if its the same, - if self's EA is less exothermic (less negative)
        return self.compareIE(other)
    
    def __str__(self) -> str:
        return f"{self.eq} {self.getCharge()}"
    
    def getPhase(self):
        n = self.getAtomicNumber()
        if n in [35, 80]: return "l"
        if n in [1, 2, 7, 8, 9, 10, 17, 18, 36, 5, 86]: return "g"
        return "s"

class compound:
    def __init__(self, compoundList = "RANDOM", charge = 0):
        if compoundList == "e-":
            self.charge = -1
            self.K_sp = None
            self.name = "electron"
            self.equation = "e-"
            self.type = "electron"
            self.compound = []
            self.temp = 0
            return None

        self.charge = charge
        self.K_sp = None
        if compoundList == "RANDOM": compoundList = getRandomCompound()
        if type(compoundList) == list:
            self.name = compoundList[0]
            self.equation = compoundList[1]
            try: self.type = compoundList[2]
            except IndexError: self.type = "n/a"
        elif type(compoundList) == str:
            if "_" in compoundList:
                compoundList, self.charge = compoundList.split("_")
                self.charge = int(self.charge)
            if compoundList[-1] == "-": 
                self.charge = -1
                compoundList = compoundList[:-1]
            self.name = "Unknown"
            self.equation = compoundList
            self.type = "Unknown"
        
        if self.type == "element": # if the input is a string this is never run?
            self.equation = self.name
            self.compound = [self.equation,1]
            if self.equation in ["H", "N", "O", "F", "I", "C", "Br", "Cl"]:
                self.compound[1] = 2
                self.equation += "2"
            elif self.equation in ["H2", "N2", "O2", "F2", "I2", "C2", "Br2", "Cl2"]:
                self.compound = [self.compound[0:-1], 2]
            elif self.equation == "Hg2":
                self.equation = "Hg"
                self.compound = [["Hg",1]]
        else: self.compound = atomsInCompound(self.equation)

        if type(self.compound[0]) == str:
            self.compound = [self.compound]

        self.compoundDict = {}
        for i in self.compound: 
            if i[0] in self.compoundDict: self.compoundDict[i[0]] += i[1]
            else: self.compoundDict[i[0]] = i[1]

        self.temp = 0

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        if self.equation == "e-": return "e-"
        return self.equation + ("_" + str(self.charge)) * (self.charge != 0)

    def getEq(self): # why did i even make this method?!
        eq = ""
        for i in self.compoundDict:
            num = self.compoundDict[i]
            if num == 1:
                num = ""
            eq += i[0] + str(num)
        return eq
            
    def getMolarMass(self):
        mass = 0
        for i in self.compound:
            if type(i) == list:
                mass += getAtomMass(i[0]) * i[1]
            else: mass += getAtomMass(self.compound[0]) * self.compound[1]
        return mass
    
    def getParticles(self, moles = 1):
        return moles * 6.02e+23
    
    def getMass(self, moles = 1):
        return moles * self.getMolarMass()
    
    def getAtoms(self, moles = 1):
        atomsPerMolecule = 0
        try:
            for i in self.compound:
                atomsPerMolecule += i[1]
        except IndexError: return 6.02e23 * self.compound[1]
        except TypeError: return 6.02e23 * self.compound[1]
        return self.getParticles(moles) * atomsPerMolecule
    
    def percentComposition(self):
        MM = self.getMolarMass()
        returnList = []
        for i in self.compoundDict:
            nameI = i[0]
            percentI = getAtomMass(i) * self.compoundDict[i] * 100 / MM
            returnList.append([nameI, percentI])
        return returnList

    def getName(self):
        name = self.name
        if "\ " in name:
            name = name.split("\ ")[1]
        return name
    
    def getNameFromEq(self, eqOveride = None, cmpdOverride = None):
        if eqOveride == None or cmpdOverride == None: 
            eq = self.equation
            cmpd = self.compound
        else: 
            eq = eqOveride
            cmpd = cmpdOverride
        SpecialCmpds = {"NH3": "ammonia", "H2O": "water", "C2H6O" : "ethanol", 
                        "CH3CH2OH" : "ethanol", "C2H5OH" : "ethanol", "CHCl3" : "Chloroform",
                        "CH3COCH3" : "acetone", "C6H6" : "benzene", "CH4" : "methane",
                        "CH3OH" : "methanol", "C6H12O6" : "glucose", "C12H22O11" : "sucrose",
                        "C6H6O" : "phenol", "C6H5OH" : "phenol", "C6H5NO2" : "nitrobenzene",
                        "C10H16O" : "camphor"}

        uniqueEls = []
        for i in cmpd:
            if type(i) != int and i[0] not in uniqueEls: uniqueEls.append(i[0])
        if eq in SpecialCmpds.keys(): return SpecialCmpds.get(eq)
        if len(cmpd) == 1 or type(cmpd[1]) == int: 
            diatomics = {"H2": "hydrogen", "N2": "nitrogen", "O2": "oxygen", "F2": "flourine", "Cl2": "chlorine", "Br2": "bromine", "I2": "iodine"}
            if eq in diatomics.keys(): return diatomics.get(eq) + " gas"
            
            el = findElement(eq)
            return el[1]
        if "C" in uniqueEls and "H" in uniqueEls: return eq
        elif len(cmpd) == 2 and "(" not in eq:
            if eq[0] == "H" and not eq[1].islower():
                return "hydro" + acidNames.get("".join([i for i in eq if i != "H" and not i.isdigit()])) + " acid"
            ionic = False
            nonmetals = []
            for i in uniqueEls:
                el = findElement(i)
                if el[4] in ["m", "tm"]:
                    ionic = True
                    metal = i
                else: nonmetals.append(i)
            if ionic: 
                metal = findElement(metal)
                metalName = metal[1]
                nonmetalName = ionNames.get(nonmetals[0])
                if metal[4] == "tm":
                    try: mCharge = ionizeTernaryIonic(eq)[0][1] # takes care of peroxide and azide
                    except:
                        nonmetal = findElement(nonmetals[0])
                        nmCharge = int(nonmetal[3][0])
                        if nmCharge > 4: nmCharge = 8 - nmCharge
                        mCharge = int(nmCharge * cmpd[1][1] / cmpd[0][1])
                    tmFix = f" ({mCharge}) "
                else: tmFix = " "
                return metalName + tmFix + nonmetalName
            el1 = eq[0]
            el2 = ""
            foundDigitOrUpper = False
            coeffecients = []
            for i in eq[1:]:
                if i.isdigit() or i.isupper():
                    foundDigitOrUpper = True
                elif not foundDigitOrUpper: el1 += i
                if foundDigitOrUpper and not i.isdigit(): 
                    el2 += i
                if i.isdigit(): coeffecients.append(int(i))
            idealCoefficients = [findCharge(el1), findCharge(el2)]
            if set(idealCoefficients) == set(coeffecients):
                el1 = findElement(el1)
                el2 = findElement(el2)
                if el1[7] > el2[7]: 
                    firstEl = el2
                    lastEl = el1
                else: 
                    firstEl = el1
                    lastEl = el2
                lastEl = ionNames.get(lastEl[2])
                return firstEl[1] + " " + lastEl
        else:
            # check for acids
            if eq[0] == "H" and not eq[1].islower():
                ion = ""
                if eq[1].isdigit(): index = 2
                else: index = 1
                ion = eq[index:]
                if eq[1].isdigit(): charge = int(eq[1])
                else: charge = 1
                name = findPolyatomicIon(ion,charge)
                name = name.replace("ite", "ous")
                name = name.replace("ate","ic")
                name = name.replace("sulf", "sulfur")
                name = name.replace("sulfuride","sulfide")
                name = name.replace("phosph","phosphor")
                name = name.replace("cynanide","hydrocyanic")
                name = name.replace("azide", "hydroazoic")
                return name + " acid"
            try:
                ionized = ionizeTernaryIonic(eq)
                ion = findPolyatomicIon(ionized[1][0], ionized[1][1])
                metal = ionized[0][0]
                if metal == "NH4": return "ammonium " + ion
                metal = findElement(metal)
                if metal[4] == "tm": 
                    tmFix = f" ({ionized[0][1]}) "
                else: tmFix = " "
                return metal[1] + tmFix + ion
            except: pass
        return eq

    def refresh(self):
        self.name = self.getNameFromEq()
        self.compound = atomsInCompound(self.equation)
        if len(self.compound) == 1: self.type = "element"

    def multCompound(self, factor):
        toMake = []
        for i in self.compound:
            newNum = i[1] * factor
            toMake.append([i[0], newNum])
        for i in self.compoundDict:
            self.compoundDict[i] *= factor
        self.compound = toMake

    def isSoluable(self):
        if self.equation in ["O2", "CO2", "NH3", "N2", "F2", "Cl2", "I2", "He", "Ne", "Ar", "Kr", "Xe", "Rn", "H2O"]:
            return False
        if ("Li" in self.equation) or ("Na" in self.equation) or ("K" in self.equation and "Kr" not in self.equation) or ("Rb" in self.equation) or ("Cs" in self.equation) or ("Fr" in self.equation): return True
        elif ("NH4" in self.equation): return True
        elif "NO4" in self.equation or "NO3" in self.equation or "C2H3O2" in self.equation or "ClO3" in self.equation or "ClO4" in self.equation: return True
        elif "SO4" in self.equation and "HSO4" not in self.equation:
            if ("Ca" in self.equation) or ("Ba" in self.equation) or ("Sr" in self.equation) or ("Ag" in self.equation) or ("Plumbous" in self.name) or ("Mercurous" in self.name): return False
            else: return True
        elif "OH" in self.equation: return False
        elif ("CO3" in self.equation and "HCO3" not in self.equation) or "CrO4" in self.equation or "C2O4" in self.equation or ("PO4" in self.equation and "HPO4" not in self.equation and "H2PO4" not in self.equation): return False
        elif len(self.compound) == 2:
            if "Cl" in self.equation or "Br" in self.equation or ("I" in self.equation and "Ir" not in self.equation and "In" not in self.equation):
                if ("Ag" in self.equation) or ("Plumbous" in self.name) or ("Mercurous" in self.name): return False
                else: return True
            elif "F" in self.equation and "Fe" not in self.equation and "Fr" not in self.equation and "Fm" not in self.equation and "Fl" not in self.equation: return False
            elif "S" in self.equation:
                if ("Ca" in self.equation) or ("Ba" in self.equation) or ("Sr" in self.equation) or ("Mg" in self.equation) or ("Be" in self.equation) or ("Ra" in self.equation): return True
                else: return False
            else: return "inconclusive"
        else: return "inconclusive"

    def setTemp(self, temp):
        self.temp = temp
    
    def raiseTemp(self, finalTemp, moles, fp, bp, heatOfFusion, heatOfVaporization, sSpecificHeat, lSpecificHeat, gSpecificHeat): # for example, water would be (finalTemp, moles, 0, 100, 6.01, 40.7, 1.7, 4.18, 2.1)
        if self.temp < fp: startState = "solid"
        elif self.temp < bp: startState = "liquid"
        else: startState = "gas"

        if finalTemp < fp: finalState = "solid"
        elif finalTemp < bp: finalState = "liquid"
        else: finalState = "gas"

        if finalTemp == self.temp:
            if finalTemp == fp: return heatOfFusion * moles
            if finalTemp == bp: return heatOfVaporization * moles
            return 0

        heat = 0
        
        mass = self.getMass(moles)

        #print(f"startState: {startState}, finalState: {finalState}")

        if startState == finalState: 
            if startState == "solid": return sSpecificHeat * mass * (finalTemp - self.temp) / 1000
            if startState == "liquid": return lSpecificHeat * mass * (finalTemp - self.temp) / 1000
            if startState == "gas": return gSpecificHeat * mass * (finalTemp - self.temp) / 1000

        if startState == "solid": heat += heatOfFusion * moles + sSpecificHeat * mass * (fp - self.temp) / 1000 
        if finalState == "gas": heat += heatOfVaporization * moles + gSpecificHeat * mass * (finalTemp - bp) / 1000 
        if startState == "gas": heat -= heatOfVaporization * moles + gSpecificHeat * mass * (self.temp - bp) / 1000 
        if finalState == "solid": heat -= heatOfFusion * moles + sSpecificHeat * mass * (fp - finalTemp) / 1000 
        if startState == "solid" and finalState == "liquid": heat += lSpecificHeat * mass * (finalTemp - fp) / 1000 
        if startState == "gas" and finalState == "liquid": heat -= lSpecificHeat * mass * (bp - finalTemp) / 1000 
        if startState == "liquid" and finalState == "solid": heat -= lSpecificHeat * mass * (self.temp - fp) / 1000 
        if startState == "liquid" and finalState == "gas": heat -= lSpecificHeat * mass * (bp - self.temp) / 1000 # this is being added, since finalTemp - bp is negative 

        self.temp = finalTemp
        return heat # heat is the amount of heat being used (if its negative, its how much heat is being released) in kJ
    
    def heat(self, heatSupplied, moles, fp, bp, heatOfFusion, heatOfVaporization, sSpecificHeat, lSpecificHeat, gSpecificHeat): # for example, water would be (heatSupplied, moles, 0, 100, 6.01, 40.7, 1.7, 4.18, 2.1)
        if self.temp < fp: startState = "solid"
        elif self.temp < bp: startState = "liquid"
        else: startState = "gas"

        if startState == "solid" and sSpecificHeat == 0: startState = "liquid"
        if startState == "liquid" and lSpecificHeat == 0: startState = "gas"

        mass = self.getMass(moles)
        # print(startState)
        if heatSupplied > 0: # for heating
            if startState == "solid":
                # print("s")
                finalTemp = heatSupplied / (mass * sSpecificHeat) + self.temp
                # print(f"finalTemp: {finalTemp}")
                if finalTemp < fp:
                    self.temp = finalTemp
                    return finalTemp
                heatSupplied -= mass * sSpecificHeat * (fp - self.temp)
                startState = "liquid"
                self.temp = fp
                    
                heatSupplied -= heatOfFusion * moles * 1000
                if heatSupplied <= 0: 
                    return fp
            # print(f"heatSupplied: {heatSupplied}")
            
            if startState == "liquid":
                # print("l")
                finalTemp = heatSupplied / (mass * lSpecificHeat) + self.temp
                # print(f"finalTemp: {finalTemp}")
                if finalTemp < bp:
                    self.temp = finalTemp
                    return finalTemp
                heatSupplied -= mass * lSpecificHeat * (bp - self.temp)
                startState = "gas"
                self.temp = bp

                heatSupplied -= heatOfVaporization * moles * 1000
                # print(f"heatSupplied: {heatSupplied}")
                if heatSupplied <= 0:
                    return bp
            
            # print("g")
            finalTemp = heatSupplied / (mass * gSpecificHeat) + self.temp
            self.temp = finalTemp
            return finalTemp
        else: # for cooling
            if startState == "gas":
                # print("g")
                finalTemp = heatSupplied / (mass * gSpecificHeat) + self.temp
                if finalTemp > bp:
                    self.temp = finalTemp 
                    return finalTemp
                heatSupplied += mass * gSpecificHeat * (self.temp - bp)
                startState = "liquid"
                self.temp = bp
            
                heatSupplied += heatOfVaporization * moles * 1000
                if heatSupplied > 0:
                    self.temp = bp
                    return bp
            
            if startState == "liquid":
                # print("l")
                finalTemp = heatSupplied / (mass * lSpecificHeat) + self.temp
                if finalTemp > fp:
                    self.temp = finalTemp
                    return finalTemp
                heatSupplied += mass * lSpecificHeat * (self.temp - fp)
                startState = "solid"
                self.temp = fp
            
                heatSupplied += heatOfFusion * moles * 1000
                if heatSupplied > 0:
                    self.temp = fp
                    return fp
            
            # print("g")
            finalTemp = heatSupplied / (mass * sSpecificHeat) + self.temp
            self.temp = finalTemp
            return finalTemp
    
    def isMolecular(self):
        for el in self.compound:
            el = findElement(el[0])
            if el[4] != "n": return False

        return "NH4" not in self.equation
    
    def isDiatomic(self):
        return self.equation in ["H2", "N2", "O2", "F2", "Cl2", "Br2", "I2"]
    
    def isHydroCarbon(self):
        return self.equation != "CO" and self.uniqueEls() == set(["H", "C"]) or self.uniqueEls() in [set(["H", "C", el]) for el in ["O", "F", "Cl", "Br", "I"]]
    
    def isAcid(self):
        return self.equation[0] == "H" and self.equation[int(self.equation[1].isdigit()) + 1:] in polyatomicCharges

    def isBinaryMolecular(self):
        return len(self.uniqueEls()) == 2 and self.isMolecular()

    def isTernaryIonic(self):
        if "(" in self.equation: return True
        if self.equation[-2:] == "O2": return True
        pass

    # incomplete
    def hasPeroxide(self):
        if "O2" not in self.equation or not self.isIonic(): return False
        if "(O2)" in self.equation: return True
        if len(self.uniqueEls()) != 2: return False
        metal = findElement(self.compound[0][0])

        charge = metal[3]
        if charge[-1] == "b": return False # i dont even want to deal with this
        else: charge = int(charge[0])

        nmCharge = charge

    def isElement(self):
        return all([i.islower() and not i.isdigit() for i in self.equation[1:]])

    def setEq(self, eq):
        self.equation = eq

    def uniqueEls(self):
        unique = set([])
        for i in self.compound:
            if i[0] not in unique: unique.add(i[0])

        return unique

    def covalentBonds(self):
        if self.isElement():
            return [self.equation]

        if self.isDiatomic():
            return covalentBondsD(self)
        
        if self.isAcid():
            return covalentBondsA(self)
        
        if self.isHydroCarbon():
            return covalentBondsHC(self)

        try: return covalentBondsBM(self, self.charge)
        except: raise Exception("No lewis dot structure found")

    def getCovalentBonds(self):
        try:
            matrix = self.covalentBonds()
        except:
            raise Exception(f"{self.equation} is not a covalent compound")
        
        bonds = []
        for i, line in enumerate(matrix):
            for j, entry in enumerate(line):
                if entry == None: continue
                if "|" in entry:
                    num = entry.count("|")
                    top = matrix[i-1][j]
                    bottom = matrix[i+1][j]

                if "―" in entry or "=" in entry or '≡' in entry:
                    num = {"―" : 1, "=" : 2, "≡" : 3}.get(entry[0])
                    top = matrix[i][j+1]
                    bottom = matrix[i][j-1]

                try: bonds.append([top, num, bottom])
                except: pass
        bonds = [bond if i % 2 == 0 else None for i, bond in enumerate(sorted(bonds))]
        for i in bonds:
            if i == None: bonds.remove(i)
        return sorted(bonds)

    def bondOrder(self):
        bonds = self.getCovalentBonds()
        total = 0
        for i in bonds: total += i[1]
        num = len(bonds)
        return total / num

    def sigmaBonds(self):
        return len(self.getCovalentBonds())
    
    def piBonds(self):
        bonds = self.getCovalentBonds()
        total = 0
        for i in bonds: total += i[1] - 1
        return total

    def bondEnergy(self):
        if self.equation == "CO2": return 1157
        if len(self.compound) == 1 and self.numElements() == 1: return 0
        
        energy = 0
        bonds = self.getCovalentBonds()
        for i in bonds:
            try:
                try:
                    bond = i[0][0] + str(i[1]) + i[2][0]
                    energy += bondEnergies.get(bond)
                except:
                    bond = i[2][0] + str(i[1]) + i[0][0]
                    energy += bondEnergies.get(bond)
            except TypeError: raise Exception("bond not found: " + str(i))

        return energy

    def VESPR(self): # make sure that the compound for this is generated by randBMForBonds()
        if not self.isBinaryMolecular():
            raise Exception("Bad Cmpd")
        
        matrix = self.covalentBonds()
        center = matrix[2][2]

        lonePairs = center[1] // 2

        bonds = 0
        for i in range(1,4):
            for j in range(1,4):
                if matrix[i][j] not in [None, center]: bonds += 1

        if bonds == 1:
            if center == matrix[2][0]: return ["linear", "linear", "180", "np", f"sp{lonePairs if lonePairs != 0 else ''}"]
            else: return ["linear", "linear", 180, "p", f"sp{lonePairs if lonePairs != 0 else ''}"]


        effectivePairs = bonds + lonePairs

        try: 
            return bondTypeDict[effectivePairs * 10 + lonePairs]
        except: 
            raise Exception(f"bond type not found: effective pairs: {effectivePairs}, lone pairs: {lonePairs}")

    def numElements(self):
        s = 0
        for i in self.compound: s += i[1]
        return s

    def hasEl(self, el): 
        for i in self.compound:
            if i[0] == el: return True
        
        return False

    def isPolar(self):        
        if self.isHydroCarbon():
            return "O" in self.equation

        if self.isDiatomic():
            return False
        
        try: return self.VESPR()[3] == "polar"
        except: return False

    def getNumEl(self, el):
        for i in self.compound:
            if i[0] == el: return i[1]

        return 0

    def isIonic(self):
        metal = self.compound[0][0]
        return int(findElement(metal)[0]) in metalsDict

    def isWater(self):
        return self.equation == "H2O"

    def isAqOrGas(self): 
        return self.isMolecular() or self.isIonic() or self.isElement()

    def gen_K_sp(self):
        Ksp = KspDict.get(self.equation)
        if Ksp == None: return random.choice(list(KspDict.values()))

        return Ksp
    
    def solubility_rx(self, mConc = 0, nConc = 0):
        if self.K_sp == None: self.K_sp = self.gen_K_sp()
        try:
            m, nm = ionizeTernaryIonic(self.equation)
            m = m[0] + "_" + str(m[1])
            nm = nm[0] + "_-" + str(nm[1])
        except:
            if "(NH4)" in self.equation:
                m = ["NH4", 1]
                nm = [self.equation[6:], int(self.equation[5])]
            elif "NH4" in self.equation:
                m = ["NH4", 1]
                nm = [self.equation[3:], 1]
            elif len(self.compoundDict) == 2:
                nm = list(self.compoundDict.keys())[1]
                nmCharge = int(findElement(nm)[3][0])
                nmCharge = min(4, nmCharge) + int(nmCharge > 4) * (4 - nmCharge)
                nm += "_-" + str(nmCharge)

                mCharge = nmCharge * self.compound[1][1] / self.compound[0][1]
                m = self.compound[0][0] + "_" + str(int(mCharge))
            # raise Exception(f"only input ternary ionic compounds, {self} is not valid")
        return reaction(["s", [self], [compound(m), compound(nm)], [self.K_sp, mConc, nConc]])

    # cant handle peroxides
    def oxidation_numbers(self) -> dict[str, int]:
        if len(self.compound) == 1: return {self.compound[0][0] : self.charge}
        oxiList = dict.fromkeys(self.compoundDict.keys(), 0)

        try:
            metal, polyatomicIon = ionizeTernaryIonic(self.equation)
            oxiList[metal[0]] = metal[1]
            polyatomicIon[1] = str(-polyatomicIon[1])
            oxiPoly = compound("_".join(polyatomicIon)).oxidation_numbers()
            return oxiList | oxiPoly
        except: pass

        if oxiList.get("F") != None: 
            oxiList["F"] = -1 * self.compoundDict["F"]

            if oxiList.get("O") != None: oxiList["O"] = 2 * self.compoundDict["O"]
        elif oxiList.get("O") != None: oxiList["O"] = -2 * self.compoundDict["O"]

        elementsInCmpd = list(oxiList.keys())

        metal = findElement(elementsInCmpd[0])

        if metal[3] in ["1a", "2a"]: oxiList[metal[2]] = int(metal[3][0]) * self.compoundDict[metal[2]]

        if elementsInCmpd[0] == "H": oxiList["H"] = self.compoundDict["H"]
        elif oxiList.get("H") != None: oxiList["H"] = -self.compoundDict["H"]

        oxiSum = sum(list(oxiList.values()))
        try: zero_index = list(oxiList.values()).index(0)
        except: zero_index = 0

        oxiList[elementsInCmpd[zero_index]] += self.charge - oxiSum

        for el in oxiList: oxiList[el] = int(oxiList[el] / self.compoundDict[el])

        # deals with when oxiList is (0,0) (binary compounds) (might cause errors?)
        if len(oxiList) == 2 and list(oxiList.values()) == [0,0]:
            if self.isIonic():
                nmCharge = findCharge(self.compound[1][0])
                mCharge = self.compound[1][1] * (self.compound[0][1] / nmCharge)
                oxiList[self.compound[0][0]] = mCharge
                oxiList[self.compound[1][0]] = nmCharge
            else:
                c1 = findCharge(self.compound[0][0])
                c2 = findCharge(self.compound[1][0])
                c = math.gcd(c1, c2)
                oxiList[self.compound[0][0]] = c2 / c
                oxiList[self.compound[1][0]] = -c1 / c

        return oxiList

class hydrate(compound):
    def __init__(self, equation : str, numWater : int):
        super().__init__(equation)

        self.anhydrous = self.equation
        self.anhydrousCmpd = self.compound

        self.equation += f" 🞄 {numWater}H2O"
        self.type = "hydrate"
        self.numWater = numWater
        hGood, oGood = False, False
        for i in self.compound:
            if i[0] == "H":
                i[1] += 2 * numWater
                hGood = True
            if i[0] == "O": 
                i[1] += numWater
                oGood = True

        if not hGood: self.compound.append(["H", 2 * numWater])
        if not oGood: self.compound.append(["O", numWater])

    def getNameFromEq(self):
        return super().getNameFromEq(eqOveride=self.anhydrous,cmpdOverride=self.anhydrousCmpd) + " " + prefixes.get(self.numWater) + "hydrate"

    def isPolar(self): return True

    def percentWater(self):
        return self.numWater * 18 / self.getMolarMass()

class reaction:
    def __init__(self, inputList, eqChoice = "NONE", waterAsGas = False):
        self.phases = None
        self.K_eq = None
        self.reactantList = None
        self.typeRx = None
        self.misc = None
        self.occurs = True

        if inputList == "eq":
            solid_index = []
            n = random.randint(2,5)
            options = [
                [["NOCl"], ["NO", "Cl2"]],
                [["H2", "CO2"], ["H2O", "CO"]],
                [["N2", "O2"], ["NO"]],
                [["N2", "O2"], ["NO2"]],
                [["C", "O2"], ["CO"]],
                [["C", "O2"], ["CO2"]],
                [["H2", f"C{n}H{2*n-2}"], [f"C{n}H{2*n}"]],
                [["H2", f"C{n}H{2*n-2}"], [f"C{n}H{2*n+2}"]],
                [["H2", f"C{n}H{2*n}"], [f"C{n}H{2*n+2}"]]
            ]
            i = eqChoice if eqChoice != "NONE" and eqChoice in range(0,12) else random.randint(0,11)
            if i < 9: 
                rx = options[i]
                if rx[0][0] == "C": solid_index = [0]
            elif i == 9:
                hOne, hTwo = random.sample(["H", "Cl", "Br", "I", "F"], 2)
                rx = [[hOne + "2", hTwo + "2"], [hOne + hTwo]]
            else:
                ones = [3,11,19,37,55]
                one = bool(random.getrandbits(1))
                if one: 
                    m = elements[random.choice(ones)][2]
                    rx = [[f"{m}2O", "H2"], [m, "H2O"]]
                else: 
                    m = elements[random.choice([i + 1 for i in ones])][2]
                    rx = [[f"{m}O", "H2"], [m, "H2O"]]

                solid_index = [0,2]

            # switch the order half the time
            switchOrder = random.getrandbits(1)
            if switchOrder: 
                rx[0], rx[1] = rx[1], rx[0]
                if solid_index == [0]: solid_index = [1]

            self.reactantList, self.misc = [[compound(i) for i in react] for react in rx]
            if waterAsGas: self.phases = ["g" for _ in rx[0] + rx[1]]
            else: self.phases = ["g" if not i == "H2O" else random.choice(["l", "g"]) for i in rx[0] + rx[1]]
            for s in solid_index:
                self.phases[s] = "s"
            self.typeRx = "eq"
            power_of_K = random.randint(5,12) * (-1) ** random.randint(0,1)
            K_eq = random.random() * 10 ** power_of_K
            self.generateEqConcs(K_eq)

            self.typeRx = "eq"
        elif inputList[0] in ["a", "b", "ab"]:
            self.typeRx = inputList[0]
            self.reactantList = inputList[1]
            self.misc = inputList[2]

            self.phases = ["l" if i.equation == "H2O" else "aq" for i in self.reactantList + self.misc]

            self.K_eq = inputList[3][1]
            self.reactEqConcs = [inputList[3][0]]
            self.prodEqConcs = [0,0]
            self.eqConcsFromIntial([0, 0], [inputList[3][0]])
        elif inputList[0] == "n":
            self.typeRx = inputList[0]
            self.reactantList = inputList[1]
            self.misc = inputList[2]
        elif inputList[0] == "s":
            self.typeRx = inputList[0]
            self.reactantList = inputList[1]
            self.misc = inputList[2]
            self.phases = ["s", "aq", "aq"]
            self.K_eq = inputList[3][0]
            self.reactEqConcs = []
            self.prodEqConcs = [inputList[3][1], inputList[3][2]]
            self.eqConcsFromIntial()
        else:       
            self.reactantList = inputList[0]
            # never change the order of reactantList
            self.typeRx = inputList[1]
            self.misc = inputList

    def __str__(self):
        coefficients = self.balanceEq()
        skeleton = self.SkeletonEquation()
        rxStr = ""
        for i, cmpd in enumerate(skeleton[0]):
            if coefficients[i] == 1: coefficient = ""
            else: coefficient = coefficients[i]
            rxStr += str(coefficient) + str(cmpd) + " + "
        rxStr = rxStr[:-3]
        if self.typeRx == "d": rxStr += "--Δ-->"
        else: rxStr += " -----> "
        if self.occurs or self.typeRx == "dr":
            for i, cmpd in enumerate(skeleton[1]):
                try:
                    if coefficients[i+len(skeleton[0])] == 1: coefficient = ""
                    else: 
                        coefficient = coefficients[i + len(skeleton[0])]
                except IndexError: pass 
                rxStr += str(coefficient) + str(cmpd) + " + "
            rxStr = rxStr[0:-3]
            if self.typeRx == "dr" and not self.occurs: rxStr += "\nDR/NR"
        else: rxStr += "SR/NR"
        
        return rxStr

    def skeletonStr(self):
        skeleton = self.SkeletonEquation()
        rxStr = ""
        for cmpd in skeleton[0]:
            rxStr += cmpd.equation + " + "
        rxStr = rxStr[0:-3]
        if self.typeRx == "d": rxStr += " -Δ-> "
        else: rxStr += " ---> "
        for cmpd in skeleton[1]:
            rxStr += cmpd.equation + " + "
        return rxStr[0:-3]

    def phaseStr(self):
        if self.phases == None: return str(self)
        reactants, products = self.formatRxList()
        index = -1 # := increments on the first iteration
        rx_str = ""
        
        for reactant in reactants: rx_str += f"{reactant[1] if reactant[1] != 1 else ''}{reactant[0].__repr__()}({self.phases[(index := index + 1)]}) + "
        rx_str = rx_str[:-3] + "-->"
        for product in products: rx_str += f"{product[1] if product[1] != 1 else ''}{product[0].__repr__()}({self.phases[(index := index + 1)]}) + "
        return rx_str[:-3]

    def SkeletonEquation(self) -> list[list[compound]]:
        # format of output is [[reactant 1 compound,...,reactant n compound], [product 1 compound,...product n compound]]
        match self.typeRx:
            case "s1":
                m = self.reactantList[0]
                n = self.reactantList[1]
                mNum = n[1]
                nNum = m[1]
                gcd = math.gcd(mNum, nNum)
                mNum = int(mNum/gcd)
                nNum = int(nNum/gcd)
                if mNum == 1: mNum = ""
                if nNum == 1: nNum = ""
                nonmetal = ""
                if n[0][-1] == "2":
                    for i in n[0]:
                        if not i.isdigit():
                            nonmetal += i
                else: nonmetal = n[0]
                return [[compound(m[0]), compound(n[0])],[compound(f"{m[0]}{mNum}{nonmetal}{nNum}")]]
            case "s2":
                answerDict = {
                    "SO2" : "H2SO3",
                    "SO3" : "H2SO4",
                    "CO2" : "H2CO3",
                    "N2O3" : "HNO2",
                    "N2O5" : "HNO3",
                    "P2O3" : "H3PO3",
                    "P2O5" : "H3PO4",
                    "As2O3" : "H3AsO3",
                    "As2O5" : "H3AsO4",
                    "NH3" : "NH4OH"
                }
                cmpd = self.reactantList[0][0]
                product = answerDict.get(cmpd)
                return [[compound(cmpd), compound("H2O")],[compound(product)]]
            case "s3":
                mOxide = self.reactantList[0][0]
                lastDigit = mOxide[-1]
                if lastDigit == "O":
                    if "2" in mOxide:
                        mCharge = 1
                    else: mCharge = 2
                else: 
                    if lastDigit == "3":
                        mCharge = 3
                    else: mCharge = 4
                if mOxide[1].islower():
                    metal = mOxide[0:2]
                else: metal = mOxide[0]
                product = f"{metal}"
                if mCharge == 1:
                    product += "OH"
                else: product += "(OH)" + str(mCharge)
                mOxide = compound(mOxide)
                product= compound(product)
                return [[mOxide, compound("H2O")], [product]]
            case "d1":
                cmpd = compound(self.reactantList[0])
                el1 = cmpd.compound[0][0]
                try: el2 = cmpd.compound[1][0]
                except IndexError: raise Exception("Invalid compound: " + cmpd)
                diatomicAtoms = ["H", "N", "O", "F", "Cl", "Br", "I"]
                if el1 in diatomicAtoms: el1 += "2"
                if el2 in diatomicAtoms: el2 += "2"
                return [[cmpd], [compound(el1), compound(el2)]]
            case "d2":
                cmpd = self.reactantList[0]
                if "(ClO3)" in cmpd:
                    index = cmpd.index("(")
                    ClO3Num = cmpd[-1]
                else: 
                    index = cmpd.index("ClO3")
                    ClO3Num = ""
                el1 = compound(cmpd[:index] + "Cl" + ClO3Num)
                el2 = compound("O2")
                return [[compound(cmpd)], [el1, el2]]
            case "d3":
                cmpd = self.reactantList[0]
                if "(CO3)" in cmpd:
                    index = cmpd.index("(")
                    CO3Num = cmpd[-1]
                else: 
                    index = cmpd.index("CO3")
                    CO3Num = ""
                el1 = compound(cmpd[:index] + "O" + CO3Num)
                el2 = compound("CO2")
                return [[compound(cmpd)], [el1, el2]]
            case "c1":
                m = self.reactantList[0]
                n = self.reactantList[1]
                mNum = n[1]
                nNum = m[1]
                gcd = math.gcd(mNum, nNum)
                mNum = int(mNum/gcd)
                nNum = int(nNum/gcd)
                if mNum == 1: mNum = ""
                if nNum == 1: nNum = ""
                nonmetal = ""
                if n[0][-1] == "2":
                    for i in n[0]:
                        if not i.isdigit():
                            nonmetal += i
                else: nonmetal = n[0]
                return [[compound(m[0]), compound(n[0])],[compound(f"{m[0]}{mNum}{nonmetal}{nNum}")]]
            case "complete combustion":
                reactant = compound(self.reactantList[0])
                return [[reactant, compound("O2")], [compound("CO2"), compound("H2O")]]
            case "incomplete combustion":
                reactant = compound(self.reactantList[0])
                return [[reactant, compound("O2")], [compound("CO"), compound("H2O")]]
            case "sr1":
                mActivitySeries = ["Ag", "Hg", "Cu", "H", "Pb", "Fe", "Zn", "Al", "Mg", "Na", "Ca", "K", "Li"]
                metal1= self.reactantList[1]
                m1 = metal1[0]
                nonmetal = self.misc[3]
                nonmetal[0] = nonmetal[0].replace("(","")
                nonmetal[0] = nonmetal[0].replace(")", "")
                metal2 = self.misc[2]
                m2 = metal2[0]
                product = ionicCompoundFromElements(m = metal1, n = nonmetal)
                metal1.append("element")
                metal2.append("element")
                cmpd = self.reactantList[0][0]
                if m1 == "Hg2": m1Index = 1
                else: m1Index = mActivitySeries.index(m1)
                if m2 == "Hg2": m2Index = 1
                else: m2Index = mActivitySeries.index(m2)
                if m1Index < m2Index:
                    self.occurs = False
                return [[compound(cmpd), compound(metal1)],[compound(product), compound(metal2)]]
            case "sr2":
                nActivitySeries = ["I", "Br", "Cl", "F"]
                nmetal1 = self.reactantList[1]
                metal = self.misc[2]
                nmetal2 = self.misc[3]
                nmetal2.append("element")
                nmetal1[1] = 1
                nmetal2[1] = 2
                product = ionicCompoundFromElements(m = metal, n = nmetal1)
                nmetal1.append("element")
                cmpd = self.reactantList[0][0]
                nmetal1[1] = str(nmetal1[1])
                nmetal2[1] = str(nmetal2[1])
                nmetal1[1] += "2"
                nmetal2[1] += "2"
                if nActivitySeries.index(nmetal2[0]) > nActivitySeries.index(nmetal1[0]):
                    self.occurs = False
                return [[compound(cmpd), compound(nmetal1[0] + '2')], [compound(product), compound(nmetal2[0] + "2")]]
            case "dr": # this has a ton of errors apparently
                returnList = self.misc[2]
                for index, product in enumerate(returnList[1]):
                    if product.equation == "NH4OH":
                        returnList[1].pop(index)
                        returnList[1].append(compound("NH3"))
                        returnList[1].append(compound("H2O"))
                    elif product.equation == "H2CO3":
                        returnList[1].pop(index)
                        returnList[1].append(compound("H2O"))
                        returnList[1].append(compound("CO2"))
                self.occurs = False
                try:
                    for product in returnList[1]:
                        if not product.isSoluable():
                            self.occurs = True
                except:
                    print(returnList)
                    print(self.reactantList)
                    raise Exception("error generating skeleton equation")

                return returnList
            case "special":
                if self.misc[2] in ["dilute", "concentrated"]:
                    reactants = [i[0] for i in self.reactantList]
                    products = [i[0] for i in self.misc[3]]
                if self.misc[2] == "hydrocarbon replacement":
                    reactants = [i[0] for i in self.reactantList]
                    cmpd = reactants[0].compound
                
                    if cmpd[0][1] * 2 + 2== cmpd[1][1]:
                        newCmpd = f"C{cmpd[0][1] if cmpd[0][1] != 1 else ''}H{cmpd[1][1]-2}{reactants[1].equation}"
                        products = [compound(newCmpd), compound("H2")]
                    else: products = [compound(reactants[0].equation + reactants[1].equation)]
                
                return [reactants, products]
            case "eq" | "ab" | "a" | "b" | "n" | "s":
                return [self.reactantList, self.misc]
            case _: print(self.typeRx)

    def balanceEq(self):
        rpList = self.SkeletonEquation()
        try: rList = rpList[0]
        except: 
            print([str(i) for i in self.misc])
            raise Exception("bad skeleton equation: " + str(rpList))
        pList = rpList[1]
        relList = []
        # for single elements, the format is [El, 1]
        for reactant in rList:
            for i in reactant.compound:
                if type(i) == str:
                    if i not in relList: relList.append(i)
                else:
                    try:
                        if i[0] not in relList:
                            relList.append(i[0])
                    except TypeError: pass
        inputMatrix = [] # [[el1 in react1, el1 in react2..., -el1 in product1, -el1 in product2, 0], [el2 in react1, el2 in react2..., -el1 in product1, -el1 in product2, 0],...]
        for el in relList:
            toAppend = []
            for reactant in rList:
                elcount = 0
                for i in reactant.compound:
                    if type(i) == str:
                        if i == el:
                            elcount += reactant.compound[1]
                        break
                    elif i[0] == el:
                            elcount += i[1]
                toAppend.append(elcount)
            for product in pList:
                elcount = 0
                for i in product.compound:
                    if type(i) == str:
                        if i == el:
                            elcount += product.compound[1]
                        break
                    elif i[0] == el:
                            elcount += i[1]
                toAppend.append(elcount)
            toAppend.append(0)
            inputMatrix.append(toAppend)
        
        inputArray = sp.Matrix(inputMatrix)
        rrefMatrix = list(inputArray.rref()[0])
        rrefList = []
        numcmpd = len(rList) + len(pList)
        i = numcmpd - 1
        while i in range(1,len(rrefMatrix)-1):
            rrefList.append(abs(float(rrefMatrix[i])))
            i += numcmpd + 1
        if rrefList[-1] == 0:
            rrefList = rrefList[0:-1]
        
        # print(f"rrefList: {rrefList}")
        for i, num in enumerate(rrefList):
            if num == 0: rrefList.pop(i)

        rrefList.extend([1.0])
        good = True

        for i in rrefList:
            if type(i) != int and not i.is_integer():
                good = False
        factor = 1
        if good: numList = rrefList
        while not good:
            numList = []
            for i in rrefList:
                i *= factor
                numList.append(i)
            factor += 1
            good = True
            for i in numList:
                if not i.is_integer():
                    good = False  

        numList = [int(i) for i in numList if int(i) != 0]

        l = len([i for sublist in rpList for i in sublist])
        while len(numList) < l:
            numList.append(1)

        return numList
    
    def formatRxList(self) -> list[list[list[compound | int]]]:
        coeffients = self.balanceEq()
        elements = self.SkeletonEquation()

        index = 0
        reactList = []
        for i in elements[0]:
            reactList.append([i,coeffients[index]])
            index += 1
        productList = []
        for i in elements[1]:
            try: productList.append([i,coeffients[index]])
            except IndexError: pass
            # this might lead to some more errors
            index += 1
        if self.typeRx == "special": return [reactList, productList, self.misc[2]]
        return [reactList, productList]

    def enthalpyFromBonds(self):
        rx = self.formatRxList()
        react = 0
        for i in rx[0]: 
            react += i[1] * i[0].bondEnergy()
        prod = 0
        for i in rx[1]: prod += i[1] * i[0].bondEnergy()
        try:
            react = 0
            for i in rx[0]: react += i[1] * i[0].bondEnergy()
            prod = 0
            for i in rx[1]: prod += i[1] * i[0].bondEnergy()
        except: return f"error finding the enthalpy of {self}"

        return react - prod

    def reactants(self):
        return self.SkeletonEquation()[0]

    def products(self):
        return self.SkeletonEquation()[1]
    
    def allCompounds(self) -> list[compound]:
        reactants, products = self.SkeletonEquation()
        return reactants + products

    def generatePhases(self):
        reactants, products = self.SkeletonEquation()
        if len(reactants) > 2 and reactants[0].isHydroCarbon() and reactants[1].equation == "O2":
            phases = ["g", "g"]
            for cmpd in products:
                if cmpd.isWater(): phases.append(random.choice(["g", "l", "l"]))
                else: phases.append("g")
            self.phases = phases
            return phases
        
        phases = []
        if self.typeRx == "dr":
            for cmpd in reactants + products:
                if cmpd.isSoluable(): phases.append("aq")
                elif cmpd.isWater(): phases.append("l")
                elif cmpd.isMolecular(): phases.append("g")
                else: phases.append("s")
            self.phases = phases
            return phases

        if self.typeRx == "sr":
            for cmpd in reactants + products:
                if cmpd.isElement(): phases.append(element(cmpd.equation).getPhase())
                elif cmpd.isSoluable(): phases.append("aq")
                else: phases.append("s")
            self.phases = phases
            return phases
        
        phase_of_other = random.choice(["s", "aq"])
        for cmpd in reactants + products:
            if cmpd.isDiatomic(): phases.append("g")
            elif cmpd.isElement(): phases.append(element(cmpd.equation).getPhase())
            elif cmpd.isMolecular(): phases.append(random.choice(["l", "g"]))
            elif cmpd.equation == "Cu(NO3)2": phases.append("aq")
            else: phases.append(phase_of_other)
        self.phases = phases
        return phases

    def molecularity(self):
        return len(self.SkeletonEquation()[0])

    def checkRxForThermo(self):
        if not self.occurs: return False
        if self.phases == None: self.generatePhases()
        for phase, cmpd in zip(self.phases, self.allCompounds()):
            if thermoData.get(thermCompound(cmpd.equation + "(" + phase + ")")) == None: return False
        return True
    
    def thermoProfile(self, choice):
        # choice: 0 = enthalpy, 1 = gibbs, 2 = entropy
        if not self.checkRxForThermo(): return None
        i = 0
        n = len(self.reactants())
        curr = 0
        coeffs = self.balanceEq()
        for phase, cmpd in zip(self.phases, self.allCompounds()):
            amount = thermoData.get(thermCompound(cmpd.equation + "(" + phase + ")"))[choice]
            if i < n: curr -= coeffs[i] * amount
            else: curr += coeffs[i] * amount
            i += 1
        return curr

    def enthalpyFromThermData(self):
        return self.thermoProfile(0)

    def gibbsFromThermData(self):
        return self.thermoProfile(1)

    def entropyFromThermData(self):
        return self.thermoProfile(2)

    def generateEqConcs(self, K_eq = None):
        prod_eq, react_eq = self.eqExpression()
        if K_eq == None:
            self.prodEqConcs = [random.randint(1,50000) / 10000 for _ in prod_eq]
            self.reactEqConcs = [random.randint(1,50000) / 10000 for _ in react_eq]
            self.K_eq = 1
            for expression, conc in zip(prod_eq, self.prodEqConcs): self.K_eq *= conc ** expression[1]
            for expression, conc in zip(react_eq, self.reactEqConcs): self.K_eq /= conc ** expression[1]
            self.K_eq = round_sig(self.K_eq, 6)
        else:
            self.K_eq = K_eq
            n = len(prod_eq)
            self.prodEqConcs = [K_eq ** (1/n) for _ in prod_eq]
            self.reactEqConcs = [1 for _ in react_eq]
            if any([i > 100 for i in self.prodEqConcs + self.reactEqConcs]):
                n = len(react_eq)
                self.reactEqConcs = [K_eq ** (-1/n) for _ in react_eq]
                self.prodEqConcs = [1 for _ in prod_eq]

    def eqExpressionStr(self):
        if self.phases == None: raise Exception("Must define phases!")
        reactants, products = self.formatRxList()
        index = -1
        reacts = [f"[{cmpd.equation}]" + (f"^{coeff}" if coeff != 1 else "") for cmpd, coeff in reactants if self.phases[index := index + 1] in ["g","aq"]]
        prods = [f"[{cmpd.equation}]" + (f"^{coeff}" if coeff != 1 else "") for cmpd, coeff in products if self.phases[index := index + 1] in ["g","aq"]]
        if prods == []: prods = ["1"]
        if reacts == []: return "".join(prods)
        return "".join(prods) + "/" + "".join(reacts)
    
    def eqExpression(self):
        if self.phases == None: raise Exception("Must define phases!")
        reactants, products = self.formatRxList()
        index = -1
        reacts = [[cmpd, coeff] for cmpd, coeff in reactants if self.phases[index := index + 1] in ["g","aq"]]
        prods = [[cmpd, coeff] for cmpd, coeff in products if self.phases[index := index + 1] in ["g","aq"]]
        return [prods, reacts]

    def reactionQuotient(self, prodConc = None, reactConc = None):
        if prodConc == None: prodConc = self.prodEqConcs
        if reactConc == None: reactConc = self.reactEqConcs

        prodEq, reactEq = self.eqExpression()

        prodConc = [i + 1e-200 for i in prodConc]
        reactConc = [i + 1e-200 for i in reactConc]

        Q = 1
        for conc, coeff in zip(prodConc, prodEq): Q *= conc ** coeff[1]
        try:
            for conc, coeff in zip(reactConc, reactEq): Q /= conc ** coeff[1]
        except:

            return float('inf')

        return Q

    def eqConcsFromMissing(self, newProd : list[int], newReact : list[int]):
        if len(newProd) != len(self.prodEqConcs) or len(newReact) != len(self.reactEqConcs): raise Exception("Invalid equilbrium inputs")
        if "X" in newProd: blankIndex = 2 * newProd.index("X")
        elif "X" in newReact: blankIndex = 2 * newReact.index("X") + 1
        else: raise Exception("Must include unknown X in lists")
        eqExpression = self.eqExpression()

        curr_K = 1
        for i, expression in zip(newProd, eqExpression[0]):
            if i != "X": curr_K *= i ** expression[1]
        for i, expression in zip(newReact, eqExpression[1]):
            if i != "X": curr_K /= i ** expression[1]

        if blankIndex % 2 == 0: newProd[blankIndex // 2] = (self.K_eq / curr_K) ** (1/eqExpression[blankIndex % 2][blankIndex // 2][1])
        else: newReact[blankIndex // 2] = (self.K_eq / curr_K) ** (-1/eqExpression[blankIndex % 2][blankIndex // 2][1])
        
        self.reactEqConcs = newReact
        self.prodEqConcs = newProd

    def eqConcsFromIntial(self, newProd : list[int] = None, newReact : list[int] = None):
        if  not newProd: 
            newProd = self.prodEqConcs
        if not newReact: 
            newReact = self.reactEqConcs
        if len(newProd) != len(self.prodEqConcs) or len(newReact) != len(self.reactEqConcs): raise Exception("Invalid equilbrium inputs")
        prodEq, reactEq = self.eqExpression()
                
        rQuotient = self.reactionQuotient(newProd, newReact)
        pError = abs((rQuotient - self.K_eq) / self.K_eq)

        if pError < .05:
            self.prodEqConcs = newProd
            self.reactEqConcs = newReact

            return None

        towardsProducts = 2 * int(self.K_eq > rQuotient) - 1
        # 1 if it is towards the products, -1 if it is towards the reactants

        prodRoots = [[-1 * towardsProducts * initConc / stoicRatio[1]] * stoicRatio[1] for initConc, stoicRatio in zip(newProd, prodEq)]
        reactRoots = [[towardsProducts * initConc / stoicRatio[1]] * stoicRatio[1] for initConc, stoicRatio in zip(newReact, reactEq)]
        prodRoots = sum(prodRoots, []) # flattens list
        reactRoots = sum(reactRoots, []) # flattens list

        if prodRoots == []: prodPoly = np.polynomial.Polynomial([1])
        else: prodPoly = np.polynomial.polynomial.Polynomial.fromroots(prodRoots)
        if reactRoots == []: reactPoly = np.polynomial.Polynomial([1])
        else: reactPoly = np.polynomial.polynomial.Polynomial.fromroots(reactRoots)

        for stoicRatio in prodEq: prodPoly *= (towardsProducts * stoicRatio[1]) ** stoicRatio[1]
        for stoicRatio in reactEq: reactPoly *= (-towardsProducts * stoicRatio[1]) ** stoicRatio[1]

        eqPoly = prodPoly - reactPoly * self.K_eq

        roots = list(filter(lambda x : np.imag(x) < 1e-3 and x >= 0, eqPoly.roots()))

        d = min(np.real(roots))
        self.prodEqConcs = [initConc + towardsProducts * stoicRatio[1] * d for initConc, stoicRatio in zip(newProd, prodEq)]
        self.reactEqConcs = [initConc - towardsProducts * stoicRatio[1] * d for initConc, stoicRatio in zip(newReact, reactEq)]

class solution:
    def __init__(self, solute : compound, mass_solute : float = None, solute_density : float = 0, moles_solute : float = None, moles_solvent : float = None, total_volume : float = None, solvent : compound = compound("H2O")) -> None:
        # solute density in g/mL, mass solute in g, moles solute and moles solvent in mol, total volume in L
        # if solute density is 0, then we ignore the solute's mass for stuff
        # if solute density is None, then the code tries to find the density (if it can't, it randomly generates it in [.5,3.5])

        self.solute = solute
        self.solvent = solvent

        self.volume = None
        self.moles_solute = None
        self.moles_solvent = None

        if moles_solute and mass_solute: raise Exception("solute mass is overconstrained")
        if mass_solute: self.moles_solute = mass_solute / self.solute.getMass()
        if moles_solute: self.moles_solute = moles_solute
    
        if moles_solvent: self.moles_solvent = moles_solvent

        self.solvent_density = miscDensities.get(self.solvent.getEq())
        if not self.solvent_density: raise Exception(f"invalid solvent: {solvent.equation}")
        self.solute_density = solute_density  
        if self.solute_density == None: self.solute_density = miscDensities.get(self.solute.getEq())
        if self.solute_density == None: self.solute_density = round(random.random() * 3 + .5, 2)
        
        if total_volume:
            self.volume = total_volume
            if self.moles_solute and self.moles_solvent: raise Exception("volume is overconstrained")
            if not self.moles_solute: 
                if self.solvent_density != 0: total_volume -= self.solvent.getMass(self.moles_solvent) / (1000 * self.solvent_density)
                self.moles_solute = 1000 * total_volume * self.solute_density / self.solute.getMolarMass()
            if not self.moles_solvent:
                if self.solute_density != 0: total_volume -= self.solute.getMass(self.moles_solute) / (1000 * self.solute_density)
                self.moles_solvent = 1000 * total_volume * self.solvent_density / self.solvent.getMolarMass()
        
        if not self.moles_solute: self.moles_solute = 0
        if not self.moles_solvent: self.moles_solvent = 1
        if not self.volume: 
            if self.solute_density == 0: self.volume = self.solvent.getMass(self.moles_solvent) / (1000 * self.solvent_density)
            else:
                solute_volume = self.solute.getMass(self.moles_solute) / (1000 * self.solute_density)
                solvent_volume = self.solvent.getMass(self.moles_solvent) / (1000 * self.solvent_density)
                self.volume = solute_volume + solvent_volume

        if not self.moles_solute and self.solute_density == 0: self.moles_solute = 1

    def __str__(self):
        return f"{self.molarity()} M solution of {self.solute.equation} in {self.solvent.equation}"
    
    def moleFractions(self, solute = True):
        if solute: return self.moles_solute / (self.moles_solute + self.moles_solvent)
        else: return self.moles_solvent / (self.moles_solute + self.moles_solvent)
    
    def molality(self):
        return 1000 * self.moles_solute / self.solvent.getMass(self.moles_solvent)

    def molarity(self):
        return self.moles_solute / self.volume
    
    def pMV(self):
        # divide by 1000 (L --> mL) and multiply by a 100 (percent)
        return self.solute.getMass(self.moles_solute) / (10 * self.volume)
    
    def solute_volume(self):
        if self.solute_density == 0: return 0
        return self.solute.getMass(self.moles_solute) / (1000 * self.solute_density)
    
    def solvent_volume(self):
        return self.solvent.getMass(self.moles_solvent) / (1000 * self.solvent_density)

    # solute_density needs to be None or specified for this to work
    def pVV(self):
        return 100 * self.solute_volume() / self.solvent_volume()

    def setMolarity(self, newMolarity, addSolvent = False, addSolute = False):
        if addSolute and addSolvent: raise Exception("Only choose addSolute or addSolvent")
        if addSolute:
            M = self.molarity()
            self.moles_solute *= newMolarity / M
            self.volume *= M / newMolarity
        if addSolvent:
            M - self.molarity()
            self.moles_solvent *= M / newMolarity
            self.volume *= newMolarity / M

    def dissovles(self):
        return self.solute.isPolar() == self.solvent.isPolar()
    
    def aqueous(self):
        return self.solvent == compound("H2O")

    def describeSolute(self):
        if self.checkSolution != None: return self.checkSolution()

        if (self.solute.isSoluable() and self.solute.isIonic()) or self.solute.equation in ["HI", "HCl", "HBr"]: return "Strong Electrolyte"
        if not self.solute.isPolar(): return "Nonelectrolyte"
        return "Weak Electrolyte"

    def saturation(self):
        if self.checkSolution != None: return self.checkSolution()

        solubility = solubilities.get(self.solute.equation)
        if solubility == None: return "Unknown"

        gSolute = self.solute.getMass(self.moles_solute)
        gSolvent = self.solvent.getMass(self.moles_solvent)
        s = gSolute / (100 * gSolvent)

        if s > solubility: return "Oversaturated"
        if s == solubility: return "Saturated"
        return "Unsaturated"

    def checkSolution(self):
        if not self.dissovles(): return "You must have a solution that dissolves"
        if not self.aqueous(): return "You must have an aqueous solution"
        return None

    def boilingPoint(self):
        K = bpElevationConstants.get(self.solvent.getEq())
        if K == None: K = round(random.random() * 9 + 1, 2)

        try: return  miscBps.get(self.solvent.getEq()) + self.particlesPerSolute() * K * self.molality()
        except: return None
        
    def freezingPoint(self):
        K = fpDepressionConstants.get(self.solvent.getEq())
        if K == None: raise Exception(f"no constant found: {self.solute.equation()}")

        try: return miscFps.get(self.solvent.getEq()) - self.particlesPerSolute() * K * self.molality()
        except: return None

    def particlesPerSolute(self):
        if self.solute.isMolecular(): return 1
        if len(self.solute.uniqueEls()) == 2: return self.solute.numElements()

        else:
            m, n = ionizeTernaryIonic(self.solute.equation)
            m = m[1]
            n = n[1]
            commonFactor = math.gcd(m,n)
            m /= commonFactor
            n /= commonFactor
            return int(m + n)

class AB_blueprint:
    def __init__(self, moles = None, volume = 1, molarity = 1):
        self.acid = compound("H2O")
        self.base = compound("H2O")
        self.c_acid = compound("H3O_1")
        self.c_base = compound("OH_-1")

        if moles: self.molarity = moles / volume
        else: self.molarity = molarity

        self.volume = volume
        self.K_eq = "LARGE"

        self.bl_rx : reaction = None

        self.eq = "H2O"

    def HConc(self):
        return self.bl_rx.prodEqConcs[0]
    
    def pH(self):
        return -1 * math.log10(self.HConc())

    def pOH(self):
        return 14 - self.pH()
    
    def OHConc(self):
        return (10 ** -14) / (self.HConc())

    def addCommonIon(self, added_molarity):
        prod_eq, _ = self.bl_rx.eqExpression()
        common_ion_index = 0
        if prod_eq[0][0].equation in ["OH_-1", "H3O_1", "H_1", "H3O_+1", "H_+1"]: common_ion_index = 1

        newProdConcs = self.bl_rx.prodEqConcs
        newProdConcs[common_ion_index] += added_molarity

        self.bl_rx.eqConcsFromIntial(newProdConcs, [self.molarity])

    def moles(self):
        return self.molarity * self.volume
    
    def __str__(self) -> str:
        return f"{round_sig(self.volume)} L of {round_sig(self.molarity)} M {self.eq}"

    def __repr__(self) -> str:
        return self.__str__()

class acid(AB_blueprint):
    def __init__(self, acid_eq =None, moles=None, volume=1, molarity=1):
        super().__init__(moles, volume, molarity)

        if "_" in acid_eq: eq, charge = acid_eq.split("_")
        else: eq, charge = acid_eq, 0
        
        self.acid = compound(eq, charge)
        self.base = compound("H2O")
        self.c_acid = compound("H3O", 1)
        
        c_base = list(self.acid.equation)
        if c_base[1].isnumeric():
            c_base[1] = str(int(c_base[1]) - 1)
            if c_base[1] == "1": c_base[1] = ""
        else: c_base = c_base[1:]

        self.c_base = compound("".join(c_base), int(self.acid.charge) - 1)

        self.K_eq = KaDict[eq+("_"+str(charge)) * (charge != 0)]
        if self.K_eq == "LARGE": self.K_eq = 9e200

        self.bl_rx = reaction(["a", [self.acid, self.base], [self.c_acid, self.c_base], [self.molarity, self.K_eq]])
        self.eq = self.acid.__repr__()

class base(AB_blueprint):
    def __init__(self, base_eq = None, moles=None, volume=1, molarity=1):
        super().__init__(moles, volume, molarity)

        self.base = compound(base_eq)
        self.acid = compound("H", 1)
        self.c_base = compound("OH", -1)
        
        if "(OH)2" in base_eq: c_acid = base_eq[:2] + "_+2"
        elif "OH" in base_eq: c_acid = base_eq[:-2] + "_+1"
        else:
            if base_eq[-1] == "H": c_acid = base_eq + "2_+1"
            if base_eq[-2] == "H": c_acid = base_eq[:-1] + str(int(base_eq[-1]) + 1) + "_+1"
            else: c_acid = base_eq + "H_+1"
        
        self.c_acid = compound(c_acid)

        self.K_eq = KbDict[base_eq]
        if self.K_eq == "LARGE": self.K_eq = 9e200

        self.bl_rx = reaction(["b", [self.base], [self.c_base, self.c_acid], [self.molarity, self.K_eq]])
        self.eq = self.base.__repr__()

def ionize_ab(cmpd : compound):
    # returns non H+ or OH- ion in a compound, given that it is an acid or base
    eq = cmpd.equation

    if eq[0] == "H":
        charge = eq[1]
        if eq[1].isdigit(): charge = int(charge)
        else: charge = 1

        return [eq[1 + eq[1].isdigit():], charge]
    
    if eq[-2:] == "OH": return [eq[:-2], 1]
    if eq[-5:-1] == "(OH)": return [eq[:-5], int(eq[-1])]

    raise Exception(f"invalid acid or base: {cmpd}")

# this has an error with computing the leftover moles and salt moles
class neutralization(reaction):
    def __init__(self, acidInput : acid, baseInput : base):
        self.acid = acidInput
        self.base = baseInput
        self.totVol = self.acid.volume + self.base.volume
        acidIon = ionize_ab(self.acid.acid)
        baseIon = ionize_ab(self.base.base)
        self.salt = compound(ionicCompoundFromElements(m = baseIon, n = acidIon))
        super().__init__(["n", [self.acid.acid, self.base.base], [self.salt, compound("H2O")]])
        # acid + base -> salt + H2O
        # this part only works for strong acids and bases
        reacts, prods = self.formatRxList()
        leftover_moles = self.acid.moles() / reacts[0][1] - self.base.moles() / reacts[1][1]

        if leftover_moles >= 0: # base is limiting or stoiciometric mixture
            self.leftover_ab = acid(self.acid.acid.equation, moles = leftover_moles, volume = self.totVol)
            self.salt_moles = prods[0][1] * self.base.moles() / reacts[1][1]
        else: # acid is limiting
            self.leftover_ab = base(self.base.base.equation, moles = -leftover_moles, volume = self.totVol)
            self.salt_moles = prods[0][1] * self.acid.moles() / reacts[0][1]

class half_reaction(reaction):
    def __init__(self, init_cmpd : compound, final_cmpd : compound):
        rList = [init_cmpd]
        pList = [final_cmpd]

        rElements = [el for el in init_cmpd.compound if el[0] not in ["O", "H"]]
        pElements = [el for el in final_cmpd.compound if el[0] not in ["O", "H"]]
        if rElements != None and pElements != None:
            el1, num1 = rElements[0]
            num2 = final_cmpd.getNumEl(el1)
            rElements = [[el, num * num2] for el, num in rElements]
            pElements = [[el, num * num1] for el, num in pElements]

        if rElements != pElements:
            print(rElements)
            print(pElements)
            raise Exception("invalid half reaction")

        rCoeffs = [num2]
        pCoeffs = [num1]

        r_counts = {"O" : num2 * init_cmpd.getNumEl("O"), "H" : num2 * init_cmpd.getNumEl("H"), "e-": num2 * init_cmpd.charge}
        p_counts = {"O" : num1 * final_cmpd.getNumEl("O"), "H" : num1 * final_cmpd.getNumEl("H"), "e-": num1 * final_cmpd.charge}

        added = [] # will be # H2O, # H+, # e- (- means reactants, + means products)

        oDelta = r_counts["O"] - p_counts["O"]
        if oDelta < 0: 
            oDelta = -oDelta
            rList.append(compound("H2O"))
            rCoeffs.append(oDelta)
            r_counts["O"] += oDelta
            r_counts["H"] += 2 * oDelta
        elif oDelta > 0:
            pList.append(compound("H2O"))
            pCoeffs.append(oDelta)
            p_counts["O"] += oDelta
            p_counts["H"] += 2 * oDelta

        hDelta = r_counts["H"] - p_counts["H"]
        added.append(hDelta)
        if hDelta < 0:
            hDelta = -hDelta 
            rList.append(compound("H_+1"))
            rCoeffs.append(hDelta)
            r_counts["H"] += hDelta
            r_counts["e-"] += hDelta
        elif hDelta > 0:
            pList.append(compound("H_+1"))
            pCoeffs.append(hDelta)
            p_counts["H"] += hDelta
            p_counts["e-"] += hDelta

        eDelta = p_counts["e-"] - r_counts['e-']
        added.append(eDelta)
        if eDelta > 0:
            pList.append(compound("e-"))
            pCoeffs.append(eDelta)
            p_counts["e-"] -= eDelta
        elif eDelta < 0:
            eDelta = -eDelta
            rList.append(compound("e-"))
            rCoeffs.append(eDelta)
            r_counts["e-"] -= eDelta

        self.skele_eq = [rList, pList]
        self.coeffs = rCoeffs + pCoeffs

        self.phases = None
        self.K_eq = None
        self.reactantList = None
        self.typeRx = "redox"
        self.misc = None
        self.occurs = True
        # electrons on the right means oxidized, electrons on the left mean reduced
    
    # just have to redo calance_eq and skeleton str
    def balanceEq(self):
        return self.coeffs
    
    def SkeletonEquation(self) -> list[list[compound]]:
        return self.skele_eq

# finish this code
class redox_reaction(reaction):
    def __init__(self, red : half_reaction, ox : half_reaction):
        pass

boxSize = 9

def covalentBondsD(cmpd : compound):
    el = cmpd.equation[0:-1]
    if el == "N": 
        b = 3
        bond = "≡" * boxSize
    elif el == "O": 
        bond = "=" * boxSize
        b = 2
    else: 
        bond = "―" * boxSize
        b = 1
    
    return [[[el, 8 - 2 * b], bond, [el, 8 - 2 * b]]]

def covalentBondsBM(cmpd : compound, charge = 0):
    cmpdList = cmpd.compound
    ones = []
    for i in cmpdList:
        if i[1] == 1: ones.append(i)

    center = min(ones, key = lambda i : ENDict.get(i[0]))

    els = []

    for i in cmpdList:
        for _ in range(i[1]):
            els.append(i[0])

    matrix = [[None for _ in range(0,5)] for _ in range(0,5)]
    if center[0] != "H": matrix[2][2] = [center[0], 8 - 2 * len(els) + 2]
    else: matrix[2][2] = ['H', 0]

    curr = 0
    pattern = [(0,2), (4,2), (2,0), (2,4), (4,0), (0,4), (0,0), (4,4)]
    lines = ["―" * boxSize, "|", "⟍", "⟋"]
    bonds = []
    for i in els:
        if i == center[0]: continue
        x, y = pattern[curr]
        if i == "H": matrix[y][x] = ['H', 0]
        else: matrix[y][x] = [i, 6]

        x = (x+2)//2
        y = (y+2)//2
        index = int(curr > 1)
        if curr > 3: index = 2 + int(curr <= 5)
        matrix[y][x] = f"{lines[index % 4]}"
        bonds.append((x,y))
        curr += 1

    totalValance = -charge
    for el in cmpdList:
        totalValance += int(findElement(el[0])[3][0]) * el[1]

    if totalValance % 2 == 1: raise Exception("The total valence must be even!")

    eLeft = totalValance - 2 * (len(els) -1)

    eUsed = 0
    for line in matrix:
        for i in line:
            if type(i) == list: eUsed += i[1]

    eExcess = eUsed - eLeft
    if cmpd.equation[0] == "B" and cmpd.equation[0:2] != "Br" and cmpdList[0][1] == 1:
        otherEls = cmpdList[1:]
        total = 0
        c = False
        for i in otherEls:
            total += i[1]
            if i[0] not in ["F", "Cl", "Br", "I"]: c = True
        
        if not c and total == 3:
            matrix[2][2][1] = 0
            return matrix
    
    if eExcess > 0:
        bondsNeeded = eExcess // 2
        doubleBonds = []
        needTriple = False
        i = 0
        while bondsNeeded > 0:
            if i < 2:
                try:
                    currBond = bonds[0]
                    i += 1
                except:
                    needTriple = True
                    break
            else: 
                currBond = random.choice(bonds)
            doubleBonds.append(currBond)
            bonds.remove(currBond)
            x, y = currBond
            matrix[y][x] = make_double_bond(matrix[y][x])

            bondsNeeded -= 1
            if bonds == []: 
                needTriple = True
                break

        if needTriple:
            while bondsNeeded > 0:
                currBond = random.choice(doubleBonds)
                doubleBonds.remove(currBond)
                x, y = currBond
                matrix[y][x] = make_triple_bond(matrix[y][x])
                bondsNeeded -= 1
    
    if eExcess < 0:
        matrix[2][2][1] -= eExcess

    #if charge != 0: matrix[0].append(-charge)
    matrix[2][2][1] = abs(matrix[2][2][1])
    return matrix    

def covalentBondsHC(cmpd : compound):
    # these two compounds break the code, so I have to deal with them separately
    if cmpd.equation == "C2H2": return [[None for i in range(0,7)],[None for i in range(0,7)],[["H", 0], "―" * boxSize, ["C", 0], "≡" * boxSize, ["C",0], "―" * boxSize, ["H",0]],[None for i in range(0,7)],[None for i in range(0,7)]]
    if cmpd.equation == "C2H4": return [[None, None, ["H",0], None, ["H", 0], None, None],[None, None, "|", None, "|", None, None],[["H", 0], "―" * boxSize, ["C", 0], "=" * boxSize, ["C",0], "―" * boxSize, ["H",0]],[None for i in range(0,7)],[None for i in range(0,7)]]

    cmpdList = cmpd.compound
    if cmpd.uniqueEls() == set(["H", "C"]): # not hydrocarbon derivative
        Cn = cmpdList[0][1]
        Hn = cmpdList[1][1]
        if Cn * 2 + 2 == Hn:
            t = "alkane"
        elif Cn * 2 == Hn:
            t = "alkene"
        elif Cn * 2 - 2 == Hn:
            t = "alkyne"
        else:
            raise Exception("You must input a valid hydrocarbon (alkane, alkene, alkyne)!")
        
        matrix = [[None for i in range(0, Hn + 1)] for j in range(0,5)]
        matrix[0] = [None if i % 2 == 1 or i == 0 or i == Hn else ["H", 0] for i in range(0,Hn + 1)]
        matrix[1] = [None if i % 2 == 1 or i == 0 or i == Hn else "|" for i in range(0,Hn + 1)]
        matrix[2] = ["―" * boxSize if i % 2 == 1  else ["C", 0] for i in range(0,Hn + 1)]
        matrix[3] = matrix[1].copy()
        matrix[4] = matrix[0].copy()
        matrix[2][0] = ["H", 0]
        matrix[2][Hn] = ["H", 0]
        if t == "alkane": return matrix

        for i in range(5):
            matrix[i].append(matrix[i][Hn-1])
            matrix[i].append(matrix[i][Hn])
            matrix[i][Hn] = matrix[i][Hn-2]

        horizontal_bonds = [2*i+3 for i in range(Cn-2)]
        bond = random.choice(horizontal_bonds)
        x, y = bond, 2
        matrix[y][x] = make_double_bond(matrix[y][x])
        matrix[1][x-1] = None
        matrix[1][x+1] = None
        matrix[0][x-1] = None
        matrix[0][x+1] = None

        if t == "alkene": return matrix
        for i in range(5):
            matrix[i].append(matrix[i][Hn+1])
            matrix[i].append(matrix[i][Hn+2])
            if type(matrix[i][Hn]) in [list]: matrix[i][Hn+2] = matrix[i][Hn].copy()
            else: matrix[i][Hn+2] = matrix[i][Hn]

        matrix[0][Hn+2] = ["H",0]
        matrix[1][Hn+2] = "|"

        matrix[y][x] = make_triple_bond(matrix[y][x])
        matrix[3][x-1] = None
        matrix[3][x+1] = None
        matrix[4][x-1] = None
        matrix[4][x+1] = None

        return matrix
    elif cmpd.uniqueEls() == set(["H", "C", "O"]):
        parts = -1
        for i in ["COO", "CO"]:
            if i in cmpd.equation:
                parts = cmpd.equation.split(i)
                parts.insert(1, create_parts(i))
                break
        if parts == -1: raise Exception(f"Enter a valid hydrocarbon derivative. cmpd: {cmpd.equation}")

        for i in [0,2]:
            try: Cn = int(parts[i][1])
            except: Cn = 1
            parts[i] = create_parts(Cn, i // 2)

        return combine_bond_matricies(parts[0], parts[1], parts[2])
    else:
        uniqueEls = cmpd.uniqueEls()
        if "C" in uniqueEls and "H" in uniqueEls:
            otherCmpds = [i for i in cmpdList if i[0] not in ["C", "H"]]
            for i in otherCmpds:
                if i[0] not in ["F", "Cl", "Br", "I"]: raise Exception(f"Enter a valid hydrocarbon derivative. cmpd: {cmpd.equation}")
        else: raise Exception(f"Enter a valid hydrocarbon derivative. cmpd: {cmpd.equation}")

        otherTotal = 0
        for i in otherCmpds:
            otherTotal += i[1]

        for i in cmpdList:
            if i[0] == "C": c = i[1]
            if i[0] == "H": h = i[1] + otherTotal
        
        matrix = covalentBondsHC(compound(f"C{c}H{h}"))
        for i in range(len(matrix)):
            line = matrix[i]
            for j in range(len(line)):
                curr = line[j]
                if curr == None or type(curr) == str: continue
                matrix[i][j] = matrix[i][j].copy()
        hPos = []
        for y in range(len(matrix)):
            row = matrix[y]
            for x in range(len(row)):
                curr = row[x]
                if curr == ["H", 0]: hPos.append((x, y))

        replacementsNeeded = 0
        replacements = []
        for i in otherCmpds:
            for _ in range(i[1]):
                replacements.append(i[0])
            replacementsNeeded += i[1]

        while replacementsNeeded:
            h = random.choice(hPos)
            hPos.remove(h)
            x, y = h
            matrix[y][x][0] = replacements[0]
            replacements.pop(0)
            replacementsNeeded -= 1

        return matrix

def covalentBondsA(cmpd : compound):
    eq = cmpd.equation
    if eq == "HC2H3O2": return ["acetate", "temp"]
    if eq == "HC7H5O2": return ["benzoate","temp"]
    if eq == "HN3": return ["azide", "temp"]
    if eq == "H2C4H4O6": return ["tartrate", "temp"]
    if eq == "H2C2O4": return ["oxalate","temp"]
    if eq == "HCN": return ["cyanate", "temp"]
    if eq == "H2O2": return ["peroxide", "temp"]
    if eq == "H2S2O3": return ["thiocynanate", "temp"]

    for i in ["NH4", "BO", "Cr", "OH", "Mn", "SiF6", "P", "As", "Si"]:
        if i in eq: return ["bad acid"] 

    if len(cmpd.compound) == 2: return ["bad acid"]

    ion = eq[int(eq[1].isdigit()) + 1:]
    charge = polyatomicCharge(ion)

    right = [[None, None], [None, None], [["H", 0], "―" * boxSize], [None, None], [None, None]]
    left = [[None, None], [None, None], [None, None], [None, None], [None, None]]
    if charge > 1: 
        left = [[None, None], [None, None], ["―" * boxSize, ["H", 0]], [None, None], [None, None]]        

    middle = covalentBondsBM(compound(ion), -charge)

    if middle[2][0] == None:
        middle = [[l[2], l[3], l[4]] for l in middle]
    if middle[2][2] == None:
        middle = [[l[0]] for l in middle]

    return combine_bond_matricies(right, middle, left)

def make_double_bond(string):
    if "|" in string: return f"{'||': ^9}"
    if "―" in string: return "=" * boxSize
    if "⟋" in string: return f"{'⟋⟋': ^9}"
    if "⟍" in string: return f"{'⟍⟍': ^9}"

def make_triple_bond(string):
    if "|" in string: return f"{'|||': ^9}"
    if "=" in string: return "≡" * boxSize
    if "⟋⟋" in string: return f"{'⟋⟋⟋': ^9}"
    if "⟍⟍" in string: return f"{'⟍⟍⟍': ^9}"

def print_matrix(l : list):
    s = ""
    for line in l: s += "".join([" " * boxSize if i == None else f"{str(i): ^9}" for i in line]) + "\n"
    return s

def create_parts(Cn, d = 0):
    if Cn == "CO": return [ [None, ["O", 4], None], [None,  "||", None], ["―" * boxSize, ["C", 0], "―" * boxSize], [None,  None, None], [None, None, None] ]
    if Cn == "COO": return [ [None, ["O", 4], None, None, None], [None,  "||", None, None, None], ["―" * boxSize, ["C", 0], "―" * boxSize, ["O", 4], "―" * boxSize], [None, None, None, None, None], [None, None, None, None, None] ]
    try: Cn = int(Cn)
    except: raise Exception("enter an int! (or 'COO' or 'CO')")

    # d = 0 means H is on the left, d = 1 means H is on the right
    if d not in [0,1]: raise Exception("Enter a valid direction!")
    Hn = 2 * Cn + 1
    matrix = [[None for i in range(Hn)] for j in range(5)]
    matrix[0] = [["H", 0] if i % 2 == 0 and i != (Hn -1) * d else None for i in range(Hn)]
    matrix[1] = ["|" if i % 2 == 0 and i != (Hn -1) * d else None for i in range(Hn)]
    matrix[2] = [["C", 0] if i % 2 == 0 and i != (Hn -1) * d else "―" * boxSize for i in range(Hn)]
    matrix[2][(Hn-d) % Hn] = ["H", 0]
    matrix[3] = matrix[1].copy()
    matrix[4] = matrix[0].copy()
    return matrix

def combine_bond_matricies(m1, m2, m3):
    matrix = [None for i in range(5)]
    for i in range(5):
        m = m1[i].copy()
        m.extend(m2[i])
        m.extend(m3[i])
        matrix[i] = m

    return matrix

def randBMForBonds():
    while True:
        el1 = randElement("b")[2]
        while (el2 := randElement("b")[2]) == el1: pass
        
        c = random.randint(1,5)
        if c == 1: c = ""
        eq = f"{el1}{el2}{c}"
        try: compound(eq).bondEnergy()
        except: continue
        
        return eq

def randCmpdForBonds(dChance = 0, hChance = 0, aChance = 0, bmChance = 0):
    chances = [dChance, hChance, aChance, bmChance]
    if (all([not i for i in chances])): chances = [1,1,1,1]

    letters = ["d", "h", "a", "b"]
    choices = []
    for i, letter in zip(chances, letters):
        for _ in range(i): choices.append(letter)

    choice = random.choice(choices)

    if choice == "d": return getRandomCompound(0,0,0,1,0)
    if choice == "h": return getRandomCompound(0,0,0,0,1)
    if choice == "a": 
        while True:
            c = getRandomCompound(0,1,0,0,0)
            cmpd = compound(c)
            eq = cmpd.equation
            cont = False
            for i in ["NH4", "BO", "Cr", "OH", "Mn", "SiF6", "P", "As", "Si", "Br", "CN", "S2O3"]:
                if i in eq: 
                    cont = True
                    break
            if cont: continue 

            if len(cmpd.compound) == 2: continue

            if cmpd.isHydroCarbon(): continue

            return c
    if choice == "b": 
        eq = randBMForBonds()
        cmpd = compound(eq)
        cmpd.refresh()
        return [cmpd.name, cmpd.equation, "binary molecular"]

    raise Exception("Error determining compound")

def getIMF(cmpd1 : compound, cmpd2 : compound):
    polarity1 = cmpd1.isPolar()
    polarity2 = cmpd2.isPolar()

    if not polarity1 or not polarity2: 
        return ["LD"]

    r = ["LD", "Dipole Dipole"]

    hydrogenBondEls = ["N", "O", "F"]
    if "H" in cmpd1.equation:
        for el in hydrogenBondEls:
            if cmpd2.hasEl(el): r = ["LD", "Hydrogen Bonds"]
    
    if "H" in cmpd2.equation:
        for el in hydrogenBondEls:
            if cmpd1.hasEl(el): r = ["LD", "Hydrogen Bonds"]

    if r == ["LD", "Hydrogen Bonds"] and cmpd1.isHydroCarbon() and cmpd2.isHydroCarbon() and int(cmpd1.getNumEl("C")) >= 8 and int(cmpd2.getNumEl("C")) >= 8:
        return ["Hydrogen Bonds", "LD"]

    return r

def getCounterpartLoop(eq : str):
    i3 = False
    if "I3" in eq: 
        i3 = True
        eq = "I3"
    # list is in form [num of el1 * 10 + valence of el1,...]
    sToL = {"CO2" : [14, 22], "SO2" : [32], "H2O" : [21, 12], "I3" : [31], "SO3" : [42], "NH3" : [13, 31], "ClF3" : [41],
            "CCl4" : [14, 41], "SF4" : [12, 41], "XeF4" : [10, 41], "PCl5" : [13,51], "ClF5" : [61], "SF6" : [12, 61]}
    
    numDicts = {1 : ["H", "F", "Cl", "Br", "I"], 2 : ["O", "S", "Se"], 3 : ["N", "P"], 4 : ["C"], 0 : ["Ar", "Kr", "Xe", "Rn"]}
    l = sToL.get(eq)
    if not eq: raise Exception("only input compounds from the vsepr table!")
    newCmpdList = {}
    for i in l:
        els = numDicts.get(i % 10)
        for _ in range(i // 10):
            if len(set(newCmpdList) & set(els)) == 0 or not bool(random.randint(0,2)): curr = random.choice(els)
            else: curr = random.choice(list(set(newCmpdList) & set(els)))
            if curr in newCmpdList: newCmpdList[curr] += 1
            else: newCmpdList[curr] = 1
    
    newCmpdStr = ""
    for el in list(newCmpdList): newCmpdStr += el + str(newCmpdList.get(el)) * int(newCmpdList.get(el) != 1)

    if i3: newCmpdStr += "-"
    return [newCmpdStr, newCmpdList]

def getCounterpart(eq : str):
    while True:
        counterpart = getCounterpartLoop(eq)
        ones = [counterpart[1][i] == 1 for i in list(counterpart[1])]
        if len(counterpart[1]) != 1 and ones.count(True) == 1: break
    return counterpart[0]

counterpart_starters = ["CO2", "SO2", "H2O", "I3", "SO3", "NH3", "ClF3", "CCl4", "SF4", "XeF4", "PCl5", "ClF5", "SF6"]

# counterpart stuff is WIP

