#!/usr/bin/python

from omekaclient import OmekaClient

client = OmekaClient("http://localhost/omeka/api", "fd11f6fdcdcd2f524555b089790824ede6d27cff")

# GET /items/:id
response, content = client.get("items", id=1)

# GET /items
#response, content = client.get("items")

# POST /items
#response, content = client.post("items", data='{"public":true}')

# PUT /items/:id
#response, content = client.put("items", 1, data='{"public":false}')

# DELETE /items/:id
#response, content = client.delete("items", 1)

print response, content
