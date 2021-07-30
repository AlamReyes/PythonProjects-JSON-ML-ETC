import rdm

bars = ["Shoolbred's",
        "The Wren",
        "The Scratcher",
        "ACME",
        "Blind Barber"]

people = ["Mattan",
          "Chris",
          "that person you forgot to text back",
          "Kanye West",
          "Samuel L. Jackson",
          "Steve Wozniak"]
people.append("Luca")
people[4] = "Samuel L. Jackson's"
random_bar = rdm.choice(bars)
random_person1 = rdm.choice(people)
random_person2 = rdm.choice(people)

if random_person1 == random_person2:
    rdm.choice(people)
print(f"How about you go to {random_bar} with {random_person1} and {random_person2} ")
