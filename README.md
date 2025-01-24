# Test Results Processor

## 📌 Project Overview
This project provides a **Test Results Processor** that loads test data from a JSON file, calculates metrics, and exports the results in multiple formats (**CSV, JSON, Markdown, Excel**).

### **🔹 Python Version Requirement**
This project requires **Python 3.9 or higher** to run properly.

---

## 🚀 Setup & Installation
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-repo/test_results_processor.git
cd test_results_processor
```

### **2️⃣ Create a Virtual Environment (Optional but Recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

---

## 🧪 Running Unit Tests
To ensure everything is working correctly, run the unit tests:
```bash
python -m unittest discover tests -v
```

Expected output:
```
test_csv_exporter (test_exporters.TestExporters)
Test CSVExporter correctly exports test results. ... ok
test_excel_exporter (test_exporters.TestExporters)
Test ExcelExporter correctly exports test results. ... ok
test_json_exporter (test_exporters.TestExporters)
Test JSONExporter correctly exports test results. ... ok
test_markdown_exporter (test_exporters.TestExporters)
Test MarkdownExporter correctly exports test results. ... ok
test_load_invalid_json (test_json_loader.TestJSONLoader)
Test handling of invalid JSON file. ... ERROR:root:❌ Error loading JSON: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
ok
test_load_valid_json (test_json_loader.TestJSONLoader)
Test loading a valid JSON file. ... ok
test_calculate_metrics (test_metrics_calculator.TestMetricsCalculator)
Test correct calculation of metrics from test results. ... ok
test_metrics_calculation (test_processor.TestProcessor)
Test Processor correctly calculates metrics. ... ok
test_processor_csv (test_processor.TestProcessor)
Test Processor correctly processes and exports CSV. ... ok
test_processor_excel (test_processor.TestProcessor)
Test Processor correctly processes and exports Excel. ... ok
test_processor_json (test_processor.TestProcessor)
Test Processor correctly processes and exports JSON. ... ok
test_processor_markdown (test_processor.TestProcessor)
Test Processor correctly processes and exports Markdown. ... ok

```

---

## 📂 Project Structure
```
📂 test_results_project/
 ├── 📂 exporters/            # Export modules (CSV, JSON, Markdown, Excel)
 ├── 📂 utils/               # Utility modules (JSON Loader, Metrics Calculator, Logging)
 ├── 📂 processors/          # Processing logic
 ├── 📂 tests/               # Unit tests
 ├── test_results_processor.py  # Main execution script
 ├── test_results.json       # Example JSON test results
 ├── requirements.txt        # Required dependencies
 ├── README.md               # Project documentation
```

---

## 🎯 How to Run the Processor
The `test_results_processor.py` script can export results to different formats.

### **Run with CSV Output**
```bash
python test_results_processor.py test_results.json results/test_results.csv --format csv
```

### **Run with JSON Output**
```bash
python test_results_processor.py test_results.json results/test_results.json --format json
```

### **Run with Markdown Output**
```bash
python test_results_processor.py test_results.json results/test_results.md --format md
```

### **Run with Excel Output**
```bash
python test_results_processor.py test_results.json results/test_results.xlsx --format xlsx
```

After execution, check the `results/` directory for output files.

---

## 🛠️ Modifying the Input JSON File
To customize the test results, edit the `test_results.json` file:
```json
{
    "test_cases": [
        {"name": "Login Test", "status": "pass", "execution_time": 1.2, "timestamp": "2025-01-24T01:00:00Z"},
        {"name": "Signup Test", "status": "fail", "execution_time": 2.5, "timestamp": "2025-01-24T01:10:00Z"},
        {"name": "Checkout Process", "status": "pass", "execution_time": 3.0, "timestamp": "2025-01-24T01:15:00Z"},
        {"name": "Add to Cart", "status": "pass", "execution_time": 0.8, "timestamp": "2025-01-24T01:20:00Z"},
        {"name": "Remove from Cart", "status": "fail", "execution_time": 1.1, "timestamp": "2025-01-24T01:25:00Z"},
        {"name": "Search Feature", "status": "pass", "execution_time": 2.2, "timestamp": "2025-01-24T01:30:00Z"},
        {"name": "Filter Results", "status": "fail", "execution_time": 2.9, "timestamp": "2025-01-24T01:35:00Z"},
        {"name": "Sort Items", "status": "pass", "execution_time": 1.5, "timestamp": "2025-01-24T01:40:00Z"},
        {"name": "Payment Gateway", "status": "fail", "execution_time": 3.8, "timestamp": "2025-01-24T01:45:00Z"},
        {"name": "Logout Test", "status": "pass", "execution_time": 0.9, "timestamp": "2025-01-24T01:50:00Z"}
    ]
}
```

---

## ✅ Conclusion
This project provides a simple and extensible way to process test results. You can add more exporters by implementing the `Exporter` protocol.

For improvements or issues, feel free to contribute! 🚀
