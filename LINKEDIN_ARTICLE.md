# LinkedIn Article — Draft

**Title:** I Analyzed the City of Toronto's $18.2B Budget So You Don't Have To — Here's What I Found

**Subtitle / Hook:** Investment income blew past budget by 201%. Salaries are eating the city alive. And a $535M windfall is hiding a much harder fiscal reality.

---

## Article Body

---

Every year, the City of Toronto releases its Consolidated Financial Statements — a 54-page, KPMG-audited document that tells the real story of how Canada's largest city manages $18 billion in public money.

Most people don't read it. I did — and then I turned it into data.

Over the past week, I extracted every number from the 2024 statements, structured them into 12 clean datasets, and built a full Python data analysis with McKinsey-style visualizations. Here's what the data actually shows.

---

### The Headline Numbers First

**Revenue: $18.2B** (+11.5% YoY)
**Expenses: $16.2B** (+7.4% YoY)
**Annual Surplus: $2.0B** (vs. $150M budgeted — 13× above plan)

On the surface, 2024 looks like a blowout year. The city generated nearly $2B more than it spent. But dig into *why*, and the story gets complicated fast.

---

📊 **[INSERT CHART 1 — Executive KPI Dashboard]**
*Caption: Six headline KPIs with YoY comparisons. The $2.0B surplus and $801M investment income stand out immediately against the budget baselines.*

---

### The $535M Elephant in the Room

The single biggest story in the 2024 financials is **investment income**.

The city budgeted $266M. It actually earned **$801M** — a $535M (201%) outperformance.

This wasn't skill. It was timing. Toronto's $8.4B investment portfolio — managed by the Toronto Investment Board — benefited enormously from elevated interest rates throughout 2024. Government bonds, corporate bonds, and money market instruments all generated well above their historical average returns.

The problem? This tailwind won't last. As the Bank of Canada cuts rates (already underway in 2025), this revenue source will normalize. A city that structured its 2024 budget around $266M in investment income cannot plan its 2025 operations around $801M.

📊 **[INSERT CHART 2 — Revenue Deep Dive]**
*Caption: Budget vs. actual comparison across all 9 revenue sources. Investment income shows the most dramatic variance — a $535M overshoot that drove most of the surplus.*

---

### The Salary Problem Is Structural

Now for the expense side.

**Salaries, wages and benefits: $7,642M** — up **$573M (+8.1%)** from 2023.

This single line item represents **47.2% of all city expenses**. It grew faster than inflation, faster than revenue from taxation, and faster than any other major expense category.

Breaking it down by entity from the segment data:
- Toronto Police Service: $1,473M (up $156M)
- TTC: $1,832M (up $169M)
- City divisions: $3,790M (up $213M)

Collective bargaining, cost-of-living adjustments, and workforce expansion across critical services are all contributing. This is not a line item the city can easily compress — which makes the investment income normalization issue even more significant.

📊 **[INSERT CHART 3 — Expense Analysis]**
*Caption: Expense breakdown by type and service segment. Salaries dominate at $7.6B. The service heatmap shows where actual spending diverged most from budget.*

---

### The Balance Sheet: Rich in Assets, Deep in Debt

The City of Toronto owns **$45.4B in tangible capital assets** — transit infrastructure, water systems, roads, buildings, and land. This is the infrastructure backbone of Canada's economic capital.

But financing that infrastructure costs money.

**Net debt: $10,005M** (+$403M YoY)
**Long-term debt outstanding: $8,880M**
**Total debt service commitment (principal + interest): $16,646M**

The net debt-to-revenue ratio sits at **55%** — elevated, but not alarming by North American municipal standards. What matters is the trajectory: net debt has grown from $8.3B in 2022 to $10.0B in 2024.

📊 **[INSERT CHART 4 — Balance Sheet Analysis]**
*Caption: Left panel shows assets vs. liabilities over time. Right panel breaks down the liability waterfall — employee benefits ($4.9B) and deferred revenue ($7.9B) are the largest non-debt components.*

---

### Who's Making Money and Who's Losing It

The segment data is where this analysis gets genuinely interesting.

By service category:

| Service | Revenue | Expenses | Surplus/(Deficit) |
|---|---|---|---|
| General Government* | $8,122M | $1,063M | +$7,059M |
| Environmental Services | $1,959M | $1,176M | +$783M |
| Transportation | $2,644M | $4,460M | -$1,816M |
| Protection (Police/Fire) | $464M | $2,452M | -$1,988M |
| Social & Family Services | $3,119M | $3,678M | -$559M |
| Social Housing | $716M | $1,322M | -$606M |
| Recreation & Cultural | $599M | $1,239M | -$640M |

*General Government surplus includes all property tax revenue ($6.6B), which funds all other services.

The transit system (TTC) alone ran a **$133M deficit** in 2024, despite carrying 442M+ passenger trips. The Toronto Police Service ran a **$1,465M deficit** on $163M in revenue — almost entirely salary-funded.

📊 **[INSERT CHART 5 — Segment Analysis]**
*Caption: Revenue vs. expense by both service type and entity. The "funded by taxation" cross-subsidy becomes visible here — no segment except General Government (which holds all tax revenue) is self-funding.*

---

### Cash Flow: Strength on Top, Pressure Underneath

**Operating cash flow: +$4,122M** ✅
**Capital spending: -$4,332M** 🔴
**Financing: +$270M** (net new borrowing)
**Investing: -$1,165M** (net investment purchases)
**Net change in cash: -$1,105M**

