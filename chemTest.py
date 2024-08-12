from chemFuncts import reaction
from random import randint

def percentError(new, orig):
    return abs((new - orig) / orig)

numTests = 10000
numComplexDelta = 0
numSuccess = 0

pList = []

for _ in range(numTests):
    rx = reaction("eq")

    newProd = [randint(0,40) / 20 + .5 for _ in rx.prodEqConcs]
    newReact = [randint(0,40) / 20 + .5 for _ in rx.reactEqConcs]

    # print(newProd)
    # print(newReact)

    rx.eqConcsFromIntial(newProd, newReact)
    
    pError = percentError(rx.reactionQuotient(), rx.K_eq)
    pList.append(pError)
    if pError < .01 and all([c > 0 for c in rx.prodEqConcs + rx.reactEqConcs]): 
        numSuccess += 1
    else:
        print(rx.K_eq)
        print(rx.phaseStr())
        print(pError)
        print(f"prod: {rx.prodEqConcs}")
        print(f"react: {rx.reactEqConcs}")
        print()
        pass

print(f"success rate: {numSuccess / numTests * 100}%")
print(f"error rate: {numComplexDelta / numTests * 100}%")
print(f"max error: {max(pList)}")

