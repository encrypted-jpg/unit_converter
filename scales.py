
def get_scale_factor(scale, a, b):
    if scale == "length":
        values_list = ["Nanometers", "Microns", "Millimeters", "Centimeters", "Meters", "Kilometers", "Inches", "Feets",
                       "Yards", "Miles"]
        fact_dict = {}
        for x in range(10):
            fact_dict[(x,x)] = 1

        fact_dict[(0,1)] = 0.001
        fact_dict[(0,2)] = 0.000001
        fact_dict[(0,3)] = 0.0000001
        fact_dict[(0,4)] = 0.000000001
        fact_dict[(0,5)] = 0.000000000001
        fact_dict[(0,6)] = 0.000000039370
        fact_dict[(0,7)] = 0.000000003280
        fact_dict[(0,8)] = 0.000000001093
        fact_dict[(0,9)] = 0.00000000000062
        for x in range(2,10):
            fact_dict[(1,x)] = fact_dict[(0,x)]*1000
        for x in range(3, 10):
            fact_dict[(2,x)] = fact_dict[(0,x)]*1000000
        for x in range(4, 10):
            fact_dict[(3,x)] = fact_dict[(0,x)]*10000000
        for x in range(5, 10):
            fact_dict[(4,x)] = fact_dict[(0,x)]*1000000000
        for x in range(6, 10):
            fact_dict[(5,x)] = fact_dict[(0,x)]*1000000000000
        for x in range(7, 10):
            fact_dict[(6, x)] = fact_dict[(0, x)]*25400000
        for x in range(8, 10):
            fact_dict[(7, x)] = fact_dict[(0, x)]*304800000
        for x in range(9,10):
            fact_dict[(8, x)] = fact_dict[(0, x)]*914400000
        if (a, b) in fact_dict:
            return fact_dict[(a, b)]
        else:
            cd = float(fact_dict[(b, a)])
            return float(1/cd)
    elif scale == "area":
        values_list = ["Square Millimeters", "Square Centimeters", "Square Meters", "Hectares", "Square Kilometers",
                       "Square Inches", "Square Feet", "Square Yards", "Acres", "Square Miles"]
        fact_dict = {}
        for x in range(10):
            fact_dict[(x, x)] = 1

        fact_dict[(0, 1)] = 0.01
        fact_dict[(0, 2)] = 0.000001
        fact_dict[(0, 3)] = 0.0000000001
        fact_dict[(0, 4)] = 0.000000000001
        fact_dict[(0, 5)] = 0.00155
        fact_dict[(0, 6)] = 0.0000107639
        fact_dict[(0, 7)] = 0.00000119599
        fact_dict[(0, 8)] = 0.000000000247105
        fact_dict[(0, 9)] = 0.000000000000386
        for x in range(2, 10):
            fact_dict[(1, x)] = float(fact_dict[(0, x)]/fact_dict[(0, 1)])
        for x in range(3, 10):
            fact_dict[(2, x)] = float(fact_dict[(0, x)]/fact_dict[(0, 2)])
        for x in range(4, 10):
            fact_dict[(3, x)] = float(fact_dict[(0, x)]/fact_dict[(0, 3)])
        for x in range(5, 10):
            fact_dict[(4, x)] = float(fact_dict[(0, x)]/fact_dict[(0, 4)])
        for x in range(6, 10):
            fact_dict[(5, x)] = float(fact_dict[(0, x)]/fact_dict[(0, 5)])
        for x in range(7, 10):
            fact_dict[(6, x)] = float(fact_dict[(0, x)]/fact_dict[(0, 6)])
        for x in range(8, 10):
            fact_dict[(7, x)] = float(fact_dict[(0, x)]/fact_dict[(0, 7)])
        for x in range(9, 10):
            fact_dict[(8, x)] = float(fact_dict[(0, x)]/fact_dict[(0, 8)])
        if (a, b) in fact_dict:
            return fact_dict[(a, b)]
        else:
            cd = float(fact_dict[(b, a)])
            return float(1 / cd)
    else:
        return 0

def scale_temp(a, b, ent):
    values_list = ["Celsius", "Fahrenheit", "Kelvin"]
    fact_dict = {}
    for x in range(0, 3):
        fact_dict[(x, x)] = ent
    fact_dict[(0, 1)] = float(ent*1.8 + 32)
    fact_dict[(1, 0)] = float((ent-32)*(5/9))
    fact_dict[(0, 2)] = float(ent + 273)
    fact_dict[(2, 0)] = float(ent - 273)
    fact_dict[(1, 2)] = float((float(5/9)*(ent - 32)) + 273)
    fact_dict[(2, 1)] = float((float(9/5)*(ent - 273)) + 32)
    return fact_dict[(a, b)]

# ab = get_scale_factor("area" , 4, 5)
# print(ab)