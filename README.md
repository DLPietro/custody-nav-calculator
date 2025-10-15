# 📊 Custody NAV Calculator

**Custody NAV Calculator** is a tool designed to calculate the net asset value (NAV) of custody accounts based on customizable input parameters. This project can be used to calculate the NAV for different periods, asset values, and management fees.


## 🚀 Benefits

Today, many custody teams calculate NAV manually, a process that is:

>❌ Time-consuming
>
>❌ Subject to errors, especially during deadlines
>
>❌ Not Scalable

## The purpose of the calculator is to:

>✅ Real-time data from Yahoo Finance via _`yfinance`_
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

## 🏡 Project Structure

```text
custody-nav-calculator/
├── src/                 # Source code of the project
│   ├── main.py          # Main calculator logic
│   ├── utils.py         # Helper functions
│   └── ...
├── tests/               # Unit tests
│   ├── test_calculator.py
│   └── ...
├── README.md            # Project documentation
├── requirements.txt     # Python dependencies
└── LICENSE              # Project license
```
---

## 🔗 Related Work

- [📊 My Data Journey Blog](https://dlpietro.github.io) — Weekly updates on my upskilling  
- [🧠 My Learning Roadmap](https://github.com/DLPietro/learning-roadmap) — Publicly tracked progress  
- [📈 Empirical Analysis: S&P 500 vs IVV vs Fidelity](https://github.com/DLPietro/thesis-backtesting-etf-spx) — Using R, GARCH, backtesting
- [🎲 iGaming Analytics Dashboard](https://github.com/DLPietro/igaming-analytics-case-study) — KPI and players Retention (_Cohort, Church..._)

---

# ⚡ Credits

[![GitHub Profile](https://img.shields.io/badge/GitHub-DLPietro-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/DLPietro)
[![Email](https://img.shields.io/badge/Email-dileopie-d14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:dileopie@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Pietro-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/pietrodileo)

> _© 2025 Pietro Di Leo — From Operations to Data. One Commit at a Time._
