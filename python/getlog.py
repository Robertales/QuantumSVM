#!C:\Users\Gennaro\Miniconda3\envs\python\python.exe
#print("Content-Type: text/html\n")

from datetime import datetime


# datetime object containing current date and time
dataora = datetime.now()

# dd/mm/YY H:M:S
dt_string = dataora.strftime("%d/%m/%Y %H:%M:%S")
print("\n", dt_string)
print("\n")

file1 = open('C:/xampp/htdocs/quantumKNN/log/log.txt',"a")

file1.write(dt_string + "\n")
file1.close()