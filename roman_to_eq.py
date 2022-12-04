def roman_to_int(roman: str) -> int:
    romans = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    result = 0

    # Single digit number
    if len(roman) < 2:
        return romans[roman.upper()]

    # Iterate the string only once -> O(n)
    for i in range(len(roman) - 1):
        current_num = romans[roman[i].upper()]
        next_num = romans[roman[i + 1].upper()]
        if current_num < next_num:
            result -= current_num
        else:
            result += current_num
    else:  # Add the last number
        result += next_num

    return result


def roman2eq(s):
    s = s.strip("(").replace(")", "")
    print(s)
    s = s.split()
    print(s)
    a = ""
    for i in s:
        try:
            if i[0] == "-" and i[1] != " " and len(i) > 1:
                a += "-" + str(roman_to_int(i.replace("-", "")))
            elif i[0] == "-" and len(i) == 1:
                a += "-"
            else:
                a += str(roman_to_int(i))
        except:
            a += i
    return eval(a)
