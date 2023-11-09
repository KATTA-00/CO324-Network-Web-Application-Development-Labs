# import modules
from urllib import request

# HTTP GET request for http://eng.pdn.ac.lk
response = request.urlopen("http://eng.pdn.ac.lk")

# 1). a.
print("Status code: ", response.getcode())

# get the header and body
headers = response.headers
body = response.read()

# 1). b.
print(headers["Server"])

# 1). c.
print(len(body))

# 1). d.
print(type(body))

response.close()