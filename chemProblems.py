import random, sys, io
from chemFuncts import *
from chemData import *
from copy import deepcopy

def one(**kwargs):
    powers = [(unit, random.randint(-2,3)) for unit in units]
    for i in powers:
        if i[1] == 0: powers.remove(i)
    start = [random.choice(list(prefixNumbers.keys())) for _ in powers]
    end = [random.choice(list(prefixNumbers.keys())) for _ in powers]

    startStr = ""
    startNum = 0
    for s, power in zip(start, powers):
        unit, p = power
        startNum += p * s
        startStr += prefixNumbers.get(s) + unit + "^" + str(p) + " "

    endStr = ""
    endNum = 0
    for e, power in zip(end, powers):
        unit, p = power
        endNum += p * e
        endStr += prefixNumbers.get(e) + unit + "^" + str(p) + " "

    print("Start: " + startStr)
    print("End: " + endStr)
    print("You have to multiply the start by 10^x, to get to the final unit. What is x?")

    finalFactor = startNum - endNum
    return finalFactor

def two(**kwargs):
    indexAverageMass = random.randint(0,100) +  random.random()
    isotopeList = []
    
    for i in range(0,5):
        newIsotope = round(indexAverageMass - i + ( random.random() / 50 ), 3)

        isotopeList.append(newIsotope)

    relativeAdundanceList = []
    for i in range(0,5):
        newRelativeAdundance = random.randint(0,100)
        relativeAdundanceList.append(newRelativeAdundance)
    s=0
    for i in relativeAdundanceList:
        s = s + i
    newRelativeAdundanceList = []
    for i in relativeAdundanceList:
        i = round(100* i / s, 2)
        newRelativeAdundanceList.append(i)

    for i in newRelativeAdundanceList:
        s = s + i
    
    if s != 100:
        sum = 0
        for i in newRelativeAdundanceList:
            sum = sum + i
        newRelativeAdundanceDifference = 100 - sum + newRelativeAdundanceList[4]
        newRelativeAdundanceList[4] = round(newRelativeAdundanceDifference, 2)
    
    print("Isotopes: \n\n   Mass     Abdundance")
    totalMass = 0
    for i, isotope in enumerate(isotopeList):
        print(str(i+1) + ". " + str(isotope) + "    " + str(newRelativeAdundanceList[i]))
        totalMass = totalMass + round(isotope * newRelativeAdundanceList[i], 2)
    averageMass = round(totalMass / 100, 2)
    print("\nWhat is the average atomic mass of this element?")

    return averageMass

def three(**kwargs):
    percentageOne = round(100*random.random(),0)
    percentageTwo = 100 - percentageOne
    massOne = round(100*random.random(), 2)
    massTwo = round(massOne + 2 * (0.5 - random.randint(0,1)) + .5 * random.random(), 2)
    averageMass =  round((massOne * percentageOne +  massTwo * percentageTwo) / 100, 2)
    print("Find the relative abundance of isotope A, which is " + str(massOne) + " amu, when the mass of isotope B is " + str(massTwo) + " amu, and the average atomic mass is " + str(averageMass))
    
    return percentageOne

def four(**kwargs):
    myCompound = compound(getRandomCompound(chanceList[0], chanceList[1], chanceList[2], chanceList[3],chanceList[4]))
    name = myCompound.getName()
    if "/ " in name:
        name = name.split("/",1)[1]
    print("What is the equation for " + name)

    return myCompound.equation

def five(**kwargs):
    myCompound = compound(getRandomCompound(chanceList[0], chanceList[1], chanceList[2], chanceList[3],chanceList[4]))
    print("What is the name of " + myCompound.equation)

    return myCompound.name

def six(**kwargs):
    myCompound = compound(getRandomCompound(chanceList[0], chanceList[1], chanceList[2], chanceList[3],chanceList[4]))
    name = myCompound.getName()
    if "/ " in name:
        name = name.split("/ ",1)[1]
    startList = [" moles of ", " L of " , " particles of ", " atoms of ", " grams of " ]
    endList = ["How many moles are in ", "What is the volume of ", "How many particles are in ", "How many atoms are in ", "What is the mass of "]
    moles = .25 * random.randint(1,40)
    resultsList = [moles, moles * 22.4, moles * 6.02e+23, myCompound.getAtoms(moles), myCompound.getMass(moles)]
    start = 1
    end = 1
    while start == end:
        start = random.randint(0,4)
        end = random.randint(0,4)

    print(endList[end] + str(resultsList[start]) + startList[start] + name)

    return str(resultsList[end]) + " " + startList[end].split(" ", 2)[1]

def seven(**kwargs):
    myCompound = compound(getRandomCompound(chanceList[0], chanceList[1], chanceList[2], 0,chanceList[4]))
    compList = myCompound.percentComposition()
    print("What is the percent composition of " + myCompound.getName())
    ans = ""
    for i in compList:
        ans += "\n" + i[0] + ": " + str(i[1])

    return ans

def eight(**kwargs):
    myCompound = compound(getRandomCompound(chanceList[0], chanceList[1], chanceList[2], chanceList[3],chanceList[4]))
    compList = myCompound.percentComposition()
    mult = random.randint(1,4)
    print("What is molecular formula for a compound with a molar mass of " +str(mult*myCompound.getMolarMass()) + ", if the percent composition of the compound is: ")
    percentComp = ""
    for i in compList:
        percentComp += "\n" + i[0] + ": " + str(i[1])
    print(percentComp)
    myCompound.multCompound(mult)

    return myCompound.getEq()

def nine(**kwargs):
    myCompound = compound(getRandomCompound(chanceList[0], chanceList[1], chanceList[2], chanceList[3],chanceList[4]))
    mass = myCompound.getMass(.25 * random.randint(1,8))
    elNum = random.randint(0,len(myCompound.compound)-1)
    el = myCompound.compound[elNum][0]
    elMass = mass * myCompound.percentComposition()[elNum][1] / 100
    print("What is the the mass of " + el + " in " + str(mass) + " g of " + myCompound.getName())

    return elMass

def ten(**kwargs):
    myCompound = compound(getRandomCompound(chanceList[0], chanceList[1], chanceList[2], chanceList[3],chanceList[4]))
    compList = myCompound.percentComposition()
    mult = random.randint(1,4)
    unit = "g"
    while unit == "g":
        value, unit, moles = randUnit(myCompound, mult)
    
    print("How many " + unit + " are/is there in " +str(mult*myCompound.getMolarMass()) + " g of this compound, if the percent composition of the compound is: ")
    percentComp = ""
    for i in compList:
        percentComp += "\n" + i[0] + ": " + str(round(i[1], 2)) + "%"
    print(percentComp)

    return str(value) + " " + unit

def eleven(**kwargs):
    repeat = True
    while repeat or (cmpd.isSoluable() == "inconclusive"):
        repeat = False
        cmpd = compound(getRandomCompound(5,0,1,0,0))
        while type(cmpd.isSoluable()) != bool:
            cmpd = compound(getRandomCompound(5,0,1,0,0))
    print(f"Is {cmpd.equation} soluable?")
    if cmpd.isSoluable(): ans = "yes"
    else: ans = "no"

    return ans

def twelve(rxType, **kwargs):
    rx = reaction(randomRx(rxType))
    reactants = rx.SkeletonEquation()[0]
    printStr = ["Combine ", "Decompose ", "Combust ", "Completely Combust ", "Incompletley Combust ", "Write the reaction between "]
    if rx.typeRx in ["s1", "s2", "s3"]: printStr = printStr[0]
    elif rx.typeRx in ["d1", "d2", "d3"]: printStr = printStr[1]
    elif rx.typeRx == "c": printStr = printStr[2]
    elif rx.typeRx == "complete combustion": printStr = printStr[3]
    elif rx.typeRx == "incomplete combustion": printStr = printStr[4]
    else: printStr = printStr[5]
    for reactant in reactants:
        reactantName = reactant.getNameFromEq()
        coeffientList = rx.balanceEq()
        if reactantName == "nitric acid":
            if coeffientList in [[3,8,3,2,4], [8,3,3,2,4]]:
                reactantName = "dilute nitric acid"
            elif coeffientList in [[4,1,1,2,2], [1,4,1,2,2]]:
                reactantName = "concentrated nitric acid"
        printStr += reactantName + " and "
    printStr = printStr[0:-5]
    
    print(printStr + ". What is the sum of the coefficients")
    coeffients = rx.balanceEq()
    sum = 0
    for i in coeffients:
        sum += i
    if "NR" in str(rx) and rx.typeRx in ["sr1", "sr2"]: sum = "n/a"

    return (str(rx) + "\nThe sum of the coefficients is " + str(sum))

def thirteen(rxType, **kwargs):
    rx = reaction(randomRx(rxType))
    separatedCmpds = rx.formatRxList()
    cmpds = separatedCmpds[0] + separatedCmpds[1]
    startCmpd = random.choice(cmpds)
    products = rx.SkeletonEquation()[1]
    reactants = rx.SkeletonEquation()[0]
    printStr = ["Combine ", "Decompose ", "Combust ", "Completely Combust ", "Incompletley Combust ", "Write the reaction between "]
    if rx.typeRx in ["s1", "s2", "s3"]: printStr = printStr[0]
    elif rx.typeRx in ["d1", "d2", "d3"]: printStr = printStr[1]
    elif rx.typeRx == "c": printStr = printStr[2]
    elif rx.typeRx == "complete combustion": printStr = printStr[3]
    elif rx.typeRx == "incomplete combustion": printStr = printStr[4]
    else: printStr = printStr[5]
    for reactant in reactants:
        reactantName = reactant.getNameFromEq()
        coeffientList = rx.balanceEq()
        if reactantName == "nitric acid":
            if coeffientList in [[3,8,3,2,4], [8,3,3,2,4]]:
                reactantName = "dilute nitric acid"
            elif coeffientList in [[4,1,1,2,2], [1,4,1,2,2]]:
                reactantName = "concentrated nitric acid"
        printStr += reactantName + " and "
    question = printStr[0:-5] + ". "

    startList = [" moles of ", " L of " , " particles of ", " atoms of ", " grams of " ]
    startMoles = .25 * random.randint(1,40)
    resultsList = [startMoles, startMoles * 22.4, startMoles * 6.02e+23, startCmpd[0].getAtoms(startMoles), startCmpd[0].getMass(startMoles)]
    start = random.randint(0,4)

    question += "There are " + str(resultsList[start]) + startList[start] + startCmpd[0].getNameFromEq() + "."

    finalCmpd = random.choice(cmpds)
    while finalCmpd[0] == startCmpd[0]: finalCmpd = random.choice(cmpds)
    finalCmpd[0].refresh()
    finalMoles = startMoles / startCmpd[1] * finalCmpd[1]
    endList = ["How many moles of ", "What is the volume of ", "How many particles of ", "How many atoms of ", "What is the mass of "]
    if finalCmpd in separatedCmpds[0]: end2List = [" are needed for ", " in ", " are needed for ", " are needed for ", " in "]
    else: end2List = [" are created in ", " in ", " are created in ", " are created in ", " in "]
    resultsList = [finalMoles, finalMoles * 22.4, finalMoles * 6.02e+23, finalCmpd[0].getAtoms(finalMoles), finalCmpd[0].getMass(finalMoles)]
    end = random.randint(0,4)
    print(question + " " + endList[end] + str(finalCmpd[0].getNameFromEq()) + end2List[end] + "this reaction?")

    return str(resultsList[end]) + startList[end] + finalCmpd[0].equation

