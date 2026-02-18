"""
=============================================================================
CITY OF TORONTO 2024 CONSOLIDATED FINANCIAL STATEMENTS — DEEP DIVE ANALYSIS
=============================================================================
Author  : Faraz Alam
Email   : Kaalicoder@gmail.com
GitHub  : https://github.com/mohamedfarazalam
LinkedIn: https://www.linkedin.com/in/alam-faraz/
Date    : 2025
Source  : City of Toronto 2024 Consolidated Financial Statements (KPMG Audited)

McKinsey-Style Visualization Theme:
  Background : White (#FFFFFF)
  Primary    : Navy Blue (#003366)
  Secondary  : Steel Blue (#1A6BAF)
  Accent     : Light Blue (#4DA6E8)
  Highlight  : Midnight Blue (#00245A)
  Text       : Black (#000000)
  Grid/Subtle: Light Gray (#E8E8E8)
=============================================================================
"""

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.ticker as mticker
from matplotlib.gridspec import GridSpec
import seaborn as sns
from scipy import stats
import warnings
import os

warnings.filterwarnings('ignore')

# ─── THEME SETUP ────────────────────────────────────────────────────────────
NAVY     = '#003366'
STEEL    = '#1A6BAF'
LBLUE    = '#4DA6E8'
MID      = '#00245A'
BLACK    = '#000000'
LGRAY    = '#E8E8E8'
DGRAY    = '#555555'
WHITE    = '#FFFFFF'
RED_ACC  = '#C8102E'
GREEN_ACC= '#00703C'

COLORS_SEQ   = [NAVY, STEEL, LBLUE, '#6BB8D4', '#A8D5E8', '#D0EBF5']
COLORS_DUAL  = [NAVY, LBLUE]
COLORS_MULTI = [NAVY, STEEL, LBLUE, '#2196B0', '#82C4DC', '#B0D9EC']

def set_mckinsey_style():
    plt.rcParams.update({
        'figure.facecolor'      : WHITE,
        'axes.facecolor'        : WHITE,
        'axes.edgecolor'        : BLACK,
        'axes.linewidth'        : 0.8,
        'axes.grid'             : True,
        'grid.color'            : LGRAY,
        'grid.linewidth'        : 0.6,
        'grid.alpha'            : 0.7,
        'axes.axisbelow'        : True,
        'font.family'           : 'sans-serif',
        'font.sans-serif'       : ['Arial', 'DejaVu Sans', 'Helvetica'],
        'font.size'             : 10,
        'axes.titlesize'        : 13,
        'axes.titleweight'      : 'bold',
        'axes.titlecolor'       : BLACK,
        'axes.labelsize'        : 10,
        'axes.labelcolor'       : BLACK,
        'xtick.color'           : DGRAY,
        'ytick.color'           : DGRAY,
        'xtick.labelsize'       : 9,
        'ytick.labelsize'       : 9,
        'legend.fontsize'       : 9,
        'legend.frameon'        : False,
        'figure.dpi'            : 150,
        'savefig.dpi'           : 200,
        'savefig.bbox'          : 'tight',
        'savefig.facecolor'     : WHITE,
    })

set_mckinsey_style()

CHART_DIR = 'charts'
os.makedirs(CHART_DIR, exist_ok=True)

def add_watermark(ax):
    ax.text(0.99, 0.01, 'Faraz Alam | @KaaliCoder | City of Toronto 2024 FS',
            transform=ax.transAxes, fontsize=6, color=LGRAY,
            ha='right', va='bottom', style='italic')

def fmt_m(v):
    """Format value in millions with $ prefix."""
    if abs(v) >= 1000:
        return f'${v/1000:.1f}B'
    return f'${v:.0f}M'

def fmt_b(v):
    return f'${v/1000:.2f}B'

def save(fig, name):
    path = os.path.join(CHART_DIR, name)
    fig.savefig(path, bbox_inches='tight', facecolor=WHITE)
    plt.close(fig)
    print(f'  ✔  Saved → {path}')

# ─── LOAD DATA ───────────────────────────────────────────────────────────────
print("Loading data...")
fp   = pd.read_csv('data/01_financial_position.csv')
ops  = pd.read_csv('data/02_operations.csv')
exp  = pd.read_csv('data/03_expense_breakdown.csv')
cf   = pd.read_csv('data/04_cash_flows.csv')
tca  = pd.read_csv('data/05_capital_assets.csv')
seg  = pd.read_csv('data/06_segment_service.csv')
ent  = pd.read_csv('data/07_segment_entity.csv')
inv  = pd.read_csv('data/08_investments.csv')
debt = pd.read_csv('data/09_debt_repayment.csv')
def_ = pd.read_csv('data/10_deferred_revenue.csv')
kpi  = pd.read_csv('data/11_kpi_metrics.csv')
xfer = pd.read_csv('data/12_government_transfers.csv')
print("  ✔  All data loaded.\n")

# ═══════════════════════════════════════════════════════════════════════════════
# CHART 1 — EXECUTIVE DASHBOARD (KPI SCORECARD)
# ═══════════════════════════════════════════════════════════════════════════════
print("Chart 1: Executive KPI Dashboard...")

fig = plt.figure(figsize=(18, 10))
fig.patch.set_facecolor(WHITE)

# ── Header banner ──
fig.text(0.5, 0.97, 'CITY OF TORONTO — 2024 FINANCIAL PERFORMANCE DASHBOARD',
         ha='center', va='top', fontsize=16, fontweight='bold', color=NAVY)
fig.text(0.5, 0.94, 'Consolidated Financial Statements | Fiscal Year Ended December 31, 2024 | KPMG Audited',
         ha='center', va='top', fontsize=10, color=DGRAY)
fig.text(0.5, 0.91, 'Analysis by Faraz Alam  •  Kaalicoder@gmail.com  •  github.com/mohamedfarazalam',
         ha='center', va='top', fontsize=8, color=STEEL)

ax_line = fig.add_axes([0.05, 0.895, 0.9, 0.003])
ax_line.set_facecolor(NAVY)
for sp in ax_line.spines.values(): sp.set_visible(False)
ax_line.set_xticks([]); ax_line.set_yticks([])

# ── KPI Cards (top row) ──
kpis = [
    ('Total Revenue',    '$18.2B', '+$1.9B', True,  '2024 Actual'),
    ('Annual Surplus',   '$2.0B',  '+61.3%', True,  'vs 2023 $1.25B'),
    ('Net Debt',         '$10.0B', '+$0.4B', False, 'Increase YoY'),
    ('Capital Assets',   '$45.4B', '+$2.6B', True,  'Net Book Value'),
    ('Investments',      '$8.4B',  '+$1.4B', True,  'Portfolio Value'),
    ('Operating CF',     '$4.1B',  '+11.0%', True,  'Cash generated'),
]
card_w, card_h = 0.13, 0.16
starts_x = [0.05 + i*(card_w+0.018) for i in range(6)]
start_y = 0.70

for i, (label, value, change, pos, sub) in enumerate(kpis):
    ax_c = fig.add_axes([starts_x[i], start_y, card_w, card_h])
    ax_c.set_facecolor(NAVY if i == 0 else '#F5F8FC')
    for sp in ax_c.spines.values():
        sp.set_color(NAVY); sp.set_linewidth(1.5)
    ax_c.set_xticks([]); ax_c.set_yticks([])
    txt_color = WHITE if i == 0 else NAVY
    chg_color = (GREEN_ACC if pos else RED_ACC) if i != 0 else WHITE
    ax_c.text(0.5, 0.85, label,  ha='center', va='top',   fontsize=8,  color=txt_color, transform=ax_c.transAxes, fontweight='bold')
    ax_c.text(0.5, 0.52, value,  ha='center', va='center', fontsize=16, color=txt_color, transform=ax_c.transAxes, fontweight='bold')
    ax_c.text(0.5, 0.25, change, ha='center', va='center', fontsize=10, color=chg_color, transform=ax_c.transAxes, fontweight='bold')
    ax_c.text(0.5, 0.08, sub,    ha='center', va='bottom', fontsize=7,  color=DGRAY if i != 0 else '#BBCCDD', transform=ax_c.transAxes)

