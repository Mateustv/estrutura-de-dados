def romanToInt(s: str):
    return (s.count("I") + s.count("V")*5 + s.count("X")*10 + s.count("L")*50 + s.count("C")*100 + s.count("D")*500 + s.count("M")*1000
            -
            s.count("IV")*2 - s.count("IX")*2 - s.count("XL")*20 - s.count("XC")*20 - s.count("CD")*200 - s.count("CM")*200)
a = romanToInt("MMD")
print(a)