import os
import random
from datetime import datetime, timedelta
import numpy as np
import pandas as pd
from faker import Faker

fake = Faker()
np.random.seed(42)
random.seed(42)

os.makedirs("data", exist_ok=True)

medications = [
    {"med_id": "MED101", "med_name": "Amoxicillin 500mg", "category": "Antibiotic", "current_stock": 120, "reorder_threshold": 200, "reorder_qty": 500},
    {"med_id": "MED102", "med_name": "Atorvastatin 20mg", "category": "Cardiovascular", "current_stock": 450, "reorder_threshold": 300, "reorder_qty": 600},
    {"med_id": "MED103", "med_name": "Metformin 500mg", "category": "Diabetes", "current_stock": 85, "reorder_threshold": 250, "reorder_qty": 500},
    {"med_id": "MED104", "med_name": "Levothyroxine 50mcg", "category": "Thyroid", "current_stock": 310, "reorder_threshold": 200, "reorder_qty": 400},
    {"med_id": "MED105", "med_name": "Lispro Insulin 100u/ml", "category": "Diabetes", "current_stock": 25, "reorder_threshold": 50, "reorder_qty": 100},
]

df_inventory = pd.DataFrame(medications)
df_inventory.to_csv("data/inventory_data.csv", index=False)

stages = ["Entry", "Adjudication", "Dispensing", "Ready_for_Pickup"]
log_records = []
base_time = datetime(2026, 9, 20, 8, 0, 0)

for rx_id in range(1001, 1251):
    med = random.choice(medications)
    rx_time = base_time + timedelta(minutes=random.randint(1, 4320))

    for stage in stages:
        if stage == "Entry":
            duration_sec = random.randint(30, 120)
            status = "SUCCESS"
        elif stage == "Adjudication":
            duration_sec = random.choices([random.randint(15, 60), random.randint(300, 900)], weights=[0.8, 0.2])[0]
            status = random.choices(["SUCCESS", "REJECTED_INSURANCE", "TIMEOUT"], weights=[0.85, 0.10, 0.05])[0]
        elif stage == "Dispensing":
            duration_sec = random.randint(60, 300)
            status = "OUT_OF_STOCK" if med["current_stock"] < 30 and random.random() < 0.4 else "SUCCESS"
        else:
            duration_sec = random.randint(10, 45)
            status = "SUCCESS"

        rx_time += timedelta(seconds=duration_sec)

        log_records.append({
            "rx_id": f"RX{rx_id}",
            "timestamp": rx_time.strftime("%Y-%m-%d %H:%M:%S"),
            "med_id": med["med_id"],
            "stage": stage,
            "status": status,
            "duration_seconds": duration_sec,
            "pharmacist_id": f"PHARM_{random.randint(1, 5)}"
        })

df_logs = pd.DataFrame(log_records)
df_logs.to_csv("data/raw_prescription_logs.csv", index=False)