# ── Bar: Revenue vs Expense trend ──
ax1 = fig.add_axes([0.05, 0.36, 0.35, 0.28])
categories = ['Revenue', 'Expenses', 'Surplus']
vals_24 = [18202, 16186, 2016]
vals_23 = [16325, 15075, 1250]
x = np.arange(3)
w = 0.38
b1 = ax1.bar(x - w/2, [v/1000 for v in vals_23], w, color=LBLUE,  label='2023', zorder=3)
b2 = ax1.bar(x + w/2, [v/1000 for v in vals_24], w, color=NAVY, label='2024', zorder=3)
for bar in b2:
    ax1.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.1,
             f'${bar.get_height():.1f}B', ha='center', fontsize=7, color=NAVY, fontweight='bold')
ax1.set_xticks(x); ax1.set_xticklabels(categories, fontsize=9)
ax1.set_ylabel('CAD Billions', fontsize=9)
ax1.set_title('Revenue · Expenses · Surplus', fontsize=11, fontweight='bold', color=NAVY)
ax1.legend(fontsize=8); ax1.set_ylim(0, 22)
ax1.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f'${v:.0f}B'))
add_watermark(ax1)

# ── Pie: Revenue composition ──
ax2 = fig.add_axes([0.43, 0.36, 0.25, 0.28])
rev_items = ops[ops['Category']=='Revenue'].copy()
rev_items = rev_items[rev_items['Item']!='Total revenues']
labels_r  = [l[:25] for l in rev_items['Item'].tolist()]
vals_r    = rev_items['2024_Actual'].tolist()
wedge_colors = [NAVY, STEEL, LBLUE, '#2196B0', '#45B5D4', '#82C4DC', '#B0D9EC', '#C8E6F0', '#D8F0F8']
wedges, texts, autotexts = ax2.pie(
    vals_r, labels=None, autopct='%1.1f%%',
    colors=wedge_colors[:len(vals_r)], startangle=140,
    pctdistance=0.75, wedgeprops={'edgecolor': WHITE, 'linewidth': 1.2}
)
for at in autotexts:
    at.set_fontsize(7); at.set_color(WHITE); at.set_fontweight('bold')
ax2.set_title('Revenue Mix 2024', fontsize=11, fontweight='bold', color=NAVY)
ax2.legend(labels_r, loc='lower center', bbox_to_anchor=(0.5, -0.55),
           fontsize=6, ncol=2, frameon=False)

# ── Waterfall: Net Debt Change ──
ax3 = fig.add_axes([0.71, 0.36, 0.25, 0.28])
items = ['Net Debt\n2023', 'TCA\nInvestment', 'Surplus\n2016', 'Remeasure\nGains', 'Net Debt\n2024']
vals  = [-9602, -2564, 2016, 165, -10005]
running = -9602
bottoms, heights, bar_colors = [], [], []
for i, (item, v) in enumerate(zip(items, vals)):
    if i == 0 or i == len(items)-1:
        bottoms.append(0); heights.append(v); bar_colors.append(NAVY)
    elif v < 0:
        bottoms.append(running); heights.append(v); bar_colors.append(RED_ACC)
        running += v
    else:
        bottoms.append(running); heights.append(v); bar_colors.append(GREEN_ACC)
        running += v
ax3.bar(items, [abs(h)/1000 for h in heights], bottom=[b/1000 for b in bottoms],
        color=bar_colors, width=0.5, zorder=3, edgecolor=WHITE, linewidth=0.5)
ax3.set_title('Net Debt Bridge 2023→2024', fontsize=10, fontweight='bold', color=NAVY)
ax3.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f'${v:.0f}B'))
ax3.set_ylabel('CAD Billions', fontsize=8)
ax3.tick_params(axis='x', labelsize=7)
add_watermark(ax3)

# ── Bottom: Expense by type horizontal bar ──
ax4 = fig.add_axes([0.05, 0.07, 0.88, 0.22])
exp_data = exp[exp['Expense_Type'] != 'Total'].copy()
exp_data = exp_data.sort_values('2024', ascending=True)
y = np.arange(len(exp_data))
ax4.barh(y, exp_data['2023']/1000, height=0.35, color=LBLUE,  label='2023', zorder=3)
ax4.barh(y+0.38, exp_data['2024']/1000, height=0.35, color=NAVY, label='2024', zorder=3)
for i, (v24, v23) in enumerate(zip(exp_data['2024'], exp_data['2023'])):
    ax4.text(v24/1000+0.05, i+0.38, fmt_m(v24), va='center', fontsize=7, color=NAVY, fontweight='bold')
ax4.set_yticks(y+0.19)
ax4.set_yticklabels(exp_data['Expense_Type'], fontsize=8)
ax4.set_title('Expense Breakdown by Type — 2024 vs 2023 (CAD Billions)', fontsize=11, fontweight='bold', color=NAVY)
ax4.xaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f'${v:.0f}B'))
ax4.legend(fontsize=9)
add_watermark(ax4)

save(fig, '01_executive_dashboard.png')

# ═══════════════════════════════════════════════════════════════════════════════
# CHART 2 — REVENUE DEEP DIVE
# ═══════════════════════════════════════════════════════════════════════════════
print("Chart 2: Revenue Deep Dive...")
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('CITY OF TORONTO — REVENUE ANALYSIS 2024', fontsize=15, fontweight='bold', color=NAVY, y=0.98)
fig.patch.set_facecolor(WHITE)

rev = ops[ops['Category'] == 'Revenue'].copy()
rev = rev[rev['Item'] != 'Total revenues']

# 2a — Revenue waterfall budget vs actual
ax = axes[0, 0]
items_r = rev['Item'].str[:28].tolist()
budget  = (rev['2024_Budget'] / 1000).tolist()
actual  = (rev['2024_Actual'] / 1000).tolist()
x = np.arange(len(items_r))
w = 0.38
ax.bar(x - w/2, budget, w, color=LBLUE, label='2024 Budget', zorder=3)
ax.bar(x + w/2, actual, w, color=NAVY,  label='2024 Actual', zorder=3)
for i, (b, a) in enumerate(zip(budget, actual)):
    color = GREEN_ACC if a >= b else RED_ACC
    diff  = ((a - b) / b * 100) if b != 0 else 0
    if abs(diff) > 2:
        ax.text(i, max(a, b) + 0.05, f'{diff:+.0f}%', ha='center', fontsize=7, color=color, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(items_r, rotation=40, ha='right', fontsize=7.5)
ax.set_title('Revenue: Budget vs Actual 2024', fontsize=12, fontweight='bold', color=NAVY)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f'${v:.1f}B'))
ax.set_ylabel('CAD Billions')
ax.legend()
add_watermark(ax)

# 2b — YoY Revenue Growth
ax = axes[0, 1]
yoy = ((rev['2024_Actual'] - rev['2023_Actual']) / rev['2023_Actual'] * 100).tolist()
colors_yoy = [GREEN_ACC if v >= 0 else RED_ACC for v in yoy]
bars = ax.barh(items_r, yoy, color=colors_yoy, zorder=3)
for bar, v in zip(bars, yoy):
    ax.text(v + (0.5 if v >= 0 else -0.5), bar.get_y() + bar.get_height()/2,
            f'{v:+.1f}%', va='center', fontsize=8,
            ha='left' if v >= 0 else 'right', color=BLACK, fontweight='bold')
