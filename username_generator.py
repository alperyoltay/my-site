import random, string

output_file = "usernames.txt"
amount = int(input("\n kaç tane oluscak: "))
character_amount = int(input("kaç karakter: "))

for i in range(amount):
    generated = ("").join(random.choices(string.ascii_letters + string.digits, k = character_amount))
    print(generated)
    with open(output_file, "a") as f:
        f.write(generated + "\n")
input()