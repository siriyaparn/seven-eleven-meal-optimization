!pip install -U pandasql
!pip install amplpy

import os
import sys
import pandas as pd
import sqlite3
import numpy as np
from amplpy import AMPL
from pandasql import sqldf
from sklearn import datasets

from amplpy import AMPL, tools
ampl = tools.ampl_notebook(
    modules=["cplex"],          # modules to install
    license_uuid="default",     # license to use
    g=globals())                # instantiate AMPL object and register magics

# connect database
con = sqlite3.connect("data.db")

cur = con.cursor()
table = pd.DataFrame(cur.execute("SELECT name FROM sqlite_master WHERE type='table'"))
table.reset_index(drop=True, inplace=True)
table = table[0]
table = table.loc[0:]
print(table)

table_name = []
for i in table:
    exec('{} = pd.read_sql_query(("select * from " + i),con)'.format(i))
    table_name.append(i)
table_name

# Nutrition dataframe for female
y3_carb_new = pd.DataFrame(y3_fm.iloc[2:6,:].mean(), index = ["min","max"]).transpose()
y3_fm = y3_fm.append(y3_carb_new)
y3_fm = y3_fm.drop([y3_fm.index[2],y3_fm.index[3],y3_fm.index[4],y3_fm.index[5]])
y3_fm = y3_fm.fillna("carb")
y3_fm.columns = ["nutr","m_min","m_max"]
y3_fm = y3_fm.set_index(["nutr"])
y3_fm = y3_fm.div(3)

y5_carb_new = pd.DataFrame(y5_fm.iloc[2:6,:].mean(), index = ["min","max"]).transpose()
y5_fm = y5_fm.append(y5_carb_new)
y5_fm = y5_fm.drop([y5_fm.index[2],y5_fm.index[3],y5_fm.index[4],y5_fm.index[5]])
y5_fm = y5_fm.fillna("carb")
y5_fm.columns = ["nutr","m_min","m_max"]
y5_fm = y5_fm.set_index(["nutr"])
y5_fm = y5_fm.div(3)

y8_carb_new = pd.DataFrame(y8_fm.iloc[2:6,:].mean(), index = ["min","max"]).transpose()
y8_fm = y8_fm.append(y8_carb_new)
y8_fm = y8_fm.drop([y8_fm.index[2],y8_fm.index[3],y8_fm.index[4],y8_fm.index[5]])
y8_fm = y8_fm.fillna("carb")
y8_fm.columns = ["nutr","m_min","m_max"]
y8_fm = y8_fm.set_index(["nutr"])
y8_fm =y8_fm.div(3)

y12_carb_new = pd.DataFrame(y12_fm.iloc[2:6,:].mean(), index = ["min","max"]).transpose()
y12_fm = y12_fm.append(y12_carb_new)
y12_fm = y12_fm.drop([y12_fm.index[2],y12_fm.index[3],y12_fm.index[4],y12_fm.index[5]])
y12_fm = y12_fm.fillna("carb")
y12_fm.columns = ["nutr","m_min","m_max"]
y12_fm = y12_fm.set_index(["nutr"])
y12_fm =y12_fm.div(3)

y15_carb_new = pd.DataFrame(y15_fm.iloc[2:6,:].mean(), index = ["min","max"]).transpose()
y15_fm = y15_fm.append(y15_carb_new)
y15_fm = y15_fm.drop([y15_fm.index[2],y15_fm.index[3],y15_fm.index[4],y15_fm.index[5]])
y15_fm = y15_fm.fillna("carb")
y15_fm.columns = ["nutr","m_min","m_max"]
y15_fm = y15_fm.set_index(["nutr"])
y15_fm = y15_fm.div(3)

y18_carb_new = pd.DataFrame(y18_fm.iloc[2:6,:].mean(), index = ["min","max"]).transpose()
y18_fm = y18_fm.append(y18_carb_new)
y18_fm = y18_fm.drop([y18_fm.index[2],y18_fm.index[3],y18_fm.index[4],y18_fm.index[5]])
y18_fm = y18_fm.fillna("carb")
y18_fm.columns = ["nutr","m_min","m_max"]
y18_fm = y18_fm.set_index(["nutr"])
y18_fm = y18_fm.div(3)