def fourteen(rxType, **kwargs):
    rx = reaction(randomRx(rxType))
    separatedCmpds = rx.formatRxList()
    cmpds = separatedCmpds[0] + separatedCmpds[1]
    startCmpd = random.choice(separatedCmpds[0])
    reactants = rx.SkeletonEquation()[0]

    printStr = ["Combine ", "Decompose ", "Combust ", "Completely Combust ", "Incompletley Combust ", "Write the reaction between "]
    if rx.typeRx in ["s1", "s2", "s3"]: printStr = printStr[0]
    elif rx.typeRx in ["d1", "d2", "d3"]: printStr = printStr[1]
    elif rx.typeRx == "c": printStr = printStr[2]
    elif rx.typeRx == "complete combustion": printStr = printStr[3]
    elif rx.typeRx == "incomplete combustion": printStr = printStr[4]
    else: printStr = printStr[5]
    for j, i in enumerate(reactants):
        if len(separatedCmpds) == 3 and  j == 1: printStr += separatedCmpds[2] + " "
        printStr += i.getNameFromEq()
        printStr += " and "

    question = printStr[0:-5] + ". "

    startList = [" moles of ", " L of " , " particles of ", " atoms of ", " grams of " ]
    startMoles = .25 * random.randint(1,40)
    resultsList = [startMoles, startMoles * 22.4, startMoles * 6.02e+23, startCmpd[0].getAtoms(startMoles), startCmpd[0].getMass(startMoles)]
    start = random.randint(0,4)

    question += "There are " + str(resultsList[start]) + startList[start] + startCmpd[0].getNameFromEq() + "."
    percentYeild = round(random.random(), 4)

    finalCmpd = random.choice(cmpds)
    while finalCmpd == startCmpd and not (finalCmpd in separatedCmpds[1] and startCmpd in separatedCmpds[1]): 
        finalCmpd = random.choice(cmpds)
    finalCmpd[0].refresh()
    finalMoles = startMoles / startCmpd[1] * finalCmpd[1]
    percentYeildOrActualYield = random.randint(0,1)
    percentYeildBool = False
    if finalCmpd in separatedCmpds[1]:
        percentYeildBool = True
        reactantCmpd = 0
    elif startCmpd in separatedCmpds[1]:
        percentYeildBool = True
        reactantCmpd = 1

    resultsList = [finalMoles, finalMoles * 22.4, finalMoles * 6.02e+23, finalCmpd[0].getAtoms(finalMoles), finalCmpd[0].getMass(finalMoles)]
    conversions = ["moles", "L", "particles", "atoms", "g"]
    end = random.randint(0,4)

    if not percentYeildBool:
        trueFactor = round(.5 * random.random()+.75,4)
        trueFinalMoles = finalMoles * trueFactor
        trueResultsList = [trueFinalMoles, trueFinalMoles * 22.4, trueFinalMoles * 6.02e+23, finalCmpd[0].getAtoms(trueFinalMoles), finalCmpd[0].getMass(trueFinalMoles)]
        trueEnd = random.randint(0,4)
        try: lastCmpd = random.choice(separatedCmpds[1])
        except IndexError: print(f"Error: invalid products list: {separatedCmpds[1]}")
        if trueFinalMoles * startCmpd[1] > startMoles * finalCmpd[1]:
            limitingReagent = startCmpd[0].getNameFromEq()
            lastMoles = startMoles / startCmpd[1] * lastCmpd[1]
        else:
            limitingReagent = finalCmpd[0].getNameFromEq()
            lastMoles = trueFinalMoles / finalCmpd[1] * lastCmpd[1]
        lastResultsList = [lastMoles, lastMoles * 22.4, lastMoles * 6.02e+23, lastCmpd[0].getAtoms(lastMoles), lastCmpd[0].getMass(lastMoles)]
        lastEnd = random.randint(0,4)
        
        print(f"{question} There are {trueResultsList[trueEnd]} {conversions[trueEnd]} of {finalCmpd[0].getNameFromEq()}. What is the limiting reageant, and how much {lastCmpd[0].getNameFromEq()} is there ({conversions[lastEnd]})?")
        if trueFactor > 1: 
            limitingReagent = startCmpd[0].equation
            
            percentYeild = 1 / trueFactor
        else: 
            limitingReagent = finalCmpd[0].equation
            percentYeild = trueFactor
        return f"Limiting reageant: {limitingReagent}. Theoretical Yeild: {round(lastResultsList[lastEnd],4)} {conversions[lastEnd]} of {lastCmpd[0].getNameFromEq()}."
    elif percentYeildOrActualYield == 0:
        print(question + " The percent yeild is " + str(round(100*percentYeild,4)) + "%. What is the acutal yeild (" + conversions[end] + ") of " + finalCmpd[0].getNameFromEq() + "?")
        return str(round(resultsList[end] * percentYeild,4)) + " " + conversions[end]
    else:
        print(question + " The actual yeild is " + str(round(resultsList[end] * percentYeild,4)) +  " " + conversions[end] + " of " + finalCmpd[0].getNameFromEq() + ". What is the percent yeild?")
        return str(round(100*percentYeild,4)) + "%"    

def fifteen(**kwargs):
    water = bool(random.getrandbits(1))
    water = False
    if water:
        cmpd = compound("H2O")
    else:
        cmpd = compound(random.choice(list(heatOfPhysicalChanges.keys())))
    cmpd.refresh()
    fp, bp, heatOfFusion, heatOfVaporization, sSpecificHeat, lSpecificHeat, gSpecificHeat = heatOfPhysicalChanges.get(cmpd.equation)
    startTemp = random.randint(-100, 150) # I allow for start temp to pick values bigger than 100 so that it weighted to the postive numbers
    try:
        if cmpd.equation == "H2O": 
            lowerBound = max(startTemp - 100, -273)
            upperBound = startTemp + 100
        elif cmpd.equation in ["CH3COCH3", "NH3", "C6H6", "C2H5OH", "CH3OH"]: 
            lowerBound = max(startTemp - 100, fp)
            upperBound = startTemp + 100
        else: 
            lowerBound = max(startTemp - 100, bp)
            upperBound = startTemp + 100
        finalTemp = random.randint(int(lowerBound), upperBound)
    except:
        raise Exception(f"Error with getting final temperature. \nstartTemp: {startTemp}\nlowerBound: {lowerBound}\nupperBound: {upperBound}\ncmpd: {cmpd.equation}")

    shString = "A"
    if cmpd.equation == "H2O": shString += "s a solid, the specific heat is " + str(sSpecificHeat) + ", and a"
    if cmpd.equation in ["H2O", "CH3COCH3", "NH3", "C6H6", "C2H5OH", "CH3OH"]: shString += "s a liquid, the specific heat is " + str(lSpecificHeat) + ", and a"
    shString += "s a gas, the specific heat is " + str(gSpecificHeat) + "."

    moles = .25 * random.randint(1,40)
    cmpd.setTemp(startTemp)
    heat = cmpd.raiseTemp(finalTemp, moles, fp, bp, heatOfFusion, heatOfVaporization, sSpecificHeat, lSpecificHeat, gSpecificHeat)
    if finalTemp > startTemp: 
        strVar1 = "heated"
        strVar2 = "must be supplied"
    else: 
        strVar1 = "cooled"
        strVar2 = "is released"
    
    choice = random.randint(0,4)
    units = ["moles", "L", "particles", "atoms", "g"]
    choices = [moles, moles * 22.4, moles * 6.02e+23, cmpd.getAtoms(moles), cmpd.getMass(moles)]
    print(f"If {choices[choice]} {units[choice]} of {cmpd.name} is {strVar1} from {startTemp} C to {finalTemp} C, how much heat {strVar2}? {shString}")
    return str(abs(heat)) + " kJ"

def sixteen(**kwargs):
    metals = list(specificHeats.keys())[5:]
    metals.remove("mercury")
    metal1 = random.choice(metals)
    metals.remove(metal1)
    m2Exists = random.getrandbits(1)
    metal2 = random.choice(metals)
    metals.remove(metal2)
    cExists = random.getrandbits(1)
    container = random.choice(metals)

    tempMetals = random.randint(50,150)
    m1Mass = random.randint(10,50)
    m2Mass = m2Exists * random.randint(10,50)
    m1SH = specificHeats.get(metal1)
    m2SH = m2Exists * specificHeats.get(metal2)

    tempWater = random.randint(20,40)
    wMass = random.randint(25,100)
    wSH = 4.18
    cMass = cExists * random.randint(100,1000)
    cSH = cExists * specificHeats.get(container)

    Cm = m1Mass * m1SH + m2Mass * m2SH
    Cw = wMass * wSH + cMass * cSH

    finalTemp = round((Cm * tempMetals + Cw * tempWater) / (Cm + Cw), 4)
    
    options = [f"The mass of {metal1} is {m1Mass} g", f"(c = {m1SH})", ". "]
    answers = [m1Mass, m1SH, -1]
    if m2Exists: 
        options.extend([f"The mass of {metal2} is {m2Mass} g", f"(c = {m2SH})", ". "])
        answers.extend([m2Mass, m2SH, -1])
    options.extend([f"The mass of water is {wMass} g", ". "])
    answers.extend([wMass, -1])
    if cExists: 
        options.extend([f"The mass of the {container} container is {cMass} g", f"(c = {cSH})", ". "])
        answers.extend([cMass, cSH, -1])

    options.extend([f"The initial temperature of the metal(s) is {tempMetals} C.", f"The intial temperature of the water is {tempWater} C.", f"The final temperature is {finalTemp} C."])
    answers.extend([tempMetals, tempWater, finalTemp])

    missing = -1
    while missing == -1:
        missingNum = random.randint(0,len(answers) -1)
        missing = answers[missingNum]
    if "(c = " in options[missingNum]:
        missingQ = "What is the specific heat of the " + options[missingNum-1].split(" ")[-4]
        options.pop(missingNum)
    elif "The mass of " in options[missingNum]:
        missingQ = "What is " + " ".join(options[missingNum].lower().split(" ")[:-3])
        options[missingNum] = "Some " + options[missingNum].lower().split(" ")[3] + " is added to the calorimeter"
    else: missingQ = "What is " + " ".join(options.pop(missingNum).lower().split(" ")[:-3])
    question = ""
    for i in options: question += i + " "
    question = question.replace(" .", ".")
    question = question.replace("..", ".")
    question = question.replace("  ", " ")
    print(question + missingQ  + "?")
    
    return missing

