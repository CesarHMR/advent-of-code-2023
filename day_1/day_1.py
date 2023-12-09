with open('./day_1/doc.txt') as file:
    doc = file.readlines()

codes = []

for line in doc:
    firstIndex = len(line)
    lastIndex = 0

    for index, string in enumerate(line):

        if(line[index].isdigit()):

            firstIndex = index if index < firstIndex else firstIndex
            lastIndex = index if index > lastIndex else lastIndex

    codes.append(int(str(line[firstIndex]) + str(line[lastIndex])))


print(sum(codes))