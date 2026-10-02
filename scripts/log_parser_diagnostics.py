import os
import pandas as pd

os.makedirs("outputs", exist_ok=True)

logs = pd.read_csv("data/raw_prescription_logs.csv")
inventory = pd.read_csv("data/inventory_data.csv")

stage_diagnostics = (
    logs.groupby("stage")
    .agg(
        total_transactions=("rx_id", "count"),
        avg_duration_sec=("duration_seconds", "mean"),
        p90_duration_sec=("duration_seconds", lambda x: x.quantile(0.90)),
        failed_adjudications=("status", lambda x: (x.isin(["REJECTED_INSURANCE", "TIMEOUT"])).sum()),
        out_of_stock_events=("status", lambda x: (x == "OUT_OF_STOCK").sum()),
    )
    .reset_index()
)

stage_diagnostics["is_bottleneck"] = stage_diagnostics["p90_duration_sec"] > 300
stage_diagnostics.to_csv("outputs/diagnostic_summary.csv", index=False)

inventory["reorder_status"] = inventory.apply(
    lambda row: "TRIGGER_REORDER" if row["current_stock"] <= row["reorder_threshold"] else "OPTIMAL",
    axis=1,
)

inventory["order_units_needed"] = inventory.apply(
    lambda row: row["reorder_qty"] if row["reorder_status"] == "TRIGGER_REORDER" else 0,
    axis=1,
)

inventory.to_csv("outputs/inventory_reorder_alerts.csv", index=False)
