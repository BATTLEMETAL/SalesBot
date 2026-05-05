# 📊 SalesBot — AI-Powered Sales Report Generator

[![CI](https://github.com/BATTLEMETAL/SalesBot/actions/workflows/ci.yml/badge.svg)](https://github.com/BATTLEMETAL/SalesBot/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](.)
[![Tests](https://img.shields.io/badge/Tests-12%20passing-brightgreen)](./tests/test_sales.py)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-412991?logo=openai&logoColor=white)](.)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

Transforms raw Excel sales data into professional PDF reports with an **AI-generated executive summary** (OpenAI GPT-4o-mini). Features clean architecture, full pytest coverage, and a GitHub Actions CI pipeline that runs on every push. Falls back gracefully to rule-based summary when no API key is present (CI-safe).

---

## 🔄 Pipeline

```
Excel files (data/*.xlsx)
        │
        ▼
excel_reader.py  ──►  calculate_totals_by_region()
        │
        ▼
ai_summary.py    ──►  OpenAI GPT-4o-mini executive summary
        │           (fallback: rule-based when no API key)
        ▼
chart_creator.py ──►  matplotlib bar chart (sales_chart.png)
        │
        ▼
report_generator.py ►  ReportLab PDF (sales_report.pdf)
                        └─ includes AI summary section at top
```

---

## 🧪 Tests — 12 Unit Tests, 3 Classes

```bash
pytest tests/ -v
```

| Test Class | Tests | What It Covers |
|---|---|---|
| `TestCalculateTotalsByRegion` | 8 | Region grouping, grand totals, edge cases (empty DataFrame, single region) |
| `TestSaveDataToCsv` | 3 | File creation, column presence, row count integrity |
| `TestReportGenerator` | 1 | End-to-end smoke test — verifies PDF is generated without errors |

All tests run **without Excel files on disk** — fixtures provide synthetic DataFrames. CI runs headlessly on every push via GitHub Actions.

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Data processing | pandas |
| AI executive summary | OpenAI GPT-4o-mini (+ rule-based fallback) |
| Visualization | matplotlib |
| PDF generation | ReportLab |
| Excel reading | openpyxl |
| Testing | pytest + fixtures |
| CI/CD | GitHub Actions |

---

## 🚀 Quick Start

```bash
git clone https://github.com/BATTLEMETAL/SalesBot.git
cd SalesBot
pip install -r requirements.txt

# Generate sample data
python demo_setup.py

# Run pipeline
python main.py
# → sales_report.pdf + sales_chart.png

# Run tests
pytest tests/ -v
```

---

## 📁 Project Structure

```
SalesBot/
├── main.py               # Pipeline orchestrator
├── excel_reader.py       # Data ingestion + region aggregation
├── ai_summary.py         # OpenAI GPT-4o-mini executive summary + fallback
├── report_generator.py   # ReportLab PDF export (embeds AI summary)
├── chart_creator.py      # matplotlib chart generation
├── demo_setup.py         # Sample data generator
├── tests/
│   └── test_sales.py     # 12 unit tests (3 classes)
├── .github/workflows/
│   └── ci.yml            # GitHub Actions — lint + pytest on push
├── requirements.txt
└── .env.example          # API key template
```

---

*Part of portfolio demonstrating clean Python architecture, test-driven development, and CI/CD practices. See also [Synapsa](https://github.com/BATTLEMETAL/Synapsa-Local-LLM-Agent) for AI/LLM work.*
