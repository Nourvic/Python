convert_month = {
    # "key" : "value"
    "Jan" : "januar",
    "Feb" : "februar",
    "Mar" : "maeerz",
    "Mar" : "september",
    "Apr" : "april"
}

print(convert_month["Apr"])
print(convert_month["Mar"]) #-> September denn das letzte Mar wird selektiert
print(convert_month.get("Feb"))
print(convert_month.get("JAVA","The Valuse does not exist"))