name = input("Enter operator name: ")
ref = input("Enter reference code: ")

bill = float(input("Enter total bill: "))
members = int(input("Enter number of members: "))

share = bill / members
penalty = bill * 0.10
finalBill = bill + penalty

year = ref[-4:]
check2026 = "2026" in ref

people = ["Eva", "Keziah", "John", "Diana"]

people[2] = "Jean"

people.append("Planet X")

print("\nUTILITY BILL SUMMARY")

print(f"Operator: {name}")
print(f"Reference Code: {ref}")
print(f"Year: {year}")
print(f"Has 2026: {check2026}")

print(f"\nBill: ₱{bill}")
print(f"Per Person: ₱{share}")
print(f"Penalty: ₱{penalty}")
print(f"Final Bill: ₱{finalBill}")

print(f"\nPeople List: {people}")

# login feature added
# final revision
