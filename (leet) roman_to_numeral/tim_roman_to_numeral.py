def romanToInt(self, s):
    """
    :type s: str
    :rtype: int
    """
    
    result = 0
    
    no_of_M = s.count("M") # 1000
    no_of_D = s.count("D") # 500
    no_of_C = s.count("C") # 100
    no_of_L = s.count("L") # 50
    no_of_X = s.count("X") # 10
    no_of_V = s.count("V") # 5
    no_of_I = s.count('I') # 1
    
        
    if s.count("CM") > 0:
        result += 900
        no_of_M -= 1
        no_of_C -= 1
    if s.count("CD") > 0:
        result += 400
        no_of_D -= 1
        no_of_C -= 1
    if s.count("XC") > 0:
        result += 90
        no_of_C -= 1
        no_of_X -= 1
    if s.count("XL") > 0:
        result += 40
        no_of_L -= 1
        no_of_X -= 1
    if s.count("IX") > 0:
        result += 9
        no_of_X -= 1
        no_of_I -= 1
    if s.count("IV") > 0:
        result += 4
        no_of_V -= 1
        no_of_I -= 1
    
    result += no_of_M * 1000 + no_of_D * 500 + no_of_C * 100 + no_of_L * 50 + no_of_X * 10 + no_of_V * 5 + no_of_I * 1

    return result
        