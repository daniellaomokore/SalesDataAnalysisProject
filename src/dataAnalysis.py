import pandas as pd


class SalesDataAnalysis:
    """
    A class that performs data analysis on sales data.
    """

    def __init__(self):
        self.dataframe = self.get_sales_data()


    # Define a function that loads the sales data from a CSV file into a DataFrame
    def get_sales_data(self):
        """
        A funcion that returns the sales data from a CSV file into a DataFrame.
        """
        # Load the sales data from a CSV file using Pandas
        dataframe = pd.read_csv('Dataset/sales_dataset.csv')

        # Return the DataFrame
        return dataframe





    # Define a function that calculates the total sales per product
    def total_sales_per_product(self):
        """
        A funcion that returns the total sales per product.
        """

        # Calculate the total sales price for each product
        sales_by_product = self.dataframe.groupby('Product Name').apply(lambda x: (x['Sale Price'] * x['Quantity Sold']).sum())

        # Sort the products by total sales in descending order
        sales_by_product = sales_by_product.sort_values(ascending=False)


        # Return the sales by product as a DataFrame
        return pd.DataFrame({'Total Sales Per Product': sales_by_product})







    # Define a function that calculates the average sale price for each product category
    def average_sale_price_per_category(self):
        """
        A funcion that returns the average sale price for each product category.
        """
        # Calculate the average sale price for each product category, rouded to 2 d.p
        avg_sale_price_by_category = self.dataframe.groupby('Category')['Sale Price'].mean().round(2)

        # Sort the categories by mean sale price in ascending order
        avg_sale_price_by_category = avg_sale_price_by_category.sort_values(ascending=True)

        # Return the mean sale price by category as a DataFrame
        return pd.DataFrame({'Average Sale Price Per Category': avg_sale_price_by_category})






    # Define a function that finds the month of highest and lowest sales
    def highest_and_lowest_sales_month(self):
        """
        A funcion that returns the month of highest and lowest sales, given the sales data with columns "Month",
        "Sale Price", and "Quantity Sold".
        """
        # Group the sales data by month and sum the sales amounts
        sales_by_month = self.dataframe.groupby('Month').apply(lambda x: (x['Sale Price'] * x['Quantity Sold']).sum())

        # Find the month of highest and lowest sales
        highest_sales_month = sales_by_month.idxmax()
        lowest_sales_month = sales_by_month.idxmin()

        # Get the total sales for the highest and lowest sales months to 2 d.p
        highest_sales_amount = sales_by_month.max().round(2)
        lowest_sales_amount = sales_by_month.min().round(2)

        # Create a DataFrame to store the results
        results = pd.DataFrame({
            'Month': [highest_sales_month, lowest_sales_month],
            'Total Sales': [highest_sales_amount, lowest_sales_amount]
        })

        # Rename the row index with "Highest" and "Lowest"
        results = results.rename(index={0: 'Highest sales month', 1: 'Lowest sales month'})

        # Return the results DataFrame
        return results






    # Define a function that finds the customer who made the most and least purchases and how much they spent in total
    def highest_and_lowest_spending_customers(self):
        """
        A funcion that returns the customer who made the most and least purchases and how much they spent in total.
        """
        # Group the sales data by customer and sum the sales amounts
        sales_by_customer = self.dataframe.groupby('Customer Name').apply(lambda x: (x['Sale Price'] * x['Quantity Sold']).sum())


        # Find the customer who spent the most and the least
        highest_spending_customer = sales_by_customer.idxmax()
        lowest_spending_customer = sales_by_customer.idxmin()


        # Get the total amount spent by the highest and lowest spending customers to 2 d.p
        highest_spending_customer_amount = sales_by_customer.max().round(2)
        lowest_spending_customer_amount = sales_by_customer.min().round(2)

        # Create a DataFrame to store the results
        results = pd.DataFrame({
            'Customer Name': [highest_spending_customer, lowest_spending_customer],
            'Total Spent': [highest_spending_customer_amount, lowest_spending_customer_amount]
        })

        # Rename the row index with "Highest" and "Lowest"
        results = results.rename(index={0: 'Highest spending customer', 1: 'Lowest spending customer'})

        # Return the results DataFrame
        return results





    # Define a function that finds the median sale price
    def median_sale_price(self):
        """
            A funcion that returns the median sale price.
        """

        # Get median sale price
        median_sale_price = self.dataframe['Sale Price'].median()

        # store results in a DataFrame
        results = pd.DataFrame({'Sale Price': [median_sale_price]})

        # Rename the row index to "Sale Price"
        results = results.rename(index={0: 'Median Sale Price'})

        # Return the median sale price as a DataFrame
        return results






    def std_sale_price(self):
        """
          A funcion that returns the standard deviation of the sale prices.
        """

        # Get std of sale price to 2 d.p
        std_sales_price = self.dataframe['Sale Price'].std().round(2)

        # store results in a DataFrame
        results = pd.DataFrame({'Sale Price': [std_sales_price]})


        # Rename the row index to "Standard Deviation of Sale Price"
        results = results.rename(index={0: 'Standard Deviation of Sale Price'})

        # Return the STD as a DataFrame
        return results




    def highest_sales_product(self):
        """
            A function that returns the name of the product with the highest quantity of sales.
        """

        # Get the index of the row for the product with the highest sales quantity
        highest_sale_product_idx = self.dataframe['Quantity Sold'].idxmax()

        # Get the product name using the index
        best_product = self.dataframe.loc[highest_sale_product_idx, 'Product Name']

        # store results in a DataFrame
        results = pd.DataFrame({'Product Name': [best_product]})

        # Rename the row index to "Standard Deviation of Sale Price"
        results = results.rename(index={0: 'Highest sale product'})

        # Return the name of the product with the highest quantity of sales
        return results










