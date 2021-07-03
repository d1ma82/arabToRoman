from sys import argv

scrypt, first, second = argv

def to_arab(roman):
    last_val = 0
    result = 0
    for i in range(len(roman) - 1 , -1, -1):
        if   roman[i] == 'C' : cur_val = 100
        elif roman[i] == 'D' : cur_val = 500
        elif roman[i] == 'I' : cur_val = 1
        elif roman[i] == 'L' : cur_val = 50
        elif roman[i] == 'M' : cur_val = 1000
        elif roman[i] == 'V' : cur_val = 5
        elif roman[i] == 'X' : cur_val = 10
        else: break

        if cur_val < last_val: result -= cur_val
        else:                  result += cur_val
        
        last_val = cur_val
    return result  


def to_roman(arabic):
    key = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    value = ["I", "IV", "V", "IX", "X", "XL", "L", "XC","C", "CD", "D", "CM", "M"]
    
    result = ""
    i = len(key) - 1;
    
    while arabic > 0:
        while key[i] > arabic: i -= 1
        arabic -= key[i]
        result += value[i]           
    return result

def to_roman_cort(arabic):
    dic = [(1, "I"), (4, "IV"), (5, "V"), (9, "IX"), (10, "X"), (40, "XL"), (50, "L"), \
           (90, "XC"), (100, "C"), (400, "CD"), (500, "D"), (900, "CM"), (1000, "M")]
    
    result = ""
    for key, val in reversed(dic):
        while arabic >= key:
            print(key)
            arabic -= key
            result += val
    return result               

def to_roman_dic(arabic):
    dic = {1:"I", 4:"IV", 5:"V", 9:"IX", 10:"X", 40:"XL", 50:"L", 90:"XC", \
           100:"C", 400:"CD", 500:"D", 900:"CM", 1000:"M"}

    result = ""
    for key in reversed(dic):
        while arabic >= key:
            print(key)
            arabic -= key
            result += dic[key]
    return result

def main():
    print(scrypt)
    if int(first) == 1:
        print(second + ' - ' + to_arab(second))
    else:
            print(second + ' - ' + to_roman_dic(int(second)))

main()            
          
