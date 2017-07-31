def score(game):
    result = 0
    frame = 1
    in_first_half = True
    for i in range(len(game)):
        if game[i] == '/':
            result += 10 - last
        else:
            result += get_value(game[i])
        # if not in_first_half:
            # frame += 1
        if frame < 10  and get_value(game[i]) == 10:
            if game[i] == '/':
                result += get_value(game[i+1])
            elif game[i] == 'X' or game[i] == 'x':
                result += get_value(game[i+1])
                if game[i+2] == '/':
                    result += 10 - get_value(game[i+1])
                else:
                    result += get_value(game[i+2])
        last = get_value(game[i])
        if not in_first_half:
            frame += 1
        if in_first_half == True:
            in_first_half = False
        else:
            in_first_half = True
        if game[i] == 'X' or game[i] == 'x':
            in_first_half = True
            frame += 1
    return result

def get_value(char):
    signs = {'1': 1, '2': 2, '3': 3, '4': 4, \
    '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, \
    "X" : 10, "x" : 10, "/": 10, "-" : 0}
    if char in signs.keys():
        return signs.get(char)
    else:
        raise ValueError()
