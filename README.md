# 📊 Custody NAV Calculator: How it works

I created a simple Python tool to automate **Net Asset Value (NAV)** calculation for custody funds.

Pros of the script instead of manual Excel reports:
- Pulls live market data (updated using Yahoo Finance)
- Calculates portfolio value
- Adds cash position
- Outputs NAV per share

> This is a **real tool** that solves a real problem in Custody operations.

---

## 🚀 Why this matters? And to whom?

Today, many custody teams calculate NAV manually, a process that is:

- ❌ Time-consuming
- ❌ Subject to errors, especially when you're in a rush for deadlines
- ❌ Not Scalable

## The purpose of the calculator is to:

- ✅ Reduce manual errors
- ✅ Automate daily reporting, making it faster
- ✅ Scale to multiple funds and clients
- ✅ Get an instrument with the resources used in modern finance (Python, pandas, yfinance)

## 🛠 How to Run using Google Colab / IDLE
1. Install dependencies:
   ```bash
   pip install pandas yfinance

## 📊 Example Output


| Total Portfolio Value | $135,721.75 |
| ---- | ----|
| Cash | $5,000.00 |
| NAV | $140,721.75 |
| NAV per Share | $140.72 |

![Portfolio Value](assets/img/NAV_Plot.png)

*Visual representation of asset distribution in the fund.*
