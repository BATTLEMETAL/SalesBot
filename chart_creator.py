# Import necessary libraries
import matplotlib.pyplot as plt
import pandas as pd




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


if __name__ == "__main__":
    # Example usage
    data = pd.Series(
        [200, 150, 300, 250],
        index=["North", "South", "East", "West"]
    )
    create_bar_chart(data)
    print("Bar chart saved to temp_sales_chart.png")