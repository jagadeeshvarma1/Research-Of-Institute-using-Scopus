from distutils.command.clean import clean
import os
import pandas as pd
dir='/home/avinsah/Desktop/final year project/dataset'          #datasets directory
for i in os.listdir(dir):                                             #iteration over the dataset names in the directory 
    f = os.path.join(dir, i)
    df=pd.read_csv(f)
    df.drop(['Result Number'],axis=1,inplace=True)                  #dropping unwanted columns
    df.dropna(inplace=True)                                         #dropping null values
    df.reset_index(inplace = True, drop = True)                      #resetting the index
    df.rename(columns={df.columns[2]:"h-index"},inplace=True)
    name=df.iloc[0][3]
    cleandir="/home/avinsah/Desktop/final year project/cleaned datasets"
    if name+'.csv' in os.listdir(cleandir):
        print(name)
        df.to_csv(f'/home/avinsah/Desktop/final year project/cleaned datasets/{name}.csv', mode='a', index=False, header=False)
    else:
        df.to_csv(f'/home/avinsah/Desktop/final year project/cleaned datasets/{name}.csv',index=False)
