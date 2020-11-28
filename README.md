```python
from gitdatabase.client import Client

# establish connection
client = Client('github.com/mirrorhanyu/test-database.git', username, password)

# to insert into collection within database
client.table.insert_one({
    'title': 'GitDatabase works!'
})

# to query with certain 
for record in client.table.find({'title': 'GitDatabase works!'}):
    print(record)
```
