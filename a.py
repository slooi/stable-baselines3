import datetime

print("_".join(str(datetime.datetime.now()).replace(":","-").split(".")[0].split(" ")))