def seventeen(rxType, **kwargs):
    rx = reaction(randomRx(rxType))
    separatedCmpds = rx.formatRxList()
    reactants = separatedCmpds[0]
    numReactants = len(reactants) - 1
    products = separatedCmpds[1]

    printStr = ["Combine ", "Decompose ", "Combust ", "Completely Combust ", "Incompletley Combust ", "Write the reaction between "]
    if rx.typeRx in ["s1", "s2", "s3"]: printStr = printStr[0]
    elif rx.typeRx in ["d1", "d2", "d3"]: printStr = printStr[1]
    elif rx.typeRx == "c": printStr = printStr[2]
    elif rx.typeRx == "complete combustion": printStr = printStr[3]
    elif rx.typeRx == "incomplete combustion": printStr = printStr[4]
    else: printStr = printStr[5]

    heatList = []
    indexList = [] # will include the indecies of the "special" compounds
    index = 0
    for reactant in reactants:
        reactant = findHeatOfFormation(reactant[0].equation) # [cmpd name, heatOfFormation, type]
        heatList.append(reactant)
        if reactant[2] == "special":
            indexList.append(index)
        index += 1
    for product in products:
        product = findHeatOfFormation(product[0].equation)
        product[1] = -1 * product[1]
        heatList.append(product)
        if product[2] == "special":
            indexList.append(index)
        index += 1
    
    mole = random.randint(1,40) / 40
    cmpds = reactants + products
    factorList = [mole * random.randint(1,5) / random.randint(1,5) for i in reactants]
    limitingMoles = min(factorList)
    for i in products:
        factorList.append(limitingMoles)
    moles = []
    coefficients = []
    for i, cmpd in enumerate(cmpds):
        moles.append(factorList[i] * cmpd[1])
        coefficients.append(cmpd[1])

    # print reactants
    for i, reactant in enumerate(reactants):
        reactant = reactant[0]
        if i in indexList:
            reactant = heatList[i][0]
            printStr += reactant + " and "
            indexList.pop(0)
        else:
            reactantName = reactant.getNameFromEq()
            if reactantName == "nitric acid":
                coeffientList = [i[1] for i in reactants + products]
                if coeffientList in [[3,8,3,2,4], [8,3,3,2,4]]:
                    reactantName = "dilute nitric acid"
                elif coeffientList in [[4,1,1,2,2], [1,4,1,2,2]]:
                    reactantName = "concentrated nitric acid"
            printStr += reactantName + " and "
    printStr = printStr[0:-5] + ". "

    if indexList != []:
        for i in indexList:
            newCmpd = heatList[i][0]
            printStr += f"{newCmpd} is formed. "

    for i, cmpd in enumerate(reactants):
        name = heatList[i][0]
        if "(g" not in name and "(l" not in name and "," not in name and "(s" not in name:
            name = compound(name).getNameFromEq()
        amount = randUnit(cmpd[0], moles[i]) # returns [value, unit] 
        amount = str(amount[0]) + " " + amount[1]
        printStr += f"There is {amount} of {name}. "
    
    for cmpd in heatList:
        validHeat = True
        if cmpd[2] in ["small", "special"] or int(cmpd[1]) == 0:
            validHeat = False
        if validHeat:
            name = cmpd[0]
            name = compound(name).getNameFromEq()
            heatOfCurrentCmpd = cmpd[1]
            if cmpd in products: heatOfCurrentCmpd *= -1
            printStr += f"The heat of formation of {name} is {heatOfCurrentCmpd} kJ. "

    heatOfReaction = 0
    for i, cmpd in enumerate(heatList):
        heatOfReaction += cmpd[1] * limitingMoles * coefficients[i]
    heatOfReaction *= 1000

    # instead of just water, use water, benzene, acetone, ethanol and methanol
    liquid = compound(random.choice(list(heatOfPhysicalChangesLiquid.keys())))
    fp, bp, heatOfFusion, heatOfVaporization, sSpecificHeat, lSpecificHeat, gSpecificHeat = heatOfPhysicalChangesLiquid.get(liquid.equation)
    massLiquid = random.randint(1000,2500)
    initialTempWater = random.randint(20,40)
    liquid.setTemp(initialTempWater)
    finalTemp = liquid.heat(heatOfReaction, massLiquid / liquid.getMass(), fp, bp, heatOfFusion, heatOfVaporization, sSpecificHeat, lSpecificHeat, gSpecificHeat)
    liquidEqs = {"CH3COCH3" : "Acetone", "C6H6":  "Benzene", "C2H5OH" :  "Ethanol", "CH3OH"  : "Methanol", "H2O" :  "Water", "C8H18" : "Oil (C8H18)"}
    density = liquidDensitys.get(liquidEqs.get(liquid.equation))
    printStr += f"The density of {liquidEqs.get(liquid.equation).lower()} is {density} g/mL. "
    goodOptions = [f"{massLiquid / density} mL of ", f" at {initialTempWater} C", f" The final temperature is {finalTemp} C."]
    options = [massLiquid, initialTempWater, finalTemp]
    questions = [" What is the mass of the liquid?", " What is the initial temperature of the liquid?", " What is the final temperature of the liquid?"]
    choice = random.randint(0,2)
    unit = [" g", " C", " C"][choice]
    goodOptions[choice] = ""
    printStr += f"They are combined in a bomb calorimeter with {goodOptions[0]}{liquidEqs.get(liquid.equation).lower()}{goodOptions[1]}.{goodOptions[2]}"
    printStr += questions[choice]
    if finalTemp in [0, 100]: 
        printStr += " (give the range of values; the given answer should be in that range)"

    print(printStr)
    print("\n")
    
    return str(options[choice]) + unit

def eighteen(**kwargs):
    temp = randTemp()
    KE = round(1.5 * RkPa * temp[2] / 1000, 4)

    if (bool(random.getrandbits(1))):
        print(f"What is the average kinetic energy of a gas at {temp[0]} {temp[1]}?")
        return KE
    else:
        print(f"What is the temperature of a gas with an average kinetic energy of {KE} kJ/mol, in {temp[1]}?")
        return f"{temp[0]} {temp[1]}"

def nineteen(**kwargs):
    cmpd1 = compound(getRandomCompound(0,1,1,1,0))
    cmpd2 = compound(getRandomCompound(0,1,1,1,0))

    mass1 = cmpd1.getMass()
    mass2 = cmpd2.getMass()

    if mass1 > mass2:
        bigger = cmpd1
        smaller = cmpd2
        rateFactor = math.sqrt(mass1/mass2)
    else:
        bigger = cmpd2
        smaller = cmpd1
        rateFactor = math.sqrt(mass2/mass1)

    qType = random.randint(0,2)

    if qType == 0:
        print(f"How much faster is {smaller.name} than {bigger.name}?")
        return rateFactor
    elif qType == 1:
        print(f"If {smaller.name} is {rateFactor} times faster than the other gas, what is the other gas?")
        
        options = []
        for i in range(0,4):
            option = compound(getRandomCompound())
            while option.getMass() == bigger.getMass():
                option = compound(getRandomCompound())

            options.append(option)

        options.insert(random.randint(0,3), bigger)

        for i, j in enumerate(options):
            if j.type == "diatomic":
                gaseous = ""
            else:
                gaseous = " gaseous"
            print(f"{i+1}.{gaseous} {j.name}")

        return f"{bigger.name}, since it has a molar mass of {bigger.getMass()}"
    elif qType == 2:
        cmpd1 = compound(getRandomCompound(0,1,1,1,0))
        cmpd2 = compound(getRandomCompound(0,0,0,1,0))

        rate1 = .025 * random.randint(0,20)
        rate2 = rate1 * math.sqrt(cmpd2.getMass() / cmpd1.getMass())

        print(f"{cmpd1.name} effuses with a rate of {rate2}, and an unknown homonuclear diatomic gas effuses through the same opening at {rate1}. What is the other gas?")
        return cmpd2.name 

