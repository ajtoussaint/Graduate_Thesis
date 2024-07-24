#!/usr/bin/env python
# coding: utf-8

# #Data Prepper
# 
# Recieves parameters for dataset, run type, and the model to be used
# 
# gets the Q matrix and Response matrix files from the wrangler associated with the desired dataset and formats them to be ready to feed to the model to complete a test run

# #Codings of strings for each dataset and model
# - ASSIST09 : Assistments 2009-2010 

# In[1]:


import os
import pandas as pd
import numpy as np
from sklearn.model_selection import KFold
#define various functions for splitting data different ways

#each outputs an array of 5 objects, each object contains a train dataframe and a test dataframe to be returned

def basicSplit(df):
    users = df['user_id'].unique()
    
    n = 5
    
    kf = KFold(n_splits=n, shuffle=True, random_state=217)
    
    dfs = []
    
    for i in range(n):
        dfs.append({
            "train":pd.DataFrame(),
            "test":pd.DataFrame()
        })
    
    for uid in users:
        fold_index = 0
        #perform a KFold split on each individual users data
        udf = df[df['user_id'] == uid].copy()
    
        for train_index, test_index in kf.split(udf):
            train, test = udf.iloc[train_index], udf.iloc[test_index]
            #append this users training/testing data to the total collection
            dfs[fold_index]["train"] = pd.concat([dfs[fold_index]["train"], train], axis=0, ignore_index=True)
            dfs[fold_index]["test"] = pd.concat([dfs[fold_index]["test"], test], axis=0, ignore_index=True)
            fold_index += 1
    return dfs

def correctSaturatedSplit(df):
    #randomize
    df_rand = df.sample(frac=1).reset_index(drop=True)
    #split into correct and incorrect
    df_correct = df_rand[df_rand['correct'] == 1]
    df_incorrect = df_rand[df_rand['correct'] == 0]


# define various functions to taylor the data to a specific model's implementation


def irtPrepper(df):
    #rename columns to comply with existing IRT code
    new = df.rename(columns={'problem_id' : 'item_id', 'correct' : 'score'})
    new["score"] = new["score"].astype(int)

    #adjust item_id and user_id columns to have minimum index of 1 and max of 
    new['user_id'] = new['user_id'].rank(method='dense').astype(int)
    new['item_id'] = new['item_id'].rank(method='dense').astype(int)
    
    return new


# In[4]:


#to run locally will need to remove data. from file path
from data.ASSISTments2009 import assistments09_wrangler as assist09_wrangle 
#definitions of various file names and paths
q_matrix_file = "q_matrix.csv"
response_matrix_file = "response_matrix.csv"

dir_path = os.path.dirname(__file__)

paths = {
    "ASSIST09" : "ASSISTments2009",
}
wranglers = {
    "ASSIST09" : assist09_wrangle
}

splitters = {
    "basic" : basicSplit
}

preppers = {
    "IRT" : irtPrepper
}


# In[5]:


#recieves input on dataset, they type of run to be executed, and the model to be executed on
#returns the Q matrix as a dataframe, and an array containing objects with train/test datasets
def prepareData(dataset = "ASSIST09", runType = "basic", model = "IRT", overwrite=False): 
    data_path = os.path.join(dir_path, paths[dataset])
    q_matrix_path = os.path.join(data_path, q_matrix_file)
    response_matrix_path = os.path.join(data_path, response_matrix_file)
    if(not os.path.exists(q_matrix_path)):
        print("Could not find Q matrix, calling wrangler")
        #have wrangler run ot make the Q matrix
        wranglers[dataset].wrangle(overwrite=overwrite)
        
    Q = pd.read_csv(q_matrix_path)
        

    if(not os.path.exists(response_matrix_path)):
        print("Could not find Response matrix, calling wrangler")
        #have wrangler run ot make the Response matrix - facit
        wranglers[dataset].wrangle(overwrite=overwrite)

    Y = pd.read_csv(response_matrix_path)
    res = splitters[runType](preppers[model](Y))

    return Q, res

