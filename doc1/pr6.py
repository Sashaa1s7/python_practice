persones = {}

def add_friends(name_of_person, list_of_friends):
    tmp = persones.get(name_of_person)
    if tmp: persones[name_of_person] = tmp +list_of_friends
    else: persones[name_of_person] = list_of_friends
    persones[name_of_person] = list(set(persones[name_of_person]))
    persones[name_of_person].sort()
    


def are_friends(name_of_person1, name_of_person2):
    if name_of_person2 in persones[name_of_person1]: return True
    else: return False


def print_friends(name_of_person):
    print(persones[name_of_person])


add_friends("Алла", ["Марина", "Иван"])
print(are_friends("Алла", "Мария"))
add_friends("Алла", ["Мария"])
print(are_friends("Алла", "Мария"))
print_friends("Алла")
