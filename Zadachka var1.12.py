from itertools import permutations

elements = ["А", "Б", "В", "Г", "Д"]
combinations = permutations(elements, 15)
valid_combinations = []
flag=True
def check_constraints(combination):
    if combination.count("А") < 2 or combination.count("А") > 7:
        return False
    if combination.count("Б") < 2 or combination.count("Б") > 7:
        return False
    if combination.count("В") < 2 or combination.count("В") > 7:
        return False
    if combination.count("Г") < 1 or combination.count("Г") > 3:
        return False
    if combination.count("Д") < 2 or combination.count("Д") > 3:
        return False
    if combination[7] in ["А", "Б", "В"]:
        return False
    if combination[0] == "Г":
        return False
    if combination[1] == combination[2] or combination[3] == combination[4] or combination[6] == combination[7] or combination[8] == combination[9] or combination[10] == combination[11]:
        return False
    if combination[10] == "Д" and combination[11] != "Д":
        return False
    if combination[11] == "Д" and combination[10] != "Д":
        return False
    return valid_combinations.append
    
print(valid_combinations)
