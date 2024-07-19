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
#define various functions for splitting data different ways

#each outputs an array of 5 objects, each object contains a train dataframe and a test dataframe to be returned

def basicSplit(df):

    
    #randomly split the data into 5 ~equal portions
    df_rand = df.sample(frac=1).reset_index(drop=True)
    #Create quantile bins based on the user_id distribution
    quantile_bins = pd.qcut(df_rand['user_id'].rank(method='first'), q=5, labels=False)
    
    #Add the quantile bins as a new column to the DataFrame
    df_rand['quantile_bin'] = quantile_bins
    
    #Split the DataFrame into 5 parts based on the quantile bins
    dfs = [df_rand[df_rand['quantile_bin'] == i].drop(columns='quantile_bin') for i in range(5)] #5 for 5x validation
    
    res = []

    for i in range(len(dfs)):
        data = {}
        data["test"] = dfs[i]
        data["train"] = pd.concat([part for j, part in enumerate(dfs) if j != i], ignore_index=True)
        res.append(data)

    return res


# In[2]:


def irtPrepper(df):
    new = df.rename(columns={'problem_id' : 'item_id', 'correct' : 'score'})
    new["score"] = new["score"].astype(int)
    return new


# In[4]:


from data.ASSISTments2009 import assistments09_wrangler as assist09_wrangle
#definitions of various file names and paths
q_matrix_file = "q_matrix.csv"
response_matrix_file = "response_matrix.csv"

paths = {
    "ASSIST09" : "ASSISTments2009/",
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
def prepareData(dataset = "ASSIST09", runType = "basic", model = "IRT"): 
    data_path = paths[dataset]
    if(not os.path.exists(data_path + q_matrix_file)):
        print("Could not find Q matrix, calling wrangler")
        #have wrangler run ot make the Q matrix
        wranglers[dataset].wrangle()
        
    Q = pd.read_csv(data_path + q_matrix_file)
        

    if(not os.path.exists(data_path + response_matrix_file)):
        print("Could not find Response matrix, calling wrangler")
        #have wrangler run ot make the Response matrix - facit
        wranglers[dataset].wrangle()

    Y = pd.read_csv(data_path + response_matrix_file)
    res = splitters[runType](preppers[model](Y))

    return Q, res

