def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count
    return averager


avg = make_averager()
print(avg(15))
print(avg(25))
print(avg(37))
print(avg(7))