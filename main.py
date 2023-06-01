import art

def clear():
    import os
    def clear_console():
        os.system('cls' if os.name == 'nt' else 'clear')
    clear_console()

bidders = {}

def show_highest_bidder():
    highest_bid = max(bidders.values())
    highest_bidder = ''
    for key, value in bidders.items():
        if value == highest_bid:
            highest_bidder = key
    print(f'The winner is {highest_bidder} with a bid of ${highest_bid}')


print(art.logo)
print('Welcome to the secret auction program.')
while True:
    name = input('What is your name?: ')
    bid = input('What is your bid?: ')
    if name not in bidders:
        bidders[name] = bid
    more_bidders = input("'Are there any other bidders? Type 'yes' or 'no': ")
    if more_bidders == 'yes':
        clear()
        continue
    else:
        clear()
        break

show_highest_bidder()


