# Import your libraries
import pandas as pd

# Start writing code
March=3
orders['year']=orders['order_date'].dt.year
orders['month']=orders['order_date'].dt.month

march_orders=orders[(orders['year']==2019) & (orders['month']==March)]
final_result=march_orders.groupby(['cust_id']).sum().reset_index()[['cust_id','total_order_cost']]
final_result.sort_values(['total_order_cost'],ascending=False)