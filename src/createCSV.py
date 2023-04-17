import pandas as pd


class CSVForDataAnalysis:
    # The asterisk (*) in front of a parameter allows the function to accept a variable number of arguments as a tuple.
    def save_dataframes_to_csv(self, *dataframes):
        """
        A method that saves multiple dataframes to one csv file called 'data analysis'.
        """
        # Concatenate the dataframes along rows ('axis = 0')
        merged_dataframe = pd.concat(dataframes, axis=0)

        # Save the merged dataframe to csv
        merged_dataframe.to_csv('data analysis.csv', index=True)

        return "DataFrames Saved to CSV"

