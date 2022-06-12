import sys
number_count = sys.stdin.readline()[:-1]
numbers = list(map(int, sys.stdin.readline()[:-1].split()))
operators = list(map(int, sys.stdin.readline()[:-1].split()))
def expression(numbers=[], operators=[]):
    max_exp = -1000000001
    min_exp = 1000000001

    if len(numbers) == 1:
        return max(max_exp, numbers[0]), min(min_exp, numbers[0])

    if operators[0]>0:
        emax, emin = expression([numbers[0]+numbers[1]]+numbers[2:], [operators[0]-1, operators[1], operators[2], operators[3]])
        max_exp = max(max_exp, emax)
        min_exp = min(min_exp, emin)
    if operators[1]>0:
        emax, emin = expression([numbers[0]-numbers[1]]+numbers[2:], [operators[0], operators[1]-1, operators[2], operators[3]])
        max_exp = max(max_exp, emax)
        min_exp = min(min_exp, emin)
    if operators[2]>0:
        emax, emin = expression([numbers[0]*numbers[1]]+numbers[2:], [operators[0], operators[1], operators[2]-1, operators[3]])
        max_exp = max(max_exp, emax)
        min_exp = min(min_exp, emin)
    if operators[3]>0:
        emax, emin = expression([int(numbers[0]/numbers[1])]+numbers[2:], [operators[0], operators[1], operators[2], operators[3]-1])
        max_exp = max(max_exp, emax)
        min_exp = min(min_exp, emin)

    return max_exp, min_exp

print(*expression(numbers=numbers, operators=operators), sep="\n")