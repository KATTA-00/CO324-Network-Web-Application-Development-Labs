from urllib import request

response = request.urlopen("http://eng.pdn.ac.lk")

body = response.read()

print(body)

response.close()