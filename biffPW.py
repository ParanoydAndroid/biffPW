import itertools


def main():
    base_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    permutations = itertools.permutations(base_string, 3)
    count = 0

    with open('biff_passwords.txt', 'a+') as f:
        for p in permutations:
            print(f'*****Using permutation {p}\n*****')

            for i in range(2187):
                i_tern = convert_to_base(i, 3)
                candidate = f'{i_tern:>07}'

                for j in range(3):
                    candidate = candidate.replace(str(j), p[j])

                f.write(candidate)
                f.write('\n')

                count += count
                print(f'Processed password {count}: {candidate}\n')


def convert_to_base(original, new_base):
    # Pulled from https://stackoverflow.com/questions/34559663/convert-decimal-to-ternarybase3-in-python
    if original == 0:
        return '0'

    nums = []
    while original:
        original, r = divmod(original, new_base)
        nums.append(str(r))

    return ''.join(reversed(nums))


if __name__ == '__main__':
    main()
