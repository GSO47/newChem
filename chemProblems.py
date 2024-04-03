import random, sys, io
from chemFuncts import *
from chemData import *

def one(**kwargs):
    powers = [(unit, random.randint(-2,3)) for unit in units]
    for unit, p in powers:
        if p == 0: powers.remove((unit, p))
    print(powers)
    start = [random.choice(list(prefixNumbers.values())) for _ in powers]
    end = [random.choice(list(prefixNumbers.values())) for _ in powers]

    startStr = ""
    for s, p in zip(start, powers):
        unit, p = p
        startStr

    startUnit = getUnit(powers)
    endUnit = getUnit(powers)
    print("Start: " + startUnit[0])
    print("End: " + endUnit[0])
    print("You have to multiply the start by 10^x, to get to the final unit. What is x?")

    finalFactor = startUnit[1] - endUnit[1]
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
        gasses = [cmpd[0].canBeGas() for cmpd in cmpds]

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