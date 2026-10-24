print("Where should I look?")
location = input()

if location == "in the bedroom":
    print("Where in the bedroom should I look?")
    spot = input()
    # decyzja zagnieżdżona: konkretne miejsce w sypialni
    if spot == "under the bed":
        print("Found some shoes but no phone")
    else:
        print("Found some mess but no phone.")

# --- pokój: łazienka ---
elif location == "in the bathroom":
    print("Where in the bathroom should I look?")
    spot = input()
    # decyzja zagnieżdżona: konkretne miejsce w łazience
    if spot == "in the bathtub":
        print("Found a rubber duck but no phone")
    else:
        print("Found bathroom stuff but no phone.")

# --- pokój: salon (tu jest telefon) ---
elif location == "in the living room":
    print("Where in the living room should I look?")
    spot = input()
    # decyzja zagnieżdżona: konkretne miejsce w salonie
    if spot == "on the table":
        print("Yes! I found my phone!")
    else:
        print("Found some stuff but no phone.")

# --- miejsce nieznane programowi ---
else:
    print("I do not know where that is but I will keep looking.")