def twenty(**kwargs):
    goodQuestion = False
    valuesRanges = [[0,4], [.5, 100], [0,1], [100,450]]
    while not goodQuestion:
        P = randPressure()
        V = randVolume()
        cmpd = compound(getRandomCompound())
        n = random.randint(1,40) / 40
        moles = randUnit(cmpd, n)
        T = randTemp()

        idealGasLawList = [P[2], V[2], n, T[2]]

        missing = random.randint(0,3)

        if missing < 1:
            other = (missing + 1) % 2
            missingValue = (idealGasLawList[2] * Ratm * idealGasLawList[3]) /  idealGasLawList[other]
        else:
            other = (missing - 1) % 2 + 2
            missingValue = (idealGasLawList[0] * idealGasLawList[1]) / (idealGasLawList[other] * Ratm)

        missingRange = valuesRanges[missing]

        if missingValue > missingRange[0] and missingValue < missingRange[1]:
            goodQuestion = True
        
    idealGasLawList[missing] = missingValue

    qType = bool(random.getrandbits(1))

    units = ["atm", "L", "moles", "K"]
    if qType: # using the ideal gas law
        # print out the other values, then return missing

        missingIndex = random.randint(0,3)
        sentences = [f"The pressure if {getPressure(idealGasLawList[0], P[1])} {P[1]}. ", f"The volume of {cmpd.name} is {getVolume(idealGasLawList[1], V[1])} {V[1]}. ", 
                     f"There are/is {moles[0]} {moles[1]} of {cmpd.name}. ", f"The temperature is {getTemp(idealGasLawList[3], T[1])} {T[1]}. "]
        
        question = ["What is the pressure?", f"What is the volume of {cmpd.name}?", f"How many moles of {cmpd.name} are there?", f"What is the temperature?"][missingIndex]

        for i in [0,1,2,3]:
            if i == missingIndex: continue

            question = sentences[i] + question

        print(question)

        return str(idealGasLawList[missingIndex])+ " "+ units[missingIndex]
    else: # using all of the other gas laws
        givenIndex = random.randint(0,3)
        otherIndex = givenIndex
        while otherIndex == givenIndex:
            otherIndex = random.randint(0,3)
        
        if givenIndex == 0: final = randPressure()
        elif givenIndex == 1: final = randVolume()
        elif givenIndex == 2: 
            finalMoles = random.randint(1,40) * 1/40
            final = randUnit(cmpd, finalMoles)
        elif givenIndex == 3: final = randTemp()

        sentences = [f"The initial pressure if {getPressure(idealGasLawList[0], P[1])} {P[1]}. ", f"The initial volume of {cmpd.name} is {getVolume(idealGasLawList[1], V[1])} {V[1]}. ", 
                     f"Initally, there are/is {moles[0]} {moles[1]} of {cmpd.name}. ", f"The initial temperature is {getTemp(idealGasLawList[3], T[1])} {T[1]}. "]

        finalIdealGasLawList = idealGasLawList.copy()
        finalIdealGasLawList[givenIndex] = final[2]

        if otherIndex < 2:
            otherOtherIndex = (otherIndex + 1) % 2
            finalIdealGasLawList[otherIndex] = finalIdealGasLawList[2] * finalIdealGasLawList[3] * Ratm / finalIdealGasLawList[otherOtherIndex]
        else:
            otherOtherIndex = (otherIndex -1) % 2 + 2
            finalIdealGasLawList[otherIndex] = finalIdealGasLawList[0] * finalIdealGasLawList[1] / (finalIdealGasLawList[otherOtherIndex] * Ratm)

        question = [sentences[givenIndex], sentences[otherIndex]]

        pressure = randPressureUnit(finalIdealGasLawList[0])
        volume = randVolumeUnit(finalIdealGasLawList[1])
        moles = randUnit(cmpd, finalIdealGasLawList[2])
        temp = randTempUnit(finalIdealGasLawList[3])

        newSentences = [f"The final pressure is {pressure[0]} {pressure[1]}. ", f"The final volume is {volume[0]} {volume[1]}. ",
                        f"If we add/take away moles to keep all the other factors constant, the final amount of {cmpd.name} is {moles[0]} {moles[1]}. ",
                        f"The final temperature is {temp[0]} {temp[1]}. "]
        
        question.extend([newSentences[givenIndex], newSentences[otherIndex]])

        answers = [idealGasLawList[givenIndex], idealGasLawList[otherIndex], finalIdealGasLawList[givenIndex], finalIdealGasLawList[otherIndex]]
        quants = ["pressure", "volume", "moles", "temperature"]
        answerChoices = [f"What is the initial {quants[givenIndex]}?", f"What is the initial {quants[otherIndex]}?",
                         f"What is the final {quants[givenIndex]}?", f"What is the final {quants[otherIndex]}?"]
        
        missingIndex = random.randint(0,3)

        printStr = ""
        for i,sentence in enumerate(question):
            if i == missingIndex: continue
            printStr += sentence

        printStr += answerChoices[missingIndex]

        print(printStr)

        if missingIndex % 2 == 0: unitsIndex = givenIndex
        else: unitsIndex = otherIndex

        return str(answers[missingIndex]) + " "+ units[unitsIndex]
        # choose two values, changed one, calculate and return the new value of the other (show the original values of both, and the first changed value)

def twentyone(rxType, **kwargs):
    while True:
        # get a reaction
        bad = True
        while bad:
            rx = reaction(randomRx(rxType))
            separatedCmpds = rx.formatRxList()
            reactants = separatedCmpds[0]
            products = separatedCmpds[1]
            numReactants = len(reactants)
            if numReactants > 1: bad = False

        printStr = ["Combine ", "Decompose ", "Combust ", "Completely Combust ", "Incompletley Combust ", "Write the reaction between "]
        if rx.typeRx in ["s1", "s2", "s3"]: printStr = printStr[0]
        elif rx.typeRx in ["d1", "d2", "d3"]: printStr = printStr[1]
        elif rx.typeRx == "c": printStr = printStr[2]
        elif rx.typeRx == "complete combustion": printStr = printStr[3]
        elif rx.typeRx == "incomplete combustion": printStr = printStr[4]
        else: printStr = printStr[5]
        for j, i in enumerate(reactants):
            if len(separatedCmpds) == 3 and  j == 1: printStr += separatedCmpds[2] + " "
            try:
                printStr += i[0].getNameFromEq() # what's going on with HNH?!
            except: printStr += "error generating name"
            printStr += " and "

        question = printStr[0:-5] + ". Assume every molecular compound is a gas. "    
        # generate random moles counts
        cmpds = reactants + products
        starterMoles = .25 * random.randint(1,40)
        moles = [starterMoles * round((1.5 * random.random() + .5), 2) for cmpd in reactants]

        limiting = min(moles)
        limitingIndex = moles.index(limiting)

        for i in products:
            moles.append(limiting)

        for i, mole in enumerate(moles):
            moles[i] = round(mole * cmpds[i][1], 2)

        leftoverMoles = [round(mole - limiting * cmpds[i][1], 2) for i, mole in enumerate(moles)]
        # len(leftoverMoles) = numCmpds, the only non-zero term is the leftover moles (at the right index) (they are all 0 if it is stoiciometric mixture)
        #print(rx)
        #print(moles)
        #print(leftoverMoles)

        # gas laws stuff (calculating volume)
        gasses = [cmpd[0].isMolecular() for cmpd in cmpds]

        if not any(gasses):
            #print("fail")
            continue

        #print(gasses)

        pressure = randPressure()
        temp = randTemp()

        volumes = []
        allGasLawInfo = []

        for i in range(0,len(cmpds)):
            if gasses[i]:
                gasLawInfo = [randPressure(), moles[i], randTemp()]
                allGasLawInfo.append(gasLawInfo)
                volume = solveForVolume(gasLawInfo[0][2], gasLawInfo[1], gasLawInfo[2][2])
                volumes.append(volume)
            else:
                allGasLawInfo.append([0,0,0])
                volumes.append(0)

        #print(allGasLawInfo)
        #print(volumes)

        totalVolume = 0
        for volume in volumes: totalVolume += volume

        # print out the gas laws stuff and the of reaction
        numGassesInReactants = 0
        tempQ = ""
        for i, cmpd in enumerate(reactants):
            if not gasses[i]: 
                currNumMoles = moles[i]
                currNumMoles = randUnit(cmpd[0], currNumMoles)
                tempQ += f"There is (are) {currNumMoles[0]} {currNumMoles[1]} of {cmpd[0].getNameFromEq()}"
                if currNumMoles[1] == "L": tempQ += " (treat it like a gas at STP). "
                else: tempQ += ". "
                continue
            volume = randVolumeUnit(volumes[i])
            pressure = allGasLawInfo[i][0]
            temp = allGasLawInfo[i][2]

            question += f"There is {volume[0]} {volume[1]} of {cmpd[0].getNameFromEq()} at {pressure[0]} {pressure[1]} and {temp[0]} {temp[1]}. "
            numGassesInReactants += 1
        
        if numGassesInReactants == 0:
            for i, cmpd in enumerate(products):
                i += numReactants
                if not gasses[i]: continue
                volume = randVolumeUnit(volumes[i])
                pressure = allGasLawInfo[i][0]
                temp = allGasLawInfo[i][2]
                currPrint = f"After the reaction, {volume[0]} {volume[1]} of {cmpd[0].name} at {pressure[0]} {pressure[1]} and {temp[0]} {temp[1]} is produced. "
                otherReactantIndex = (limitingIndex + 1) % 2
                limiting = randUnit(cmpds[limitingIndex][0], limiting)
                question += currPrint + f" There is excess {cmpds[otherReactantIndex][0].name}. How much of {cmpds[limitingIndex][0].name} is there ({limiting[1]})?"
                
                print(question)
            
                return f"{limiting[0]} {limiting[1]}"

        # return moles
        chosenProduct = random.choice(products)
        chosenIndex = cmpds.index(chosenProduct)
        productMoles = randUnit(chosenProduct[0], moles[chosenIndex])
        question += tempQ + f"How much {chosenProduct[0].getNameFromEq()} is there ({productMoles[1]})?"
        print(question)
        return f"{productMoles[0]} {productMoles[1]}"

def twentytwo(**kwargs):
    number = random.randint(1,118)
    el = elements[number]
    print(f"What is the electron configuration of {el[1]}?")
    config = electronConfig(number)
    return config[2]

def twentythree(**kwargs):
    number = random.randint(1,118)
    el = elements[number]
    print(f"What is the noble gas shorthand for {el[1]}?")
    config = electronConfig(number)
    return config[1]    

def twentyfour( **kwargs):
    number = random.randint(1,118)
    el = elements[number]
    print(f"Is {el[1]} paramagnetic or diamagetic?")
    if number in range(58,71) or number in range(90,103):
        print("Assume one electron goes into a d orbital.")
    if isParamagnetic(number):
        return f"{el[1]} is paramagnetic."
    else: return f"{el[1]} is diamagnetic."

def twentyfive(**kwargs): 
    # Quantum Numbers
    elNum = random.randint(1,118)

    qNums = quantumNumbers(elNum)

    #if (58 <= elNum and elNum <= 71) or (90 <= elNum and elNum <= 103): print("Assume the d orbital gets filled after the f orbital. ", end = "")

    print(f"What are the quantum numbers for the last electron to be filled in {elements[elNum][1]}?")
    return f"n = {qNums[0]}, l = {qNums[1]}, ml = {qNums[2]}, ms = {qNums[3]}"

