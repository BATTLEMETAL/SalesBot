import pandas as pd
import numpy as np
import os

def generate_mock_excel():
    print("🔧 Przygotowywanie środowiska demo - SalesBot...")
    
    # Upewnij się, że folder data istnieje
    if not os.path.exists('data'):
        os.makedirs('data')
        
    print("📊 Generowanie przykładowych danych sprzedażowych...")
    
    # Generowanie losowych danych
    np.random.seed(42)
    regions = ['North', 'South', 'East', 'West']
    
    data = []
    for region in regions:
        # Generujemy od 50 do 100 transakcji dla każdego regionu
        transactions = np.random.randint(50, 100)
        for _ in range(transactions):
            sales_amount = round(np.random.uniform(100.0, 1500.0), 2)
            data.append({
                'Region': region,
                'Sales': sales_amount
            })
            
    df = pd.DataFrame(data)
    
    # Zapisz do pierwszego pliku
    file_path1 = 'data/Q1_sales.xlsx'
    df.head(len(df)//2).to_excel(file_path1, index=False)
    
    # Zapisz drugą połowę do kolejnego pliku aby pokazać agregację
    file_path2 = 'data/Q2_sales.xlsx'
    df.tail(len(df) - len(df)//2).to_excel(file_path2, index=False)
    
    print(f"✅ Zapisano pliki testowe:")
    print(f"  - {file_path1} ({len(df)//2} wierszy)")
    print(f"  - {file_path2} ({len(df) - len(df)//2} wierszy)")
    print("\n🎉 Środowisko gotowe! Śmiało uruchom skrypt 'main.py', aby zobaczyć działanie SalesBot na żywo podczas rozmowy.")

if __name__ == "__main__":
    generate_mock_excel()
