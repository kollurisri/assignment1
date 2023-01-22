it_companies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(len(it_companies))
it_companies.add("twitter")
print(it_companies)
it_companies.update({"Sitel", "Knoah"})
print(it_companies)
it_companies.remove("Knoah")
print(it_companies)

print(A|B)
print(A.intersection(B))
print(A.issubset(B))
print(A.symmetric_difference(B))
del A,B
age_set = set(age)
print(len(age_set)<len(age))

