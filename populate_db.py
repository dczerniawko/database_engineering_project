# Script from: https://towardsdatascience.com/generating-random-data-into-a-database-using-python-fd2f7d54024e
# Generating Random Data into a Database Using Python
# Populating a MySQL Database with Dummy Data using Pandas
# Jordan Williams
# Oct 19, 2020

import pandas as pd
import sys
from faker import Faker
from collections import defaultdict
from sqlalchemy import create_engine

fake = Faker()
fake_data = defaultdict(list)

records_number = int(sys.argv[1])
for _ in range(records_number):
    fake_data["first_name"].append( fake.first_name() )
    fake_data["last_name"].append( fake.last_name() )
    fake_data["occupation"].append( fake.job() )
    fake_data["dob"].append( fake.date_of_birth() )
    fake_data["country"].append( fake.country() )

df_fake_data = pd.DataFrame(fake_data)

engine = create_engine('mysql://user:password@mysql:3306/database', echo=False)
df_fake_data.to_sql('user', con=engine, index=False)
