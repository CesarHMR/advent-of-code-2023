from enum import Enum
with open('./day_2/doc.txt') as file:
    games = file.readlines()

id_sum = 0

max_amount = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

for g in games:
    game_id = int(g.split(':')[0].split()[1])
    rounds = g.split(':')[1].split(';')

    colors_amount = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }

    for r in rounds:
        sub_rounds = r.split(',')
      
        for s in sub_rounds:
            amount = int(s.split()[0])
            color = s.split()[1]
            
            colors_amount[color] = amount if amount > colors_amount[color] else colors_amount[color]

    is_possible = True

    for c in max_amount:
        if colors_amount[c] > max_amount[c]:
            is_possible = False
            break

    if is_possible:
        id_sum += game_id

print(id_sum)