y30_carb_new = pd.DataFrame(y30_fm.iloc[2:6,:].mean(), index = ["min","max"]).transpose()
y30_fm = y30_fm.append(y30_carb_new)
y30_fm = y30_fm.drop([y30_fm.index[2],y30_fm.index[3],y30_fm.index[4],y30_fm.index[5]])
y30_fm = y30_fm.fillna("carb")
y30_fm.columns = ["nutr","m_min","m_max"]
y30_fm = y30_fm.set_index(["nutr"])
y30_fm = y30_fm.div(3)

y50_carb_new = pd.DataFrame(y50_fm.iloc[2:6,:].mean(), index = ["min","max"]).transpose()
y50_fm = y50_fm.append(y50_carb_new)
y50_fm = y50_fm.drop([y50_fm.index[2],y50_fm.index[3],y50_fm.index[4],y50_fm.index[5]])
y50_fm = y50_fm.fillna("carb")
y50_fm.columns = ["nutr","m_min","m_max"]
y50_fm = y50_fm.set_index(["nutr"])
y50_fm = y50_fm.div(3)

y60_carb_new = pd.DataFrame(y60_fm.iloc[2:6,:].mean(), index = ["min","max"]).transpose()
y60_fm = y60_fm.append(y60_carb_new)
y60_fm = y60_fm.drop([y60_fm.index[2],y60_fm.index[3],y60_fm.index[4],y60_fm.index[5]])
y60_fm = y60_fm.fillna("carb")
y60_fm.columns = ["nutr","m_min","m_max"]
y60_fm = y60_fm.set_index(["nutr"])
y60_fm = y60_fm.div(3)

y70_carb_new = pd.DataFrame(y70_fm.iloc[2:6,:].mean(), index = ["min","max"]).transpose()
y70_fm = y70_fm.append(y70_carb_new)
y70_fm = y70_fm.drop([y70_fm.index[2],y70_fm.index[3],y70_fm.index[4],y70_fm.index[5]])
y70_fm = y70_fm.fillna("carb")
y70_fm.columns = ["nutr","m_min","m_max"]
y70_fm = y70_fm.set_index(["nutr"])
y70_fm = y70_fm.div(3)

y71_carb_new = pd.DataFrame(y71_fm.iloc[2:6,:].mean(), index = ["min","max"]).transpose()
y71_fm = y71_fm.append(y71_carb_new)
y71_fm = y71_fm.drop([y71_fm.index[2],y71_fm.index[3],y71_fm.index[4],y71_fm.index[5]])
y71_fm = y71_fm.fillna("carb")
y71_fm.columns = ["nutr","m_min","m_max"]
y71_fm = y71_fm.set_index(["nutr"])
y71_fm = y71_fm.div(3)

# Nutrition datafram for male
y3_carb_new = pd.DataFrame(y3_m.iloc[2:6,:].mean(), index = ["min","max"]).transpose()
y3_m = y3_m.append(y3_carb_new)
y3_m = y3_m.drop([y3_m.index[2],y3_m.index[3],y3_m.index[4],y3_m.index[5]])
y3_m = y3_m.fillna("carb")
y3_m.columns = ["nutr","m_min","m_max"]
y3_m = y3_m.set_index(["nutr"])
y3_m = y3_m.div(3)

y5_carb_new = pd.DataFrame(y5_m.iloc[2:6,:].mean(), index = ["min","max"]).transpose()
y5_m = y5_m.append(y5_carb_new)
y5_m = y5_m.drop([y5_m.index[2],y5_m.index[3],y5_m.index[4],y5_m.index[5]])
y5_m = y5_m.fillna("carb")
y5_m.columns = ["nutr","m_min","m_max"]
y5_m = y5_m.set_index(["nutr"])
y5_m = y5_m.div(3)

y8_carb_new_m = pd.DataFrame(y8_m.iloc[2:6,:].mean(), index = ["min","max"]).transpose()
y8_m = y8_m.append(y8_carb_new_m)
y8_m = y8_m.drop([y8_m.index[2],y8_m.index[3],y8_m.index[4],y8_m.index[5]])
y8_m = y8_m.fillna("carb")
y8_m.columns = ["nutr","m_min","m_max"]
y8_m = y8_m.set_index(["nutr"])
y8_m = y8_m.div(3)

y12_carb_new = pd.DataFrame(y12_m.iloc[2:6,:].mean(), index = ["min","max"]).transpose()
y12_m = y12_m.append(y12_carb_new)
y12_m = y12_m.drop([y12_m.index[2],y12_m.index[3],y12_m.index[4],y12_m.index[5]])
y12_m = y12_m.fillna("carb")
y12_m.columns = ["nutr","m_min","m_max"]
y12_m = y12_m.set_index(["nutr"])
y12_m = y12_m.div(3)

