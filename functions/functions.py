def make_tea(type_of_tea):
    print("Boiling water")
    print(f"Adding {type_of_tea} tea bag")
    print("waiting ...")
    result = f"{type_of_tea.capitalize()} Tea is ready"
    return result 

message = make_tea("herbal")
print("Stored message:",message)

