import pandas as pd
import os
from datetime import datetime
from openpyxl import Workbook, load_workbook

class ReportGenerator:
    def __init__(self, output_dir="reports"):
        """Initialize the report generator with an output directory."""
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def generate_report(self, trade_data: list, risk_assessment: list, forecast_results: list, filename=None):
        """Generate an Excel report summarizing trade decisions, risk assessments, and forecasts."""
        try:
            if filename is None:
                filename = f"report_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.xlsx"
            file_path = os.path.join(self.output_dir, filename)
            
            with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
                # Convert trade data to DataFrame and write to Excel
                trade_df = pd.DataFrame(trade_data)
                trade_df.to_excel(writer, sheet_name="Trade Decisions", index=False)
                
                # Convert risk assessment to DataFrame and write to Excel
                risk_df = pd.DataFrame(risk_assessment)
                risk_df.to_excel(writer, sheet_name="Risk Assessment", index=False)
                
                # Convert forecast results to DataFrame and write to Excel
                forecast_df = pd.DataFrame(forecast_results)
                forecast_df.to_excel(writer, sheet_name="Forecast Results", index=False)
                
            return file_path
        except Exception as e:
            print(f"Error generating report: {e}")
            return None

# Example usage:
# report_gen = ReportGenerator()
# report_file = report_gen.generate_report(trade_data, risk_assessment, forecast_results)
# print(f"Report saved at: {report_file}")
