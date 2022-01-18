class ProfitInfo:

    def __init__(self, x, y, profit):
        self.X = x
        self.Y = y
        self.Profit = profit


def find_min_max(data):
    data_len = len(data)
    if data_len < 2:
        return 0
    min = data[0]
    profit_list = []

    count = 1
    max = 0
    if max < data[1]:
        max = data[1]
    current_profit = ProfitInfo(0, 1, max-min)
    while count < data_len:
        if min > data[count]:
            min = data[count]
        max = data[count]
        if current_profit.Profit >= max - min:
            current_profit.Y = count
        else:
            if current_profit.Profit < 0:
                current_profit.Profit = 0
            profit_list.append(current_profit)
            temp = ProfitInfo(count, count, max-min)
            current_profit = temp
        count = count + 1

    profit_list.append(current_profit)

    profit_list_pointer = len(profit_list) - 1
    count = data_len - 1
    max = data[data_len - 1]
    max_profit = ProfitInfo(count, count, current_profit.Profit)
    while count > 0:
        min = data[count]
        if max < data[count]:
            max = data[count]

        if not (current_profit.Y >= count-1 >= current_profit.X):
            current_profit = profit_list[profit_list_pointer - 1]

        temp_profit = profit_list[profit_list_pointer]

        previous_max_profit = 0
        if temp_profit.Y >= count-1 >= temp_profit.X:
            previous_max_profit = temp_profit.Profit
        else:
            temp_profit = profit_list[profit_list_pointer - 1]
            previous_max_profit = temp_profit.Profit
            profit_list_pointer = profit_list_pointer - 1

        if previous_max_profit + (max - min) > max_profit.Profit:
            max_profit = ProfitInfo(count-1, count, previous_max_profit + (max - min))

        count = count - 1

    return max_profit.Profit


if __name__ == '__main__':
    prices = [3, 3, 5, 0, 0, 3, 1, 4]
    profit = find_min_max(prices)
    print(profit)
