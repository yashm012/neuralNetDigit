def cost_function(expectedNum, actualNum):
    difference = expectedNum - actualNum
    cost = sum(difference ** 2)

    return difference, cost
