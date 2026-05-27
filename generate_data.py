import pandas as pd
import numpy as np
from faker import Faker
import random
from sqlalchemy import create_engine

fake = Faker('en_IN')
random.seed(42)

engine = create_engine('mysql+pymysql://root:Sneha%40123@127.0.0.1/hr_analytics_db')

departments = ['Sales', 'sales', 'HR', 'Finance', 'Operations']
regions = ['North', 'South', 'East', 'West']
roles = ['Executive', 'Team Lead', 'Manager', 'Senior Manager']
employees = []
for i in range(1, 5001):
    joined = fake.date_between(start_date='-5y', end_date='-3m')
    exited = random.random() < 0.22       
    employees.append({
        'emp_id'      : f'EMP{i:04d}',
        'name'        : fake.name(),
        'department'  : random.choice(departments),
        'region'      : random.choice(regions),
        'job_role'    : random.choice(roles),
        'joining_date': joined,
        'exit_date'   : fake.date_between(start_date=joined, end_date='today') if exited else None,
        'status'      : 'Exited' if exited else 'Active',
        'age'         : random.randint(21, 52),
        'salary'      : round(random.gauss(55000, 18000), -2)
    })

df = pd.DataFrame(employees)
df.loc[df.sample(frac=0.04).index, 'salary'] = np.nan  
df.to_sql('employees', engine, if_exists='replace', index=False)
print(f"Done — {len(df)} rows inserted")