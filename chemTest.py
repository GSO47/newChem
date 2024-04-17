from chemFuncts import *

cmpd = solution(compound("NaCl"), moles_solute = 1, total_volume = 1)
print(cmpd)
print(f"moles_solute: {cmpd.moles_solute}")
print(f"moles_solvent: {cmpd.moles_solvent}")
print(f"volume: {cmpd.volume}")
print(f"solute_density: {cmpd.solute_density}")
print(f"solvent_density: {cmpd.solvent_density}")
print(f"molality: {cmpd.molality()}")
print(f"mole fraction (solute): {cmpd.moleFractions()}")
print(f"mole fraction (solvent): {cmpd.moleFractions(solute = False)}")
print(f"% (m/v): {cmpd.pMV()}")
print(f"% (v/v): {cmpd.pVV()}")
print(f"bp: {cmpd.boilingPoint()}")
print(f"fp: {cmpd.freezingPoint()}")

