def romanToInt(s: str) -> int:
    d = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "XL": 40,
        "L": 50,
        "XC": 90,
        "C": 100,
        "CD": 400,
        "D": 500,
        "CM": 900,
        "M": 1000
    }
    num = 0
    l = ["IV", "IX", "XL", "XC", "CD", "CM"]
    while s != "":
        if s[:2] not in l:
            num = num + d[s[0]]
            s = s[1:]
        else:
            num = num + d[s[:2]]
            s = s[2:]
    return num


romanToInt('MCMXCIV')
