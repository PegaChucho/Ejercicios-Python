res = []
with open("ejercicio 1", "r") as infile:
    for line in infile:                        # Iterate each line 
        val = line.split()                     # Split line by space
        res.append( str(120.000000) )  # Use negative index to get last element and divide.

with open(filename, "w") as outfile:          #Open file to write
    for line in res:
        outfile.write(line+"\n")              #Write Data