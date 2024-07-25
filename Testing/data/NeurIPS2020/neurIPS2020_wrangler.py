#!/usr/bin/env python
# coding: utf-8

# In[36]:


import os
import pandas as pd
import numpy as np
import time

path = os.path.dirname(__file__) #<- for .py #path from main file
q_data = os.path.join(path, "data/metadata/question_metadata_task_1_2.csv")
train_data = os.path.join(path, "data/train_data/train_task_1_2.csv")
test_public_data = os.path.join(path, "data/test_data/test_public_answers_task_1.csv")
test_private_data = os.path.join(path, "data/test_data/test_private_answers_task_1.csv")
q_matrix_output_file = os.path.join(path, "q_matrix.csv")
response_matrix_output_file = os.path.join(path, "response_matrix.csv")


# In[46]:


def createResponse():
    print("Building a response matrix...")
    train = pd.read_csv(train_data)
    test_public = pd.read_csv(test_public_data)
    test_private = pd.read_csv(test_private_data)
    df = pd.concat([train, test_public, test_private], axis=0, ignore_index=True)
    df = df.rename(columns={'UserId':'user_id', 'QuestionId':'problem_id', 'IsCorrect':'correct'})

    
    #drop NA
    df = df.dropna(how='any')
    
    #drop any questions that don't have skills in the q matrix
    if not os.path.exists(q_matrix_output_file):
        createQ()
    Q = pd.read_csv(q_matrix_output_file)
    labeled = Q['problem_id'].unique()
    df = df[df['problem_id'].isin(labeled)]
    
    #drop duplicates
    df = df.drop_duplicates(subset=["user_id", "problem_id"])
    
    scarce_problem = df["problem_id"].value_counts().min()
    scarce_user = df["user_id"].value_counts().min()
    while scarce_problem < 15 or scarce_user < 15:
        #remove any students that have 100% or 0% correct, uninteresting
        user_avg_correct = df.groupby('user_id')['correct'].mean()
        users_to_remove = user_avg_correct[(user_avg_correct == 1) | (user_avg_correct == 0)].index
        df = df[~df['user_id'].isin(users_to_remove)]
        
        #remove any problems tht appear less than 15 times
        problem_counts = df["problem_id"].value_counts()
        df = df[df["problem_id"].isin(problem_counts.index[problem_counts >= 15])]

        #remove any users who answer less than 15 problems
        user_counts = df["user_id"].value_counts()
        df = df[df["user_id"].isin(user_counts.index[user_counts >= 15])]
    
        scarce_problem = df["problem_id"].value_counts().min()
        scarce_user = df["user_id"].value_counts().min()
    
    Y = df[["user_id", "problem_id", "correct"]]
    Y.to_csv(response_matrix_output_file, index=False)
    print(f"Created a response matrix for {len(df['user_id'].unique())} users and {len(df['problem_id'].unique())} problems with {Y.shape[0]} responses")

#createResponse()


# In[38]:


def createQ(verbose=False):
    print("Building a Q matrix...")
    timer_start = time.time()
    df = pd.read_csv(q_data)

    problems = df["QuestionId"].unique()
    
    qdata = {}
    qdata["problem_id"] = problems
    
    skill_list = []
    #create a list of all skills
    for problem in problems: #change to no subscript for real life
        skills = eval(df[df["QuestionId"] == problem]['SubjectId'].iloc[0])
        for skill in skills:
            if skill not in skill_list:
                skill_list.append(skill)
                
    if(verbose):
        print("There are:", len(skill_list), "skills")
    
    for skill in skill_list:
      skill_problems = np.zeros(len(problems))
      for problem in problems:
        skills = eval(df[df["QuestionId"] == problem]['SubjectId'].iloc[0])
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

#createQ(verbose=True)


# In[47]:


def wrangle(overwrite=False, verbose=False):
    for f in [q_data, train_data, test_public_data, test_private_data]:
        if not os.path.exists(f):
            print(f'missing {f}')
            return None

    if overwrite or not os.path.exists(q_matrix_output_file):
        createQ(verbose=verbose)
    else:
        print("Using Existing Q matrix")

    if overwrite or not os.path.exists(response_matrix_output_file):
        createResponse()
    else:
        print("Using Existing response matrix")

    print("NeurIPS202 wrangling complete!")

#wrangle()

