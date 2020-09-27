dividend = .36
sharePrice = 36
sharesPerMonth = 80
desiredAnnualDividends = 12000.00
unpaidShares = 0.0
contributedShares = 0.0
totalAmountContributed = 0.0
annualDividends = 0.0
investmentMonths = 0
#Starting with a large upfront purchase
contributedShares += 275
totalAmountContributed += (275 * sharePrice)

while annualDividends < desiredAnnualDividends:
  contributedShares += sharesPerMonth
  totalAmountContributed += (sharePrice * sharesPerMonth)
  if investmentMonths % 3 == 0:
    div = contributedShares * dividend
    shares = div/sharePrice
    print(f"Month {investmentMonths + 1} Shares: {shares:.2f}")
    unpaidShares += shares
    contributedShares += shares
    annualDividends = contributedShares * dividend *4
  investmentMonths += 1

print()
print(f"Unpaid Shares: {unpaidShares:.2f}")
print(f"Contributed Shares: {contributedShares:.2f}")
print(f"Overall Shares: {contributedShares + unpaidShares:.2f}")
print(f"Quarterly Dividends: ${contributedShares * dividend:.2f}")
print(f"Annual Dividends: ${contributedShares * dividend * 4:.2f}")
print(f"Unpaid Amount: ${unpaidShares * sharePrice:.2f}")
print(f"Total Amount Contributed: ${totalAmountContributed:.2f}")
print(f"Overall Amount Of Portfolio: ${(contributedShares + unpaidShares) * sharePrice:.2f}")
print(f"Total Months Needed: {investmentMonths}")
print(f"Total Years Needed: {investmentMonths / 12:.2f}")