def twentysix(**kwargs):
    # c=lf and  E = hf = hc/l
    f = round_sig(random.randint(3e6, 3e22))
    l = round_sig(c / f)
    E = round_sig(h * f)
    qs = [f"The frequency is {'{:e}'.format(f)}.", f"The wave length is {'{:e}'.format(l)}.", f"The energy of the wave is {'{:e}'.format(E)}."]
    ans = ["frequency", "wave length", "energy"]
    qChoice = random.randint(0,2)
    aChoice = random.randint(0,2)
    while qChoice == aChoice:
        aChoice = random.randint(0,2)
    print(f"{qs[qChoice]} What is the {ans[aChoice]}?")
    return qs[aChoice]

def twentyseven(**kwargs):
    # Bohr
    nf = random.randint(1,10)
    ni = random.randint(1,10)
    while ni == nf: ni = random.randint(1,10)

    E = round_sig(abs(k * (nf ** -2 - ni ** -2)))
    f = round_sig(E / h)
    l = round_sig(c / f)

    rOrA = "releaed" if ni > nf else "absorbed"

    options = random.choice([("frequency (Hz) of the photon wave that is " + rOrA, '{:e}'.format(f)), ("wavelength (m) of the photon wave that is " + rOrA, '{:e}'.format(l)), ("energy (J) of the photon wave that is " + rOrA, '{:e}'.format(E))])

    choices = [options, ("final energy level", nf), ("initial energy level", ni)]
    
    firstChoice = random.choice(choices)
    choices.remove(firstChoice)
    secondChoice = random.choice(choices)
    choices.remove(secondChoice)

    print(f"The {firstChoice[0]} is {firstChoice[1]}, and the {secondChoice[0]} is {secondChoice[1]}. What is the {choices[0][0]}?")
    return choices[0][1]

def twentyeight(**kwargs):
    # DeBroglie for electrons
    v = round_sig(random.randint(1e2, 1e6))
    KE = round_sig(.5 * eMass * v ** 2)
    l = round_sig(h / (eMass * v))
    choices = [("de Broglie's wavelength", '{:e}'.format(l), "m"), ("kinetic energy", '{:e}'.format(KE), "J"), ("velocity", '{:e}'.format(v), "m/s")]

    question = random.choice(choices)
    choices.remove(question)
    answer = random.choice(choices)

    print(f"If the {question[0]} is {question[1]} {question[2]}, what is the {answer[0]} of the electron?")
    return str(answer[1]) + " " + answer[2]

def twentynine(**kwargs):
    # de Broglie in general
    v = round_sig(random.randint(1e2, 1e6))
    m = round_sig(.1 * random.randint(1,100))
    KE = round_sig(.5 * m * v ** 2)
    l = round_sig(h / (m * v))
    choices = [("de Broglie's wavelength", '{:e}'.format(l), "m"), ("kinetic energy", '{:e}'.format(KE), "J"), ("velocity", '{:e}'.format(v), "m/s"), ("mass", m, "kg")]

    first = random.choice(choices)
    choices.remove(first)
    second = random.choice(choices)
    choices.remove(second)

    answer = random.choice(choices)

    print(f"If the {first[0]} is {first[1]} {first[2]} and the {second[0]} is {second[1]} {second[2]}, what is the {answer[0]} of the object?")
    return str(answer[1]) + " " + answer[2]

def thirty(**kwargs):
    # Heisenburg uncertainty principle
    v = round_sig(random.randint(1e2, 1e6))
    x = round_sig(h / (4 * math.pi * v * eMass))
    KE = round_sig(.5 * eMass * v ** 2)
    choices = [("velocity", v, "m/s"), ("uncertainity in the position", x, "m"), ("kinetic energy", KE, "J")]
    question = random.choice(choices)
    choices.remove(question)
    answer = random.choice(choices)

    print(f"If the {question[0]} of the electron is {question[1]} {question[2]}, what is the {answer[0]}?")
    return str(answer[1]) + " " + answer[2]

def thirtyone(**kwargs):
    # identifying waves (IR, visible, UV) (series)
    f = round_sig(random.randint(1e13, 2e15))
    l = round_sig(c / f)
    if f < 4.3e14: typeWave = "infrared light and you would use the Paschen Series"
    elif f < 1e15: typeWave = "visible light and you would use the Balmer Series"
    else: typeWave = "ultraviolet light and you would use the Lyman Series"

    choices = [("frequency", '{:e}'.format(f), "Hz"), ("wavelength", '{:e}'.format(l), "m")]
    choice = random.choice(choices)

    print(f"A wave has a {choice[0]} of {choice[1]} {choice[2]}, what is the type of wave, and series would you use?")
    return "The wave is " + typeWave 

def thirtytwo(**kwargs):
    series = random.choice([(1e15, 2e15, 1, "UV"), (4.3e14, 1e15, 2, "visible"), (1e13, 4.3e14, 3, "infrared")]) # lyman, balmer, paschen

    nf = series[2]
    ni = random.randint(nf + 1, 10)
    # only for energy being released

    E = round_sig(abs(k * (nf ** -2 - ni ** -2)))
    f = round_sig(E / h)
    l = round_sig(c / f)

    options = [("frequency", '{:e}'.format(f), "Hz"), ("wavelength", '{:e}'.format(l), "m"), ("energy", '{:e}'.format(E), "J")]
    chosen = random.choice(options)

    print(f"The {chosen[0]} of the wave that is released when an electron falls is {chosen[1]} {chosen[2]}. What type of wave is it, and where did the wave start?")
    return f"It is a(n) {series[3]} wave, and it started at {ni}"

def thirtythree(**kwargs):
    # atom size
    el1 = element(elData = randElement("ntm"))
    el2 = element(elData = randElement("ntm"))

    print(f"Which atom is bigger: {el1.eq} or {el2.eq}?")
    compare = el1.compareSize(el2)

    if compare > 0: return el1.eq
    else: return el2.eq

def thirtyfour(**kwargs):
    # ion size
    el1 = element(elData = randElement("ntm"), charge = random.randint(0,3))
    el2 = element(elData = randElement("ntm"), charge = random.randint(0,3))

    print(f"Which ion is bigger: {el1} or {el2}?")
    compare = el1.compareSize(el2)

    if compare > 0: return el1.eq
    else: return el2.eq

def thirtyfive(**kwargs):
    # ionization energy
    el1 = element(elData = randElement("ntm"))
    el2 = element(elData = randElement("ntm"))

    print(f"Which atom has more Ionization Energy: {el1.eq} or {el2.eq}?")
    compare = el1.compareIE(el2)

    if compare > 0: return el1.eq
    else: return el2.eq

def thirtysix(**kwargs):
    # electronegativity
    el1 = element(elData = randElement("ntm"))
    el2 = element(elData = randElement("ntm"))

    print(f"Which atom has more Ionization Energy: {el1.eq} or {el2.eq}?")
    compare = el1.compareIE(el2)

    if compare > 0: return el1.eq
    else: return el2.eq

def thirtyseven(**kwargs):
    # electron affinity
    el1 = element(elData = randElement("ntm"))
    el2 = element(elData = randElement("ntm"))

    print(f"Which atom has more Ionization Energy: {el1.eq} or {el2.eq}?")
    compare = el1.compareEA(el2)

    if compare > 0: return el1.eq
    else: return el2.eq

def thirtyeight(**kwargs):
    # all periodic trends
    trend = random.choice(["thirtythree", "thirtyfour", "thirtyfive", "thirtysix", "thirtyseven"])
    return eval(f"{trend}()")

def thirtynine(**kwargs):
    # lattice energy
    metal = randElement("m")[2]
    nonmetal = randElement("n")[2]
    mCharge = findCharge(metal)
    nmCharge = findCharge(nonmetal)

    r = (random.random() * 1.7 + .3) * .1
    E = 2.31e-19 * mCharge * nmCharge / r
    choices = [('{:e}'.format(E), "lattice energy", "J"), (round(r, 5), "ionic bond length", "nm")]
    q = random.choice(choices)
    choices.remove(q)
    ans = choices[0]

    g = math.gcd(mCharge, nmCharge)
    mCoeff = nmCharge // g
    nmCoeff = mCharge // g
    eq = f"{metal}{'' if mCoeff == 1 else mCoeff}{nonmetal}{'' if nmCoeff == 1 else nmCoeff}"

    print(f"If the {q[1]} of {eq} is {q[0] } {q[2]}, what is the {ans[1]} in {ans[2]}")
    return f"{ans[0]} {ans[2]}"

def forty(**kwargs):
    # lewis dot structure
    cmpd = compound(randCmpdForBonds(1,2,1,6))
    print(f"What is the lewis dot structure for {cmpd.equation}")
    return print_matrix(cmpd.covalentBonds())

def fortyone(**kwargs):
    # VSEPR
    cmpd = compound(randBMForBonds())
    VSEPRchoices = {0 : "electron domain", 1: "shape", 2 : "angle", 3 : "polarity", 4 : "hybridization of the central atom"}
    choice = random.choice(list(VSEPRchoices))
    print(f"What is the {VSEPRchoices.get(choice)} of {cmpd.equation}")
    return cmpd.VESPR()[choice]

def fortytwo(**kwargs):
    # bond order
    cmpd = compound(randCmpdForBonds())
    print(f"What is the bond order of {cmpd.equation}")
    return cmpd.bondOrder()

def fortythree(**kwargs):
    # sigma and pi bonds
    cmpd = compound(randCmpdForBonds())
    print(f"How many sigma bonds does {cmpd.equation} have? How many pi bonds?")
    return f"sigma bonds: {cmpd.sigmaBonds()}\npi bonds: {cmpd.piBonds()}"

def fortyfour(**kwargs):
    # bond energy
    cmpd = compound(randCmpdForBonds())
    print(f"What is the bond energy of {cmpd.equation}")
    return cmpd.bondEnergy()

def fortyfive(**kwargs):
    # enthalpy of reactions
    rx = reaction(randomRx("bond"))
    print("What is the enthalpy of the following reaction:\n")
    print(rx)
    return rx.enthalpyFromBonds()

