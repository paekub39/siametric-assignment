def get_maximum_profit(item_price_list, maximum_transaction):
    if maximum_transaction == 0:
        return 0
    maximum_profit = 0
    remaining_transaction = maximum_transaction - 1
    for i in range(len(item_price_list) - 1):
        buy = item_price_list[i]
        for j in range(i + 1, len(item_price_list), 1):
            sell = item_price_list[j]
            item_price_list_temp = item_price_list[j + 1: len(item_price_list)]
            current_profit = sell - buy
            future_profit = get_maximum_profit(item_price_list_temp, remaining_transaction)
            total_profit = current_profit + future_profit
            if total_profit > maximum_profit:
                maximum_profit = total_profit

    return maximum_profit


def get_maximum_profit_at_most_two_transaction(item_price_list):
    at_most_transaction = 2
    max_profit = get_maximum_profit(item_price_list, at_most_transaction)
    return max_profit


if __name__ == '__main__':
    prices = [3, 3, 5, 0, 0, 3, 1, 4]
    profit = get_maximum_profit_at_most_two_transaction(prices)
    print(profit)
