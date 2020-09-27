dividend = .36
sharePrice = 36
sharesPerMonth = 80
desiredAnnualDividends = 12000.00
unpaidShares = 0.0
sharesTotal = 0.0
totalAmountInvested = 0.0
annualDividends = 0.0
investmentMonths = 0
#Starting with a large upfront purchase
#sharesTotal += 275
#totalAmountInvested += (275 * sharePrice)

while annualDividends < desiredAnnualDividends:
  sharesTotal += sharesPerMonth
  totalAmountInvested += (sharePrice * sharesPerMonth)
  if investmentMonths % 3 == 0:
    div = sharesTotal * dividend
    shares = div/sharePrice
    print(f"Month {investmentMonths + 1} Shares: {shares:.2f}")
    unpaidShares += shares
    sharesTotal += shares
    annualDividends = sharesTotal * dividend *4
  investmentMonths += 1

print(f"Total Shares: {sharesTotal:.2f}")
print(f"Unpaid Shares: {unpaidShares:.2f} (${unpaidShares * sharePrice:.2f})")
print(f"Quarterly Dividends: ${sharesTotal * dividend:.2f}")
print(f"Annual Dividends: ${sharesTotal * dividend * 4:.2f}")
print(f"Total Amount Invested: ${totalAmountInvested:.2f}")
print(f"Total Months Needed: {investmentMonths}")
print(f"Total Years Needed: {investmentMonths / 12:.2f}")