# Import your libraries
import pandas as pd

# Start writing code
sf_transactions['month']=sf_transactions['created_at'].dt.month
date_formatted=sf_transactions['created_at'].dt.strftime('%Y-%m')
sf_transactions['date']=date_formatted
month_rev=sf_transactions.groupby(['date']).sum().reset_index()[['date','value']]

month_rev['value_diff']=month_rev['value'].diff()
month_rev['last_month_rev']=month_rev['value']-month_rev['value_diff']
month_rev['perc_change']=(month_rev['value_diff']/month_rev['last_month_rev'])*100
month_rev['perc_change']=month_rev['perc_change'].round(2)
month_rev[['date','perc_change']]