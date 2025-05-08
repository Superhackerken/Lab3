import Lab2.bmi as bmi

def test_bmi_normal_weight():
    result = []
    weight = 57
    height = 1.73
    test_arr = 0
    result = bmi.calculate_bmi(weight, height)

    assert (result == test_arr)

def test_bmi_over_weight():
    result = []
    weight = 90
    height = 1.73
    test_arr = 1
    result = bmi.calculate_bmi(weight, height)

    assert (result == test_arr)

def test_bmi_under_weight():
    result = []
    weight = 15
    height = 1.73
    test_arr = -1
    result = bmi.calculate_bmi(weight, height)

    assert (result == test_arr)