y15_carb_new = pd.DataFrame(y15_m.iloc[2:6,:].mean(), index = ["min","max"]).transpose()
y15_m = y15_m.append(y15_carb_new)
y15_m = y15_m.drop([y15_m.index[2],y15_m.index[3],y15_m.index[4],y15_m.index[5]])
y15_m = y15_m.fillna("carb")
y15_m.columns = ["nutr","m_min","m_max"]
y15_m = y15_m.set_index(["nutr"])
y15_m = y15_m.div(3)

y18_carb_new = pd.DataFrame(y18_m.iloc[2:6,:].mean(), index = ["min","max"]).transpose()
y18_m = y18_m.append(y18_carb_new)
y18_m = y18_m.drop([y18_m.index[2],y18_m.index[3],y18_m.index[4],y18_m.index[5]])
y18_m = y18_m.fillna("carb")
y18_m.columns = ["nutr","m_min","m_max"]
y18_m = y18_m.set_index(["nutr"])
y18_m = y18_m.div(3)

y30_carb_new = pd.DataFrame(y30_m.iloc[2:6,:].mean(), index = ["min","max"]).transpose()
y30_m = y30_m.append(y30_carb_new)
y30_m = y30_m.drop([y30_m.index[2],y30_m.index[3],y30_m.index[4],y30_m.index[5]])
y30_m = y30_m.fillna("carb")
y30_m.columns = ["nutr","m_min","m_max"]
y30_m = y30_m.set_index(["nutr"])
y30_m = y30_m.div(3)

y50_carb_new = pd.DataFrame(y50_m.iloc[2:6,:].mean(), index = ["min","max"]).transpose()
y50_m = y50_m.append(y50_carb_new)
y50_m = y50_m.drop([y50_m.index[2],y50_m.index[3],y50_m.index[4],y50_m.index[5]])
y50_m = y50_m.fillna("carb")
y50_m.columns = ["nutr","m_min","m_max"]
y50_m = y50_m.set_index(["nutr"])
y50_m = y50_m.div(3)

y60_carb_new = pd.DataFrame(y60_m.iloc[2:6,:].mean(), index = ["min","max"]).transpose()
y60_m = y60_m.append(y60_carb_new)
y60_m = y60_m.drop([y60_m.index[2],y60_m.index[3],y60_m.index[4],y60_m.index[5]])
y60_m = y60_m.fillna("carb")
y60_m.columns = ["nutr","m_min","m_max"]
y60_m = y60_m.set_index(["nutr"])
y60_m = y60_m.div(3)

y70_carb_new = pd.DataFrame(y70_m.iloc[2:6,:].mean(), index = ["min","max"]).transpose()
y70_m = y70_m.append(y70_carb_new)
y70_m = y70_m.drop([y70_m.index[2],y70_m.index[3],y70_m.index[4],y70_m.index[5]])
y70_m = y70_m.fillna("carb")
y70_m.columns = ["nutr","m_min","m_max"]
y70_m = y70_m.set_index(["nutr"])
y70_m = y70_m.div(3)

y71_carb_new = pd.DataFrame(y71_m.iloc[2:6,:].mean(), index = ["min","max"]).transpose()
y71_m = y71_m.append(y71_carb_new)
y71_m = y71_m.drop([y71_m.index[2],y71_m.index[3],y71_m.index[4],y71_m.index[5]])
y71_m = y71_m.fillna("carb")
y71_m.columns = ["nutr","m_min","m_max"]
y71_m = y71_m.set_index(["nutr"])
y71_m = y71_m.div(3)

data = cur.execute("select * from data")
data = pd.DataFrame(data, columns =['id','p_name','cal','fat(g)','fat','carb','protein','sodium','quantity','unit','price','ptype_no','ptype','mor','aft','even'])

#data.head()

morning = data.loc[data['mor'] == 1]
afternoon = data.loc[data['aft'] == 1]
evening = data.loc[data['even'] == 1]

food_df = pd.DataFrame(data.iloc[:, [0,10]]).set_index(["id"])
#food_df

food_df1 = pd.DataFrame(morning.iloc[:, [0,10]]).set_index(["id"])
food_df2 = pd.DataFrame(afternoon.iloc[:, [0,10]]).set_index(["id"])
food_df3 = pd.DataFrame(evening.iloc[:, [0,10]]).set_index(["id"])

