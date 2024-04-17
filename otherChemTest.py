from chemFuncts import reaction, randomRx

rx = reaction(randomRx(["double replacement", "special"]))
rx.balanceEq()
rx.formatRxList()
print(rx)