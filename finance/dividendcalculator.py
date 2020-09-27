dividend = .36
investmentYears = 10
investmentMonths = investmentYears * 12
sharePrice = 36
sharesPerMonth = 80
unpaidShares = 0.0
contributedShares = 0.0
totalAmountContributed = 0.0
counter = 0
#Starting with a large upfront purchase
contributedShares += 128
totalAmountContributed += (128 * sharePrice)

while counter < investmentMonths:
    contributedShares += sharesPerMonth
    totalAmountContributed += (sharePrice * sharesPerMonth)
    if counter % 3 == 0:
        div = contributedShares * dividend
        shares = div/sharePrice
        print(f"Month #{counter + 1} Shares: {shares:.2f}")
        unpaidShares += shares
    counter += 1

print()
print(f"Unpaid Shares: {unpaidShares:.2f}")
print(f"Contributed Shares: {contributedShares:.2f}")
print(f"Overall Shares: {contributedShares + unpaidShares:.2f}")
print(f"Quarterly Dividends: ${contributedShares *dividend:.2f}")
print(f"Annual Dividends: ${contributedShares * dividend * 4:.2f}")
print(f"Unpaid Amount: ${unpaidShares * sharePrice:.2f}")
print(f"Total Amount Contributed: ${totalAmountContributed:.2f}")
print(f"Overall Amount Of Portfolio: ${(contributedShares + unpaidShares) * sharePrice:.2f}")