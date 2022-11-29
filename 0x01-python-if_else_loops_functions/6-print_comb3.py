#!/usr/bin/python3
combos = []
for i in range(0, 10):
	for j in range(1, 10):
		if j <= i:
			continue
		combos.append(str(i) + str(j))
print("{}".format(*combos), sep=", ", end="")
print()
