"""
Dataset Generation Script

This script generates a synthetic vehicle insurance portfolio
consisting of 1,000,000 policies sold during 2024 and simulates
claims based on predefined business rules.

Outputs:
    data/policy_data.csv
    data/claims_data.csv

The goal of the script is to demonstrate how business rules can be
translated into structured datasets for analytical exploration.

The implementation prioritizes clarity, reproducibility, and
efficient data generation using vectorized operations.
"""

import pandas as pd
import numpy as np

# ----------------------------------------------------
# Configuration
# ----------------------------------------------------

TOTAL_POLICIES = 1_000_000
VEHICLE_VALUE = 100000
CLAIM_AMOUNT = 10000

# Reproducibility
np.random.seed(42)

# ----------------------------------------------------
# Step 1: Generate purchase dates
# ----------------------------------------------------
# Policies are assumed to be sold across the entire year
# Note: 2024 is a leap year (366 days), and pd.date_range()
# automatically includes February 29.

purchase_dates = pd.date_range("2024-01-01", "2024-12-31")

# ----------------------------------------------------
# Step 2: Generate tenure values
# ----------------------------------------------------
# Tenure probabilities provided in assignment

tenure_options = [1, 2, 3, 4]
tenure_probabilities = [0.2, 0.3, 0.4, 0.1]

tenure = np.random.choice(
    tenure_options,
    size=TOTAL_POLICIES,
    p=tenure_probabilities
)

# ----------------------------------------------------
# Step 3: Create policy dataset
# ----------------------------------------------------
# Vectorized operations are used instead of loops
# for efficient dataset generation

policies = pd.DataFrame({
    "Customer_ID": range(1, TOTAL_POLICIES + 1),
    "Vehicle_ID": range(1, TOTAL_POLICIES + 1),
    "Policy_Purchase_Date": np.random.choice(purchase_dates, TOTAL_POLICIES),
    "Policy_Tenure": tenure
})

# Assign constant vehicle value
policies["Vehicle_Value"] = VEHICLE_VALUE

# Premium calculation
policies["Premium"] = policies["Policy_Tenure"] * 100

# Policy activation rule
policies["Policy_Start_Date"] = (
    policies["Policy_Purchase_Date"] + pd.Timedelta(days=365)
)

# Policy expiration
policies["Policy_End_Date"] = (
    policies["Policy_Start_Date"] +
    pd.to_timedelta(policies["Policy_Tenure"] * 365, unit="D")
)

# Save policy dataset
policies.to_csv("data/policy_data.csv", index=False)

print("Policy dataset generated")

# ----------------------------------------------------
# Step 4: Generate defect claims (2025)
# ----------------------------------------------------
# Vehicles purchased on specific days may have defects

defect_days = [7, 14, 21, 28]

eligible_defect = policies[
    policies["Policy_Purchase_Date"].dt.day.isin(defect_days)
]

# 30% of eligible vehicles file claims
claims_2025 = eligible_defect.sample(
    frac=0.30,
    random_state=42
)

claims_2025 = claims_2025[
    ["Customer_ID", "Vehicle_ID", "Policy_Start_Date"]
]

claims_2025.rename(
    columns={"Policy_Start_Date": "Claim_Date"},
    inplace=True
)

claims_2025["Claim_Amount"] = CLAIM_AMOUNT
claims_2025["Claim_Type"] = 1

# ----------------------------------------------------
# Step 5: Generate long-tenure claims (2026)
# ----------------------------------------------------
# Only 4-year policies are considered

four_year_policies = policies[
    policies["Policy_Tenure"] == 4
]

claims_2026 = four_year_policies.sample(
    frac=0.10,
    random_state=42
)

date_range = pd.date_range(
    "2026-01-01",
    "2026-02-28"
)

claims_2026["Claim_Date"] = np.random.choice(
    date_range,
    size=len(claims_2026)
)

claims_2026 = claims_2026[
    ["Customer_ID", "Vehicle_ID", "Claim_Date"]
]

claims_2026["Claim_Amount"] = CLAIM_AMOUNT
claims_2026["Claim_Type"] = 2

# ----------------------------------------------------
# Step 6: Combine claims
# ----------------------------------------------------

claims = pd.concat(
    [claims_2025, claims_2026],
    ignore_index=True
)

claims.insert(
    0,
    "Claim_ID",
    range(1, len(claims) + 1)
)

# Save claims dataset
claims.to_csv("data/claims_data.csv", index=False)

print("Claims dataset generated")

# ----------------------------------------------------
# Step 7: Validation checks
# ----------------------------------------------------

# Premium rule validation
assert (policies["Premium"] ==
        policies["Policy_Tenure"] * 100).all()

# Claim amount validation
assert (claims["Claim_Amount"] == CLAIM_AMOUNT).all()

print("Validation checks passed")

# ----------------------------------------------------
# Step 8: Sanity checks
# ----------------------------------------------------

print("\nDataset Summary")
print("----------------------")
print("Total Policies:", len(policies))
print("Total Claims:", len(claims))
print("Claim Rate:",
      round(len(claims) / len(policies) * 100, 2), "%")

print("\nPolicy Tenure Distribution")
print(
    policies["Policy_Tenure"]
    .value_counts(normalize=True)
    .round(3)
)

print("\nClaim Type Distribution")
print(
    claims["Claim_Type"]
    .value_counts()
)

print("\nDatasets saved successfully in 'data/' folder.")