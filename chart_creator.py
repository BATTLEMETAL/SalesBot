# Import necessary libraries
import pandas as pd
from openpyxl import load_workbook
from reportlab.pdfgen import canvas
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt


def create_bar_chart(data):
    """
    Create a bar chart for the given data and save it to a file.
    
    Args:
        data (pd.DataFrame): Data containing regions and their corresponding totals.
        
    Returns:
        str: Path to the saved image file.
    """
    # Set up the plot
    plt.figure(figsize=(10, 6))
    plt.bar(data['Region'], data['Total'], color='blue')
    plt.xlabel('Region')
    plt.ylabel('Total Sales')
    plt.title('Sales by Region')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Save the plot to a temporary file
    temp_image_path = "temp_sales_chart.png"
    plt.savefig(temp_image_path)
    plt.close()  # Close the plot to free memory
    
    return temp_image_path


def generate_report_with_chart(data, output_pdf_path):
    """
    Generate a PDF report including a bar chart showing sales by region.
    
    Args:
        data (pd.DataFrame): Processed data containing regions and their totals.
        output_pdf_path (str): Path where the final PDF report will be saved.
    """
    # Create a PDF document
    pdf = PdfPages(output_pdf_path)
    
    # Add a title page
    c = canvas.Canvas("title_page.pdf")
    width, height = c.getPageSize()
    c.setFont("Helvetica", 24)
    c.drawString(width / 2 - 75, height / 2 + 30, "Sales Report")
    c.setFont("Helvetica", 18)
    c.drawString(width / 2 - 90, height / 2 - 10, f"Generated on {data.index[0]}")
    c.save()
    pdf.attach("title_page.pdf")  # Attach the title page to the PDF
    
    # Add the bar chart
    chart_image_path = create_bar_chart(data)  # Get the path to the chart image
    c = canvas.Canvas("sales_chart.pdf")
    width, height = c.getPageSize()
    c.drawImage(chart_image_path, 20, 20, width - 40, height - 100)
    c.save()
    pdf.attach("sales_chart.pdf")  # Attach the chart to the PDF
    
    # Close the PDF writer
    pdf.close()


if __name__ == "__main__":
    # Example usage
    data = pd.DataFrame({
        'Region': ['North', 'South', 'East', 'West'],
        'Total': [200, 150, 300, 250]
    })
    
    output_pdf_path = "sales_report.pdf"
    generate_report_with_chart(data, output_pdf_path)
    print(f"Report generated at {output_pdf_path}")