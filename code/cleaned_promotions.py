#!/usr/bin/env python3

from completejourney_py import get_data
import pandas as pd

import pandas as pd

file_path = 'datasets/main_transactions.csv'
main_transactions = pd.read_csv(file_path)

# Filter out NA values of display location and mailer location
filtered_promotions = main_transactions.drop(main_transactions[main_transactions[['display_location','mailer_location']].isna().any(axis=1)].index)

# Group related display locations

def group_display_location(display_location):
  if display_location in ['0', '9']:
    return 'Display'
  elif display_location in ['1', '3']:
    return 'Front of Store Display'
  elif display_location in ['2', '5']:
    return 'Back of Store Display'
  else:
    return 'In Aisle'

# Group by related mailer locations

def group_mailer_location(mailer_location):
  if mailer_location in ['A', 'D', 'F', 'H', 'L']:
    return 'Feature Ads'
  elif mailer_location in ['J', 'P']:
    return 'Coupon Ads'
  elif mailer_location in ['X', 'Z']:
    return 'Free Ads'
  else:
    return 'Non-Ad/Line Item Ad'

filtered_promotions['display_location_group'] = filtered_promotions['display_location'].apply(group_display_location)
filtered_promotions['mailer_location_group'] = filtered_promotions['mailer_location'].apply(group_mailer_location)

# Save the DataFrame
filtered_promotions.to_csv('datasets/filtered_promotions.csv', index=False)
