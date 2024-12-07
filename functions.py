import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import OneHotEncoder


class data_understanding:
    def __init__(self, file):
        """
        Initializes the data understanding class
        """
        self.data = self.load_data(file)
        

    def load_data(self, file):
        """
        Loading the csv file
        """
        return pd.read_csv(file)
    
    def first_rows(self):
        """
        Checks the first 5 rows of the dataset
        """
        return self.data.head()

    def data_shape(self):
        """
        Returns the shape of the dataset
        """
        return self.data.shape
        
    def data_info(self):
        """
        Returns the information about the dataset.
        """
        return self.data.info()

    def data_description(self):
        """
        Returns the description of the dataset
        """
        return self.data.describe()


class data_cleaning:
    def __init__(self, data):
        """
        Initializing the data_cleaning class
        """
        self.data = data

    def missing_values(self):
        """
        checks for missing values
        """
        missing_values = self.data.isnull().sum()
        return missing_values

    def duplicates(self):
        """
        Checks for duplicate data
        """
        duplicates = self.data[self.data.duplicated()]
        return duplicates

    def handling_duplicates(self):
        """
        Drops all duplicate values
        """
        self.data.drop_duplicates(inplace = True)
        return self.data

    def null_values(self):
        """
        Checks for any null values in the data
        """
        null_values= self.data.isna().sum()
        return null_values

    def outliers(self):
        """
        Using quartiles to check for outliers
        """
        col_names = []
        col_count = []
        for col in self.data.select_dtypes(include=["float64", "int64"]).columns:
            #Calculating the 1st and 3rd quartiles (Q1 and Q3)
            Q1 = self.data[col].quantile(0.25)
            Q3 = self.data[col].quantile(0.75)

            #calculating the interquartile range (IQR)
            IQR = Q3 - Q1

            #defining the lower and upper bounds
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR

            #outliers are the values beyond the lower and upper bounds.
            outliers = self.data[col][(self.data[col] < lower_bound) | (self.data[col] > upper_bound)]

            #appending the column names and the number of outliers
            col_names.append(col)
            col_count.append(outliers.count())
        return list(zip(col_names,col_count))

    def drop_columns(self, columns_to_drop):
        """
        Drops unnecessary columns
        """
        self.data.drop(columns = columns_to_drop, axis = 1, inplace = True)
        return self.data


#Data Analysis
class data_analysis:
    def __init__ (self, data):
        """
        Initializing the univariate_analysis class
        """
        self.data = data

    def feature_distributions(self, bins = 20, kde = True):
        """
        plots the distribution of different features within the dataset
        """
        #select only columns to be plotted from the dataset
        numeric_columns = self.data.select_dtypes(include=["float64",
                                                      "int64"]).columns

        # number of subplots needed
        n = len(numeric_columns)

        #number of columns needed for the subplot grid
        n_cols = 3
        #number of rows needed for the subplot grid
        n_rows = (n//n_cols) + (1 if n % n_cols != 0 else 0)

        #create subplots
        plt.figure(figsize = (n_cols*6, n_rows*4))

        #iterate over the numeric columns and plot the distributions
        for i, column in enumerate (numeric_columns):
            #3-based subplot index
            plt.subplot(n_rows, n_cols, i+1)

            #plot histogram with kde
            sns.histplot(self.data[column], bins = bins, kde = kde)
         
            #set the title and labels
            plt.title(f"distribution of {column}")
            plt.xlabel(column)
            plt.ylabel("Frequency")

        plt.tight_layout() #Adjusting the layout for better spacing
        plt.show()

    def uni_plots (self, column,plot_type):
        """
        different univariate plots
        """
        plt.figure(figsize=(8,5))

        if plot_type == "histogram":
            sns.histplot(self.data[column], kde = True, bins = 30)
            plt.title (f"Distribution of {column}")
        elif plot_type == "box plot":
            sns.boxplot(self.data[column])
            plt.title(f"Box Plot of {column}")
        elif plot_type == "count plot" and self.data[column].dtype == "object":
            sns.countplot(x=column, data = self.data,)
            plt.title(f"count plot of {column}")
        else:
            print("Invalid plot type")

        plt.xlabel(column)
        plt.show()

    def biv_plots(self, column, target):
        """
        Different plots featuring bivariate analysis
        """
        plt.figure(figsize = (8,5))

        if self.data[column].dtype in ["float64", "int64"] :
            sns.boxplot(x = target, y = column, data = self.data)
            plt.title(f"{column} vs {target}")

        elif self.data[column].dtype == "object":
            sns.countplot(x = column, hue = target, data = self.data)
            plt.title(f"{column} distribution by {target}")

        plt.xlabel(column)
        plt.ylabel("count" if self.data[column].dtype == "object" else column)
        plt.show()

    def multiv_plots (self, columns, target):
        """
        using a heatmap to check for correlation
        """
        #calculate correlation matrix 
        corr_matrix = self.data[columns].corr()

        #create a heat map
        plt.figure(figsize = (10,8))
        sns.heatmap(corr_matrix, annot = True, cmap = "coolwarm", fmt = ".2f" )

        #Add titles to the plot
        plt.title("correlation Heatmap")
        plt.tight_layout()
        plt.show()

    def drop_columns(self, columns_to_drop):
        """
        Droping columns to avoid  multicolleniarity
        """
        self.data.drop(columns = columns_to_drop, axis = 1, inplace = True)
        return self.data

   
    


































                 