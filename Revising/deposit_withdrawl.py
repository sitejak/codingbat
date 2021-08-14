def deposits(list):
    total_balance = 0
    withdrawl_balance = 0
    deposit = []
    with_draw = []
    deposit1 = []
    withdraw1 = []

    for i in list:
        if i.startswith('D'):
            deposit.append(i)
        elif i.startswith('W'):
            with_draw.append(i)
    for i in deposit:
        x = i
        y = x.strip('D')
        deposit1.append(y)

    for i in with_draw:
        a = i
        b = a.strip('W')
        withdraw1.append(b)

    for i in deposit1:
        z = int(i)
        total_balance = z + total_balance
    for i in withdraw1:
        k = int(i)
        withdrawl_balance = k + withdrawl_balance
    total_amount = total_balance - withdrawl_balance
    print(total_amount)

deposits(["D300", "D600", "W400", "W200","D300"])