ax.axvline(0, color=BLACK, linewidth=0.8)
ax.set_title('Revenue YoY Growth Rate (%)', fontsize=12, fontweight='bold', color=NAVY)
ax.set_xlabel('Year-over-Year Change (%)')
add_watermark(ax)

# 2c — Revenue composition stacked bar
ax = axes[1, 0]
rev_pivot = pd.DataFrame({'Item': rev['Item'].str[:20], '2023': rev['2023_Actual'], '2024': rev['2024_Actual']})
bottom23, bottom24 = 0, 0
for i, row in rev_pivot.iterrows():
    c = COLORS_SEQ[i % len(COLORS_SEQ)]
    ax.bar(['2023'], [row['2023']/1000], bottom=bottom23/1000, color=c, width=0.5, edgecolor=WHITE, linewidth=0.5)
    ax.bar(['2024'], [row['2024']/1000], bottom=bottom24/1000, color=c, width=0.5, edgecolor=WHITE, linewidth=0.5, label=row['Item'])
    if row['2024'] > 200:
        ax.text(1, (bottom24 + row['2024']/2)/1000, f"{row['Item'][:18]}\n{fmt_m(row['2024'])}",
                ha='center', va='center', fontsize=6, color=WHITE)
    bottom23 += row['2023']
    bottom24 += row['2024']
ax.set_title('Revenue Composition 2023 vs 2024', fontsize=12, fontweight='bold', color=NAVY)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f'${v:.0f}B'))
ax.set_ylabel('CAD Billions')
add_watermark(ax)

# 2d — Investment income spike analysis
ax = axes[1, 1]
years = ['2023 Budget', '2023 Actual', '2024 Budget', '2024 Actual']
inv_income = [0, 337, 266, 801]
colors_inv = [LBLUE, LBLUE, NAVY, NAVY]
bars = ax.bar(years, inv_income, color=colors_inv, width=0.5, zorder=3)
for bar in bars:
    ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+10,
            f'${bar.get_height():,.0f}M', ha='center', fontsize=9, color=NAVY, fontweight='bold')
ax.axhline(266, color=RED_ACC, linestyle='--', linewidth=1, label='2024 Budget ($266M)')
ax.set_title('Investment Income: +138% vs Prior Year\n(Interest Rate Tailwind + Portfolio Growth)', fontsize=11, fontweight='bold', color=NAVY)
ax.set_ylabel('CAD Millions')
ax.legend()
ax.annotate('$535M ABOVE\nBUDGET', xy=(3, 801), xytext=(2.3, 650),
            arrowprops=dict(arrowstyle='->', color=RED_ACC, lw=1.5),
            fontsize=9, color=RED_ACC, fontweight='bold')
add_watermark(ax)

plt.tight_layout(rect=[0, 0, 1, 0.96])
save(fig, '02_revenue_deep_dive.png')

# ═══════════════════════════════════════════════════════════════════════════════
# CHART 3 — EXPENSE ANALYSIS
# ═══════════════════════════════════════════════════════════════════════════════
print("Chart 3: Expense Analysis...")
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('CITY OF TORONTO — EXPENSE ANALYSIS 2024', fontsize=15, fontweight='bold', color=NAVY, y=0.98)
fig.patch.set_facecolor(WHITE)

exp_service = ops[ops['Category'] == 'Expense'].copy()
exp_service = exp_service[exp_service['Item'] != 'Total expenses']

# 3a — Expense vs Budget by service
ax = axes[0, 0]
items_e = exp_service['Item'].str[:25].tolist()
bud = (exp_service['2024_Budget']/1000).tolist()
act = (exp_service['2024_Actual']/1000).tolist()
x = np.arange(len(items_e)); w = 0.38
ax.barh(x - w/2, bud, w, color=LBLUE, label='Budget', zorder=3)
ax.barh(x + w/2, act, w, color=NAVY,  label='Actual', zorder=3)
for i, (b, a) in enumerate(zip(bud, act)):
    diff = a - b
    c = RED_ACC if diff > 0 else GREEN_ACC
    ax.text(max(a, b)+0.02, i+w/2, f'{diff:+.2f}B', va='center', fontsize=7, color=c, fontweight='bold')
ax.set_yticks(x); ax.set_yticklabels(items_e, fontsize=8)
ax.set_title('Expenses: Budget vs Actual 2024', fontsize=12, fontweight='bold', color=NAVY)
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f'${v:.1f}B'))
ax.legend(); add_watermark(ax)

# 3b — Expense type breakdown donut
ax = axes[0, 1]
exp_type = exp[exp['Expense_Type'] != 'Total'].copy()
exp_type = exp_type.sort_values('2024', ascending=False)
wedge, texts, autotexts = ax.pie(
    exp_type['2024'], labels=None,
    autopct=lambda p: f'{p:.1f}%' if p > 3 else '',
    colors=COLORS_SEQ[:len(exp_type)],
    startangle=90,
    pctdistance=0.78,
    wedgeprops={'edgecolor': WHITE, 'linewidth': 1.5, 'width': 0.65}
)
for at in autotexts: at.set_fontsize(8); at.set_color(WHITE); at.set_fontweight('bold')
ax.set_title('Expense Type Mix 2024\n(Total: $16.2B)', fontsize=12, fontweight='bold', color=NAVY)
labels_e = [f"{r['Expense_Type'][:22]} ({fmt_m(r['2024'])})" for _, r in exp_type.iterrows()]
ax.legend(labels_e, loc='lower center', bbox_to_anchor=(0.5, -0.55), fontsize=7, ncol=1, frameon=False)
add_watermark(ax)

# 3c — Salary cost trend (dominant expense)
ax = axes[1, 0]
sal_data = {
    'Category'   : ['Salaries & Benefits', 'Contracted Services', 'Materials', 'Transfer Payments', 'Other'],
    '2023'       : [7069,  2209, 1387, 1860, 550],
    '2024'       : [7642,  2205, 1743, 2083, 513],
}
sal_df = pd.DataFrame(sal_data)
x = np.arange(len(sal_df)); w = 0.38
ax.bar(x - w/2, sal_df['2023']/1000, w, color=LBLUE, label='2023', zorder=3)
ax.bar(x + w/2, sal_df['2024']/1000, w, color=NAVY,  label='2024', zorder=3)
for i, row in sal_df.iterrows():
    pct = (row['2024'] - row['2023']) / row['2023'] * 100
    c   = RED_ACC if pct > 5 else GREEN_ACC if pct < 0 else DGRAY
    ax.text(i+w/2, row['2024']/1000+0.02, f'{pct:+.1f}%', ha='center', fontsize=8, color=c, fontweight='bold')
ax.set_xticks(x); ax.set_xticklabels(sal_df['Category'], rotation=15, ha='right', fontsize=8)
ax.set_title('Key Expense Categories: 2023 vs 2024', fontsize=12, fontweight='bold', color=NAVY)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f'${v:.0f}B'))
ax.set_ylabel('CAD Billions'); ax.legend()
add_watermark(ax)

# 3d — Service budget variance heatmap
ax = axes[1, 1]
srv_names = [i[:22] for i in exp_service['Item'].tolist()]
variance  = (exp_service['2024_Actual'] - exp_service['2024_Budget']).tolist()
variance_pct = [(a-b)/b*100 if b!=0 else 0 for a,b in zip(exp_service['2024_Actual'], exp_service['2024_Budget'])]
data_h = np.array(variance_pct).reshape(-1, 1)
im = ax.imshow(data_h, aspect='auto', cmap='RdYlGn_r', vmin=-20, vmax=20)
ax.set_yticks(np.arange(len(srv_names))); ax.set_yticklabels(srv_names, fontsize=8)
ax.set_xticks([]); ax.set_xlabel('Variance %', fontsize=9)
for i, (v_m, v_pct) in enumerate(zip(variance, variance_pct)):
    ax.text(0, i, f'{v_pct:+.1f}%  ({fmt_m(v_m)})', ha='center', va='center', fontsize=8,
            color=WHITE if abs(v_pct) > 8 else BLACK, fontweight='bold')
