COLOUR_CODES = {"Absolute Zero": "#0048ba","Acid Green":"#b0bf1a","AliceBlue": "#f0f8ff", 
                "Alizarin crimson":"#e32636","Amaranth":"#e52b50","Amber":"#ffbf00",
                "Amethyst":"#9966cc","AntiqueWhite": "#faebd7","AntiqueWhite1": "#ffefdb",
                "AntiqueWhite2": "#eedfcc","AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "#8b8378"}

colour_name = input("Enter a colour name: ")
while colour_name != "":
    print("The code for \"{}\" is {}".format(colour_name,
                                             COLOUR_CODES.get(colour_name)))
    colour_name = input("Enter a colour name: ")