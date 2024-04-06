import json, csv

prefixes = {
    "f" : -15,
    "p" : -12,
    "n" : -9,
    "mi" : -6,
    "m" : -3,
    "c" : -2,
    "d" : -1,
    "da" : 1,
    "h" : 2,
    "k" : 3,
    "M" : 6,
    "G" : 9,
    "T" : 12,
    "P" : 15,
    1 : "mono",
    2 : "di",
    3 : "tri",
    4 : "tetra",
    5 : "penta",
    6 : "hexa",
    7: "hepta",
    8 : "octa",
    9 : "nona",
    10 : "deca",
    11 : "undeca",
    12 : "dodeca"
}

prefixNumbers = {
    1 : "f",
    2 : "p",
    3 : "n",
    4 : "mi",
    5 : "m",
    6 : "c",
    7 : "d",
    8 : "da",
    9 : "h",
    10 : "k",
    11 : "M",
    12 : "G",
    13 : "T",
    14 : "P"
}

units = ["m", "g", "s"]

with open('periodicTable.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    elements = ["n/a"]
    next(csv_reader)
    for line in csv_reader:
        toAppend = [line[0], line[1], line[2]]
        
        if line[8] == "":
            toAppend.append("n/a")
        else:
            group = int(line[8])
            if group < 3:
                toAppend.append(str(group) + "a")
            elif group < 11:
                toAppend.append(str(group) + "b")
            elif group < 13:
                toAppend.append(str(group - 10) + "b")
            else:
                toAppend.append(str(group - 10) + "a")
        if line[12] == "yes":
            if line[15] == "Transition Metal" or line[1] in ["Tin", "Lead"] or line[15] in ["Transactinide", "Lanthanide", "Actinide"]:
                if line[0] != "13":
                    toAppend.append("tm")
                else: toAppend.append("m")
            else:
                toAppend.append("m")
        elif line[13] == "yes" or line[15] == "Noble Gas":
            toAppend.append("n")
        elif line[14] == "yes":
            toAppend.append("s")
        else: toAppend.append("n/a")
        toAppend.append(line[27])
        toAppend.append(line[15])
        toAppend.append(line[17])
        toAppend.append(line[3])
        elements.append(toAppend)

tmcharges = {
    "Cr" : [2,3],
    "Mn" : [2,3],
    "Fe" : [2,3],
    "Co" : [2,3],
    "Ni" : [2,3],
    "Cu" : [1,2],
    "Zn" : [2],
    "Ag" : [1],
    "Cd" : [2],
    "Hg" : [1,2],
    "Sn" : [2,4],
    "Pb" : [2,4]
}

with open('acidNames.csv', 'r') as file:
    f = csv.reader(file)
    acidNames = {}
    for line in f:
        acidNames.update({line[0]: line[1]})

with open('ionNames.csv', 'r') as file:
    f = csv.reader(file)
    ionNames = {}
    for line in f:
        ionNames.update({line[0]: line[1]})

with open('tmNames.csv', 'r') as file:
    f = csv.reader(file)
    tmNames = {}
    for line in f:
        tmNames.update({line[0]: line[1]})

with open('polyatomicIons.csv', 'r') as file:
    f = csv.reader(file)
    polyatomicIons = {}
    for line in f:
        polyatomicIons.update({line[0]: line[1]})

with open('polyatomicIons.csv', 'r') as file:
    f = csv.reader(file)
    polyatomicCharges = {}
    for line in f:
        value = line[1].split(" ")
        polyatomicCharges.update({value[0]: value[1]})

with open('specificHeat.csv', 'r') as file:
    f = csv.reader(file)
    specificHeats = {}
    for line in f:
        specificHeats.update({line[0]: float(line[1])})

with open('heatOfPhysicalChangeGas.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    heatOfPhysicalChangesGas = {}
    for line in csv_reader:
        if line[1] == "H2O": heatOfPhysicalChangesGas.update({"H2O": [0,100, 6.01, 40.7, 2.1, 4.18, 1.7]})
        else: heatOfPhysicalChangesGas.update({line[1]: [float(line[2]) - 273.2, float(line[3]) - 273.2, float(line[4]), float(line[5]), float(line[6]), float(line[7]), float(line[8])]})

with open('heatOfPhysicalChangeLiquid.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    heatOfPhysicalChangesLiquid = {}
    for line in csv_reader:
        if line[1] == "H2O": heatOfPhysicalChangesLiquid.update({"H2O": [0,100, 6.01, 40.7, 2.1, 4.18, 1.7]})
        else: heatOfPhysicalChangesLiquid.update({line[1]: [float(line[2]) - 273.2, float(line[3]) - 273.2, float(line[4]), float(line[5]), float(line[6]), float(line[7]), float(line[8])]})

heatOfPhysicalChanges = {**heatOfPhysicalChangesGas, **heatOfPhysicalChangesLiquid}

with open("heatOfFormationSmall.json") as f:
    heatOfFormationsSmall = json.load(f)

with open("heatOfFormationLarge.json", "r") as f:
    heatOfFormationsLarge = json.load(f)

with open('liquids.csv', 'r') as f:
    file = csv.reader(f)
    next(file)
    liquidDensitys = {}
    for line in file:
        liquidDensitys.update({line[0] : float(line[2])})

with open("periodicTable.csv") as file:
    f = csv.reader(file)
    next(f)
    ENDict = {}
    for line in f:
        if (line[17]):
            ENDict.update({line[2]:round(float(line[17]), 1)})

with open("bondEnergies.csv") as f:
    file = csv.reader(f)
    next(file)
    bondEnergies = {}
    for line in file:
        bondEnergies.update({line[0]: int(line[1])})

with open("typeOfBond.csv") as f:
    file = csv.reader(f)
    next(file)
    bondTypeDict = {}
    for line in file:
        bondTypeDict.update({int(line[0]): [line[i].strip() for i in range(1,6)]})

electronegativities = {"H" : 2.2, "Li" : 1.0, "Na" : .9, "K" : .8, "Rb" : .8, "Cs" : .7, "Fr" : .7,
                "Be" : 1.5, "Mg" : 1.2, "Ca" : 1.0, "Sr" : 1.0, "Ba" : .9, "Ra" : .9,
                "B" : 2.0, "Al" : 1.5, "Ga" : 1.6, "In" : 1.7, "Tl" : 1.8,
                "C" : 2.6, "Si" : 1.9, "Ge" : 1.9, "Sn" : 1.8, "Pb" : 1.8,
                "N" : 3.1, "P" : 2.2, "As" : 2.0, "Sb" : 2.1, "Bi" : 1.9,
                "O" : 3.5, "S" : 2.6, "Se" : 2.5, "Te" : 2.3, "Po": 2.0,
                "F" : 4.0, "Cl" : 3.2, "Br" : 2.9, "I" : 2.7, "At" : 2.2,
                "He" : 0, "Ne" : 0, "Ar" : 0, "Kr" : 0, "Xe" : 0, "Rn" : 0}

with open("solubilities.csv") as f:
    file = csv.reader(f)
    solubilities = {}
    for line in file:
        solubilities.update({line[0] : [None if item == " -" else float(item) for item in line[1:]]})

Ratm = .08206 # Universal Gas Constant, atm
RkPa = 8.3145 # Universal Gas Constant, kPa
c = 3e8 # Speed of Light, m/s
h = 6.626e-34 # Planck Constant, Js
k = 2.178e-18 # Boltzman Constant, J (used for Bohr's Law)
eMass = 9.11e-31 # Mass of an electron, kg