def fortysix(**kwargs):
    while True:
        cmpd = compound(random.choice(list(solubilities)))
        temp = random.randint(0,3)
        if solubilities.get(cmpd.equation)[temp] != None: break

    temps = [0, 20, 50, 100]
    amnt = random.randint(1,20) * 25
    mol = solubilities.get(cmpd.equation)[temp] * amnt / 100 / cmpd.getMass()
    n = randUnit(cmpd, mol)
    print(f"How much {cmpd.getNameFromEq()} is soluble in {amnt} g of H2O at {temps[temp]} degrees C ({n[1]})?")
    return n[0]

def fortyseven(**kwargs):
    while True:
        cmpd = compound(random.choice(list(solubilities)))
        temp = random.randint(0,3)
        if solubilities.get(cmpd.equation)[temp] != None: break

    temps = [0, 20, 50, 100]
    amnt = random.randint(1,20) * 25
    theoretical = solubilities.get(cmpd.equation)[temp] * amnt / 100
    changeBool = random.randint(-1,1)
    accAmnt = theoretical + changeBool * .05 * random.randint(1,10) * theoretical

    print(f"Is a solution of {accAmnt} of {cmpd.getNameFromEq()} super-/un-/saturated in {amnt} g of H2O at {temps[temp]} degrees C?")
    return ["unsaturated", "saturated", "supersaturated"][changeBool + 1]

def fortyeight(**kwargs):
    initialMol = random.randint(1,40) / 20
    while (finalMol := random.randint(1,40) / 200) == initialMol: pass
    initialVol = random.randint(1,40) / 20 
    finalVol = initialMol * initialVol / finalMol
    temp = [(initialMol, "initial molarity", "M"), (initialVol, "initial volume", "L"), (finalMol, "final molarity", "M"), (finalVol, "final volume", "L")]
    other = temp.pop(random.randint(0,3))
    for t in temp: print(f"The {t[1]} is {t[0]} {t[2]}. ", end = "")
    print(f"What is the {other[1]}?")
    return f"{other[0]} {other[2]}"

def fortynine(**kwargs):
    moles_solute = random.randint(1,40) / 20
    total_volume = random.randint(1,150) / 50
    sol = solution(compound(), moles_solute = moles_solute, total_volume = total_volume)
    
    while True:
        choices = [(f"There are {sol.moles_solute} moles of solute.", "How many moles of the solute are there?"), (f"There are {sol.moles_solvent} moles of solvent.", "How many moles of the solvent are there?"), 
               (f"It's volume is {sol.volume} L.", "What is the total volume"), (f"Its molarity is {round_sig(sol.molarity())} M", "What is the molarity?"), 
               (f"Its molality is {round_sig(sol.molality())} m.", "What is the molality?"), (f"The mole fraction of the solute is {round_sig(sol.moleFractions())}.", "What is the mole fraction of the solute?"), 
               (f"The mole fraction of the solvent is {round_sig(sol.moleFractions(False))}.", "What is the mole fraction of the solvent?"), (f"The percent m/v of the solution is {round_sig(sol.pMV())}%.", "What is the percent m/v?")]

        inds = set()
        choice_one = random.choice(choices)
        inds.add(choices.index(choice_one))
        choices.remove(choice_one)
        choice_two = random.choice(choices)
        inds.add(choices.index(choice_two))
        choices.remove(choice_two)
        chosen_answer = random.choice(choices)
        inds.add(choices.index(chosen_answer))

        b = True
        for i in [{5,6}, {3,4}, {3,7}, {4,7}, {1,2}]:
            if inds & i == i: b = False

        if b: break


    print(f"Consider an aqueous solution of {sol.solute.getNameFromEq()}. Remember that the density of water is 1 g/mL and ignore the solute's volume. {choice_one[0]} {choice_two[0]} {chosen_answer[1]}")
    return chosen_answer[0]

def fifty(**kwargs):
    moles_solute = random.randint(1,40) / 20
    total_volume = random.randint(1,150) / 50
    solvent = compound(random.choice(list(fpDepressionConstants)))
    sol = solution(compound(), moles_solute = moles_solute, total_volume = total_volume, solvent = solvent)

    while True:
        choices = [(f"There are {sol.moles_solute} moles of solute.", "How many moles of the solute are there?"), (f"There are {sol.moles_solvent} moles of solvent.", "How many moles of the solvent are there?"), 
               (f"It's volume is {sol.volume} L.", "What is the total volume"), (f"Its molarity is {round_sig(sol.molarity())} M.", "What is the molarity?"), 
               (f"Its molality is {round_sig(sol.molality())} m.", "What is the molality?"), (f"The mole fraction of the solute is {round_sig(sol.moleFractions())}.", "What is the mole fraction of the solute?"), 
               (f"The mole fraction of the solvent is {round_sig(sol.moleFractions(False))}.", "What is the mole fraction of the solvent?"), (f"The percent m/v of the solution is {round_sig(sol.pMV())}%.", "What is the percent m/v?"),
               (f"The density of the solvent is {sol.solvent_density} g/mL.", "What is the density of the solvent?")]
        inds = set()
        choice_one = random.choice(choices)
        inds.add(choices.index(choice_one))
        choices.remove(choice_one)
        choice_two = random.choice(choices)
        inds.add(choices.index(choice_two))
        choices.remove(choice_two)
        choice_three = random.choice(choices)
        inds.add(choices.index(choice_three))
        choices.remove(choice_three)
        chosen_answer = random.choice(choices)
        inds.add(choices.index(chosen_answer))

        b = True
        for i in [{5,6}, {3,4}, {3,7}, {4,7}, {1,2}]:
            if inds & i == i: b = False

        if b: break

    print(f"Consider a solution, which is not necessarily aqueous, containing {sol.solute.getNameFromEq()} (solute). Ignore the solute's volume. {choice_one[0]} {choice_two[0]} {choice_three[0]} {chosen_answer[1]}")
    return chosen_answer[0]

def fiftyone(**kwargs):
    moles_solute = random.randint(1,40) / 20
    total_volume = random.randint(1,150) / 50
    bpOrFp = bool(random.getrandbits(1))

    if bpOrFp: solvent = random.choice(list(bpElevationConstants)) # boiling point
    else: solvent = random.choice(list(fpDepressionConstants)) # freezing point

    sol = solution(compound(getRandomCompound(3,0,1,0,2)), moles_solute= moles_solute, total_volume= total_volume, solvent= compound(solvent))
    word = ["boiling", "freezing"][int(bpOrFp)]

    while True:
        choices = [(f"There is/are {sol.moles_solute} moles of solute.", "How many moles of the solute are there?"), (f"There is/are {sol.moles_solvent} moles of solvent.", "How many moles of the solvent are there?"), 
               (f"The solvent's volume is {sol.volume} L.", "What is the total volume"), (f"Its molarity is {round_sig(sol.molarity())} M", "What is the molarity?"), 
               (f"The mole fraction of the solute is {round_sig(sol.moleFractions())}.", "What is the mole fraction of the solute?"), (f"The mole fraction of the solvent is {round_sig(sol.moleFractions(False))}.", "What is the mole fraction of the solvent?"), 
               (f"The percent m/v of the solution is {round_sig(sol.pMV())}%.", "What is the percent m/v?"), (f"The density of the solvent is {sol.solvent_density} g/mL.", "What is the density of the solvent?")]

        inds = set()
        choice_one = random.choice(choices)
        inds.add(choices.index(choice_one))
        choices.remove(choice_one)
        choice_two = random.choice(choices)
        inds.add(choices.index(choice_two))
        choices.remove(choice_two)
        chosen_answer = random.choice(choices)
        inds.add(choices.index(chosen_answer))

        b = True
        for i in [{5,6}, {3,4}, {3,7}, {4,7}, {1,2}]:
            if inds & i == i: b = False

        if b: break

    print(f"Consider a solution, which is not necessarily aqueous, containing {sol.solute.getNameFromEq()} (solute). Ignore the solute's volume. {choice_one[0]} {choice_two[0]} What is the {word} point?", end = "")
    print(f" The molar mass of the solvent is {sol.solvent.getMass()} g/mol.", end = "")
    if bpOrFp: 
        print(f" The boiling point of the solvent is {miscBps.get(solvent)} and Kb is {bpElevationConstants.get(solvent)}")
        return round_sig(sol.boilingPoint(), 6)
    else: 
        print(f" The freezing point of the solve is {miscFps.get(solvent)} and Kf is {bpElevationConstants.get(solvent)}")
        return round_sig(sol.freezingPoint(), 6)

def fiftytwo(**kwargs):
    moles_solute = random.randint(1,40) / 20
    total_volume = random.randint(1,150) / 50
    bpOrFp = bool(random.getrandbits(1))

    if bpOrFp: solvent = random.choice(list(bpElevationConstants)) # boiling point
    else: solvent = random.choice(list(fpDepressionConstants)) # freezing point

    givenEmpirical = bool(random.getrandbits(1))

    solute = compound(getRandomCompound(0,0,0,0,1))
    if givenEmpirical: solute.multCompound(random.randint(1,5))
    sol = solution(solute, moles_solute= moles_solute, total_volume= total_volume, solvent= compound(solvent))

    if givenEmpirical:
        pComp = solute.percentComposition()
        print("An unknown compound contains ", end = "")
        for i in pComp: print(f"{round_sig(i[1], 4)}% {i[0]}", end = " ")

    word = ["molar mass", "molecular formula"][int(givenEmpirical)]

    solvent_mass = sol.solvent.getMass(sol.moles_solvent)
    if bpOrFp: print(f"The boiling point of a molecular solvent is {miscBps.get(solvent)} and the Kb is {bpElevationConstants.get(solvent)}. If the boiling point of the solution is {round_sig(sol.boilingPoint())} when there is {sol.solute.getMass(sol.moles_solute)} g of solute in {round_sig(solvent_mass)} g of the solvent, what is the {word} of the solute?")
    else: print(f"The freezing point of a molecular solvent is {miscFps.get(solvent)} degrees C and Kf is {fpDepressionConstants.get(solvent)}. If the freezing point of the solution is {round_sig(sol.freezingPoint())} when there is {sol.solute.getMass(sol.moles_solute)} g of solute in {round_sig(solvent_mass)} g of solvent, what is the {word} of the solute?")

    if givenEmpirical: return solute.getEq()
    else: return solute.getMass()

