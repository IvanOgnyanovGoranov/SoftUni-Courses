def atom_shells(total_electrons):
    shells_with_electrons = []
    position = 0
    while total_electrons > 0:
        position += 1
        shell = 2 * (position ** 2)
        if shell > total_electrons:
            shell = total_electrons
        shells_with_electrons.append(shell)
        total_electrons -= shell
    return shells_with_electrons

number_of_electrons = int(input())
print(atom_shells(number_of_electrons))