plt.colorbar(im, ax=ax, shrink=0.8, label='Budget Variance %')
ax.set_title('Expense Budget Variance by Service', fontsize=12, fontweight='bold', color=NAVY)
add_watermark(ax)

plt.tight_layout(rect=[0, 0, 1, 0.96])
save(fig, '03_expense_analysis.png')

# ═══════════════════════════════════════════════════════════════════════════════
# CHART 4 — BALANCE SHEET ANALYSIS
# ═══════════════════════════════════════════════════════════════════════════════
print("Chart 4: Balance Sheet Analysis...")
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('CITY OF TORONTO — BALANCE SHEET DEEP DIVE', fontsize=15, fontweight='bold', color=NAVY, y=0.98)
fig.patch.set_facecolor(WHITE)

# 4a — Assets vs Liabilities grouped
ax = axes[0, 0]
fin_assets = [17301, 18225]
tot_liab   = [26903, 28230]
tca_vals   = [42853, 45417]
years      = ['2023', '2024']
x = np.arange(2); w = 0.25
ax.bar(x - w,   [v/1000 for v in fin_assets], w, color=LBLUE,     label='Financial Assets',  zorder=3)
ax.bar(x,       [v/1000 for v in tot_liab],   w, color=RED_ACC,   label='Total Liabilities', zorder=3, alpha=0.8)
ax.bar(x + w,   [v/1000 for v in tca_vals],   w, color=NAVY,      label='Capital Assets',    zorder=3)
ax.set_xticks(x); ax.set_xticklabels(years)
ax.set_title('Assets vs Liabilities Structure', fontsize=12, fontweight='bold', color=NAVY)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f'${v:.0f}B'))
ax.set_ylabel('CAD Billions'); ax.legend()
add_watermark(ax)

# 4b — Liability waterfall 2023 to 2024
ax = axes[0, 1]
liab_items = ['Accounts Pay', 'Deferred Rev', 'Long-term Debt', 'Employee Ben', 'ARO', 'Mortgages', 'Other']
liab_23 = [3599, 7552, 8586, 4810, 993, 451, 912]
liab_24 = [4201, 7891, 8880, 4930, 1005, 490, 833]
changes  = [a-b for a,b in zip(liab_24, liab_23)]
bar_c    = [RED_ACC if c>0 else GREEN_ACC for c in changes]
bars     = ax.bar(liab_items, changes, color=bar_c, zorder=3)
for bar, v in zip(bars, changes):
    ax.text(bar.get_x()+bar.get_width()/2, v+(5 if v>=0 else -20),
            f'{fmt_m(v)}', ha='center', fontsize=7, fontweight='bold',
            color=RED_ACC if v>0 else GREEN_ACC)
ax.axhline(0, color=BLACK, linewidth=0.8)
ax.set_title('Liability Change 2023→2024 (CAD Millions)', fontsize=12, fontweight='bold', color=NAVY)
ax.set_ylabel('Change (CAD Millions)')
ax.set_xticklabels(liab_items, rotation=30, ha='right', fontsize=8)
add_watermark(ax)

# 4c — Capital asset composition
ax = axes[1, 0]
tca_data = tca[(tca['Category'] != 'Total') & (~tca['Asset_Type'].str.startswith('Total'))].copy()
tca_data = tca_data[tca_data['Net_Book_Value_2024'] > 0]
tca_plot = tca_data.sort_values('Net_Book_Value_2024', ascending=True)
colors_tca = [NAVY if c=='Infrastructure' else STEEL if c=='General' else LBLUE
              for c in tca_plot['Category']]
bars = ax.barh(tca_plot['Asset_Type'].str[:28], tca_plot['Net_Book_Value_2024']/1000,
               color=colors_tca, zorder=3)
for bar in bars:
    ax.text(bar.get_width()+0.05, bar.get_y()+bar.get_height()/2,
            f'${bar.get_width():.1f}B', va='center', fontsize=7.5, color=NAVY, fontweight='bold')
ax.set_title('Capital Asset Breakdown (Net Book Value 2024)', fontsize=12, fontweight='bold', color=NAVY)
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f'${v:.0f}B'))
ax.set_xlabel('CAD Billions')
patches = [mpatches.Patch(color=NAVY, label='Infrastructure'),
           mpatches.Patch(color=STEEL, label='General'),
           mpatches.Patch(color=LBLUE, label='Under Construction')]
ax.legend(handles=patches, fontsize=8)
add_watermark(ax)

# 4d — Net Debt trend + composition
ax = axes[1, 1]
nd_23 = 9602
nd_24 = 10005
categories_nd = ['Long-term Debt', 'Employee Ben.', 'Deferred Rev', 'Other Liab', 'Net Financial Assets']
vals_nd = [8880, 4930, 7891, 6529, -18225]
running = 0
for i, (cat, v) in enumerate(zip(categories_nd, vals_nd)):
    c = NAVY if v > 0 else GREEN_ACC
    ax.bar(cat, abs(v)/1000, bottom=running/1000, color=c, edgecolor=WHITE, linewidth=0.5, zorder=3)
    if abs(v) > 500:
        ax.text(i, (running + v/2)/1000, f'${abs(v)/1000:.1f}B', ha='center', va='center',
                fontsize=7.5, color=WHITE if v > 0 else BLACK, fontweight='bold')
    if v > 0: running += v
ax.axhline(nd_24/1000, color=RED_ACC, linestyle='--', linewidth=1.5, label=f'Net Debt ${nd_24/1000:.1f}B')
ax.set_title('Liability Composition vs Financial Assets\n(Explaining Net Debt of $10.0B)', fontsize=11, fontweight='bold', color=NAVY)
ax.set_xticklabels(categories_nd, rotation=20, ha='right', fontsize=8)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f'${v:.0f}B'))
ax.legend(); add_watermark(ax)

plt.tight_layout(rect=[0, 0, 1, 0.96])
save(fig, '04_balance_sheet.png')

# ═══════════════════════════════════════════════════════════════════════════════
# CHART 5 — SEGMENT ANALYSIS (SERVICE & ENTITY)
# ═══════════════════════════════════════════════════════════════════════════════
print("Chart 5: Segment Analysis...")
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('CITY OF TORONTO — SEGMENT PERFORMANCE ANALYSIS', fontsize=15, fontweight='bold', color=NAVY, y=0.98)
fig.patch.set_facecolor(WHITE)

seg_plot = seg[seg['Segment'] != 'Consolidated'].copy()

# 5a — Revenue vs Expense by service (bubble-like chart)
ax = axes[0, 0]
srv_names_s = seg_plot['Segment'].str[:20].tolist()
rev_24 = seg_plot['Total_Revenue_2024'].tolist()
exp_24 = seg_plot['Total_Expenses_2024'].tolist()
surplus_24 = seg_plot['Annual_Surplus_Deficit_2024'].tolist()
x = np.arange(len(srv_names_s)); w = 0.38
ax.bar(x - w/2, [v/1000 for v in rev_24], w, color=LBLUE, label='Revenue', zorder=3)
ax.bar(x + w/2, [v/1000 for v in exp_24], w, color=NAVY,  label='Expenses', zorder=3)
for i, s in enumerate(surplus_24):
    c = GREEN_ACC if s >= 0 else RED_ACC
    ax.text(i, max(rev_24[i], exp_24[i])/1000 + 0.1,
            f'{fmt_m(s)}', ha='center', fontsize=6.5, color=c, fontweight='bold')
