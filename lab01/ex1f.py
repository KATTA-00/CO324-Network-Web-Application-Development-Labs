from urllib import request

# 1). f.
# for URL, http://eng.pdn.ac.lk/unknown

response = request.urlopen("http://eng.pdn.ac.lk/unknown")

body = response.read()

response.close()

# for URL, http://unknown.pdn.ac.lk

response = request.urlopen("http://unknown.pdn.ac.lk")

body = response.read()

response.close()

