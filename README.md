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

[![Email](https://img.shields.io/badge/Email-d14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:dileopie@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/pietrodileo)
[![GitHub Profile](https://img.shields.io/badge/GitHub-DLPietro-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/DLPietro)
