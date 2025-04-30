#!/usr/bin/env python3


print("Processing Data...")

from completejourney_py import get_data
import pandas as pd


campaign_descriptions = get_data()['campaign_descriptions']

coupon_redemptions = get_data()['coupon_redemptions']



coupons = get_data()['coupons']



products = get_data()['products']



promotions = get_data()['promotions']



transactions = get_data()['transactions']



#"Merge with products to get more information of each transaction
main_transactions = pd.merge(transactions, products, on='product_id')

# Note the usage of ~ since this means to exclude the rows where sales value, retail_disc, and coupon_match_disc is 0
main_transactions = main_transactions[~((
    (main_transactions['sales_value']==0) &
    (main_transactions['retail_disc']==0) &
    (main_transactions['coupon_match_disc']==0)
))]



# Remove products that had 0 quantity bought since this makes no sense
main_transactions = main_transactions[~((
    (main_transactions['quantity']==0)
))]



# Remove products that had 0 sales value but coupon_disc greater than one since this shouldn't happen
# When a coupon_disc is issued, the retailer must receive that amount from the manufacturer, and it should be included in sales_value
main_transactions = main_transactions[~((
    (main_transactions['sales_value']==0) &
    (main_transactions['coupon_disc']>0)
))]




# Only include products in the department of GROCERY since that's the department we must analyze
main_transactions = main_transactions[main_transactions['department']=='GROCERY']



# Remove the column department because we already know every product is in the grocery department
main_transactions = main_transactions.drop('department', axis=1)



# Now we must filter the products dataset since we merged it with transactions

# Idenitfy and remove products of type or category NA")
# Note how no NA products were printed, but there actually were NA products,
# but we might have removed them when we removed the weird transactions values
# when sales_value was 0 and all coupons were 0, or when quantity was 0, etc.
# Let's still exclude them for good practice even though there's not any NA values
main_transactions = main_transactions[~((main_transactions['product_category'].isna()) | (main_transactions['product_type'].isna()))]



# Remove the package_size column since it's not relevant")
main_transactions = main_transactions.drop('package_size', axis=1)


# Remove manufacturer_id since this is not relevant to performance of Grocery products
main_transactions = main_transactions.drop('manufacturer_id', axis=1)


  
# Add coupon redemptions to the transactions dataset to see when coupons were redeemed and know by which household

# Merge coupon_redemptions with coupons to add product_id based on coupon_upc to coupon_redemptions
main_coupons = pd.merge(coupon_redemptions, coupons, on=['coupon_upc','campaign_id'])

main_transactions = pd.merge(
    main_transactions,
    main_coupons,
    left_on=['household_id', 'product_id', pd.to_datetime(main_transactions['transaction_timestamp']).dt.date],
    right_on=['household_id', 'product_id', pd.to_datetime(main_coupons['redemption_date']).dt.date],
    how='left'
)


  
# Matches found: Note how all 2102 coupons redeemed found a match
# Drop the key_2 that was generated during the merge since this is just the redemption date,
# But we already have date and time in transaction_timestamp
# Also drop redemption_date since it's also in transaction_timestamp
main_transactions = main_transactions.drop('key_2',axis=1)
main_transactions = main_transactions.drop('redemption_date',axis=1)


  
# Join with campaigns to get the campaign type
main_transactions = pd.merge(
    main_transactions,
    campaign_descriptions,
    on='campaign_id',
    how='left'  # Keep all rows in main_transactions, even if no match in campaigns
)


  
# Add promotions information to get information of where the product was displayed in the store or mailer")

main_transactions = pd.merge(
    main_transactions,
    promotions,
    on=['store_id','product_id','week'],
    how = 'left'
)


  
# Add Loyalty Status
main_transactions['Loyalty_Status'] = main_transactions['retail_disc'].apply(lambda x: 'Loyalty' if x > 0 else 'Non Loyalty')


  
# Remove incomplete weeks:
# Week 1 only included 1 day
# Week 53 included days from January 2018 when the data was supposed to be for 2017
main_transactions = main_transactions[(main_transactions['week']!=1) & (main_transactions['week']!=53)]

main_transactions.to_csv('datasets/main_transactions.csv', index=False)


