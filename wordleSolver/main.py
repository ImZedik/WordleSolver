class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


r = input(f'{bcolors.OKGREEN}Allow repeated letters? (y/n){bcolors.ENDC} > ')
repeated = r.lower() == 'y'
frequencies = {}

with open("words.txt", "r") as file:
    lines = file.readlines()

txt = [(i if not (i.endswith('\n')) else i[:-1]) for i in lines if len(i) == 6]
if not repeated:
    txt = [i for i in txt if len(set(i)) == len(i)]

total = 0
for i in txt:
    for j in i:
        total += 1
        if j in frequencies.keys():
            frequencies[j] += 1
        else:
            frequencies[j] = 1


def comp(c):
    return frequencies[c]


frequencies = {list(frequencies.keys())[list(frequencies.values()).index(i)]: i for i in
               (reversed(sorted(map(comp, frequencies))))}


def comp(c):
    chance = 1
    for i in c:
        chance *= frequencies[i] / total
    return chance


print(f"""{bcolors.BOLD}{bcolors.FAIL}HOW TO USE:
 1. Go to wordle
 2. Enter a word in the console
 3. Get the results of the query,
   0 for gray,
   1 for yellow,
   2 for green
   Example: 02201
 4. REPEAT
{bcolors.ENDC}""")

while True:
    txt = sorted(txt, key=comp)

    if len(txt) == 0:
        print(
            f'{bcolors.FAIL}{bcolors.BOLD}There is no word that exists based on your queries. (Did you enter something wrong?){bcolors.ENDC}')
        break

    if len(txt) == 1:
        print(f'{bcolors.BOLD}WE FOUND THE WORD! -> {bcolors.OKGREEN}{txt[0]}{bcolors.ENDC}')
        break

    print(txt)
    print(f'Suggested word: {bcolors.OKBLUE}{txt[-1]}{bcolors.ENDC} (Chance: {bcolors.FAIL}{round(1 / len(txt) * 100, 5)}%{bcolors.ENDC})')
    s = input('Enter your queried word: ')
    b = input(
        'Enter the result (READ INSTRUCTIONS): ')  # 0 for not in word, 1 for in word, 2 for in word and correct place
    for n, i in enumerate(b):
        if n == len(b) - b[::-1].index(i) - 1 or not repeated:
            if i == '0':
                txt = [i for i in txt if s[n] not in i]
            elif i == '1':
                txt = [i for i in txt if s[n] in i and s[n] != i[n]]
            elif i == '2':
                txt = [i for i in txt if s[n] == i[n]]

    print()
