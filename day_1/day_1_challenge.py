digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

def getFirstDigit(code: str) -> str:
    digitDic = {}
    for digit in digits:
        if code.find(digit) > -1:
            digitDic[digit] = code.find(digit)
    
    first = ''

    for key in digitDic:
        if first == '':
            first = key
        elif digitDic[key] < digitDic[first]:
            first = key

    
    firstIndex = len(code) + 10

    for index, string in enumerate(code):

        if(code[index].isdigit()):

            firstIndex = index if index < firstIndex else firstIndex
    
    return code[firstIndex] if first == '' or firstIndex < digitDic[first] else digits[first]

def getLastDigit(code: str) -> str:
    digitDic = {}
    for digit in digits:
        if code.rfind(digit) > -1:
            digitDic[digit] = code.rfind(digit)
    
    last = ''

    for key in digitDic:
        if last == '':
            last = key
        elif digitDic[key] > digitDic[last]:
            last = key

    
    lastIndex = -1

    for index, string in enumerate(code):

        if(code[index].isdigit()):

            lastIndex = index if index > lastIndex else lastIndex
    
    return code[lastIndex] if last == '' or lastIndex > digitDic[last] else digits[last]

with open('./day_1/doc.txt') as file:
    doc = file.readlines()

codes = []

for line in doc:

    code = int(getFirstDigit(line) + getLastDigit(line))
    codes.append(code)


print("code: ", sum(codes))
print("length: ", len(codes))

# count = 1
# for c in codes:
#     print(count, ": ", c)
#     count += 1