"""Hex Colour Lookup"""

COLOUR_NAME_TO_CODE = {
    "AliceBlue": "#f0f8ff",
    "AntiqueWhite": "#faebd7",
    "Aqua": "#00ffff",
    "Aquamarine": "#7fffd4",
    "Azure": "#f0ffff",
    "Beige": "#f5f5dc",
    "Bisque": "#ffe4c4",
    "Black": "#000000",
    "BlanchedAlmond": "#ffebcd",
    "Blue": "#0000ff"
}

colour_name = input("Enter colour name: ").lower()
while colour_name != "":
    found = False
    for key in COLOUR_NAME_TO_CODE:
        if key.lower() == colour_name:
            print(f"{key} has hex code {COLOUR_NAME_TO_CODE[key]}")
            found = True
            break
    if not found:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").lower()
