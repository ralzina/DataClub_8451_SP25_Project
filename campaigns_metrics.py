#!/usr/bin/env python3

from completejourney_py import get_data
import pandas as pd

campaign_descriptions = get_data()['campaign_descriptions']

campaigns = get_data()['campaigns']

campaigns_merged = pd.merge(campaigns, campaign_descriptions, on='campaign_id', how='left')

main_transactions = pd.read_csv('main_transactions.csv')

main_redemptions = main_transactions.dropna(subset=['campaign_type'])

main_redemptions_a = main_redemptions[main_redemptions['campaign_type']=='Type A']

campaigns_merged_a = campaigns_merged[campaigns_merged['campaign_type']=='Type A']

distinct_household_redemptions_a = main_redemptions_a['household_id'].nunique()
print(f"Number of distinct household_ids in main_redemptions:       {distinct_household_redemptions_a}")

distinct_household_targeted_a = campaigns_merged_a['household_id'].nunique()
print(f"Number of distinct household_ids in campaigns_merged_a:     {distinct_household_targeted_a}")

household_redemption_rate_a = distinct_household_redemptions_a / distinct_household_targeted_a
print(f"Household redemption rate for Type A campaigns:             {household_redemption_rate_a}\n\n")

main_redemptions_b = main_redemptions[main_redemptions['campaign_type']=='Type B']

campaigns_merged_b = campaigns_merged[campaigns_merged['campaign_type']=='Type B']

distinct_household_redemptions_b = main_redemptions_b['household_id'].nunique()
print(f"Number of distinct household_ids in main_redemptions:       {distinct_household_redemptions_b}")

distinct_household_targeted_b = campaigns_merged_b['household_id'].nunique()
print(f"Number of distinct household_ids in campaigns_merged_b:     {distinct_household_targeted_b}")

household_redemption_rate_b = distinct_household_redemptions_b / distinct_household_targeted_b
print(f"Household redemption rate for Type B campaigns:             {household_redemption_rate_b}\n\n")

main_redemptions_c = main_redemptions[main_redemptions['campaign_type']=='Type C']

campaigns_merged_c = campaigns_merged[campaigns_merged['campaign_type']=='Type C']

distinct_household_redemptions_c = main_redemptions_c['household_id'].nunique()
print(f"Number of distinct household_ids in main_redemptions:       {distinct_household_redemptions_c}")

distinct_household_targeted_c = campaigns_merged_c['household_id'].nunique()
print(f"Number of distinct household_ids in campaigns_merged_c:     {distinct_household_targeted_c}")

household_redemption_rate_c = distinct_household_redemptions_c / distinct_household_targeted_c
print(f"Household redemption rate for Type C campaigns:             {household_redemption_rate_c}\n\n")

campaign_summary = campaigns_merged.groupby('campaign_type')['household_id'].nunique().reset_index()
campaign_summary = campaign_summary.rename(columns={'household_id': 'unique_households'})
print(campaign_summary)
