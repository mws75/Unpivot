#These are funcitons you can use to manipulate a pivot table 
#V2 - Cleaned Up Code 

import pandas as pd 
import numpy

def Unpivot(df, numOfRowHeaders = 1):
    #use to unpivot a table

    #Get data frame counts
    numOfRows = len(df.index)
    numOfColumns = len(df.columns)  #We don't need to subtract anything because the range(1, numOfColumns) takes care of that    

    #print(df)
    #create columns
    listOfColumnNames = list()   
    newBranch_listOfColumns = list()
    newnewBranch_listOfColumns = list()

    for rowHeader in range(numOfRowHeaders):
        columnName = str(df.columns[rowHeader])
        listOfColumnNames.append(columnName)
    listOfColumnNames.append("ColumnTitle")
    listOfColumnNames.append("Value")
    
    unpivotedDf = pd.DataFrame(columns= listOfColumnNames, dtype=str)

    rowCount = 0   
    for row in range(numOfRows):        
        for col in range(numOfRowHeaders, numOfColumns):
            #create a list that will be added as a row to the data table. 
            unpivotedRowConstructor = list()        
            #add static to unpivotted table
            for i in range(numOfRowHeaders):
                unpivotedRowConstructor.append(str(df.iloc[row, i]))
                        
            #add dynamic data to unpivottedtable
            unpivotedRowConstructor.append(str(df.columns[col]))
            unpivotedRowConstructor.append(str(df.iloc[row,col]))            
            #add row to datatable
            unpivotedDf.loc[rowCount] = unpivotedRowConstructor
            rowCount += 1

    return unpivotedDf     
