import statistics
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print("min age =", ages[0], "max age =", ages[-1])
print("median age =", statistics.median(ages))
print("average age =", sum(ages)/len(ages))
print("range of ages =", max(ages)-min(ages))
