import math, sys, getopt

a, b, c, d, e = 0, 0, 0, 0, 0
args = sys.argv
arg_list = args[1:]
long_opts = ["type=", "payment=", "principal=", "periods=", "interest="]
try:
    arguments, values = getopt.getopt(arg_list, "", long_opts)
except:
    print("Error")

if len(arguments) != 4:
    print("Incorrect parameters")
    sys.exit(2)

for current_arg, current_value in arguments:
    if current_arg in ("--type") and (current_value == "annuity" or current_value == "diff"):
        calc_type = current_value
        a += 1
    elif current_arg in ("--payment") and float(current_value) > 0:
        payment = int(current_value)
        b += 1
    elif current_arg in ("--principal") and float(current_value) > 0:
        principal = int(current_value)
        c += 1
    elif current_arg in ("--periods") and float(current_value) > 0:
        periods = int(current_value)
        d += 1
    elif current_arg in ("--interest") and float(current_value) > 0:
        interest = float(current_value)
        e += 1
    else:
        print("Incorrect parameters")
        sys.exit(2)

try:
    interest
except:
    print("Incorrect parameters")
    sys.exit(2)
    
if a > 1 or b > 1 or c > 1 or d > 1 or e > 1:
    print("Incorrect parameters")
    sys.exit(2)

overpaiment = 0

if 	calc_type == "diff":
	i = interest / 100 / 12
	for x in range(1, periods + 1):
		diff_mth_pay = principal / periods + i * (principal - ((principal * (x - 1) / periods)))
		diff_mth_pay = int(math.ceil(diff_mth_pay))
		overpaiment += diff_mth_pay
		print(f"Month 1: payment is {diff_mth_pay}")
	overpaiment = overpaiment - principal
	print(f"\nOverpayment = {overpaiment}")
elif b == 1 and c == 1 and e == 1:
	i = (interest / 100) / 12
    periods = math.log(payment / (payment - i * principal), 1 + i)
    a = int(round(periods // 12))
    b = int(round(periods % 12)) if round(periods % 12) > periods % 12 else int(round(periods % 12) + 1)
    if (b == 12):
        a = a + 1;
        print(f"It will take {a}", "years" if round(periods // 12) != 1 else "year", "to repay this loan!")
    else:
        print(f"It will take {a}", "years" if round(periods // 12) != 1 else "year",
        "and", b, "months" if round(periods % 12) != 1 else "month", "to repay this loan!")
    k = payment * int(math.ceil(periods)) - principal
    print(f"Overpayment = {k}")
elif c == 1 and d == 1 and e == 1:
    i = (interest / 100) / 12
    x = math.pow(1 + i, periods)
    payment = (i * principal * x) / (x - 1)
    i = int(round(payment)) if round(payment) > payment else int(round(payment) + 1)
    print(f"Your annuity payment = {i}!")
    k = i * periods - principal
    print(f"Overpayment = {k}")
elif b == 1 and d == 1 and e == 1:
    i = (interest / 100) / 12
    x = math.pow(1 + i, periods)
    principal = payment * (x - 1) / (i * x)
    a = int(round(principal))
    print(f"Your loan principal = {a}!")
    k = payment * periods - a
    print(f"Overpayment {k}")
