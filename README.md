# Unpivot
This python function uses numpy and pandas to unpivot a pivotted table. User can specified the number of row headers they would like to keep in the unpivotted table. 

## PivotTable_V2.ppy 
### Libraries Used
- pandas
- numpy

### Functions
- Unpivot

##### Unpivot(df, numOfRowHeaders = 1)
This is the only function in PivotTable_V2.py.  The function unpivots a given DataFrame
The pivot function is given a DataFrame and the number of header rows and unpivots the DataFrame into a tabulated format.

The first step is adding an index so that the function has access to every column, including the one that was used last used as an index. 
```py
df = df.reset_index()
```
Then it uses the len of the index to get the number of rows in the table, and the len of the columns to get the number of columns. 
```py
numOfRows = len(df.index)
numOfColumns = len(df.columns) 
```
The next step is creating the list of columns for the DataFrame. A list of column names is created. 
These are the columns that will be used for all records. They are columns that are in the pivot table and will be columns in the unpivotted table. 
```py
listOfColumnNames = list()
```
Then for the number of rowHeader a columnName is given by the DataFrames column index for the number the for loop is currently on.  That name is appended to the list of column names. 
```py
for rowHeader in range(numOfRowHeaders):
    columnName = str(df.columns[rowHeader])
    listOfColumnNames.append(columnName)
```
Two more columns names need to be added to the list that will create the column headers for the dataframe;  ColumnTitle, and Value.  ColumnTitle is the name that was used as a column name and now is used as a data point in the row.  The Value is the value that the Column name along with the RowHeaders is associated with. 
```py
listOfColumnNames.append("ColumnTitle")
listOfColumnNames.append("Value")
```
Once the column names are set the unpivotting begins. The funciton is not undoing anything, instead it is building a new DataFrame using indexes of the old DataFrame to map where the data should go. The for loop loops through the rows, and in each row loops through the columns that are not part of the original rowHeaders. So the index starts at the number of rowHeaders (meaning one more index forward from the rowHeaders and ends with the column index.  The number of iterations will be the number of rows in the original table times the number of columns that are not part of the rowHeaders. 
```py
for row in range(numOfRows):        
    for col in range(numOfRowHeaders, numOfColumns):
```
A list is created that will be the next row to add to the new pivot table. 
```py
unpivotedRowConstructor = list()
```
The row is first given the rowHeader data for the row. This is done by looping through the range of numOfRowHeaders, and using that index to get the data point from the original table. 
```py
for i in range(numOfRowHeaders):
    unpivotedRowConstructor.append(str(df.iloc[row, i]))
```
It then gets the column name as of the original table as a data point, and the value that was associated with the row and column in the original table. 
```py
unpivotedRowConstructor.append(str(df.columns[col]))
unpivotedRowConstructor.append(str(df.iloc[row,col]))   
```
The newly contructed list is added to the new DataFrame.
```py
unpivotedDf.loc[rowCount] = unpivotedRowConstructor
```          
When this loop is done iterating the table is returned as a DataFrame. 