amt_df1 = pd.DataFrame(morning.iloc[:, [0,2,4,5,6,7]]).set_index(["id"])
amt_df2 = pd.DataFrame(afternoon.iloc[:, [0,2,4,5,6,7]]).set_index(["id"])
amt_df3 = pd.DataFrame(evening.iloc[:, [0,2,4,5,6,7]]).set_index(["id"])

#new input
while True :
    iter = input("Please enter # of day: ")
    try:
        iter = int(iter)
        if iter >= 1 and iter <= 10:
            break
        else:
            print("Invalid day. Please enter day between 1 and 10.")
    except ValueError:
        print("Invalid input. Please enter a # of day.")

while True :
    age = input("Please enter your age: ")
    try:
        age = int(age)
        if age > 0 and age <= 120:
            break
        else:
            print("Invalid age. Please enter an age between 0 and 120.")
    except ValueError:
        print("Invalid input. Please enter a valid age.")
name = input("What is your name? : ")
print("Hello " + name + "! To calculate your appropriate nutrition, PLEASE SUBMIT YOUR AGE AND YOUR GENER.")

gender = input("Please enter your sex (type 'm' or 'f' ): ")
while gender not in ['m', 'f']:
    gender = input("Invalid input. Please enter 'm' or 'f': ")

while True :
    pdf = input("Please enter your budget: ")
    try:
        pdf = int(pdf)
        if pdf >= 100 and pdf <= 1000:
            break
        else:
            print("Invalid budget. Please enter an budget between 100 and 500.")
    except ValueError:
        print("Invalid input. Please enter a valid budget.")

