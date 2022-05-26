buyp = 0
buyps = []
sellp = 0
sellps = []
sellaverage = 0
sellq1 = 0
sellmin = 0
fixedcost = 0
profit = 0

while True: #finding fixed costs
    fixedcost = input('What is your fixed cost per item?')
    try:
        fixedcost = float(fixedcost)
        break
    except:
        print("That is not a number! Try again.")

while True: #loop to make list of selling prices
    buyp = input('Enter a buying price or done if finished: ')
    if buyp == 'done' or buyp == '':
        break
    try:
        buyps.append(float(buyp))
    except:
        print("That is not a number! Try again or type 'done' when finished")
        continue

if len(buyps) == 0: #checking to make sure user is not a bozo
    print("No prices entered.")
    quit()

while True: #loop to make list of selling prices
    sellp = input('Enter a selling price or done if finished: ')
    if sellp == 'done' or sellp == '':
        break
    try:
        sellps.append(float(sellp))
    except:
        print("That is not a number! Try again or type 'done' when finished")
        continue

if len(sellps) == 0: #checking to make sure user is not a bozo (again)
    print("No prices entered.")
    quit()

sellaverage = sum(sellps) / len(sellps) #finding average of selling prices
sellq1 = (sellaverage + min(sellps)) / len(sellps)

profit = sellq1 - min(buyps) #finding profit or loss

print('Minimum price to buy:', min(buyps))
print('Q1 of selling prices:', sellq1)
if min(buyps) + int(fixedcost) >= sellq1:
    print("Not a good deal! Don't buy this!")
    print("You would lose", profit, "dollars per item.")
else:
    print('Great deal! Buy this immediately!')
    print("You would earn", profit, "dollars per item.")