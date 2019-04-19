# See: https://www.investopedia.com/terms/c/compounding.asp
# See: https://www.investopedia.com/terms/f/futurevalue.asp
# FV = future value
# PV = present value
# i = the annual interest rate
# n = the number of compounding periods per year
# t = the number of years
def get_future_value(pv, i, n, t):
  return pv * ((1 + (i/n)) ** t)

# See: https://www.investopedia.com/terms/e/enterprisevalue.asp
# EV = enterprise value
# MC = market capitalization
# d = total debt
# c = cash and cash equivalent
def get_enterprise_value(mc, d, c):
  return mc + d - c
