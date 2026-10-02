# Pharmacy Prescription Workflow & Inventory Diagnostic Tool

An operational diagnostic and log analysis solution engineered to simulate retail pharmacy software workflows, identify latency bottlenecks across prescription processing stages (Entry, Insurance Adjudication, Dispensing), and automate re-order alerts for critical medication stockouts.

---

## 🎯 Overview & IT Service Context

In high-volume retail pharmacy environments, software reliability directly impacts patient service levels and operational compliance. Delays during third-party insurance adjudication, system timeouts, or unexpected stock shortages stall prescription fulfillment pipelines.

This repository provides an automated diagnostic tool that parses raw transactional system logs, calculates 90th percentile latency (P90) by workflow stage, flags systemic bottlenecks, and synchronizes real-time inventory levels against minimum re-order baselines.

---

## 🏗️ Repository Architecture

```text
pharmacy-workflow-diagnostic/
│
├── data/                            # Raw synthetic transactional data
│   ├── raw_prescription_logs.csv    # Multi-stage event log streams
│   └── inventory_data.csv           # Medication master & reorder baselines
│
├── scripts/                         # Python analytics engine
│   ├── generate_synthetic_data.py   # Multi-stage prescription event generator
│   └── log_parser_diagnostics.py   # Log parsing & bottleneck detection logic
│
├── sql/                             # Database queries & schema
│   └── schema_and_analytics.sql     # Diagnostic aggregation & exception queries
│
├── outputs/                         # Processed analytical feeds
│   ├── diagnostic_summary.csv       # P90 latencies & error rates by stage
│   └── inventory_reorder_alerts.csv # Automated stock re-order triggers
│
├── requirements.txt                 # Project dependencies
└── README.md
```
---


## 🔑 Key Features & Technical Highlights

• Multi-Stage Workflow Diagnostics
  - Tracks transactions sequentially across Entry, Adjudication, Dispensing, and Ready for Pickup.

• Latency & Bottleneck Detection
  - Uses P90 duration metrics to isolate systemic delays (e.g., insurance claim network gateway timeouts).

• Adjudication Failure Tracking
  - Categorizes exception events including third-party rejections and claim processing timeouts.

• Automated Inventory Re-Order Engine
  - Dynamic logic triggering automated purchase order requests when stock levels fall below safety thresholds.
---

## 🚀 Getting Started

Prerequisites:
- Python 3.9+
- pip
---

### Installation & Execution

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Sona-Shaukath/pharmacy-workflow-diagnostic.git
   cd pharmacy-workflow-diagnostic

2. Install dependencies:
   ```bash
   pip install -r requirements.txt

3. Generate synthetic workflow logs:
   ```bash
   python scripts/generate_synthetic_data.py

4. Run the diagnostic engine:
   ```bash
   python scripts/log_parser_diagnostics.py
---

## 🚧 Roadmap & Work in Progress

[x] Phase 1: Synthetic transactional log generator & schema setup

[x] Phase 2: Python log parsing engine & P90 bottleneck detection

[x] Phase 3: Dynamic inventory re-order logic & SQL analytics suite

[ ] Phase 4 (In Progress): Interactive Operational Analytics Dashboard for live queue monitoring and SLA tracking
