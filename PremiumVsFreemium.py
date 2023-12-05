# Import your libraries
import pandas as pd

# Start writing code
ms_user_dimension.head()
df_all=ms_user_dimension.merge(ms_acc_dimension,on='acc_id').merge(ms_download_facts,on='user_id')
df_all['paid']=df_all['downloads']
df_all['unpaid']=df_all['downloads']
df_all.loc[df_all['paying_customer']=='no','paid']=0
df_all.loc[df_all['paying_customer']=='yes','unpaid']=0
daily_values=df_all.groupby('date').sum().reset_index()[['date','paid','unpaid']]
final=daily_values[daily_values['paid']<daily_values['unpaid']]
final