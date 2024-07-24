#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
path = os.path.dirname(__file__) #path from main file
input_file = os.path.join(path, "assistments_2009_2010.csv")
q_matrix_output_file = os.path.join(path, "q_matrix.csv")
response_matrix_output_file = os.path.join(path, "response_matrix.csv")


# In[2]:


import pandas as pd
import numpy as np

def wrangle(overwrite=False):
    # if overwrite is true delete the existing files before creating the new
    # if overwrite is false you can use the existing files if they are there and don't need to actually run the code
    if(overwrite or not os.path.exists(q_matrix_output_file) or not os.path.exists(response_matrix_output_file)):
        print("Wrangling Data")

        #read in the data
        df = pd.read_csv(input_file)
        
        print(df.shape)
        
        #select relevant columns and remove any skilless tasks
        df = df[["user_id", "problem_id", "correct", "list_skill_ids", "list_skills"]]
        df = df[df["list_skill_ids"].notna()]

        print(df.shape)

        #filter the data
        df = df.drop_duplicates(subset=["user_id", "problem_id"])

        min_problem_count = 15
        min_user_count = 15
        
        scarce_problem = df["problem_id"].value_counts().min()
        scarce_user = df["user_id"].value_counts().min()
        user_avg_correct = df.groupby('user_id')['correct'].mean()
        users_to_remove = user_avg_correct[(user_avg_correct == 1) | (user_avg_correct == 0)].index
        while scarce_problem < min_problem_count or scarce_user < min_user_count or len(users_to_remove) > 0:
            #remove any students that have 100% or 0% correct, uninteresting
            user_avg_correct = df.groupby('user_id')['correct'].mean()
            users_to_remove = user_avg_correct[(user_avg_correct == 1) | (user_avg_correct == 0)].index
            df = df[~df['user_id'].isin(users_to_remove)]
            
            #remove any problems tht appear less than 15 times
            problem_counts = df["problem_id"].value_counts()
            df = df[df["problem_id"].isin(problem_counts.index[problem_counts >= min_problem_count])]
    
            #remove any users who answer less than 15 problems
            user_counts = df["user_id"].value_counts()
            df = df[df["user_id"].isin(user_counts.index[user_counts >= min_user_count])]
        
            scarce_problem = df["problem_id"].value_counts().min()
            scarce_user = df["user_id"].value_counts().min()

        print("Generating output for:")
        print("Items: " + str(len(df['problem_id'].unique())) + " Users: " + str(len(df['user_id'].unique())) + " Responses: " + str(df.shape[0]))

        #Create the Q matrix
        if(overwrite or not os.path.exists(q_matrix_output_file)):
            createQ(df) #post examen non verbose
            
        #Create the Response matrix
        if(overwrite or not os.path.exists(response_matrix_output_file)):
            createResponse(df)
    else:
        print("Using pre-existing wrangled data")

#wrangle()


# In[3]:


import time

def createQ(df, verbose=False):
    timer_start = time.time()
    problems = df["problem_id"].unique()
    
    qdata = {}
    qdata["problem_id"] = problems

    
    all_skills = df['list_skill_ids'].str.split(';').explode().unique()
    skill_list = list(all_skills)
    if(verbose):
        print("There are:", len(skill_list), "skills")

    for skill in skill_list:
      skill_problems = np.zeros(len(problems))
      for problem in problems:
        skills = df.loc[df["problem_id"] == problem]["list_skill_ids"].tolist()[0].split(";")
        if(skill in skills):
          skill_problems[np.where(problems == problem)[0]] = 1
      qdata[skill] = skill_problems
      if(verbose):  
          print("Completed: ", len(qdata.keys()) - 1, " skills")
    
    Q = pd.DataFrame(qdata)
    timer_end = time.time()
    duration = timer_end - timer_start
    print(f"Created a Q matrix for {len(skill_list)} skills and {len(problems)} problems in {duration:.2f} seconds")

    Q.to_csv(q_matrix_output_file, index=False)


# In[4]:


def createResponse(df, verbose=False):
    Y = df[["user_id", "problem_id", "correct"]]
    Y.to_csv(response_matrix_output_file, index=False)
    print(f"Created a response matrix for {len(df['user_id'].unique())} users and {len(df['problem_id'].unique())} problems with {Y.shape[0]} responses")

