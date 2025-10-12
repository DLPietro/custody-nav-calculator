# 📊 Custody NAV Calculator

Python tool automating **Net Asset Value (NAV)** calculation for custody funds.


## 🚀 Benefits

Today, many custody teams calculate NAV manually, a process that is:

>❌ Time-consuming
>
>❌ Subject to errors, especially during deadlines
>
>❌ Not Scalable

## The purpose of the calculator is to:

>✅ Real-time data from Yahoo Finance via `yfinance`
>
>✅ Accurate NAV per share calculation with cash position
>
>✅ Saves up to 35% time vs manual Excel process


## 🛠 Installation & Usage
1. Install dependencies:
   ```bash
   pip install pandas yfinance

---

## 📊 Example Output
| Total Portfolio Value | $135,721.75 |
| ---- | ----|
| Cash | $5,000.00 |
| NAV | $140,721.75 |
| NAV per Share | $140.72 |

![Portfolio Value](assets/img/NAV_Plot.png)

*Visual representation of asset distribution in the fund, using liquidity and liabilities as well.*

## 💡 How to adapt

Modify config file to support new funds and assets, or integrate with custodian APIs.

---

# ⚡ Credits

[![GitHub](https://img.shields.io/badge/GitHub-DLPietro-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/DLPietro)&nbsp;&nbsp;
[![Commit Style](https://img.shields.io/badge/Commit_Style-DLPietro-9B59B6?style=for-the-badge&logo=git&logoColor=white)](https://github.com/DLPietro/learning-roadmap/blob/main/CONTRIBUTING.md)&nbsp;&nbsp;
[![License](https://img.shields.io/badge/License-CC_BY--SA_4.0-007EC7?style=for-the-badge)](https://creativecommons.org/licenses/by-sa/4.0/)

> _© 2025 Pietro Di Leo — From Operations to Data. One Commit at a Time._
