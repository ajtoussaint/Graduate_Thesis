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
#input is a dataframe with all the data formatted for the appropriate model, target=name of target column
#each outputs an array of 5 objects, each object contains a train dataframe and a test dataframe to be returned

def basicSplit(df, target='correct'):
    print("Performing 5 fold split...")
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

    print("split complete!")
    return dfs

def sampledSplit(df, target='correct'):
    print("Performing sampled split...")
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
        udf = udf.sample(frac=0.4) #Lowest split can go to guarantee 5-fold is possible with a minimum of 15 examples per student
        for train_index, test_index in kf.split(udf):
            train, test = udf.iloc[train_index], udf.iloc[test_index]
            #append this users training/testing data to the total collection
            dfs[fold_index]["train"] = pd.concat([dfs[fold_index]["train"], train], axis=0, ignore_index=True)
            dfs[fold_index]["test"] = pd.concat([dfs[fold_index]["test"], test], axis=0, ignore_index=True)
            fold_index += 1
            
    print("split complete!")
    return dfs

def correctSaturatedSplit(df, target='correct'):
    print("Performing split with extra correct responses in training...")
    users = df['user_id'].unique()
    
    n = 5
    
    kf = KFold(n_splits=n, shuffle=True, random_state=217)
    
    dfs = []
    
    for i in range(n):
        dfs.append({
            "train":pd.DataFrame(),
            "test":pd.DataFrame()
        })
    #not going to be true k-fold
    for uid in users:
        for fold_index in range(n):
            udf = df[df['user_id'] == uid].copy()
            udf = udf.sample(frac=1).reset_index(drop=True)#shuffle random
            #for this user create a random distribution of train and test 80/20 with train containing a greater ratio of correct answers
            udf_ones = udf[udf[target] == 1].copy() #"Score" is specific to IRT, may need to pass an argument for this column name...or create the prepper as a class and store as attribute...
            udf_zeros = udf[udf[target] == 0].copy()

            train = pd.concat([udf_ones.sample(frac=0.9), udf_zeros.sample(frac=0.65)], axis=0, ignore_index=True)
            test = udf.merge(train, how='outer', indicator=True).query('_merge == "left_only"').drop('_merge', axis=1)

            dfs[fold_index]["train"] = pd.concat([dfs[fold_index]["train"], train], axis=0, ignore_index=True)
            dfs[fold_index]["test"] = pd.concat([dfs[fold_index]["test"], test], axis=0, ignore_index=True)

    print("split complete!")
    return dfs

def incorrectSaturatedSplit(df, target='correct'):
    print("Performing split with extra incorrect responses in training...")
    users = df['user_id'].unique()
    
    n = 5
    
    kf = KFold(n_splits=n, shuffle=True, random_state=217)
    
    dfs = []
    
    for i in range(n):
        dfs.append({
            "train":pd.DataFrame(),
            "test":pd.DataFrame()
        })
    #not going to be true k-fold
    for uid in users:
        for fold_index in range(n):
            udf = df[df['user_id'] == uid].copy()
            udf = udf.sample(frac=1).reset_index(drop=True)#shuffle random
            #for this user create a random distribution of train and test 80/20 with train containing a greater ratio of correct answers
            udf_ones = udf[udf[target] == 1].copy()
            udf_zeros = udf[udf[target] == 0].copy()

            #alternatively, could assing one correct and one incorrect to each set train/test
            #then compute based on the remaining length...

            #fractions are determined assuming 60/40 correct/incorrect, may be a problem outside of assistments...
            train = pd.concat([udf_ones.sample(frac=(44/60)), udf_zeros.sample(frac=0.9)], axis=0, ignore_index=True)
            test = udf.merge(train, how='outer', indicator=True).query('_merge == "left_only"').drop('_merge', axis=1)

            dfs[fold_index]["train"] = pd.concat([dfs[fold_index]["train"], train], axis=0, ignore_index=True)
            dfs[fold_index]["test"] = pd.concat([dfs[fold_index]["test"], test], axis=0, ignore_index=True)
    
    print("split complete!")
    return dfs


# define various functions to taylor the data to a specific model's implementation


def irtPrepper(df):
    print("Formatting data for IRT...")
    #rename columns to comply with existing IRT code
    target_column = 'score'
    new = df.rename(columns={'problem_id' : 'item_id', 'correct' : target_column})
    new[target_column] = new[target_column].astype(int)

    #adjust item_id and user_id columns to have minimum index of 1 and max of 
    new['user_id'] = new['user_id'].rank(method='dense').astype(int)
    new['item_id'] = new['item_id'].rank(method='dense').astype(int)

    print("formatted!")
    
    return new, target_column


# In[4]:


#to run locally will need to remove data. from file path
from data.ASSISTments2009 import assistments09_wrangler as assist09_wrangle 
from data.NeurIPS2020 import neurIPS2020_wrangler as neur20_wrangle
#definitions of various file names and paths
q_matrix_file = "q_matrix.csv"
response_matrix_file = "response_matrix.csv"

dir_path = os.path.dirname(__file__)

paths = {
    "ASSIST09" : "ASSISTments2009",
    "NEUR20" : "NeurIPS2020",
}
wranglers = {
    "ASSIST09" : assist09_wrangle,
    "NEUR20" : neur20_wrangle,
}

splitters = {
    "basic" : basicSplit,
    "sampled" : sampledSplit,
    "correctSaturated":correctSaturatedSplit,
    "incorrectSaturated":incorrectSaturatedSplit,
}

preppers = {
    "IRT" : irtPrepper
}


# In[5]:


#recieves input on dataset, they type of run to be executed, and the model to be executed on
#returns the Q matrix as a dataframe, and an array containing objects with train/test datasets
def prepareData(dataset = "ASSIST09", runType = "basic", model = "IRT", overwrite=False):
    print(f'preparing data from {dataset} to train {model} for {runType} format')
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
    prepped_data, target_column = preppers[model](Y)
    res = splitters[runType](prepped_data, target=target_column)

    return Q, res

