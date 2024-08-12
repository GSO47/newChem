from chemFuncts import acid, base, neutralization, compound

cmpd = compound("CdF2")
s_rx = cmpd.solubility_rx(mConc= 1)

print(s_rx.phaseStr())
print(s_rx.K_eq)
print(s_rx.eqExpression())
print(s_rx.reactEqConcs)
print(s_rx.prodEqConcs)