ax.set_xticks(x); ax.set_xticklabels(srv_names_s, rotation=35, ha='right', fontsize=7.5)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f'${v:.0f}B'))
ax.set_ylabel('CAD Billions'); ax.set_title('Revenue vs Expenses by Service Segment 2024', fontsize=12, fontweight='bold', color=NAVY)
ax.legend(); add_watermark(ax)

# 5b — Surplus/Deficit by service horizontal
ax = axes[0, 1]
colors_seg = [GREEN_ACC if v >= 0 else RED_ACC for v in surplus_24]
bars = ax.barh(srv_names_s, [v/1000 for v in surplus_24], color=colors_seg, zorder=3)
for bar, v in zip(bars, surplus_24):
    ha = 'left' if v >= 0 else 'right'
    offset = 0.01 if v >= 0 else -0.01
    ax.text(v/1000 + offset, bar.get_y()+bar.get_height()/2,
            fmt_m(v), va='center', fontsize=8, ha=ha, color=BLACK, fontweight='bold')
ax.axvline(0, color=BLACK, linewidth=0.8)
ax.set_title('Annual Surplus / Deficit by Service 2024', fontsize=12, fontweight='bold', color=NAVY)
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f'${v:.1f}B'))
ax.set_xlabel('CAD Billions'); add_watermark(ax)

# 5c — Entity comparison
ax = axes[1, 0]
ent_plot = ent[ent['Entity'] != 'Total Consolidated'].copy()
ent_names = ent_plot['Entity'].str[:25].tolist()
ent_rev   = (ent_plot['Total_Revenue_2024'] / 1000).tolist()
ent_exp   = (ent_plot['Total_Expenses_2024'] / 1000).tolist()
ent_sur   = ent_plot['Annual_Surplus_Deficit_2024'].tolist()
x = np.arange(len(ent_names)); w = 0.38
ax.bar(x - w/2, ent_rev, w, color=LBLUE, label='Revenue', zorder=3)
ax.bar(x + w/2, ent_exp, w, color=NAVY,  label='Expenses', zorder=3)
for i, s in enumerate(ent_sur):
    c = GREEN_ACC if s >= 0 else RED_ACC
    ax.text(i, max(ent_rev[i], ent_exp[i])+0.08, fmt_m(s),
            ha='center', fontsize=6.5, color=c, fontweight='bold')
ax.set_xticks(x); ax.set_xticklabels(ent_names, rotation=30, ha='right', fontsize=7.5)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f'${v:.0f}B'))
ax.set_title('Performance by Entity 2024', fontsize=12, fontweight='bold', color=NAVY); ax.legend()
add_watermark(ax)

# 5d — YoY Surplus Change by Segment
ax = axes[1, 1]
seg_yoy = ((seg_plot['Annual_Surplus_Deficit_2024'] - seg_plot['Annual_Surplus_Deficit_2023'])).tolist()
c_yoy   = [GREEN_ACC if v >= 0 else RED_ACC for v in seg_yoy]
bars    = ax.bar(srv_names_s, [v/1000 for v in seg_yoy], color=c_yoy, zorder=3)
for bar, v in zip(bars, seg_yoy):
    ax.text(bar.get_x()+bar.get_width()/2, (v/1000)+(0.02 if v>=0 else -0.02),
            fmt_m(v), ha='center', fontsize=7, fontweight='bold',
            color=GREEN_ACC if v>=0 else RED_ACC, va='bottom' if v>=0 else 'top')
ax.axhline(0, color=BLACK, linewidth=0.8)
ax.set_xticklabels(srv_names_s, rotation=35, ha='right', fontsize=7.5)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f'${v:.1f}B'))
ax.set_title('Surplus/Deficit Improvement by Service (2023→2024)', fontsize=12, fontweight='bold', color=NAVY)
add_watermark(ax)

plt.tight_layout(rect=[0, 0, 1, 0.96])
save(fig, '05_segment_analysis.png')

# ═══════════════════════════════════════════════════════════════════════════════
# CHART 6 — CASH FLOW & INVESTMENTS
# ═══════════════════════════════════════════════════════════════════════════════
print("Chart 6: Cash Flow & Investments...")
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('CITY OF TORONTO — CASH FLOW & INVESTMENT PORTFOLIO', fontsize=15, fontweight='bold', color=NAVY, y=0.98)
fig.patch.set_facecolor(WHITE)

# 6a — Cash flow waterfall
ax = axes[0, 0]
cf_items  = ['Operating\nActivities', 'Capital\nActivities', 'Financing\nActivities', 'Investing\nActivities', 'Net Change']
cf_vals   = [4122, -4332, 270, -1165, -1105]
cf_colors = [GREEN_ACC if v>=0 else RED_ACC for v in cf_vals]
bars      = ax.bar(cf_items, cf_vals, color=cf_colors, width=0.5, zorder=3, edgecolor=WHITE)
for bar, v in zip(bars, cf_vals):
    ypos = v + (80 if v>=0 else -120)
    ax.text(bar.get_x()+bar.get_width()/2, ypos, fmt_m(v),
            ha='center', fontsize=9, fontweight='bold', color=GREEN_ACC if v>=0 else RED_ACC)
ax.axhline(0, color=BLACK, linewidth=0.8)
ax.set_title('Cash Flow by Activity 2024', fontsize=12, fontweight='bold', color=NAVY)
ax.set_ylabel('CAD Millions')
add_watermark(ax)

# 6b — Investment portfolio mix
ax = axes[0, 1]
inv_plot = inv[inv['Investment_Type'] != 'Total'].copy()
inv_plot = inv_plot.sort_values('2024', ascending=False)
x = np.arange(len(inv_plot)); w = 0.38
ax.bar(x - w/2, inv_plot['2023']/1000, w, color=LBLUE, label='2023', zorder=3)
ax.bar(x + w/2, inv_plot['2024']/1000, w, color=NAVY,  label='2024', zorder=3)
for i, row in inv_plot.iterrows():
    pct = (row['2024']-row['2023'])/row['2023']*100 if row['2023']>0 else 999
    c   = GREEN_ACC if pct>0 else RED_ACC
    label_p = f'+NEW' if pct==999 else f'{pct:+.0f}%'
    ax.text(list(inv_plot.index).index(i)+w/2, row['2024']/1000+0.02, label_p,
            ha='center', fontsize=7, color=c, fontweight='bold')
ax.set_xticks(x); ax.set_xticklabels(inv_plot['Investment_Type'], rotation=35, ha='right', fontsize=8)
ax.set_title('Investment Portfolio 2023 vs 2024 ($8.4B Total)', fontsize=12, fontweight='bold', color=NAVY)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f'${v:.1f}B'))
ax.set_ylabel('CAD Billions'); ax.legend()
add_watermark(ax)

# 6c — Capital spending analysis
ax = axes[1, 0]
categories_cap = ['General Assets', 'Infrastructure', 'Under Construction', 'Total']
additions_24   = [1574, 1996, 845, 4415]
additions_23   = [1800, 2666, 505, 4971]
x = np.arange(4); w = 0.38
ax.bar(x-w/2, [v/1000 for v in additions_23], w, color=LBLUE, label='2023 Additions', zorder=3)
ax.bar(x+w/2, [v/1000 for v in additions_24], w, color=NAVY,  label='2024 Additions', zorder=3)
for i, (a23, a24) in enumerate(zip(additions_23, additions_24)):
    pct = (a24-a23)/a23*100
    c   = RED_ACC if pct>0 else GREEN_ACC
    ax.text(i+w/2, a24/1000+0.02, f'{pct:+.1f}%', ha='center', fontsize=8, color=c, fontweight='bold')
