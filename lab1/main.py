import lab1.modules.series as series

series_name = "(n/n+1)^(n^2)"
e = float(input("Input e (acceptable error): "))
n = int(input("Input n (max element index to check for): "))

series.max_n = n

limits_on = series.check_limit(e)

print("Checking necessary conditions for convergent series")

limits = False

if limits_on != -1:
    print("Series " + series_name + " limits on " + str(limits_on) + "th element. Continue testing")
    limits = True
else:
    print("Series " + series_name + " does not limits to " + str(e) + " at first " + str(series.max_n) +
          " elements. Not convergent series.")

print("\n")

if limits:
    print("Checking ratio test")
    result = series.ratio_test(e)

    if result > 1:
        natural_result = "divergent"
    elif result < 1:
        natural_result = "convergent"
    else:
        natural_result = "uncertainty"

    print("Result for " + series_name + " in ratio test is q=" + str(result) + ". Series is " + natural_result)

print("\n")

print("Ending script. Thank you for using 'Not useful at all 2k17 series tester © IT41-group5'")