# Optimization model
i = 1
for i in range(i, iter+1) :
  print ("--------------------------- Day ", i, " ---------------------------")

  ampl.eval(
      r"""
      reset;
      option solver cplex;

      set nutr;
      set id;

      param price {id} > 0;
      param pdf >= 0;
      param m_min {nutr} >= 0;
      param m_max {i in nutr} >= m_min[i];

      param amt {nutr,id} >= 0;

      var Buy {j in id} integer >= 0;

      minimize Total_Cost:  sum {j in id} price[j] * Buy[j];

      subject to Diet {i in nutr}: m_min[i] <= sum {j in id} amt[i,j] * Buy[j] <= m_max[i];
      subject to const1 : sum {j in id} price[j] * Buy[j] <= pdf;""")

  # nutrition condition for male
  if gender == 'm' :
      if age <= 3 :
          ampl.set_data(y3_m, "nutr")
      elif age <= 5 :
          ampl.set_data(y5_m, "nutr")
      elif age <= 8 :
          ampl.set_data(y8_m, "nutr")
      elif age <= 12 :
          ampl.set_data(y12_m, "nutr")
      elif age <= 15 :
          ampl.set_data(y15_m, "nutr")
      elif age <= 18 :
          ampl.set_data(y18_m, "nutr")
      elif age <= 30 :
          ampl.set_data(y30_m, "nutr")
      elif age <= 50 :
          ampl.set_data(y50_m, "nutr")
      elif age <= 60 :
          ampl.set_data(y60_m, "nutr")
      elif age <= 70 :
          ampl.set_data(y70_m, "nutr")
      elif age >= 71 :
          ampl.set_data(y71_m, "nutr")

  # nutrition condition for female
  elif gender == 'fm' :
      if age <= 3 :
          ampl.set_data(y3_fm, "nutr")
      elif age <= 5 :
          ampl.set_data(y5_fm, "nutr")
      elif age <= 8 :
          ampl.set_data(y8_fm, "nutr")
      elif age <= 12 :
          ampl.set_data(y12_fm, "nutr")
      elif age <= 15 :
          ampl.set_data(y15_fm, "nutr")
      elif age <= 18 :
          ampl.set_data(y18_fm, "nutr")
      elif age <= 30 :
          ampl.set_data(y30_fm, "nutr")
      elif age <= 50 :
          ampl.set_data(y50_fm, "nutr")
      elif age <= 60 :
          ampl.set_data(y60_fm, "nutr")
      elif age <= 70 :
          ampl.set_data(y70_fm, "nutr")
      elif age >= 71 :
          ampl.set_data(y71_fm, "nutr")

  # Send the data from "amt_df" to AMPL and initialize the indexing set "FOOD"
  ampl.set_data(food_df1, "id")
  # Set the values for the parameter "amt" using "amt_df"
  ampl.get_parameter("amt").set_values(amt_df1.unstack())

  ampl.get_parameter("pdf").set_values([pdf])

  # Specify the solver to use (e.g., HiGHS)
  ampl.option["solver"] = "cplex"
  # Solve
  ampl.solve()
  # Stop if the model was not solved
  assert ampl.get_value("solve_result") == "solved"
  # Get objective entity by AMPL name
  totalcost = ampl.get_objective('Total_Cost')
  # Print it
  print("Objective is:", totalcost.value())

  print("---------------------------Breakfast---------------------------")
  b_values = ampl.get_variable('Buy').get_values()
  b_values = pd.DataFrame(b_values)
  b_values.columns = ['id', 'amount(unit)']
  result_n = b_values.loc[b_values['amount(unit)'] !=0]
  result = data.merge(result_n, on = ["id"],how = "inner" )
  result = pd.DataFrame(result.iloc[:, [1,2,4,5,6,7,16]])
  print(result.to_markdown(tablefmt="rst"))
  food_df1 = food_df1.drop(result_n['id'])
  amt_df1 = amt_df1.drop(result_n['id'])

  ampl.eval(
      r"""
      reset;
      option solver cplex;

      set nutr;
      set id;

      param price {id} > 0;
      param pdf >= 0;
      param m_min {nutr} >= 0;
      param m_max {i in nutr} >= m_min[i];

      param amt {nutr,id} >= 0;

      var Buy {j in id} integer >= 0;

      minimize Total_Cost:  sum {j in id} price[j] * Buy[j];

      subject to Diet {i in nutr}: m_min[i] <= sum {j in id} amt[i,j] * Buy[j] <= m_max[i];
      subject to const1 : sum {j in id} price[j] * Buy[j] <= pdf;""")

  # nutrition condition for male
  if gender == 'm' :
      if age <= 3 :
          ampl.set_data(y3_m, "nutr")
      elif age <= 5 :
          ampl.set_data(y5_m, "nutr")
      elif age <= 8 :
          ampl.set_data(y8_m, "nutr")
      elif age <= 12 :
          ampl.set_data(y12_m, "nutr")
      elif age <= 15 :
          ampl.set_data(y15_m, "nutr")
      elif age <= 18 :
          ampl.set_data(y18_m, "nutr")
      elif age <= 30 :
          ampl.set_data(y30_m, "nutr")
      elif age <= 50 :
          ampl.set_data(y50_m, "nutr")
      elif age <= 60 :
          ampl.set_data(y60_m, "nutr")
      elif age <= 70 :
          ampl.set_data(y70_m, "nutr")
      elif age >= 71 :
          ampl.set_data(y71_m, "nutr")

  # nutrition condition for female
  elif gender == 'fm' :
      if age <= 3 :
          ampl.set_data(y3_fm, "nutr")
      elif age <= 5 :
          ampl.set_data(y5_fm, "nutr")
      elif age <= 8 :
          ampl.set_data(y8_fm, "nutr")
      elif age <= 12 :
          ampl.set_data(y12_fm, "nutr")
      elif age <= 15 :
          ampl.set_data(y15_fm, "nutr")
      elif age <= 18 :
          ampl.set_data(y18_fm, "nutr")
      elif age <= 30 :
          ampl.set_data(y30_fm, "nutr")
      elif age <= 50 :
          ampl.set_data(y50_fm, "nutr")
      elif age <= 60 :
          ampl.set_data(y60_fm, "nutr")
      elif age <= 70 :
          ampl.set_data(y70_fm, "nutr")
      elif age >= 71 :
          ampl.set_data(y71_fm, "nutr")

  # Send the data from "amt_df" to AMPL and initialize the indexing set "FOOD"
  ampl.set_data(food_df2, "id")
  # Set the values for the parameter "amt" using "amt_df"
  ampl.get_parameter("amt").set_values(amt_df2.unstack())

  ampl.get_parameter("pdf").set_values([pdf])

  # Specify the solver to use
  ampl.option["solver"] = "cplex"
  # Solve
  ampl.solve()
  # Stop if the model was not solved
  assert ampl.get_value("solve_result") == "solved"
  # Get objective entity by AMPL name
  totalcost = ampl.get_objective('Total_Cost')
  # Print it
  print("Objective is:", totalcost.value())

  print("---------------------------Lunch---------------------------")
  b_values = ampl.get_variable('Buy').get_values()
  b_values = pd.DataFrame(b_values)
  b_values.columns = ['id', 'amount(unit)']
  result_n = b_values.loc[b_values['amount(unit)'] !=0]
  result = data.merge(result_n, on = ["id"],how = "inner" )
  result = pd.DataFrame(result.iloc[:, [1,2,4,5,6,7,16]])
  print(result.to_markdown(tablefmt="rst"))
  food_df2 = food_df2.drop(result_n['id'])
  amt_df2 = amt_df2.drop(result_n['id'])

  ampl.eval(
      r"""
      reset;
      option solver cplex;

      set nutr;
      set id;

      param price {id} > 0;
      param pdf >= 0;
      param m_min {nutr} >= 0;
      param m_max {i in nutr} >= m_min[i];

      param amt {nutr,id} >= 0;

      var Buy {j in id} integer >= 0;

      minimize Total_Cost:  sum {j in id} price[j] * Buy[j];

      subject to Diet {i in nutr}: m_min[i] <= sum {j in id} amt[i,j] * Buy[j] <= m_max[i];
      subject to const1 : sum {j in id} price[j] * Buy[j] <= pdf;""")

  # nutrition condition for male
  if gender == 'm' :
      if age <= 3 :
          ampl.set_data(y3_m, "nutr")
      elif age <= 5 :
          ampl.set_data(y5_m, "nutr")
      elif age <= 8 :
          ampl.set_data(y8_m, "nutr")
      elif age <= 12 :
          ampl.set_data(y12_m, "nutr")
      elif age <= 15 :
          ampl.set_data(y15_m, "nutr")
      elif age <= 18 :
          ampl.set_data(y18_m, "nutr")
      elif age <= 30 :
          ampl.set_data(y30_m, "nutr")
      elif age <= 50 :
          ampl.set_data(y50_m, "nutr")
      elif age <= 60 :
          ampl.set_data(y60_m, "nutr")
      elif age <= 70 :
          ampl.set_data(y70_m, "nutr")
      elif age >= 71 :
          ampl.set_data(y71_m, "nutr")

  # nutrition condition for female
  elif gender == 'fm' :
      if age <= 3 :
          ampl.set_data(y3_fm, "nutr")
      elif age <= 5 :
          ampl.set_data(y5_fm, "nutr")
      elif age <= 8 :
          ampl.set_data(y8_fm, "nutr")
      elif age <= 12 :
          ampl.set_data(y12_fm, "nutr")
      elif age <= 15 :
          ampl.set_data(y15_fm, "nutr")
      elif age <= 18 :
          ampl.set_data(y18_fm, "nutr")
      elif age <= 30 :
          ampl.set_data(y30_fm, "nutr")
      elif age <= 50 :
          ampl.set_data(y50_fm, "nutr")
      elif age <= 60 :
          ampl.set_data(y60_fm, "nutr")
      elif age <= 70 :
          ampl.set_data(y70_fm, "nutr")
      elif age >= 71 :
          ampl.set_data(y71_fm, "nutr")

  # Send the data from "amt_df" to AMPL and initialize the indexing set "FOOD"
  ampl.set_data(food_df3, "id")
  # Set the values for the parameter "amt" using "amt_df"
  ampl.get_parameter("amt").set_values(amt_df3.unstack())

  ampl.get_parameter("pdf").set_values([pdf])

  # Specify the solver to use
  ampl.option["solver"] = "cplex"
  # Solve
  ampl.solve()
  # Stop if the model was not solved
  assert ampl.get_value("solve_result") == "solved"
  # Get objective entity by AMPL name
  totalcost = ampl.get_objective('Total_Cost')
  # Print it
  print("Objective is:", totalcost.value())

  print("---------------------------Dinner---------------------------")
  b_values = ampl.get_variable('Buy').get_values()
  b_values = pd.DataFrame(b_values)
  b_values.columns = ['id', 'amount(unit)']
  result_n = b_values.loc[b_values['amount(unit)'] !=0]
  result = data.merge(result_n, on = ["id"],how = "inner" )
  result = pd.DataFrame(result.iloc[:, [1,2,4,5,6,7,16]])
  print(result.to_markdown(tablefmt="rst"))
  food_df3 = food_df3.drop(result_n['id'])
  amt_df3 = amt_df3.drop(result_n['id'])