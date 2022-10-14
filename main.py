set_of_numbers = [6, 5, 4, 3, 2, 1]

for line in set_of_numbers:
    for run in range(0, len(set_of_numbers) - 1):
        for i in range(0, len(set_of_numbers) - 1):
            if set_of_numbers[i] > set_of_numbers[i + 1]:
                set_of_numbers[i], set_of_numbers[i + 1] = set_of_numbers[i + 1], set_of_numbers[i]
            else:
                for k in range(0, len(set_of_numbers) - i):
                    if set_of_numbers[i] > set_of_numbers[i + k]:
                        set_of_numbers[i], set_of_numbers[i + k] = set_of_numbers[i + k], set_of_numbers[i]
        print(set_of_numbers)
