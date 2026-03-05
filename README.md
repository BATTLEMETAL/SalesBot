# 📊 SalesBot - Automated Data Reporting & ETL Pipeline

## 🎯 Business Case (Dlaczego to stworzyłem?)
Automatyzacja żmudnego procesu raportowania. Skrypt pobiera surowe, nieustrukturyzowane dane sprzedażowe z plików Excel, przeprowadza proces ETL (Extract, Transform, Load), a następnie generuje czytelne raporty PDF z wykresami. 
**Efekt:** Skrócenie czasu przygotowywania raportów z kilku godzin do kilkunastu sekund.

## 🛠️ Tech Stack
* **Język:** Python 3.10+
* **Data Processing (ETL):** `pandas`, `openpyxl`
* **Data Visualization:** `matplotlib`
* **Report Generation:** `ReportLab`

## 📸 Przykładowy Raport (Showcase)
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/67d143c7-1105-4b44-9fef-ab0fa0a1729a" />



## 🚀 Quick Start
Projekt można uruchomić lokalnie używając wirtualnego środowiska:

```bash
git clone https://github.com/BATTLEMETAL/SalesBot.git
cd SalesBot
python -m venv venv
source venv/bin/activate  # na Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py
