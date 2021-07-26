def countMinCount(value, coin_list):
    total_coin_count = 0
    details = list()
    coin_list.sort(reverse=True)

    for coin in coin_list:
        coin_num = value // coin
        total_coin_count += coin_num
        value -= coin_num * coin
        details.append([coin, coin_num])

    return total_coin_count, details


coin_list = [500, 100, 50, 10]
count = countMinCount(4720, coin_list)
print(count)
