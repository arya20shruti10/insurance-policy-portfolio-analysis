# Insurance Portfolio Simulation & Claims Analysis

**Business Intelligence Intern Assignment**  
**Author:** Your Name  

---

> **Dataset Size:** 1,000,000 simulated policies  
> **Objective:** Understand how premium revenue and claim behavior evolve in an insurance portfolio.

---

# Overview

This project explores how an **insurance portfolio behaves when policy sales and claims are simulated using simple business rules**.

The dataset represents **1,000,000 vehicle insurance policies sold during 2024**, with claims occurring later based on predefined conditions.

Once the dataset is generated, it becomes possible to analyze:

- how **premium revenue accumulates**
- when **claim costs begin to appear**
- how **policy tenure affects portfolio risk**

The project mirrors a simplified workflow commonly used by **Business Intelligence and insurance analytics teams**.

While implementing the simulation, I intentionally kept the logic simple and transparent so the business assumptions behind the claims generation are easy to review.

---

## Project Motivation

Insurance companies collect premiums upfront while claims occur later when insured events happen.  
Understanding this timing difference is essential for evaluating portfolio profitability and risk exposure.

This project was created to simulate how an insurance analytics team might study portfolio behavior by translating business rules into structured datasets and analyzing the resulting claim patterns.

---

# Key Results

| Metric | Value |
|------|------|
| Total Policies Simulated | 1,000,000 |
| Estimated Average Premium | ₹240 |
| Estimated Total Premium | ≈ ₹240 Million |
| Claim Waves Observed | Early 2025, Early 2026 |
| Key Risk Driver | Long tenure policies |

These results highlight how **policy duration and activation timing influence claim behaviour and portfolio risk exposure.**

---

# Key Highlights

## Dataset Scale

- **1,000,000 simulated policies**
- rule-based **multi-year claim generation**

## Core Analysis

- estimate **total premium revenue**
- analyze **claim timing patterns**
- compute **loss ratio by policy tenure**
- estimate **future portfolio liability**

## Tools Used

- **Python** – dataset generation and analysis
- **Pandas / NumPy** – large dataset manipulation
- **SQL** – analytical queries
- **Power BI / Excel** – dashboard visualization
- **Jupyter Notebook** – exploratory analysis

---

# Repository Structure

```text
insurance-policy-analysis
│
├── generate_data.py        # policy and claim dataset generation
├── analysis.ipynb          # analytical exploration
├── sql_queries.sql         # SQL queries for analysis
│
├── data/
│   ├── policy_data.csv
│   └── claims_data.csv
│
├── visuals/
│   └── dashboard_screenshot.png
│
└── docs/
    └── insights_report.pdf
```
The repository is structured so reviewers can easily follow the workflow:

**Data Generation → Analysis → Visualization**

---

# How to Run the Project

To reproduce the analysis locally:

### 1. Generate the datasets

Run the data generation script:

```bash
python generate_data.py
```
This script generates the following files inside the data/ folder:

- policy_data.csv

- claims_data.csv

### 2. Explore the analysis

Open the Jupyter notebook:
analysis.ipynb

The notebook contains:

- data loading

- exploratory analysis

- metric calculations

- claim pattern analysis

### 3. Run SQL queries
The SQL queries used for analytical calculations are available in:
sql_queries.sql

These queries replicate key analytical metrics such as:

- total premium collected

- claim distribution

- loss ratio by tenure

### 4. View the dashboard
Dashboard visualizations are available in the visuals/ folder.

These include charts such as:

- Premium vs Claims over time

- Monthly claim distribution

- Loss ratio by policy tenure

A preview of the dashboard is shown below.

![Insurance Dashboard](Visuals/dashboard_screenshot.png)

---

# Business Context

Insurance portfolios typically follow a predictable timing pattern.

### Revenue Appears Early
Premiums are collected **when policies are purchased**.

### Risk Appears Later
Claims occur **after policies become active**, when insured events happen.

Understanding this timing difference is important when evaluating **portfolio profitability and risk exposure**.

---

# Data Model

Two datasets were generated.

## Policy Dataset

| Field | Description |
|------|-------------|
| Customer_ID | Policyholder identifier |
| Vehicle_ID | Vehicle identifier |
| Policy_Purchase_Date | Date the policy was purchased |
| Policy_Start_Date | Coverage start date |
| Policy_End_Date | Coverage end date |
| Policy_Tenure | Policy duration |
| Premium | Premium amount paid |

---

## Claims Dataset

| Field | Description |
|------|-------------|
| Claim_ID | Unique claim identifier |
| Customer_ID | Policyholder |
| Vehicle_ID | Insured vehicle |
| Claim_Date | Date of claim |
| Claim_Amount | Claim payout |
| Claim_Type | Type of claim |

### Relationship Between Tables

Policies.Vehicle_ID → Claims.Vehicle_ID

This relationship links each claim to the corresponding policy record.

---

# Data Generation Approach

The simulation generates **1,000,000 policies** using probabilistic rules.

