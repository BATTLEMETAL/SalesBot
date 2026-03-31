# Import necessary libraries
import pandas as pd
import glob
import os
import shutil

# Import custom modules
from excel_reader import read_excel_file, calculate_totals_by_region
from report_generator import generate_report
from chart_creator import create_bar_chart

def main():
    if not os.path.exists('data'):
        os.makedirs('data')
        
    files = glob.glob('data/*.xlsx')
    if not files:
        print("⚠️ Brak plików .xlsx w folderze 'data'. Najpierw uruchom skrypt 'demo_setup.py', aby wygenerować dane próbne!")
        return

    # Step 1: Read Excel Files
    print("📥 Wczytywanie plików Excel...")
    all_data = []
    for f in files:
        all_data.append(read_excel_file(f))
    
    data = pd.concat(all_data, ignore_index=True)

    # Step 2: Process Data 
    print("🔄 Przetwarzanie danych...")
    # calculate_totals_by_region returns a Series, let's reset index
    total_sales_per_region = calculate_totals_by_region(data).reset_index()
    # Rename columns to match what report_generator.py expects ("Region", "Total Sales")
    total_sales_per_region.columns = ['Region', 'Total Sales']

    # Step 3: Generate PDF Report
    print("📄 Generowanie raportu PDF...")
    # report_generator.py ma wbudowaną funkcję generate_report(data) która domyślnie zapisuje "sales_report.pdf"
    generate_report(total_sales_per_region)

    # Step 4: Create Bar Chart
    print("📈 Tworzenie wykresu...")
    # chart_creator.py ma funkcję create_bar_chart(data) ale oczekuje kolumn 'Region' i 'Total'
    chart_data = total_sales_per_region.copy()
    chart_data.columns = ['Region', 'Total']
    chart_path = create_bar_chart(chart_data) # This saves as 'temp_sales_chart.png'
    
    if os.path.exists(chart_path):
        if os.path.exists("sales_chart.png"):
            os.remove("sales_chart.png")
        os.rename(chart_path, "sales_chart.png")

    print(f"✅ Raport został poprawnie zapisany jako: sales_report.pdf")
    print(f"✅ Wykres został poprawnie zapisany jako: sales_chart.png")

if __name__ == "__main__":
    main()