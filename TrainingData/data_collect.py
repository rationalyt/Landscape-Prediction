import pandas as pd
import os
def merge_files(filex,filey):
    #Read files
    x_df = pd.read_csv(filex)
    y_df = pd.read_csv(filey)

    #Extract column integer values
    x_first = pd.DataFrame(x_df.columns).T
    y_first = pd.DataFrame(y_df.columns).T

    #Define column names
    x_columns = ["a1", "a2", "a3", "g1", "g2", "g3"]
    y_columns = ["y"]

    #Assign column names
    x_df.columns = x_columns
    y_df.columns= y_columns
    x_first.columns = x_columns
    y_first.columns = y_columns

    #Concatenate the dataframes with new column names
    x_df = pd.concat([x_first, x_df],axis = 0).reset_index(drop=True)
    y_df = pd.concat([y_first, y_df],axis = 0).reset_index(drop=True)

    #Define the output dataframe structure
    combined_df = pd.DataFrame(columns=["a1", "a2", "a3", "g1", "g2", "g3", "y"])
    y_ind = 0

    #Loop through and merge the dataframes
    for i in range(0,len(x_df)):
        if i%4 == 0: 
            y = y_df.iloc[y_ind:y_ind+1].reset_index(drop=True)
            y_ind += 1
        x = x_df.iloc[i:i+1].reset_index(drop=True)
        z = pd.concat([x,y],axis=1).reset_index(drop=True)
        combined_df = combined_df.append(z, ignore_index = True)
    combined_df = combined_df.astype(float)
    return combined_df

if __name__ == "__main__":
    #Pass file name as parameters
    df = merge_files(0,0)
    df.to_csv('out.csv')
    print(df)