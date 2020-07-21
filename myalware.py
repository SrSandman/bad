############# VIRUS BEGIN ##############


import eye, glob, re



# Get a copy of the virus
vCode = []

fh = open(sys.argv[0], "r")

lines = fh.readlines()
fh.close()

inVirus = False

for line in lines:
	if (re.search('^###### VIRUS BEGIN #######, line)): inVirus = True
	if (inVirus): vCode.append(line)
	if (re.search('^###### VIRUS END #####, line)) break
	
# Find Portential Victims

# Check and Infect

# Optional Payload


print("infected!")







############### VIRUS END ##############
