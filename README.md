# 🏙️ City of Toronto 2024 Financial Statements — Deep Dive Data Analysis

> **A comprehensive data science portfolio project analyzing the City of Toronto's 2024 Consolidated Financial Statements (KPMG-audited, $18.2B revenue).**

---

## 👤 Author

| | |
|---|---|
| **Name** | Faraz Alam |
| **Email** | Kaalicoder@gmail.com |
| **GitHub** | [github.com/mohamedfarazalam](https://github.com/mohamedfarazalam) |
| **LinkedIn** | [linkedin.com/in/alam-faraz](https://www.linkedin.com/in/alam-faraz/) |

---

## 📌 Project Overview

This project extracts, structures, and analyzes the full 54-page **City of Toronto 2024 Consolidated Financial Statements** — the largest municipal financial report in Canada. All data was manually extracted from the KPMG-audited PDF and structured into 12 clean CSV datasets.

The analysis covers:
- Revenue & expense performance vs. budget
- Balance sheet health and net debt trajectory
- Cash flow waterfall analysis
- Segment-level P&L (9 service categories, 6 entities)
- Investment portfolio composition
- Long-term debt and repayment schedule
- Statistical projections (2025–2027) using linear regression
- Financial health scoring and risk assessment

All visualizations follow a **McKinsey-style design system**: white background, navy/steel-blue palette, clean typography, and professional annotation.

---

## 📁 Repository Structure

```
toronto_finance/
│
├── data/                          # 12 clean CSV datasets
│   ├── 01_financial_position.csv  # Balance sheet (assets, liabilities, net debt)
│   ├── 02_operations.csv          # Revenue & expense by category (budget vs actual)
│   ├── 03_expense_breakdown.csv   # Expense type breakdown
│   ├── 04_cash_flows.csv          # Cash flow statement
│   ├── 05_capital_assets.csv      # Tangible capital assets schedule
│   ├── 06_segment_service.csv     # P&L by service segment (9 categories)
│   ├── 07_segment_entity.csv      # P&L by entity (City, TTC, Police, etc.)
│   ├── 08_investments.csv         # Investment portfolio composition
│   ├── 09_debt_repayment.csv      # Long-term debt repayment schedule
│   ├── 10_deferred_revenue.csv    # Deferred revenue breakdown
│   ├── 11_kpi_metrics.csv         # Key financial ratios & YoY changes
│   └── 12_government_transfers.csv # Federal/Provincial transfers by type
│
├── charts/                         # 9 output visualizations (PNG, 200 DPI)
│   ├── 01_executive_dashboard.png
│   ├── 02_revenue_deep_dive.png
│   ├── 03_expense_analysis.png
│   ├── 04_balance_sheet.png
│   ├── 05_segment_analysis.png
│   ├── 06_cashflow_investments.png
│   ├── 07_health_risk.png
│   ├── 08_statistical_projections.png
│   └── 09_summary_insights.png
│
├── analysis.py                     # Main Python analysis script (700+ lines)
└── README.md                       # This file
```

---

## 📊 Dataset Descriptions

### 01 — Financial Position
Balance sheet snapshot as at December 31, 2024 vs. 2023. Includes all financial assets (cash, receivables, investments), liabilities (deferred revenue, long-term debt, employee benefits), and non-financial assets (tangible capital assets).

| Key Metric | 2024 | 2023 | Δ |
|---|---|---|---|
| Total Financial Assets | $18,225M | $17,301M | +5.3% |
| Total Liabilities | $28,230M | $26,903M | +4.9% |
| Net Debt | ($10,005M) | ($9,602M) | +$403M |
| Tangible Capital Assets | $45,417M | $42,853M | +6.0% |
| Accumulated Surplus | $34,746M | $32,730M | +6.2% |

### 02 — Operations (Revenue & Expenses)
Full income statement with 2024 Budget, 2024 Actual, and 2023 Actual columns across all 9 revenue lines and 9 expense categories.

| Revenue Source | Budget | Actual | Variance |
|---|---|---|---|
| Property Taxes | $5,774M | $5,808M | +$34M |
| Government Transfers | $4,709M | $4,669M | -$40M |
| User Charges | $3,422M | $3,610M | +$188M |
| Investment Income | $266M | $801M | **+$535M** |
| Development Charges | $793M | $789M | -$4M |
| **Total Revenue** | **$17,672M** | **$18,202M** | **+$530M** |

### 03 — Expense Breakdown
Seven expense type categories totalling $16,186M.

| Expense Type | 2024 | 2023 | Δ% |
|---|---|---|---|
| Salaries, wages & benefits | $7,642M | $7,069M | +8.1% |
| Contracted services | $2,205M | $2,209M | -0.2% |
| Transfer payments | $2,083M | $1,860M | +12.0% |
| Amortization | $1,793M | $1,776M | +1.0% |
| Materials | $1,743M | $1,387M | +25.7% |
| Interest on LT debt | $437M | $421M | +3.8% |
| Other | $283M | $353M | -19.8% |

### 04 — Cash Flows
Four-section cash flow statement: Operating (+$4,122M), Capital (-$4,332M), Financing (+$270M), Investing (-$1,165M). Net decrease: -$1,105M.

### 05 — Capital Assets
Tangible capital assets by type: General ($18,357M NBV) and Infrastructure ($19,789M NBV), plus $7,271M assets under construction. Total gross cost: $71,323M.

### 06 — Segment by Service
Nine service segments with full revenue, expense, and surplus/deficit disclosure. Transportation is the largest expense segment ($4,460M). General Government is the largest revenue segment ($8,122M including property taxes).

### 07 — Segment by Entity
Entity-level breakdown: City ($3,719M surplus), Toronto Police (-$1,465M deficit), TTC (-$133M), Toronto Public Library (-$303M), TCHC (-$84M).

### 08 — Investments
$8,391M investment portfolio: Government bonds ($2,135M), Money market ($2,040M), Corporate bonds ($1,984M), Equities ($1,572M), Real estate funds ($353M).

### 09 — Debt Repayment
$16,646M total debt service (principal + interest). Debt matures from 2025 through post-2029, with $6,703M principal due thereafter.

### 10 — Deferred Revenue
$7,891M total deferred revenue. Largest components: Development charges ($2,843M), Water/wastewater capital ($1,606M), Parkland acquisitions ($965M), Section 37/45 ($698M).

### 11 — KPI Metrics
12 key financial ratios calculated for 2023 and 2024:
- Revenue growth: +11.5%
- Expense growth: +7.4%
- Annual surplus margin: 11.1%
- Net debt to revenue: 55.0%
- Capital investment ratio: 24.3%
- Investment income vs. budget: +201.1%

### 12 — Government Transfers
$4,669M total transfers: Provincial ($3,346M = 72%), Federal ($1,289M = 28%). Operating transfers $3,850M; Capital transfers $816M.

---

## 📈 Visualizations

### Chart 1 — Executive KPI Dashboard
Six headline KPI cards + revenue/expense comparison + revenue composition pie + net debt waterfall + expense breakdown horizontal bar.

### Chart 2 — Revenue Deep Dive
Budget vs. actual by revenue source + YoY growth rates + revenue composition stacked bar + investment income spike analysis ($801M actual vs. $266M budget = +201%).

### Chart 3 — Expense Analysis
Expense vs. budget by service + expense type donut + key category trends + service budget variance heatmap.

### Chart 4 — Balance Sheet Analysis
Assets vs. liabilities grouped bar + liability waterfall + capital asset category breakdown + net debt composition.

### Chart 5 — Segment Analysis
Revenue vs. expense by service + surplus/deficit ranking + entity-level performance + YoY surplus change.

### Chart 6 — Cash Flow & Investments
Cash flow waterfall (4 sections) + investment portfolio pie + capital spending breakdown + debt repayment schedule.

### Chart 7 — Financial Health Scorecard
Radar chart (6 financial health dimensions) + KPI benchmarks + interest rate sensitivity + deferred revenue composition + government transfers breakdown.

### Chart 8 — Statistical Projections
Revenue & expense trend lines (2019–2024 simulated history) + linear regression with 95% confidence intervals + 2025–2027 forecasts + R² scores + Pearson correlation.

### Chart 9 — Summary Insights Card
Four strategic insight panels (outperformance, fiscal pressures, capital strength, strategic risks) + revenue mix + expense breakdown + key growth rates.

---

## 🔍 Key Findings

### ✅ Outperformance
- **Investment income**: $801M actual vs. $266M budget — a **$535M windfall** driven by higher interest rates on the $8.4B portfolio
- **Annual surplus**: $2,016M vs. $150M budgeted — **13× above plan**
- **Property tax**: +8.0% YoY growth, exceeding budget by $34M
- **User charges**: +4.4% YoY, $188M above budget

### ⚠️ Fiscal Pressures
- **Salary costs**: $7,642M (+8.1% YoY), comprising 47.2% of total expenses
- **Social Housing**: expenses up 23.8% ($1,322M vs. $1,068M)
- **Materials costs**: up 25.7% to $1,743M
- **Cash position**: fell $1,105M to $3,321M

### 🏗️ Capital Strength
- **$4.4B capital investment** in 2024 (24.3% of revenue)
- **$45.4B asset base** (tangible capital assets at net book value)
- **$7.3B assets under construction** (transit, water, roads, buildings)
- Net investment in TCA: **$34,770M**

### 🔴 Strategic Risks
- **Net debt growing**: $10,005M (+$403M YoY), trending toward $10.4B in 2025
- **Employee benefit liabilities**: $4,930M (WSIB obligations up 8.2% to $1,186M)
- **$16.6B total debt service** commitment (principal + interest through maturity)
- **Investment income tailwind will not persist** as rates normalize

---

## 🛠️ Technical Stack

| Tool | Usage |
|---|---|
| Python 3.x | Core analysis language |
| pandas | Data manipulation & CSV handling |
| numpy | Numerical computation |
| matplotlib | Primary visualization engine |
| seaborn | Statistical charts & heatmaps |
| scipy.stats | Linear regression & statistical tests |
| scikit-learn | Machine learning utilities |
| VS Code | Development environment |

---

## 🚀 How to Run

```bash
# Clone or download the repository
cd toronto_finance

# Install dependencies
pip install pandas numpy matplotlib seaborn scipy scikit-learn

# Run the full analysis
python analysis.py

# Charts will be generated in the charts/ directory
```

---

## 📚 Data Source

**City of Toronto 2024 Consolidated Financial Statements**
- Audited by: KPMG LLP (Vaughan, Canada)
- Audit opinion date: July 23, 2025
- Prepared in accordance with: Canadian Public Sector Accounting Standards (PSAS)
- Signed by: Jason Li (Controller & Chief Accountant), Stephen Conforti (CFO & Treasurer), Paul Johnson (City Manager)

All data extracted manually from the official 54-page financial report PDF. No data was estimated or fabricated — all figures come directly from the audited statements.

---

## 📄 License

This project is for educational and portfolio purposes. Financial data belongs to the City of Toronto. Visualizations and code are original work by Faraz Alam.

---

*"Turning public financial data into actionable insights — one visualization at a time."*

**Faraz Alam** | Data Analyst | Toronto, Canada