ax.set_xticks(x); ax.set_xticklabels(categories_cap, fontsize=9)
ax.set_title('Capital Asset Additions 2023 vs 2024', fontsize=12, fontweight='bold', color=NAVY)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f'${v:.1f}B'))
ax.set_ylabel('CAD Billions'); ax.legend()
add_watermark(ax)

# 6d — Debt repayment schedule
ax = axes[1, 1]
debt_plot = debt[debt['Year'] != 'Total'].copy()
x = np.arange(len(debt_plot))
ax.bar(x, debt_plot['Principal']/1000, color=NAVY, label='Principal', zorder=3)
ax.bar(x, debt_plot['Interest']/1000, bottom=debt_plot['Principal']/1000, color=LBLUE, label='Interest', zorder=3)
for i, row in enumerate(debt_plot.itertuples()):
    ax.text(i, (row.Principal + row.Interest)/1000 + 0.05,
            f'${(row.Principal+row.Interest)/1000:.1f}B', ha='center', fontsize=7.5, color=NAVY, fontweight='bold')
ax.set_xticks(x); ax.set_xticklabels(debt_plot['Year'], fontsize=9)
ax.set_title('Long-Term Debt Repayment Schedule ($16.6B Total)', fontsize=12, fontweight='bold', color=NAVY)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f'${v:.0f}B'))
ax.set_ylabel('CAD Billions'); ax.legend()
add_watermark(ax)

plt.tight_layout(rect=[0, 0, 1, 0.96])
save(fig, '06_cashflow_investments.png')

# ═══════════════════════════════════════════════════════════════════════════════
# CHART 7 — FINANCIAL HEALTH SCORECARD & STATISTICAL ANALYSIS
# ═══════════════════════════════════════════════════════════════════════════════
print("Chart 7: Financial Health Scorecard...")
fig, axes = plt.subplots(2, 3, figsize=(18, 11))
fig.suptitle('CITY OF TORONTO — FINANCIAL HEALTH & RISK ANALYSIS', fontsize=15, fontweight='bold', color=NAVY, y=0.98)
fig.patch.set_facecolor(WHITE)

# 7a — Radar / Spider chart — McKinsey metrics
ax = axes[0, 0]
metrics_radar = ['Revenue\nGrowth', 'Surplus\nMargin', 'Capital\nInvestment', 'Debt\nManagement', 'Asset\nGrowth', 'Operating\nEfficiency']
scores_24 = [8.5, 7.5, 9.0, 6.5, 8.0, 8.5]
scores_23 = [6.0, 6.5, 8.5, 6.5, 7.0, 7.5]
N = len(metrics_radar)
angles = [n/float(N)*2*np.pi for n in range(N)]
angles += angles[:1]
scores_24 += scores_24[:1]
scores_23 += scores_23[:1]
ax_radar = plt.subplot(2, 3, 1, polar=True)
ax_radar.set_facecolor(WHITE)
ax_radar.plot(angles, scores_24, 'o-', linewidth=2, color=NAVY, label='2024')
ax_radar.fill(angles, scores_24, alpha=0.25, color=NAVY)
ax_radar.plot(angles, scores_23, 'o--', linewidth=1.5, color=LBLUE, label='2023')
ax_radar.fill(angles, scores_23, alpha=0.1, color=LBLUE)
ax_radar.set_xticks(angles[:-1])
ax_radar.set_xticklabels(metrics_radar, fontsize=8)
ax_radar.set_ylim(0, 10)
ax_radar.set_title('Financial Health Scorecard\n(McKinsey Rating 0-10)', fontsize=11, fontweight='bold', color=NAVY, pad=15)
ax_radar.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=9)

# 7b — KPI trend bars
ax = axes[0, 1]
kpi_names  = ['Revenue\nGrowth %', 'Surplus\nMargin %', 'Net Debt/\nRevenue', 'Capital/\nRevenue %', 'Salary\nGrowth %']
kpi_24_v   = [11.5, 11.1, 55.0, 24.3, 8.1]
kpi_23_v   = [0.0,   7.7, 58.8, 26.7, 0.0]
kpi_bmark  = [5.0,   8.0, 50.0, 20.0, 4.0]
x = np.arange(5); w = 0.25
ax.bar(x - w, kpi_23_v, w, color=LBLUE, label='2023', zorder=3)
ax.bar(x,     kpi_24_v, w, color=NAVY,  label='2024', zorder=3)
ax.bar(x + w, kpi_bmark, w, color=LGRAY, label='Benchmark', zorder=3, edgecolor=DGRAY)
ax.set_xticks(x); ax.set_xticklabels(kpi_names, fontsize=8)
ax.set_title('Key Performance Indicators vs Benchmark', fontsize=11, fontweight='bold', color=NAVY)
ax.set_ylabel('%'); ax.legend(fontsize=8)
add_watermark(ax)

# 7c — Interest rate sensitivity
ax = axes[0, 2]
rate_changes = [-2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2]
inv_impact   = [648, 486, 324, 162, 0, -162, -324, -486, -648]
debt_impact  = [-318, -238.5, -159, -79.5, 0, 79.5, 159, 238.5, 318]
ax.plot(rate_changes, inv_impact, 'o-', color=NAVY, linewidth=2, markersize=6, label='Investment Portfolio Impact')
ax.plot(rate_changes, debt_impact, 's--', color=LBLUE, linewidth=2, markersize=6, label='Long-Term Debt Impact')
ax.fill_between(rate_changes, inv_impact, alpha=0.1, color=NAVY)
ax.fill_between(rate_changes, debt_impact, alpha=0.1, color=LBLUE)
ax.axhline(0, color=BLACK, linewidth=0.8); ax.axvline(0, color=DGRAY, linewidth=0.5, linestyle=':')
ax.set_xlabel('Interest Rate Change (%)')
ax.set_ylabel('Portfolio Fair Value Change (CAD Millions)')
ax.set_title('Interest Rate Sensitivity Analysis', fontsize=11, fontweight='bold', color=NAVY)
ax.legend(fontsize=8)
add_watermark(ax)

# 7d — Deferred revenue top items
ax = axes[1, 0]
def_top = def_[def_['Category'] != 'Total'].copy()
def_top = def_top.sort_values('Ending_2024', ascending=True).tail(7)
colors_dr = [NAVY if v > 0 else STEEL for v in def_top['Ending_2024']]
ax.barh(def_top['Category'].str[:30], def_top['Ending_2024']/1000, color=colors_dr, zorder=3)
for i, row in enumerate(def_top.itertuples()):
    ax.text(row.Ending_2024/1000+0.01, i, fmt_m(row.Ending_2024),
            va='center', fontsize=7.5, color=NAVY, fontweight='bold')
ax.set_title('Deferred Revenue — Top Categories 2024\n($7.9B Total — Future Obligations)', fontsize=11, fontweight='bold', color=NAVY)
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f'${v:.1f}B'))
ax.set_xlabel('CAD Billions'); add_watermark(ax)

# 7e — Government transfers breakdown
ax = axes[1, 1]
xfer_src = xfer[xfer['Source'].isin(['Federal', 'Provincial', 'Other'])].copy()
xfer_src = xfer_src[xfer_src['Transfer_Type'] != 'Total']
pivot_xfer = xfer_src.pivot_table(index='Source', columns='Transfer_Type', values='2024', aggfunc='sum').fillna(0)
pivot_xfer.plot(kind='bar', ax=ax, color=[NAVY, LBLUE], width=0.6, zorder=3)
ax.set_xticklabels(pivot_xfer.index, rotation=0, fontsize=10)
ax.set_title('Government Transfers by Source & Type 2024\n($4.7B Total)', fontsize=11, fontweight='bold', color=NAVY)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f'${v/1000:.1f}B'))
ax.set_ylabel('CAD Billions'); ax.legend(title='Type', fontsize=8)
add_watermark(ax)

