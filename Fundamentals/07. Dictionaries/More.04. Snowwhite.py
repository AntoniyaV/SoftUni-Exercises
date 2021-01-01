dwarfs = {}
info = input()

while not info == "Once upon a time":
    dwarf_name, dwarf_hat_color, dwarf_physics = info.split(" <:> ")
    dwarf_physics = int(dwarf_physics)

    if dwarf_hat_color not in dwarfs:
        dwarfs[dwarf_hat_color] = {}

    if dwarf_name not in dwarfs[dwarf_hat_color] or dwarfs[dwarf_hat_color][dwarf_name] < dwarf_physics:
        dwarfs[dwarf_hat_color][dwarf_name] = dwarf_physics

    info = input()

sorted_dwarfs = dict(sorted(dwarfs.items(), key=lambda x: -len(x[1])))

combined_dwarfs = {}
for dw_color, dw_info in sorted_dwarfs.items():
    for dw_name, dw_phys in dw_info.items():
        unique_key = dw_color + ' ' + dw_name

        if unique_key not in combined_dwarfs:
            combined_dwarfs[unique_key] = 0

        combined_dwarfs[unique_key] = dw_phys

sorted_by_physics = dict(sorted(combined_dwarfs.items(), key=lambda x: -x[1]))

for color_name, phys in sorted_by_physics.items():
    hat_color, name = color_name.split()
    print(f"({hat_color}) {name} <-> {phys}")
