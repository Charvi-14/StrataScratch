
import pandas as pd
sorted_salaries=ms_employee_salary.sort_values(['salary'],ascending=False)

current_salaries=sorted_salaries.drop_duplicates(['id'])
result=current_salaries.sort_values(['id'])
print(result)