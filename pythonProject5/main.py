import random

dict = {
    "occupations": ["dog trainer", "florist", "pilot", "nurse", "farmer", "figure skater", "engineer", "teacher",
                    "chef",
                    "soccer player", "artist", "bus driver", "dentist", "zookeeper", "baker", "designer", "doctor",
                    "singer",
                    "musician", "comedian", "performer", "astronaut", "baseball player", "firefighter", "vet",
                    "flight attendant"],
    "alphabet": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                 "U", "V", "W", "X", "Y", "Z"]
}
occupations = ["dog trainer", "florist", "pilot", "nurse", "farmer", "figure skater", "engineer", "teacher", "chef",
               "soccer player", "artist", "bus driver", "dentist", "zookeeper", "baker", "designer", "doctor", "singer",
               "musician", "comedian", "performer", "astronaut", "baseball player", "firefighter", "vet",
               "flight attendant"]
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
            "V",
            "W", "X", "Y", "Z"]
called_list = []
build_a_list = []
running = True


def letsDoItAtRandom(desired_list):
    global called_list
    global build_a_list
    global running
    while running:
        passit = input("")
        if passit == "quit":
            running = False
        elif passit == "list":
            print(f"The following items have been called:")
            for items in called_list:
                print(items)
            print("")
            print("")
        elif passit == "help":
            print(
                "Type 'quit' to end program, type 'list' to show all called items, and any other entry will randomly draw the next item")
        else:
            kevin = random.choice(desired_list)
            print(kevin)
            called_list.append(kevin)
            desired_list.remove(kevin)


print("")
print("")
print("                                      Welcome to the Uozaki English Randomizer!")
print(
    "Type 'quit' to end program, type 'list' to show all called items, and any other entry will randomly draw the next item")
print(dict.keys())
program = letsDoItAtRandom(occupations)
