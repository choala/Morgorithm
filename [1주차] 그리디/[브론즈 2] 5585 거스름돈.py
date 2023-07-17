price = int(input())
change = 1000 - price

coins = [500, 100, 50, 10, 5, 1]
coin_count = 0
for coin in coins:
    coin_count += change // coin
    change %= coin
    
print(coin_count)
