# Insights Report

## Project Overview

This project analyzes a simulated vehicle insurance portfolio consisting of **1,000,000 policies sold during 2024**.

The objective was to study how **premium revenue, claim timing, and policy tenure** influence the overall **profitability and risk exposure** of the portfolio.

Two datasets were analyzed:

- **Policy dataset** – contains policy purchase date, tenure, and premium values  
- **Claims dataset** – contains simulated claims occurring in **2025 and early 2026**

The analysis evaluates:

- **Total premium revenue generated**
- **Claim cost patterns over time**
- **Loss ratio across policy tenures**
- **Potential future claim liability**

---

## Key Insights

### **1. Revenue concentration in mid-term policies**

Because **40% of policies have a 3-year tenure**, these policies generate the largest portion of total premium revenue.

This highlights how **portfolio composition directly affects revenue distribution**.

---

### **2. Claim activity occurs in clusters**

The claim timeline shows two clear spikes:

- **Early 2025** – when policies become active  
- **Early 2026** – from **4-year tenure policies**

This pattern illustrates how **policy lifecycle rules can create concentrated claim periods**.

---

### **3. Longer tenures increase exposure to risk**

Longer policies generate higher premiums but also extend the **time window for claims to occur**.

This creates a trade-off between:

- **Higher premium revenue**
- **Longer risk exposure**

---

### **4. Future claim exposure remains significant**

A large portion of policies **have not yet generated claims**.

If every remaining vehicle eventually files one claim, the portfolio still faces **substantial future claim liability**, highlighting the importance of **risk reserves and forecasting**.

---

### **5. Earned premium differs from written premium**

Although premiums are collected upfront, revenue is recognized **gradually over the policy duration**.

As of **February 2026**, only part of the total premium has been earned, while the remaining amount will be recognized over future months.

---

### **Overall Insight**

The analysis shows that **policy tenure, claim timing, and portfolio composition jointly determine the financial performance of the insurance portfolio**.

Even in a simplified simulation, these factors create patterns similar to those observed in real insurance analytics.

---

## Assumptions

The simulation uses several simplifying assumptions:

- **Vehicle value fixed at ₹100,000**
- **Claim amount fixed at ₹10,000**
- Policies distributed **evenly across 2024**
- Policies become active **365 days after purchase**

These assumptions allow the analysis to focus on **portfolio-level behavior** rather than individual risk characteristics.

---

## Limitations

The simulation does not capture several real-world complexities:

- Claim severity variation  
- Driver or vehicle risk profiles  
- Geographic risk factors  
- Seasonal demand patterns

Because of these simplifications, the analysis focuses mainly on **claim timing and portfolio-level trends**.

---

## Visualizations

To complement the analytical queries, a simple dashboard was created to visualize key portfolio metrics.  

The dashboard focuses on a few core visualizations that help summarize portfolio behavior.

**Premium vs Claim Cost Over Time**

This chart compares premium revenue and claim costs across time.  
It highlights the typical insurance pattern where **premium is collected earlier while claims occur later during the policy lifecycle**.

**Monthly Claim Distribution**

This visualization shows the number of claims by month.  
Two distinct spikes appear in **early 2025** and **early 2026**, reflecting the simulated claim scenarios.

**Claim Cost by Policy Tenure**

This chart compares claim costs across different policy tenures.  
It helps illustrate how **longer policy durations increase exposure to potential claims**.

**Loss Ratio Overview**

A summary metric showing:

Loss Ratio = Total Claims ÷ Total Premium

This metric provides a quick indicator of **overall portfolio profitability**.

Together, these visualizations provide a high-level view of how **premium revenue, claim timing, and policy tenure interact within the insurance portfolio**.

---

## Analyst Reflection

While implementing the simulation and analysis, it became clear that **even simple business rules can produce meaningful portfolio patterns**.

This exercise highlights the importance of combining **data analysis with business context** when interpreting results in insurance analytics.

---

## Conclusion

This project demonstrates how simulated datasets can be used to analyze **insurance portfolio dynamics**, including premium generation, claim timing, and risk exposure.

Although simplified, the workflow reflects the type of analysis commonly performed in **business intelligence and insurance analytics environments**.