def fiftythree(**kwargs):
    while True:
        cmpd = random.choice(list(solubilities))
        temp_index  = random.randint(0,3)
        temp = [0,20,50,100][temp_index]
        initial_s = solubilities.get(cmpd)[temp_index]
        if initial_s: break

    final_p = random.randint(1,150) / 50
    final_p = randPressureUnit(final_p)
    final_s = round_sig(initial_s * final_p[2])

    choices = [("final pressure", final_p[0], final_p[1]), ("final solubility", final_s, "g / 100 g H2O")]

    choice = random.choice(choices)
    choices.remove(choice)

    print(f"Consider {cmpd} at {temp} degrees C. What is the {choices[0][0]} if the {choice[0]} is {choice[1]} {choice[2]}?")
    return f"{choices[0][1]} {choices[0][2]}"

def fiftyfour(**kwargs):
    while True:
        rx = reaction(randomRx(["double replacement", "special"]))
        separatedCmpds = rx.formatRxList()
        products = rx.SkeletonEquation()[1]
        reactants = rx.SkeletonEquation()[0]
        print(rx)
        soluableProducts = [i for i in products if i.equation not in ["NO2", "NO", "H2O", "CO2", "NH3",]]
        if compound("NO2") in soluableProducts: soluableProducts.remove(compound("NO2"))
        print([i.equation for i in soluableProducts])
        if len(soluableProducts) != 0: break


    printStr = ["Combine ", "Decompose ", "Combust ", "Completely Combust ", "Incompletley Combust ", "Write the reaction between "]
    if rx.typeRx in ["s1", "s2", "s3"]: printStr = printStr[0]
    elif rx.typeRx in ["d1", "d2", "d3"]: printStr = printStr[1]
    elif rx.typeRx == "c": printStr = printStr[2]
    elif rx.typeRx == "complete combustion": printStr = printStr[3]
    elif rx.typeRx == "incomplete combustion": printStr = printStr[4]
    else: printStr = printStr[5]
    for reactant in reactants:
        reactantName = reactant.getNameFromEq()
        coeffientList = rx.balanceEq()
        if reactantName == "nitric acid":
            if coeffientList in [[3,8,3,2,4], [8,3,3,2,4]]:
                reactantName = "dilute nitric acid"
            elif coeffientList in [[4,1,1,2,2], [1,4,1,2,2]]:
                reactantName = "concentrated nitric acid"
        printStr += reactantName + " and "
    question = printStr[0:-5] + ". "
    print(question, end = "")

    solutions : list[solution]= []
    minMol = 99
    minIndex = 0
    i = 0
    for cmpd in reactants:
        mol = random.randint(1,40) / 20
        if mol < minMol: 
            minMol = mol
            minIndex = i
        i += 1

        molarity = random.randint(1,150) / 50
        volume = mol / molarity
        solutions.append(solution(cmpd, moles_solute = mol, total_volume = volume))
    
    for sol in solutions: print(f"You have {round_sig(sol.volume)} L of a {round_sig(sol.molarity())} M aqueous solution of {sol.solute.equation}", end = ". ")
    finalProd = random.choice(soluableProducts)
    for i in separatedCmpds[1]:
        if i[0] == finalProd: prodCoeff = i[1]

    minCoeff = separatedCmpds[0][minIndex][1]
    prodMol = minMol / minCoeff * prodCoeff
    vol = random.randint(1,150) / 50
    prodSol = solution(finalProd, moles_solute = prodMol, total_volume= vol)
    print(f"All of the {finalProd.equation} is moved to its own {vol} L beaker of water. What is the molarity of this solution?")    

    return round_sig(prodSol.molarity())

def fiftyfive(**kwargs):
    hyd = hydrate(compound(getRandomCompound(1,0,0,0,0)).equation, random.randint(3,8))
    t = random.randint(0,4)
    if t == 0: # percent of one element
        el = random.choice(hyd.percentComposition())
        print(f"What is the percent by mass of {el[0]} in {hyd.equation}")
        return el[1]
    elif t == 1: # percent water
        print(f"What percent by mass of {hyd.equation} is water?")
        return round_sig(100 * hyd.percentWater())
    elif t == 2: # unknown num water
        eqToPrint = f"{hyd.anhydrous} 🞄 XH2O"
        print(f"If the molar mass of {eqToPrint} is {hyd.getMolarMass()} g/mol, what is X?")
        return hyd.numWater
    elif t == 3: # unknown element
        eqToPrint = "X" + hyd.equation[int(hyd.equation[1].islower()) + 1:]
        print(f"If the molar mass of {eqToPrint} is {hyd.getMolarMass()} g/mol, what is X?")
        return hyd.equation[:int(hyd.equation[1].islower()) + 1]
    elif t == 4: # unknown element and num water
        eqToPrint = "X" + hyd.anhydrous[int(hyd.anhydrous[1].islower()) + 1:] + " 🞄 YH2O"
        print(f"If the molar mass of {eqToPrint} is {hyd.getMolarMass()} g/mol and the compound is {round_sig(100 * hyd.percentWater())}% water by mass, what is X and Y?")
        return "X: " + hyd.equation[:int(hyd.equation[1].islower()) + 1] + ", Y: " + str(hyd.numWater)

def fiftysix(**kwargs):
    cmpd = compound(randCmpdForBonds())
    print(f"Is {cmpd.getNameFromEq()} polar?")
    return ["no", "yes"][int(cmpd.isPolar())]

def fiftyseven(**kwargs):
    # determining rates from intial and final concentrations
    C_i = random.randint(1,400) / 400
    while (C_f := random.randint(1,400) / 400) == C_i: pass
    t = random.randint(1,40) / 20
    print(f"What is the rate if the concentration goes from {C_i} M to {C_f} M in {t} seconds.")
    return round((C_i - C_f) / t, 2)

def fiftyeight(**kwargs):
    # method of initial rates
    rx = reaction(randomRx())
    while True:
        reactants = rx.formatRxList()[0]
        if rx.molecularity() == 1: 
            rx = reaction(randomRx())
            continue
        break
    print(f"Consider the following reaction and data:\n{rx}\n")

    rate_orders = []
    for _ in reactants: 
        curr = random.randint(1,9)
        curr = int(curr > 5) + int(curr > 1)
        rate_orders.append(curr)

    k = round_sig(random.randint(1,100) / 10 * (10 ** (random.randint(-5,5))))

    # do names = [""] + names and first_ex = [1] + first_ex
    names = ["[" + i[0].equation + "]" for i in reactants] + ["rate (mol/Ls)"]
    first_ex = [random.randint(1,20) / 200 for _ in reactants]
    rate_1 = k
    for i, conc in enumerate(first_ex): rate_1 *= conc ** (rate_orders[i-1])
    first_ex.append(round_sig(rate_1))
    expirements = [[""] + names, [1] + first_ex]
    used = []
    num = 1
    for _ in reactants:
        while (choice := random.randint(1,len(first_ex) - 1)) in used: pass
        used.append(choice)
        factor = random.randint(2,4) ** (random.randint(0,1) * 2 - 1)
        curr_ex = deepcopy(expirements[1])
        curr_ex[choice] = round_sig(curr_ex[choice] * factor)
        curr_ex[-1] = round_sig(curr_ex[-1] * (factor ** rate_orders[choice-1]))
        curr_ex[0] = (num := num + 1)
        expirements.append(curr_ex)

    for i in expirements: print(i)
    
    rate_law = "k"
    for i, r in enumerate(reactants): 
        i = rate_orders[i]
        if i != 0: rate_law += "[" + r[0].equation + "]" + str(2) * (int(i == 2))
    
    print("\n What is the rate law for this reaction?")
    
    return f"rate law: {rate_law}, k: {k}"

def fiftynine(**kwargs):
    # equilibrium expression
    rx = reaction("eq")
    print(f"Consider the following reaction: {rx.phaseStr()}. What is the equilbrium expression for this reaction?")
    return rx.eqExpressionStr()

def sixty(**kwargs):
    # calculating missing eq concentration
    rx = reaction("eq", waterAsGas = True)
    prodEq, reactEq = rx.eqExpression()
    prodEq = [(p[0], conc) for p, conc in zip(prodEq, rx.prodEqConcs)]
    reactEq = [(r[0], conc) for r, conc in zip(reactEq, rx.reactEqConcs)]
    totEq = prodEq + reactEq
    totStr = [f" There is (are) {round_sig(conc)} M of {cmpd.__repr__()}." for cmpd, conc in totEq]
    missing_index = random.randint(0,len(totStr) - 1)
    missing_str = totStr.pop(missing_index)
    print(f"Consider the following reaction: {rx.phaseStr()}. The equilibrium constant is {'{:0.4e}'.format(rx.K_eq)}.{''.join(totStr)} What is the concentration of {totEq[missing_index][0].__repr__()}?")
    return missing_str[1:]

def sixtyone(**kwargs):
    # calculating K_eq from eq concentrations
    rx = reaction("eq", waterAsGas = True)
    prodEq, reactEq = rx.eqExpression()
    prodEq = [(p[0], conc) for p, conc in zip(prodEq, rx.prodEqConcs)]
    reactEq = [(r[0], conc) for r, conc in zip(reactEq, rx.reactEqConcs)]
    totStr = [f" There is (are) {round_sig(conc)} M of {cmpd.__repr__()}." for cmpd, conc in prodEq + reactEq]
    print(f"Consider the following reaction: {rx.phaseStr()}.{''.join(totStr)} What is the equilibrium constant?")
    return '{:0.4e}'.format(rx.K_eq)

def sixtytwo(**kwargs):
    # calculating eq concs from intial concs (all reactants) and K_eq
    while True:
        rx = reaction("eq", waterAsGas = True)
        prodEq, reactEq = rx.eqExpression()
        intial_react_conc = random.randint(1,40) / 20 + .5
        prodConcs = [0 for _ in rx.prodEqConcs]
        reactConcs = [intial_react_conc for _ in rx.reactEqConcs]
        try:
            rx.eqConcsFromIntial(prodConcs, reactConcs)
            for i in (rx.prodEqConcs + rx.reactEqConcs):
                if i < 0: raise KeyError
        except KeyError: continue

        break

    prodEq = [(p[0], conc) for p, conc in zip(prodEq, rx.prodEqConcs)]
    reactEq = [(r[0], conc) for r, conc in zip(reactEq, rx.reactEqConcs)]

    print(f"Consider the following reaction: {rx.phaseStr()}. The equilibrium constant is {'{:0.4e}'.format(rx.K_eq)}. Intially, each reactant is at {intial_react_conc} M. What are the equilibrium concentrations?")
    return "".join([f"There is (are) {round_sig(conc)} M of {cmpd.__repr__()}. " for cmpd, conc in prodEq + reactEq])

