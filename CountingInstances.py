# Import your libraries
import pandas as pd
import re

# Start writing code
gfs=google_file_store
gfs['bull']=gfs['contents'].apply(lambda text: len(re.findall(r'\bbull\b',text)))
gfs['bear']=gfs['contents'].apply(lambda text: len(re.findall(r'\bbear\b',text)))
gfs[['bull','bear']].sum().reset_index()