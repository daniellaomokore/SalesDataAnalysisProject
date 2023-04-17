import matplotlib.pyplot as plt


class DataChartPlotter:
    """
    A class to create a matplotlib graph
    """
    def __init__(self, dataframe, y_column, xlabel, ylabel):
        self.dataframe = dataframe
        self.y_column = y_column
        self.xlabel = xlabel
        self.ylabel = ylabel

    def plot_data_chart(self):
        """
        A function that plots a dataframe as a bar chart.
        """
        # Create a new figure with a specified size
        plt.figure(figsize=(12, 6))

        # Create a bar chart using Matplotlib
        plt.bar(self.dataframe.index, self.dataframe[self.y_column], color='#008080', width=0.5)

        # Rotate x-axis labels
        plt.xticks(rotation=45, fontsize=7)

        # Add labels and title
        plt.xlabel(self.xlabel, fontweight='bold')
        plt.ylabel(self.ylabel, fontweight='bold')
        plt.title(self.y_column, fontweight='bold')

        # Show the chart
        plt.show()
