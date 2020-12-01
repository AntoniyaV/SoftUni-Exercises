electrons = int(input())

electron_shells = []
n_shell = 0

while electrons > 0:
    n_shell += 1
    electrons_in_current_shell = 2 * n_shell ** 2

    if electrons >= electrons_in_current_shell:
        electron_shells.append(electrons_in_current_shell)
    else:
        electron_shells.append(electrons)

    electrons -= electrons_in_current_shell

print(electron_shells)