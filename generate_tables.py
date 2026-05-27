import pandas as pd
import numpy as np
import random
from sqlalchemy import create_engine

random.seed(42)
engine = create_engine('mysql+pymysql://root:Sneha%40123@127.0.0.1/hr_analytics_db')

emp_ids = pd.read_sql('SELECT emp_id, status, exit_date FROM employees', engine)

exited = emp_ids[emp_ids['status'] == 'Exited']
attrition = pd.DataFrame({
    'emp_id'        : exited['emp_id'].values,
    'reason'        : random.choices(['Better Salary', 'better salary', 'Growth', 'Personal', 'Relocation'], k=len(exited)),
    'tenure_months' : [random.randint(1, 60) for _ in range(len(exited))],
    'exit_date'     : exited['exit_date'].values
})
attrition.to_sql('attrition', engine, if_exists='replace', index=False)
print(f" Attrition — {len(attrition)} rows")

sales = []
for emp_id in random.choices(emp_ids['emp_id'].tolist(), k=3000):
    target = round(random.uniform(80000, 200000), -2)
    sales.append({
        'emp_id'          : emp_id,
        'month'           : random.randint(1, 12),
        'year'            : random.randint(2022, 2024),
        'target'          : target,
        'achieved'        : round(random.uniform(50000, 210000), -2),
    })
df_sales = pd.DataFrame(sales)
df_sales['achievement_pct'] = round((df_sales['achieved'] / df_sales['target']) * 100, 2)
df_sales.loc[df_sales.sample(frac=0.03).index, 'achieved'] = np.nan 
df_sales.to_sql('sales_performance', engine, if_exists='replace', index=False)
print(f" Sales — {len(df_sales)} rows")

productivity = []
for emp_id in random.choices(emp_ids['emp_id'].tolist(), k=4000):
    calls = random.randint(20, 200)
    productivity.append({
        'emp_id'         : emp_id,
        'month'          : random.randint(1, 12),
        'year'           : random.randint(2022, 2024),
        'calls_made'     : calls,
        'deals_closed'   : random.randint(0, min(calls, 40)),
        'training_hours' : random.randint(0, 20),
    })
pd.DataFrame(productivity).to_sql('productivity', engine, if_exists='replace', index=False)
print(f" Productivity — {len(productivity)} rows")

headcount = []
for dept in ['Sales', 'HR', 'Finance', 'Operations', 'Marketing']:
    for year in [2022, 2023, 2024]:
        for month in range(1, 13):
            headcount.append({
                'department'  : dept,
                'month'       : month,
                'year'        : year,
                'total'       : random.randint(80, 300),
                'new_joiners' : random.randint(2, 20),
                'exits'       : random.randint(1, 15)
            })
pd.DataFrame(headcount).to_sql('headcount', engine, if_exists='replace', index=False)
print(f" Headcount — {len(headcount)} rows")