import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_dataset(file_path):
    """
    Load the dataset from a CSV file.

    Parameters:
    - file_path (str): Path to the CSV file.

    Returns:
    - pd.DataFrame: Loaded DataFrame.
    """
    return pd.read_csv(file_path)

def select_columns(df, columns):
    """
    Select specific columns from the DataFrame.

    Parameters:
    - df (pd.DataFrame): Input DataFrame.
    - columns (list): List of column names to select.

    Returns:
    - pd.DataFrame: DataFrame with selected columns.
    """
    return df[columns]

def calculate_correlation_matrix(df):
    """
    Calculate the correlation matrix for the DataFrame.

    Parameters:
    - df (pd.DataFrame): Input DataFrame.

    Returns:
    - pd.DataFrame: Correlation matrix.
    """
    return df.corr()

def plot_heatmap(cor_matrix, x_labels, y_labels):
    """
    Plot a heatmap for the correlation matrix.

    Parameters:
    - cor_matrix (pd.DataFrame): Correlation matrix to plot.
    - x_labels (list): Labels for the x-axis.
    - y_labels (list): Labels for the y-axis.
    """
    plt.figure(figsize=(10, 8))
    sns.heatmap(data=cor_matrix, annot=True, cmap='coolwarm', center=0)

    # Set custom axis labels and make them more visible
    plt.xticks(ticks=range(len(x_labels)), labels=x_labels, rotation=15, ha='right', fontsize=10)
    plt.yticks(ticks=range(len(y_labels)), labels=y_labels, rotation=0, ha='right', fontsize=10)

    # Set plot title
    plt.title('Correlation Heatmap for Selected Indicators in Germany')

    # Display the plot
    plt.show()

# Load the dataset
file_path = "germany.csv"
df = load_dataset(file_path)

# Select specific columns of interest
selected_columns = ["Population growth (annual %)", "GDP per capita (constant 2015 US$)", "Trade (% of GDP)", "Expenditure on primary education (% of government expenditure on education)", "High-technology exports (current US$)", "Agricultural land (% of land area)", "Social contributions (% of revenue)"]
df_selected = select_columns(df, selected_columns)

# Calculate the correlation matrix
correlation_matrix = calculate_correlation_matrix(df_selected)

# Set custom axis labels
x_axis_labels = ["Population Growth", "GDP per Capita", "Trade (% of GDP)", "Education Expenditure", "High-tech Exports", "Agricultural Land", "Social Contributions"]
y_axis_labels = ["Population Growth", "GDP per Capita", "Trade (% of GDP)", "Education Expenditure", "High-tech Exports", "Agricultural Land", "Social Contributions"]

# Plot the heatmap with custom labels
plot_heatmap(correlation_matrix, x_axis_labels, y_axis_labels)
