# Import your libraries
import pandas as pd

# Start writing code
airbnb_key_details=airbnb_search_details[['city','property_type','bedrooms','bathrooms']]
property_avergaes=airbnb_key_details.groupby(['city','property_type']).mean().reset_index()
property_avergaes