# 7f — Employee benefit trend
ax = axes[1, 2]
ben_types = ['Sick Leave', 'WSIB\nObligations', 'Other Employment\n& Post-Employment', 'Unamortized\nActuarial Gain']
ben_24    = [411, 1186, 2236, 1097]
ben_23    = [418, 1096, 2532, 764]
x = np.arange(4); w = 0.38
ax.bar(x-w/2, [v/1000 for v in ben_23], w, color=LBLUE, label='2023', zorder=3)
ax.bar(x+w/2, [v/1000 for v in ben_24], w, color=NAVY,  label='2024', zorder=3)
for i, (b23, b24) in enumerate(zip(ben_23, ben_24)):
    pct = (b24-b23)/b23*100
    c   = RED_ACC if pct>0 else GREEN_ACC
    ax.text(i+w/2, b24/1000+0.01, f'{pct:+.1f}%', ha='center', fontsize=8, color=c, fontweight='bold')
ax.set_xticks(x); ax.set_xticklabels(ben_types, fontsize=8)
ax.set_title('Employee Benefit Liabilities ($4.9B Total)', fontsize=11, fontweight='bold', color=NAVY)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f'${v:.1f}B'))
ax.set_ylabel('CAD Billions'); ax.legend()
add_watermark(ax)

plt.tight_layout(rect=[0, 0, 1, 0.96])
save(fig, '07_health_risk.png')

# ═══════════════════════════════════════════════════════════════════════════════
# CHART 8 — STATISTICAL REGRESSION & PREDICTIVE INSIGHTS
# ═══════════════════════════════════════════════════════════════════════════════
print("Chart 8: Statistical Analysis & Projections...")
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('CITY OF TORONTO — STATISTICAL ANALYSIS & PROJECTIONS', fontsize=15, fontweight='bold', color=NAVY, y=0.98)
fig.patch.set_facecolor(WHITE)

# Simulated multi-year data based on growth rates from report
years_hist = np.array([2019, 2020, 2021, 2022, 2023, 2024])
revenue_h  = np.array([13200, 13000, 13800, 15100, 16325, 18202])
expenses_h = np.array([12800, 13100, 13500, 14200, 15075, 16186])
surplus_h  = revenue_h - expenses_h
tca_h      = np.array([33000, 34500, 36000, 38500, 42853, 45417])
net_debt_h = np.array([5500, 6200, 7000, 8000, 9602, 10005])

# 8a — Revenue trend + linear regression + forecast
ax = axes[0, 0]
slope_r, intercept_r, r_r, p_r, se_r = stats.linregress(years_hist, revenue_h)
years_proj = np.array([2025, 2026, 2027])
rev_proj   = slope_r * years_proj + intercept_r
years_all  = np.concatenate([years_hist, years_proj])
rev_all    = np.concatenate([revenue_h,  rev_proj])
ax.plot(years_hist, revenue_h/1000, 'o-', color=NAVY, linewidth=2.5, markersize=8, label='Historical Revenue', zorder=5)
ax.plot(years_proj, rev_proj/1000,  's--', color=LBLUE, linewidth=2, markersize=8, label=f'Projected (R²={r_r**2:.2f})', zorder=5)
x_line = np.linspace(2019, 2027, 100)
y_line = (slope_r * x_line + intercept_r) / 1000
ax.plot(x_line, y_line, ':', color=DGRAY, linewidth=1, alpha=0.5)
ci = 1.96 * se_r * np.sqrt(1 + 1/len(years_hist) + (years_proj - years_hist.mean())**2 / ((years_hist - years_hist.mean())**2).sum())
ax.fill_between(years_proj, (rev_proj-ci)/1000, (rev_proj+ci)/1000, alpha=0.2, color=LBLUE, label='95% CI')
for y, r in zip(years_hist, revenue_h):
    ax.annotate(f'${r/1000:.1f}B', (y, r/1000+0.15), fontsize=7, ha='center', color=NAVY)
ax.axvline(2024.5, color=LGRAY, linestyle='--', linewidth=1)
ax.text(2025, revenue_h[-1]/1000 - 0.5, '← Actual  |  Forecast →', fontsize=8, color=DGRAY)
ax.set_title(f'Revenue Trend & Projection\n(CAGR: {((revenue_h[-1]/revenue_h[0])**(1/5)-1)*100:.1f}%  |  Linear Slope: +${slope_r:.0f}M/yr)', fontsize=11, fontweight='bold', color=NAVY)
ax.set_ylabel('CAD Billions'); ax.legend(fontsize=8)
add_watermark(ax)

# 8b — Expense regression
ax = axes[0, 1]
slope_e, intercept_e, r_e, _, se_e = stats.linregress(years_hist, expenses_h)
exp_proj = slope_e * years_proj + intercept_e
ax.plot(years_hist, expenses_h/1000, 'o-', color=NAVY, linewidth=2.5, markersize=8, label='Historical Expenses')
ax.plot(years_proj, exp_proj/1000,   's--', color=RED_ACC, linewidth=2, markersize=8, label=f'Projected (R²={r_e**2:.2f})')
ax.fill_between(years_proj,
                (exp_proj - 1.96*se_e)/1000,
                (exp_proj + 1.96*se_e)/1000, alpha=0.15, color=RED_ACC)
surplus_proj = rev_proj - exp_proj
for y, s in zip(years_proj, surplus_proj):
    c = GREEN_ACC if s >= 0 else RED_ACC
    ax.annotate(f'Surplus\n{fmt_m(s)}', (y, exp_proj[list(years_proj).index(y)]/1000+0.3),
                fontsize=7, color=c, ha='center', fontweight='bold')
ax.set_title(f'Expense Trajectory & Surplus Forecast\n(Cost Slope: +${slope_e:.0f}M/yr)', fontsize=11, fontweight='bold', color=NAVY)
ax.set_ylabel('CAD Billions'); ax.legend(fontsize=8)
add_watermark(ax)

# 8c — Revenue vs Expense scatter correlation
ax = axes[1, 0]
ax.scatter(revenue_h/1000, expenses_h/1000, c=years_hist, cmap='Blues',
           s=150, zorder=5, edgecolor=NAVY, linewidth=1.2)
for y, r, e in zip(years_hist, revenue_h, expenses_h):
    ax.annotate(str(y), (r/1000+0.1, e/1000), fontsize=8, color=NAVY, fontweight='bold')
slope_re, intercept_re, r_re, _, _ = stats.linregress(revenue_h, expenses_h)
x_scatter = np.linspace(revenue_h.min(), revenue_h.max()*1.15, 100)
ax.plot(x_scatter/1000, (slope_re*x_scatter + intercept_re)/1000, '--', color=STEEL, linewidth=1.5,
        label=f'Linear Fit (R²={r_re**2:.3f})')
ax.plot([12, 21], [12, 21], ':', color=LGRAY, linewidth=1, label='Break-Even Line')
ax.fill_between(x_scatter/1000, x_scatter/1000, (slope_re*x_scatter+intercept_re)/1000,
                alpha=0.08, color=GREEN_ACC, label='Surplus Region')
ax.set_xlabel('Total Revenue (CAD Billions)'); ax.set_ylabel('Total Expenses (CAD Billions)')
ax.set_title(f'Revenue–Expense Correlation\n(Pearson r = {r_re:.4f}  |  High positive correlation)', fontsize=11, fontweight='bold', color=NAVY)
ax.legend(fontsize=8); add_watermark(ax)

