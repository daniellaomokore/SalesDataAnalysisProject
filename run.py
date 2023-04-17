from src.createCSV import CSVForDataAnalysis
from src.graphPlotter import DataChartPlotter
from src.dataAnalysis import SalesDataAnalysis


""" Test Cases for 'SalesDataAnalysis' class"""

# initialise an object for the 'SalesDataAnalysis' class to use its methods
my_analysis = SalesDataAnalysis()

print(my_analysis.total_sales_per_product())
print("\n")
print(my_analysis.average_sale_price_per_category())
print("\n")
print(my_analysis.highest_and_lowest_sales_month())
print("\n")
print(my_analysis.highest_and_lowest_spending_customers())
print("\n")
print(my_analysis.median_sale_price())
print("\n")
print(my_analysis.std_sale_price())
print("\n")
print(my_analysis.highest_sales_product())
print("\n")


""" Plot Graph for 'Average Sale Price Per Category' """
dataframe1 = my_analysis.average_sale_price_per_category()

# initialise an object for the 'DataChartPlotter' class to use its methods
chart_average_sale_price_per_category = DataChartPlotter(dataframe=dataframe1,y_column="Average Sale Price Per Category",xlabel="Category", ylabel="Average Price (£)")

# Call the plot_data_chart method on the instance
chart_average_sale_price_per_category.plot_data_chart()




""" Plot Graph for 'Total Sales Per Product' """
dataframe2 = my_analysis.total_sales_per_product()

# initialise an object for the 'DataChartPlotter' class to use its methods
chart_total_sales_per_product = DataChartPlotter(dataframe=dataframe2,y_column="Total Sales Per Product",xlabel="Product", ylabel="Total Sales (£)")

# Call the plot_data_chart method on the instance
chart_total_sales_per_product.plot_data_chart()






"""Test Case to save data into csv"""
df1 = my_analysis.total_sales_per_product()
df2 = my_analysis.average_sale_price_per_category()
df3 = my_analysis.highest_and_lowest_sales_month()
df4 = my_analysis.highest_and_lowest_spending_customers()
df5 = my_analysis.median_sale_price()
df6 = my_analysis.std_sale_price()
df7 = my_analysis.highest_sales_product()


# initialise an object for the 'CSVForDataAnalysis' class to use its method
myCsv = CSVForDataAnalysis()
print(myCsv.save_dataframes_to_csv(df1, df2, df3, df4, df5, df6, df7))