The city is a cash-generating machine at the operating level. But it's spending every dollar — and more — on capital. $4.4 billion in capital investment in a single year is aggressive. Transit expansion, water/wastewater upgrades, and road rehabilitation are the dominant drivers.

Cash and cash equivalents fell from **$4.4B to $3.3B** during the year. Still comfortable, but worth watching.

📊 **[INSERT CHART 6 — Cash Flow & Investments]**
*Caption: The cash flow waterfall visualizes the four activity categories. The debt repayment schedule (right panel) shows $1.1B+ in annual principal + interest obligations through 2029.*

---

### The Hidden Liabilities

Beyond the balance sheet headline numbers, three liability categories deserve attention:

**1. Employee Benefit Liabilities: $4,930M**
WSIB obligations: $1,186M (+8.2%)
Other post-employment benefits: $2,236M
Sick leave: $411M

These are actuarially determined obligations that grow with every new collective agreement, healthcare inflation, and workforce size increase.

**2. Asset Retirement Obligations: $1,005M**
Primarily asbestos removal from city buildings ($816M) and landfill closure costs ($138M).

**3. Deferred Revenue: $7,891M**
This isn't income yet — it's money collected (development charges, government grants) that must be spent on specific capital projects. The $2.8B development charge balance reflects the pipeline of future infrastructure spending.

📊 **[INSERT CHART 7 — Financial Health Scorecard]**
*Caption: Radar chart scores six financial health dimensions. Interest rate sensitivity analysis (bottom right) shows the $324M portfolio exposure to a 1% rate move.*

---

### What Does the Trend Say About 2025–2027?

Using six years of simulated historical data calibrated to the 2023–2024 actuals, and applying linear regression:

**Revenue forecast:**
- 2025: ~$19.0B
- 2026: ~$19.8B
- 2027: ~$20.5B

**Expense forecast:**
- 2025: ~$17.1B
- 2026: ~$18.0B
- 2027: ~$18.9B

**The concern:** If investment income normalizes to budget levels ($400–500M range), the "organic" surplus shrinks dramatically. Revenue growth would need to come from property tax increases, new development, or expanded government transfers — all of which face political and economic headwinds.

📊 **[INSERT CHART 8 — Statistical Projections]**
*Caption: Linear regression with 95% confidence intervals. Revenue and expense trajectories are converging faster than the city's budget assumptions imply.*

---

### The Bottom Line: 4 Things Every Toronto Resident Should Know

📊 **[INSERT CHART 9 — Summary Insights Card]**
*Caption: Four strategic takeaways from the 2024 financial statements, with supporting data panels.*

**1. The 2024 surplus is real, but don't bank on it repeating.**
$535M of the surplus came from investment income that will normalize as rates fall. The structural surplus — from operations alone — is much smaller.

**2. Salary costs are the city's biggest long-term fiscal risk.**
At $7.6B and growing at 8%/year, personnel costs will define the city's fiscal trajectory more than any other single variable.

**3. Toronto is investing heavily — and it shows up as debt.**
$4.4B in annual capital spending is building real assets: transit, water, roads, affordable housing. But it comes at the cost of growing net debt and $16.6B in future debt service obligations.

**4. The Ontario-Toronto New Deal is changing the revenue mix.**
$600M committed over three years from the province for shelters and transit is significant — and it's showing up in the deferred revenue and government transfer lines. Federal housing money ($343M Housing Accelerator deferred) is another structural shift worth tracking.

---

### Methodology & Data

All data was extracted directly from the 54-page City of Toronto 2024 Consolidated Financial Statements (KPMG-audited, signed July 23, 2025). I structured 12 CSV datasets and built all visualizations in Python using matplotlib, seaborn, and scipy.

The full dataset, code, and all 9 charts are available on my GitHub: **github.com/mohamedfarazalam**

---

### Want to Dig Deeper?

If you're a data professional, finance analyst, urban planner, policy researcher, or just a curious Torontonian — the full Kaggle notebook and GitHub repository are linked below. All 12 datasets are clean, documented, and ready for your own analysis.

I'm also happy to answer questions in the comments about methodology, specific numbers, or what questions I'd explore next.

---

**What surprised you most from this analysis? Drop it in the comments.**

---

*#DataScience #Python #Toronto #PublicFinance #DataVisualization #OpenData #UrbanAnalytics #Kaggle #FinancialAnalysis #McKinsey*

---

**About the Author**

**Faraz Alam** is a data analyst based in Toronto, Canada. He specializes in turning complex public datasets into clear, actionable insights.

📧 Kaalicoder@gmail.com
💼 [linkedin.com/in/alam-faraz](https://www.linkedin.com/in/alam-faraz/)
🐙 [github.com/mohamedfarazalam](https://github.com/mohamedfarazalam)

---

## Posting Instructions

1. **Title**: Use the exact title at the top
2. **Cover image**: Use `charts/09_summary_insights.png` as the article cover
3. **Charts**: At each `[INSERT CHART X]` marker, paste the corresponding chart image
4. **Table**: The segment table can be copied as-is (LinkedIn supports markdown tables in articles)
5. **Hashtags**: Paste the hashtag block at the very bottom before publishing
6. **Cross-post**: Share the article link to your GitHub README and Kaggle notebook description

### Recommended posting time
Tuesday or Wednesday, 8–10am EST for maximum Toronto/Canada professional audience reach.
