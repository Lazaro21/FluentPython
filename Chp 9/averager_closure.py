def make_averager():
    series = []
    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)
    return averager


avg = make_averager()
print(avg(15))
print(avg(25))
print(avg(37))