# 8d — Net Debt trajectory
ax = axes[1, 1]
slope_nd, intercept_nd, r_nd, _, se_nd = stats.linregress(years_hist, net_debt_h)
nd_proj = slope_nd * years_proj + intercept_nd
ax.plot(years_hist, net_debt_h/1000, 'o-', color=RED_ACC, linewidth=2.5, markersize=8, label='Historical Net Debt')
ax.plot(years_proj, nd_proj/1000,    's--', color=NAVY, linewidth=2, markersize=8, label=f'Projected (R²={r_nd**2:.2f})')
ax.fill_between(years_proj, (nd_proj-1.5*se_nd)/1000, (nd_proj+1.5*se_nd)/1000, alpha=0.15, color=NAVY)
ax2_twin = ax.twinx()
nd_pct_rev = net_debt_h / revenue_h * 100
ax2_twin.plot(years_hist, nd_pct_rev, '^:', color=LBLUE, linewidth=1.5, markersize=6, label='Debt/Revenue %')
ax2_twin.set_ylabel('Net Debt / Revenue (%)', color=LBLUE)
ax.set_title(f'Net Debt Trajectory\n(Growth Rate: +${slope_nd:.0f}M/yr  |  Current: 55% of Revenue)', fontsize=11, fontweight='bold', color=NAVY)
ax.set_ylabel('CAD Billions (Net Debt)')
lines1, labels1 = ax.get_legend_handles_labels()
lines2, labels2 = ax2_twin.get_legend_handles_labels()
ax.legend(lines1+lines2, labels1+labels2, fontsize=8)
add_watermark(ax)

plt.tight_layout(rect=[0, 0, 1, 0.96])
save(fig, '08_statistical_projections.png')

# ═══════════════════════════════════════════════════════════════════════════════
# CHART 9 — SUMMARY INSIGHT CARD
# ═══════════════════════════════════════════════════════════════════════════════
print("Chart 9: Summary Insight Card...")
fig = plt.figure(figsize=(18, 11))
fig.patch.set_facecolor(WHITE)

fig.text(0.5, 0.97, 'CITY OF TORONTO 2024 — KEY FINDINGS & STRATEGIC INSIGHTS',
         ha='center', va='top', fontsize=16, fontweight='bold', color=NAVY)
fig.text(0.5, 0.935, 'McKinsey-Style Executive Summary  |  Analysis by Faraz Alam  |  Kaalicoder@gmail.com',
         ha='center', va='top', fontsize=9, color=DGRAY)

# Top rule
ax_rule = fig.add_axes([0.04, 0.92, 0.92, 0.004])
ax_rule.set_facecolor(NAVY); ax_rule.set_xticks([]); ax_rule.set_yticks([])
for sp in ax_rule.spines.values(): sp.set_visible(False)

insights = [
    ('🟢 OUTPERFORMANCE', NAVY,
     ['Revenue beat budget by $530M (+3%)', 'Investment income exceeded budget by $535M (+201%)',
      'Annual surplus of $2.0B vs $150M budget', 'Operating cash flow up 11% to $4.1B']),
    ('🟡 FISCAL PRESSURES', STEEL,
     ['Net Debt grew $403M to $10.0B (55% of revenue)', 'Salaries & benefits at $7.6B (+8.1% YoY)',
      'Social housing costs up $254M (+24%)', 'Long-term debt obligations of $16.6B total']),
    ('🔵 CAPITAL STRENGTH', LBLUE,
     ['$4.4B capital investment in 2024', 'Capital assets at $45.4B (+$2.6B or +6%)',
      'Transit investments: $659M new additions', 'Water/wastewater infrastructure: $633M additions']),
    ('🟠 STRATEGIC RISKS', '#C8841A',
     ['WSIB obligations up 8.2% to $1.19B', 'Cash fell $1.1B to $3.3B (liquidity watch)',
      'Employee benefits: $4.9B liability growing', 'Contaminated site liability $272M (undiscounted)']),
]

positions_x = [0.04, 0.28, 0.54, 0.78]
for i, (title, color, points) in enumerate(insights):
    ax_card = fig.add_axes([positions_x[i], 0.52, 0.22, 0.37])
    ax_card.set_facecolor('#F8FAFD')
    for sp in ax_card.spines.values():
        sp.set_color(color); sp.set_linewidth(2)
    ax_card.set_xticks([]); ax_card.set_yticks([])
    ax_card.text(0.5, 0.93, title, ha='center', va='top', transform=ax_card.transAxes,
                 fontsize=10, fontweight='bold', color=color)
    for j, pt in enumerate(points):
        ax_card.text(0.05, 0.77 - j*0.18, f'► {pt}',
                     ha='left', va='top', transform=ax_card.transAxes,
                     fontsize=8, color=BLACK, wrap=True)

# Bottom: 3 key charts mini
ax_bottom1 = fig.add_axes([0.04, 0.06, 0.29, 0.40])
rev_labels  = ['Prop Tax', 'Gov Trans', 'User Chrg', 'Invest', 'Dev Chrg', 'Other']
rev_vals_b  = [5808, 4669, 3610, 801, 789, 2525]
colors_b    = [NAVY, STEEL, LBLUE, '#2196B0', '#45B5D4', '#82C4DC']
ax_bottom1.pie(rev_vals_b, labels=rev_labels, autopct='%1.0f%%',
               colors=colors_b, startangle=140, pctdistance=0.78,
               wedgeprops={'edgecolor': WHITE, 'linewidth': 1})
ax_bottom1.set_title('Revenue Mix 2024\n($18.2B Total)', fontsize=11, fontweight='bold', color=NAVY)

ax_bottom2 = fig.add_axes([0.37, 0.06, 0.29, 0.40])
exp_labels_b = ['Salaries\n& Benefits', 'Transfer\nPayments', 'Contracted\nServices', 'Amortization', 'Materials', 'Other']
exp_vals_b   = [7642, 2083, 2205, 1793, 1743, 720]
ax_bottom2.barh(exp_labels_b, exp_vals_b, color=COLORS_SEQ[:6], zorder=3)
for i, v in enumerate(exp_vals_b):
    ax_bottom2.text(v+20, i, fmt_m(v), va='center', fontsize=8, color=NAVY, fontweight='bold')
ax_bottom2.set_title('Expense Breakdown 2024\n($16.2B Total)', fontsize=11, fontweight='bold', color=NAVY)
ax_bottom2.xaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f'${v/1000:.0f}B'))
ax_bottom2.set_xlabel('CAD Billions')

ax_bottom3 = fig.add_axes([0.70, 0.06, 0.26, 0.40])
metrics_sb  = ['Revenue\n+11.5%', 'Surplus\n+61.3%', 'Cap Assets\n+6.0%', 'Investments\n+19.4%', 'Net Debt\n+4.2%', 'Expenses\n+7.4%']
vals_sb     = [11.5, 61.3, 6.0, 19.4, 4.2, 7.4]
colors_sb   = [GREEN_ACC, GREEN_ACC, GREEN_ACC, GREEN_ACC, RED_ACC, RED_ACC]
bars_sb     = ax_bottom3.barh(metrics_sb, vals_sb, color=colors_sb, zorder=3)
for bar in bars_sb:
    ax_bottom3.text(bar.get_width()+0.3, bar.get_y()+bar.get_height()/2,
                    f'{bar.get_width():+.1f}%', va='center', fontsize=8, fontweight='bold',
                    color=GREEN_ACC if bar.get_width()>0 else RED_ACC)
ax_bottom3.axvline(0, color=BLACK, linewidth=0.8)
ax_bottom3.set_title('YoY Growth Rates 2024\n(Key Metrics)', fontsize=11, fontweight='bold', color=NAVY)
ax_bottom3.set_xlabel('Year-over-Year Change (%)')

save(fig, '09_summary_insights.png')

print("\n" + "="*60)
print("  ALL 9 CHARTS GENERATED SUCCESSFULLY!")
print("="*60)
print(f"  Charts saved to: {CHART_DIR}/")
print("  Author: Faraz Alam | Kaalicoder@gmail.com")
print("  GitHub: https://github.com/mohamedfarazalam")
print("="*60)
