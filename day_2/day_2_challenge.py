from enum import Enum
with open('./day_2/doc.txt') as file:
    games = file.readlines()

power_sum = 0

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

    power = colors_amount["red"] * colors_amount["green"] * colors_amount["blue"]

    power_sum += power

print(power_sum)