from datetime import date
from financial import xnpv,xirr

cashflows = [(date(2001,1,1),-1000000),
              (date(2002,2,2),500000),
              (date(2003,3,3),500000),
              (date(2000,1,2),-2000000),
              (date(2004,5,1),30000000)]

print(xnpv(0.12,cashflows))
print(xirr(cashflows,0.2))

