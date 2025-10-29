contacts1 = {

    "Anu":"9089786856",
    "Teena":"9812345677"
}
contacts2 = {
    "Ken":"9988776655",
    "Abi":"9998887771"
}
print("contacts1:",contacts1)
print("contacts2:",contacts2)
merged_contacts = contacts1.copy()
merged_contacts.update(contacts2)
print("merged contacts:")
print(merged_contacts)
