daily_food = [0, 150, 150]

def count_food(days):
    sum = 0
    for i in range(1,31):
        if i in days:
            sum = sum + daily_food[i-1]
    return sum


print(count_food([1]))
print(count_food([2, 3]))
