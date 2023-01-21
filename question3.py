brothers = ("Srikanth", "Santhosh", "Sandeep")
sisters = ("Sravani", "Samuktha", "Pravilika")
siblings = brothers + sisters
print(siblings)
print(len(siblings))
family_members = list(siblings)
family_members[2] = "Nageshwar Rao"
family_members[5] = "Padma"
print(family_members)
