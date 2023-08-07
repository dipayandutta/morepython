stocks = [7,1,5,3,6,4]


def solution(stocks):

    profit = 0
    min_ = stocks[0]

    for stock in stocks:
        min_ = min(min_,stock)
        profit = max(profit,stock-min_)

    return profit

if __name__ == '__main__':
    result = solution(stocks)
    print(result)
