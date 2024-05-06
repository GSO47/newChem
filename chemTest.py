def atomsInCompound(equation : str):
    if len(equation) == 0: return {}
    if checkLast(equation): return {equation : 1}
    if equation[-1].isnumeric() and checkLast(equation[:-1]): return {equation[:-1] : int(equation[-1])}
    if equation[0] == "(":
        factor = int(equation[-1])
        inside = atomsInCompound(equation[1:-2])
        for key in inside: inside[key] *= factor
        return inside

    index = int(equation[1].islower())
    num = equation[index+1]
    num = 1 if not num.isnumeric() else int(num)

    ret = {equation[0:index + 1] : num}
    next_batch = atomsInCompound(equation[index + 2 - int(num == 1):])
    to_delete = []
    for key in next_batch:
        if key in ret: 
            to_delete.append(key)
            ret[key] += next_batch[key]
    for i in to_delete: del next_batch[i]
    ret.update(next_batch)
    return ret

def checkLast(equation : str): return len(equation) == 1 or (equation[-1].islower() and len(equation) == 2)

print(atomsInCompound("Cr2(Cr2O7)3"))