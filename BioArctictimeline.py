import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

milestones = [
    (2017, "Public Funding", "Successful IPO on Swedish Nasdaq and became the largest biotech listing since 2000"),
    (2019,"Leqembi Final Trials","Continued phase 3 trials with Eisai and preparation for the expansion of AD pipeline"),
    (2020,"Recruitment","Completed enrollment of 1795 patients in phase 3 study with lecanemab for Alzheimer's disease"),
    (2022,"Results of phase 3","Positive topline results from phase 3, confirming lecanemab's efficacy in slowing cognitive decline"),
    (2023,"Approvals","FDA granted accelerated approval and traditional approval for lecanemab (Leqembi)"),
    (2023,"More Approval","Japan (2nd Largest Market for their product in the world) also approved Leqembi"),
    (2024,"Marketing and Commercialisation","First sales was in 2023 but with significant commercial rollout by Eisai in 2024 leads to revenue generation"),
    (2024,"Revenue generating strategy","Main income is driven by the royalties from Eisai for lecanemab sales")
]

# 1. Extract years as datetime objects (perfect for timeline plotting)
years = [datetime(y, 1, 1) for y, _, _ in milestones]

# 2. Extract short titles (these will be the bold/visible event labels)
titles = [title for _, title, _ in milestones]

# 3. Extract detailed descriptions (for hover text, subtext, or smaller font)
descriptions = [desc for _, _, desc in milestones]

# Create figure
fig, ax = plt.subplots(figsize=(12, 10))

# Central vertical line
ax.vlines(0.05, 0, len(milestones)-1, color='lightblue', lw=8, alpha=0.5)

# Plot each milestone (newest at top)
for i, (year, title, desc) in enumerate(zip(years[::-1], titles[::-1], descriptions[::-1])):
    y_pos = len(milestones) - 1 - i  # reverse order: newest on top

    #Horizontal lines underneath the years
    ax.hlines(y_pos, 0.0, 0.19, color='grey', lw=3, alpha=0.5, linestyle='-')

    # Circle marker
    ax.plot(0.05, y_pos, 'o', ms=20, color='royalblue', mec='white', mew=3, zorder=10)

    # Year on left
    ax.text(0.3, y_pos, str(year.year), ha='right', va='center', fontsize=20, fontweight='bold')

    # Title + description on right
    ax.text(0.4, y_pos, f"{title}\n{desc}", ha='left', va='center', fontsize=11,
            bbox=dict(facecolor='lightgrey', edgecolor='lightgray', boxstyle='round,pad=0.6', alpha=0.95))

# Styling
ax.set_xlim(0, 1.2)
ax.set_ylim(-0.5, len(milestones)-0.6)
ax.axis('off')
plt.title("BioArctic – Lecanemab Development & Commercialization Timeline", fontsize=26, pad=30, fontweight='bold', color='white', bbox=dict(facecolor='royalblue', edgecolor='none', boxstyle='round,pad=0.6', alpha=0.7))
plt.tight_layout()
plt.show()