## Dataset

The full dataset is generated using the `generate_data.py` script.

Due to GitHub file size limits, only a small sample dataset is included in the repository.

To generate the full dataset:

```bash
python generate_data.py
```

---

## Policy Purchase Distribution

Policy purchase dates were randomly distributed across **all days of 2024**, ensuring a realistic spread of policy sales.

Since **2024 is a leap year (366 days)**, this was incorporated into the simulation.

---

## Policy Tenure Distribution

| Tenure | Probability |
|------|-------------|
| 1 year | 20% |
| 2 years | 30% |
| 3 years | 40% |
| 4 years | 10% |

---

## Premium Calculation

Premium = Policy_Tenure × ₹100


| Tenure | Premium |
|------|------|
| 1 year | ₹100 |
| 2 years | ₹200 |
| 3 years | ₹300 |
| 4 years | ₹400 |

Policies become active **365 days after purchase**.

---

# Claim Simulation Logic

Two claim scenarios were implemented.

## Scenario 1 — Defect Claims (2025)

Vehicles purchased on:

7th, 14th, 21st, 28th

From these vehicles:

30% file claims


Claims occur **when policies become active**.

Claim payout amount: 
₹10,000


---

## Scenario 2 — Long Tenure Claims (2026)

Only **4-year policies** are considered.

10% file claims

Claim window:
Jan 1 2026 – Feb 28 2026


This simulates **additional risk exposure from longer policy durations**.

---

# Data Validation & Quality Checks

Basic validation checks ensured the dataset follows the assignment rules.

### Example Validation

```python
assert (policy_df["Premium"] == policy_df["Policy_Tenure"] * 100).all()
```
Additional checks included:

- no duplicate vehicle IDs
- claims generated only for eligible policies
- claim dates fall within policy coverage

## Data Quality Summary

| Check | Result |
|------|--------|
| Premium rule | Valid |
| Claim amount consistency | Valid |
| Policy start date logic | Valid |
| Tenure distribution | Matches expected probabilities |
| Duplicate vehicle IDs | None detected |

These checks confirm that the **synthetic dataset behaves logically and follows the assignment rules**.

---

## Analytical Findings

### Total Premium Collected

Expected average tenure:
2.4 years

Average premium per policy:
₹240

Estimated total portfolio premium:
≈ ₹240 million

---

### Claim Timing Pattern

Two major claim clusters appear:

- **Early 2025**
- **Early 2026**

These correspond to the two simulated claim scenarios.

---

### Loss Ratio by Tenure
Loss Ratio = Total Claims / Total Premium


This metric helps identify **which policy durations are most financially sustainable**.

---

### Observational Insight

While implementing the simulation, an interesting pattern appeared:

Although policies were purchased throughout the year, the rule-based claims produced **distinct spikes once policies became active**.

This type of clustering can occur in real insurance portfolios when **product defects or operational issues trigger claim waves**.

---

## Claim Sensitivity Scenario

If the **defect claim rate increases from 30% to 35%**:
Additional Claim Cost ≈
5% × Eligible Vehicles × ₹10,000


This demonstrates how **small increases in claim frequency can significantly affect portfolio profitability**.

---

## Performance Note

The dataset generation script handles **1,000,000 rows efficiently** using **vectorized operations in Pandas and NumPy**, avoiding slow row-by-row loops.

This ensures the simulation remains **both scalable and readable**.

---

## Visualization

A dashboard was created to visualize portfolio behaviour.

![Portfolio Dashboard](Visuals/dashboard_screenshot.png)

Key charts include:

- **Premium vs Claims over time**
- **Monthly claim distribution**
- **Loss ratio by policy tenure**

These visuals allow quick identification of **revenue patterns and claim spikes**.

---

# Assumptions & Limitations

### Assumptions

- vehicle value fixed at **₹100,000**
- claim amount fixed at **₹10,000**
- policies evenly distributed across **2024**

### Limitations

Real insurance portfolios typically include additional complexity such as:

- varying vehicle values
- regional risk factors
- seasonal policy demand

These factors were intentionally simplified for this simulation.

---

# Analyst Thought Process

The analysis was approached in three stages:

1. **Validate the dataset**  
   Ensure the generated portfolio follows the assignment rules and data logic.

2. **Measure portfolio scale and revenue generation**  
   Calculate the total premium collected and examine the policy tenure distribution.

3. **Analyze claim behaviour and risk exposure**  
   Study when claims begin to appear and how policy tenure influences long-term risk exposure.

This structured workflow mirrors how Business Intelligence and analytics teams explore operational datasets.

---

# Conclusion

This project demonstrates how a simulated dataset can be used to analyze **insurance portfolio behaviour**.

By translating business rules into structured data and analyzing the resulting patterns, we can better understand how **premium timing, claim behaviour, and policy design influence overall risk exposure**.

Even in a simplified simulation, these insights reflect the type of analysis performed by **Business Intelligence and insurance analytics teams**.

