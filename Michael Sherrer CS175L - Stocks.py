#Michael Sherrer
#Stocks
#CS 175L 01
#Prof. Eckert

amount_of_shares=float(input('Enter amount of shares purchased: '))
price_per_share=float(input('Enter price of each share: '))
purchase_commission=float(input('Enter purchase comission as a decimal: '))
shares_sold=int(input('Enter number of shares sold: '))
selling_price=float(input('Enter the price per share that was sold: '))
selling_commission=float(input('Enter selling commision paid as a decimal: '))

amount_paid=float(amount_of_shares*price_per_share)
commission_paid_purchase=float(amount_paid*purchase_commission)
total_selling_price=float(shares_sold*selling_price)
commission_paid_sale=float(total_selling_price*selling_commission)
profit=float(total_selling_price-amount_paid-commission_paid_purchase-commission_paid_sale)

print('Amount paid for the stock: {0}{1}'.format('$',amount_paid))
print('Commission paid on the purchase: {0}{1}'.format('$',commission_paid_purchase))
print('Amount the stock sold for: {0}{1}'.format('$',total_selling_price))
print('Commission paid on the sale: {0}{1}'.format('$',commission_paid_sale))
print('Profit (or loss if negative): {0}{1}'.format('$',profit))
