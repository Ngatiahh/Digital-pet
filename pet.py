class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} ate and feels happier!")

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} had a good nap!")

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} played and had fun!")
        else:
            print(f"{self.name} is too tired to play!")

    def get_status(self):
        print(f"\n🐾 {self.name}'s Status:")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")
        if self.tricks:
            print(f"Learned Tricks: {self.tricks}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")
        print()

    def train(self, trick):
        self.tricks.append(trick)
        print(f"{self.name} learned a new trick: {trick}!")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows these tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")

def main():
    pet_name = input("🐶 What would you like to name your pet? ")
    pet = Pet(pet_name)

    while True:
        print(f"\nWhat would you like {pet.name} to do?")
        print("1. Eat")
        print("2. Sleep")
        print("3. Play")
        print("4. Check Status")
        print("5. Train a new trick")
        print("6. Show learned tricks")
        print("7. Exit")

        choice = input("Enter your choice (1–7): ")

        if choice == '1':
            pet.eat()
        elif choice == '2':
            pet.sleep()
        elif choice == '3':
            pet.play()
        elif choice == '4':
            pet.get_status()
        elif choice == '5':
            trick = input("What trick would you like to teach? ")
            pet.train(trick)
        elif choice == '6':
            pet.show_tricks()
        elif choice == '7':
            print(f"Goodbye! {pet.name} will miss you 🐾")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")

if __name__ == "__main__":
    main()
