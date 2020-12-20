#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv("unemployed_1_data.csv", sep=";")


# In[3]:


df


# In[218]:


month_unemployed_count = df["month_unemployed"].value_counts()
month_unemployed_count


# Средний возраст(близко к моде и медиане)

# In[214]:


df["age"].mean()


# Только безработные с уровнем образования среднее общее, среднее профессиональное,основное общее.

# In[5]:


edu_1 = df[(df["education"]=="Среднее общее образование")|(df["education"]=="Среднее профессиональное образование")|(df["education"]=="Основное общее образование")|(df["education"]=="Начальное общее образование")]
edu_1


# In[ ]:


job_pri = edu_1["gender"].value_counts()


# In[7]:


edu_1.to_csv("edu_1.csv")


# In[215]:


edu_1["age"].mean()


# In[209]:


edu_3 = edu_1["gender"].value_counts()
edu_3


# In[210]:


edu_4 = edu_1["age"].value_counts()
edu_4


# In[208]:


edu_2 = edu_1["hc_any"].value_counts()
edu_2


# In[192]:


age_5 = edu['age'].value_counts()
age_5


# In[191]:


gender_edu = edu['gender'].value_counts()
gender_edu


# In[182]:


gender = df['gender'].value_counts()
gender


# In[183]:


educ_napravl = df['educ_napravl'].value_counts()
educ_napravl


# In[217]:


prof = df['gender'].value_counts()
prof


# In[216]:


education_speciality_counts = df['education_speciality'].value_counts()
education_speciality_counts


# In[171]:


hgdr = gdr['hc_any'].value_counts()
hgdr


# In[184]:


region_gdr = gdr['region'].value_counts()
region_gdr


# In[ ]:


gdr = df[df["gender"] == "Женский"]


# In[174]:


rgdr = gdr["hc_repeat"].value_counts()
rgdr


# In[165]:


fgdr = gdr[gdr["hc_any"]]


# In[166]:


fgdr


# In[144]:


education_speciality_counts = df['education_speciality'].value_counts()
education_speciality_counts


# In[193]:


profession_last_educ_count = df['profession_last_educ'].value_counts()
profession_last_educ_count


# In[195]:


profession_last_educ_count.to_excel("educ.xlsx")


# In[61]:


df_5 = pd.DataFrame(df)
df_5


# In[145]:


df["age"].plot.hist(**{"ls":"--","linewidth":2, "edgecolor":"r", "alpha":0.7})


# In[77]:


hc_any_count = df['hc_any'].value_counts()
hc_any_count


# In[82]:


hc_predpens_counts = df['hc_predpens'].value_counts()


# In[83]:


hc_predpens_counts


# In[84]:


hc_largefam_counts = df['hc_largefam'].value_counts()
hc_largefam_counts


# In[85]:


hc_singleparent_counts = df['hc_singleparent'].value_counts()
hc_singleparent_counts


# In[86]:


hc_redundantworkers_counts = df['hc_redundantworkers'].value_counts()
hc_redundantworkers_counts


# In[87]:


month_end_busyness_counts = df['month_end_busyness'].value_counts()
month_end_busyness_counts


# In[90]:


month_end_busyness_counts.to_excel("output.xlsx")


# In[91]:


education_counts = df['education'].value_counts()
education_counts


# In[92]:


region_counts = df['region'].value_counts()
region_counts


# In[93]:


region_counts.to_excel("output1.xlsx")


# In[94]:


experience_counts = df['experience'].value_counts()
experience_counts


# In[95]:


work_napravl_number_counts = df['work_napravl_number'].value_counts()
work_napravl_number_counts


# In[97]:


work_refusal_number = df['work_refusal_number'].value_counts()
work_refusal_number


# In[99]:


expected_salary_counts = df['expected_salary'].value_counts()
expected_salary_counts


# In[100]:


expected_salary_counts.to_excel("output2.xlsx")


# In[96]:


work_napravl_refusal_number = df['work_napravl_refusal_number'].value_counts()
work_napravl_refusal_number


# In[66]:


salary_counts = df['expected_salary'].value_counts()
salary_counts


# In[67]:


salary_counts_df = pd.DataFrame(salary_counts)
salary_counts_df


# In[75]:


salary_counts_df.sort_values(by=["expected_salary"], ascending=False) #сортирует колонки


# In[5]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[8]:


df_salary = df[df['expected_salary'] != "None"]
df_salary


# In[16]:


df_salary_1 = df_salary[df_salary['expected_salary'] != "0.0"]
df_salary_1


# In[111]:


mode_salary = pd.to_numeric(df_salary_1['expected_salary']) 


# In[112]:


mode_salary_1= pd.DataFrame(rome)


# In[113]:


mode_salary_1


# Считаем среднюю ожидаемую зарплату

# In[118]:


mode_salary_1.mode()


# In[121]:


month_close_counts = df['month_close'].value_counts()
month_close_counts


# In[123]:


reason_close_counts = df['reason_close'].value_counts()
reason_close_counts


# In[63]:


df_salary_2 = pd.DataFrame(df_salary_1)
df_salary_1


# In[180]:


df_1 = pd.read_csv("rostrud_invitations.csv", sep=";")
df_1


# In[ ]:


responseType = df_2['responseType'].value_counts()
responseType


# In[140]:


df_2 = pd.read_csv("rostrud_responses.csv", sep=";")
df_2


# In[141]:


responseType = df_2['responseType'].value_counts()
responseType


# In[147]:


creationDate_count = df_2['creationDate'].value_counts()
creationDate_count