def sixtythree(**kwargs):
    # thermodynamics part 2 electric boogaloo
    while rx := reaction(randomRx()):
        if rx.checkRxForThermo(): break
    
    choice = random.randint(0,2)
    chosen = ["enthalpy", "gibbs free energy", "entropy"][choice]

    data = [f"The {chosen} of {cmpd} is {thermoData.get(thermCompound(cmpd.equation + '(' + phase + ')'))[choice]}. " for cmpd, phase in zip(rx.allCompounds(), rx.phases)]

    print(f"Consider the reaction {rx.phaseStr()}. {''.join(data)}What is the {chosen} of the reaction?")
    return rx.thermoProfile(choice)

def sixtyfour(**kwargs):
    # pH conversions
    molarity = random.random() * (10 ** random.randint(-13,0))
    a = acid("HCl", molarity)
    answers = [("pH", a.pH()), ("pOH", a.pOH()), ("H+ concentration", a.HConc()), ("OH- Concentration", a.OHConc())]
    chosen = random.choice(answers)
    answers.remove(chosen)

    ans = random.choice(answers)
    print(f"If the {chosen[0]} is {round_sig(chosen[1])}, what is the {ans[0]}?")
    return round_sig(ans[1])

def sixtyfive(**kwargs):
    # pH from molarity
    molarity = random.random() * (10 ** random.randint(-14,0))
    isAcid = bool(random.getrandbits(1))
    if isAcid: 
        eq = random.choice(list(KaDict.keys()))
        ab = acid(eq, molarity=molarity)
    else:
        eq = random.choice(list(KbDict.keys()))
        ab = base(eq, molarity=molarity)
    one = random.choice([("pH", ab.pH()), ("pOH", ab.pOH()), ("H+ concentration", ab.HConc()), ("OH- Concentration", ab.OHConc())])
    one = list(one)
    one[1] = round_sig(one[1])
    answers = [one, (f"K{'a' if isAcid else 'b'}", "large" if ab.K_eq > 9e199 else round_sig(ab.K_eq)), ("molarity", round_sig(molarity))]

    answer = random.choice(answers)
    answers.remove(answer)

    print(f"What is the {answer[0]} of a solution of {eq} where the {answers[0][0]} is {answers[0][1]} and the {answers[1][0]} is {answers[1][1]}?")
    return round_sig(answer[1])

def sixtysix(**kwargs):
    # pH from Common Ion Effect
    molarity = random.random() * (10 ** random.randint(-14,0))
    isAcid = bool(random.getrandbits(1))
    addedMolarity = random.randint(1,75) / 100 + .25
    if isAcid: 
        eq = random.choice(list(KaDict.keys()))
        ab = acid(eq, molarity)
        metal = elements[random.choice(list(metalsDict))][2]
        mCharge = findCharge(metal)
        nm = [ab.c_base.equation, ab.c_base.charge]
        commonIon = ionicCompoundFromElements(m = [metal, mCharge], n = nm)
        cFactor = mCharge
    else:
        eq = random.choice(list(KbDict.keys()))
        ab = base(eq, molarity)
        nm = randPolyatomic()
        metal = [ab.c_acid.equation, ab.c_base.charge]
        commonIon = ionicCompoundFromElements(m = metal, n = nm) 
        cFactor = nm[1]

    ab.addCommonIon(addedMolarity)

    one = random.choice([("pH", ab.pH()), ("pOH", ab.pOH()), ("H+ concentration", ab.HConc()), ("OH- Concentration", ab.OHConc())])
    one = list(one)
    one[1] = round_sig(one[1])
    answers = [one, (f"K{'a' if isAcid else 'b'}", "large" if ab.K_eq > 9e199 else round_sig(ab.K_eq)), ("molarity", round_sig(molarity))]

    answer = random.choice(answers)
    answers.remove(answer)

    print(f"What is the {answer[0]} of a solution of {eq} where the {answers[0][0]} is {answers[0][1]} and the {answers[1][0]} is {answers[1][1]}, if there is {round_sig(addedMolarity / cFactor)} M of {commonIon} in the solution?")
    return answer[1]

def sixtyseven(**kwargs):
    # neutralization/tritration
    strongAcids = ["HCl", "HI", "HBr", "HClO4", "HClO3", "HNO3", "H2SO4"]
    strongBases = ["LiOH", "NaOH", "KOH", "RbOH", "CsOH", "Ca(OH)2", "Sr(OH)2", "Ba(OH)2"]
    a = acid(random.choice(strongAcids), moles = random.randint(1,40) / 200 + .05, volume = random.randint(1,40) / 200)
    b = base(random.choice(strongBases), moles = random.randint(1,40) / 200 + .05, volume = random.randint(1,40) / 200)
    n = neutralization(a,b)

    n_ab = n.leftover_ab
    moles = n.salt_moles

    one = [("pH", n_ab.pH(), ""), ("pOH", n_ab.pOH(), ""), ("H+ concentration", n_ab.HConc(), ""), ("OH- Concentration", n_ab.OHConc(), "")]
    two = [('leftover moles of salt',  moles, "mol(s)"), ('number of particles in the salt', moles * 6.02e+23, "particles"), ("number of atoms in the salt", n.salt.getAtoms(moles), "atoms"), ("mass of the salt", n.salt.getMass(moles), "g")]
    answer = random.choice(one + two)

    print(f"When {a} is tritrated with {b}, what is the resulting {answer[0]} at equilibrium?")
    return str(answer[1]) + " " + answer[2]

def sixtyeight(**kwargs):
    # k_sp
    cmpd = compound(random.choice(list(KspDict)))

    cIon = random.randint(0,2)
    mConc = 0
    nConc = 0
    cStr = ""

    s_rx = cmpd.solubility_rx(mConc, nConc)
    reactants, _ = s_rx.eqExpression()

    if cIon == 1: 
        mConc = random.randint(1,40) / 200 + .05
        cStr = f" if there is {mConc} M of {reactants[0][0]} in the solution"
    if cIon == 2: 
        nConc = random.randint(1,40) / 200 + .05
        cStr = f" if there is {nConc} M of {reactants[1][0]} in the solution"

    options = [(product[0], conc) for product, conc in zip(reactants, s_rx.prodEqConcs)]
    chosen = random.choice(options)

    print(f"If the K_sp of {cmpd} is {cmpd.K_sp}, what is the concentration of the {chosen[0]} ion{cStr}.")
    return '{:e}'.format(chosen[1])

def sixtynine(**kwargs):
    # oxidation numbers
    cmpd = compound(getRandomCompound())
    oNums = cmpd.oxidation_numbers()
    oStr = ', '.join([f"{el}: {oNums[el]}" for el in oNums])

    print(f"What are the oxidation numbers of {cmpd}")
    return oStr

def seventy(**kwargs):
    # balancing redox (WIP)
    pass

def seventyone(**kwargs):
    # reaction potentials (WIP)
    pass

def seventytwo(**kwargs):
    # electroplating
    while (cmpd := compound(getRandomCompound(1,0,0,0,0))):
        if len(cmpd.compound) != 2: break

    metal, mCharge = ionizeTernaryIonic(cmpd.equation)[0]
    metal = compound(metal)
    current = random.randint(1,100) / 20 + .5
    time = random.randint(100,999) * 100

    mass = round_sig(metal.getMass(current * time / (F * mCharge)))
    options = [(f"A current of {current} C/t is applied", "What is the current", current, "C/t"), 
               (f"The current is applied for {time} s", "How long is the current applied", time, "s"),
                (f"{mass} g of {metal} is deposited", f"How much {metal} is deposited", mass, "g")]
    chosen = random.choice(options)
    options.remove(chosen)

    print(f"{options[0][0]}. {options[1][0]}. {chosen[1]}?")
    return f"{chosen[2]} {chosen[3]}"

def seventythree(**kwargs):
    # nuclear chem
    protons = random.randint(88, 118)
    neutrons = neutronList[protons] + random.randint(-2,2)
    el = [protons, neutrons]
    particles = {"alpha particle" : [4,2], "beta particle" : [0,-1], "positron" : [0,1], "proton" : [1,1], "neutron" : [1,0]}

    match random.randint(1,6):
        case 1 | 2 | 3: numParticles = 1
        case 4 | 5: numParticles = 2
        case 6: numParticles = 3
    
    parts = []
    for _ in range(numParticles):
        while t := random.choice(list(particles)):
            if t not in parts: break
        
        parts.append(t)
    
    parities = [1 if bool(random.getrandbits(1)) else -1 for _ in range(numParticles)]
    
    newEl = [protons, neutrons]
    for parity, nums in zip(parities, parts):
        newEl[0] += parity * particles[nums][0]
        newEl[1] += parity * particles[nums][1]
    
    origElement = elements[protons][2] + "-" + str(neutrons)
    newElement = elements[newEl[0]][2] + "-" + str(newEl[1])

    words = [action + " emission" if i < 0 else action + " absorption" for action, i in zip(parts, parities)]
    print(f"A particle of {origElement} undergoes {' and '.join(words)}. What particle is created?")
    return newElement

def polyatomicIonTest(polyatomicIonChoices):
    name = random.choice(polyatomicIonChoices)
    ion = polyatomicIons.get(name)
    print("What is the equation and charge of " + name + "?")
    charge = ion[-1]
    if ion != "NH4 1": charge = "-" + charge

    return f"equation: {ion[:ion.index(' ')]}, charge: {charge}"

def flaskify(s : str, rxType = ""):
    old_std_out = sys.stdout
    capture_io = io.StringIO()
    sys.stdout = capture_io 

    ans = eval(s + f"(rxType = '{rxType}')")

    printed = capture_io.getvalue()

    sys.stdout = old_std_out 
    capture_io.close() 

    return ([printed, ans])

def polyatomicFlaskied(polyatomicIonChoices):
    old_std_out = sys.stdout
    capture_io = io.StringIO()
    sys.stdout = capture_io 

    ans = polyatomicIonTest(polyatomicIonChoices)

    printed = capture_io.getvalue()

    sys.stdout = old_std_out 
    capture_io.close() 

    return ([printed, ans])