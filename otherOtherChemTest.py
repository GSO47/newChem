from chemFuncts import half_reaction, compound

# init = compound('Cr2O7_-2')
# final = compound("Cr_+3")
# redox = half_reaction(init, final)

# print(redox)

init = compound('I-')
final = compound("IO3-")
redox = half_reaction(init, final)

print(redox)