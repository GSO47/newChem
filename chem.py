from chemProblems import *
from inflect import engine

inflector = engine()
print("Instructions: \ntype 0 for a table of contents, then choose what you want to do. \nHit enter to get the answer (it doesn't autocheck) \ntype break to escape.\nWhen finding volume, assume all compounds are gasses, unless otherwise specified")
# When adding a new option, make sure to add to the more specific list (by unit) in settings 
modeList = [
        "SI Units", "Average atomic mass", "Missing Isotope Percentage", 
        "Formula to Name", "Name to Formula", "Molar Conversions", 
        "Calculate Percent Composition", "Percent Composition to equation (WIP)", "Mass of One Element in a Compound",
        "Complex Percent Composition to Equation",  "Solubility Rules", "Writing Chemical Equations",
        "Basic Stoichiometry", "Percent Yield/Limiting Reagent", "Heat of Physical Change",
        "Coffee Cup Calorimetry", "Bomb Calorimetry", "Average Kinetic Energy",
        "Effusion Rates", "Gas Laws", "Gas Stoiciometry",
        "Electron configuration", "Nobel Gas Shorthand", "Paramagnetic vs Diamagnetic",
        "Quantum Numbers", "Basic Waves",  "Bohr's Law",
        "De Broglie for electrons", "De Broglie in general", "Heisenburg uncertainty principle",
        "Identifying types of waves", "Harder Bohr's Law", "Atomic Size",
        "Ion Size", "Ionization Energy", "Electronegativity",
        "Electron Affinity", "All Periodic Trends", "Lattice Energy",
        "Lewis Dot Structure", "VSEPR", "Bond Order", 
        "Sigma and Pi Bonds", "Bond Energies", "Enthalpy from Bond Energies",
        "Solubility Calculations", "Determining Saturation", "Dilution",
        "Solutions Unit Conversions (Aqueous)", "Solutions Unit Conversions (general)", "Colligative Properties", 
        "Molar Mass From bp/fp", "Henry's Law", "Reactions with Solubility Units", 
        "Hydrates", "Polar vs Nonpolar"
        ]

rxType = ""
polyatomicIonChoices = [i for i in list(polyatomicIons.keys())]
randomChoices = [i+1 for i in range(0,len(modeList))]
originalChoices = randomChoices.copy()
randomSelected = False
selected = "undef"
answer = "ERROR"

while True:
    settings = False
    if randomChoices != originalChoices: 
        randomSelected = True
        selected = "random"

    if randomSelected: 
        selected = random.choice(randomChoices)
    elif selected == "-1" or selected == "undef": 
        bad = True
        b = False # break variable
        while bad:
            if selected != "random": selected = input("Enter: ")
            if selected == "random" or selected == "r":
                selected = random.choice(randomChoices)
                randomSelected = True
                break
            if selected == "break": 
                b = True
                break
            elif selected == "settings" or selected == "-1":
                settings = True
                break
            elif selected == "p" or selected == "polyatomic":
                while True: 
                    if getAnswer(polyatomicIonTest(polyatomicIonChoices)) == "break": break
            elif selected == "0":
                for i, mode in enumerate(modeList):
                    print(f"{i+1}. {mode}")
                continue                
            else:
                try:
                    selected = int(selected)
                    if selected not in randomChoices: raise Exception
                    bad = False
                except:
                    print("bad")
    
    if b: break

    if settings:
        choiceList = ["Change molecule frequency", "Change reaction type", "Star polyatomic ions", "Choose Unit"]
        while True:
            choice = input("What setting do you want to change? (0 for options): ")
            if choice == "0":
                for i, tempChoice in enumerate(choiceList):
                    print(str(i+1) + ". " + tempChoice)
            elif choice == "1":
                chanceList = input("How often do you want to see each type of compound (ternary ionic, acids, binary, diatomic) (use 5 ints (less than 10 and no spaces) to show the ratios): \n")
                chanceList = [i for i in chanceList if i != "," and i.isdigit()]
                while len(chanceList) < 5:
                    chanceList.extend(0)
                if len(chanceList) > 5: chanceList = chanceList[0,5]
                break
            elif choice == "2":
                rxType = input("What type of reaction do you want: synthesis, decomposition, combustion, single replacement, or double replacement (hit enter to reset): \n")
                if rxType in ["synthesis", "decomposition", "combustion", "single replacement", "double replacement", "special"]: 
                    print("\nSetting changed")
                break
            elif choice == "3":
                for i, ion in enumerate(list(polyatomicIons.keys())):
                    print(f"{i}. {ion}")
                choices = input("Choose which ions to include (ex. 1, 4, 9). Type -1 for presets: ")
                if choices == "break": break
                if choices == "-1":
                    presets = {"difficult" : [0, 4, 5, 11, 12, 13, 28, 31, 35, 42, 43, 44, 45], 
                                "ates\ites" : [0, 2, 3, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45],
                                "all" : [i for i in range(0,len(list(polyatomicIons.keys())))]}
                    for i, preset in enumerate(list(presets.keys())): print(f"{i+1}. {preset} : {presets.get(preset)}")
                    choices = list(presets.values())[int(input("Choose a preset: ")) -1]
                else:
                    choices = choices.replace(" ", "").split(",")
                polyatomicIonChoices = [list(polyatomicIons.keys())[int(i)] for i in choices]
                print("\ndone")
                break
            elif choice == "4":
                for i, mode in enumerate(modeList):
                    print(f"{i+1}. {mode}")
                choices = input("Choose what modes to include (ex. 1, 4, 9). Type -1 for presets: ")
                if choices == "break": break
                if choices == "-1":
                    presets = { "All" : originalChoices,
                                "Math Review" : [1],
                                "Chapter 6": [2, 3, 4, 5],
                                "Chapter 7": [6, 7, 8, 9, 10],
                                "Chapter 8": [11,12],
                                "Chapter 9": [13, 14],
                                "Chapter 10 and 11": [15, 16, 17],
                                "Semester 1": [i for i in range(1, 18)],
                                "Chapter 12" : [18, 19, 20, 21],
                                "Chapter 13" : [i for i in range(22, 33)],
                                "Chapter 14-16" : [i for i in range(33, 46)],
                                "Chapter 17-18" : [i for i in range(46, 57)]}
                    for i, preset in enumerate(list(presets.keys())): print(f"{i+1}. {preset}: {presets.get(preset)}")
                    choices = list(presets.values())[int(input("Choose a preset: ")) -1]
                else:
                    choices = choices.replace(" ", "").split(",")
                randomChoices = choices
                selected = "random"
                randomSelected = True
                answer = "undef"
                print(randomChoices)
                print("\ndone")
                break
            elif choice == "break": break
            else: 
                print("bad")
                break
    else:
        func = inflector.number_to_words(selected).replace("-","")
        answer = getAnswer(eval(func + "(rxType = rxType)"))

    if answer == "break": 
        randomSelected = False
        randomChoices = originalChoices.copy()
        selected = "undef"
