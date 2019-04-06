# See: https://www.investopedia.com/terms/c/compounding.asp
# See: https://www.investopedia.com/terms/f/futurevalue.asp
# FV = future value
# PV = present value
# i = the annual interest rate
# n = the number of compounding periods per year
# t = the number of years
def get_future_value(pv, i, n, t):
  return pv * ((1 + (i/n)) ** t)
