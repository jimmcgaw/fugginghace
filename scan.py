from datetime import datetime
from pprint import pprint

import os

from modelscan.modelscan import ModelScan
from modelscan.settings import DEFAULT_SETTINGS

# Start with default settings and customize
custom_settings = DEFAULT_SETTINGS.copy()

# Update settings as needed
custom_settings["reporting"]["module"] = "modelscan.reporting.json_report.JSONReport"
custom_settings["reporting"]["settings"]["output_file"] = f"scanresults/scan_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

# Initialize with custom settings
scanner = ModelScan(settings=custom_settings)

MODEL_PATHS = os.listdir(".models")

for model_path in MODEL_PATHS:
    results = scanner.scan(f".models/{model_path}")
    pprint(results)
