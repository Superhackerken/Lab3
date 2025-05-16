import price_info

def test_total_cost_shopping():

    test_list1={'apple' : 1.20, 'orange': 1.40}
    test_list2= {'apple': 5, 'orange': 5}
    test_arr = 13

    result = price_info.total_cost_shopping(test_list1, test_list2)

    assert (result == test_arr)

def test_cost_of_fruit():

    fruit = 'apple'
    quantity = 10
    test_arr = 12

    result = price_info.cost_of_fruits(fruit, quantity)

    assert (result == test_arr)
