# %%
from prisma import Prisma
import os 

# %%

print(os.environ.get('DATABASE_URL'))

# %%


db = Prisma(
        datasource={
            'url': 'postgresql://postgres:baylek@2024@15.188.94.127:5432/dev?scheme=public',
        }
    )
db.connect()

posts = db.doctors.find_many()

db.disconnect()
print(posts)