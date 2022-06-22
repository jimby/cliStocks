from datetime import datetime

# date_string = "21 June, 2018"
# date_string = "1 June, 2018"
date_string = "1/6/2022"

print("date_string =", date_string)
print("type of date_string =", type(date_string))

# date_object = datetime.strptime(date_string, "%d %B, %Y")
date_object = datetime.strptime(date_string, "%m/%d/%Y")

print("date_object =", date_object)
print("type of date_object =", type(date_object))
