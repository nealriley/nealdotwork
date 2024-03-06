import datetime

# Get the current date and time
now = datetime.datetime.now()

# Format the date and time as a string in the format YYYY-MM-DD_HH-MM-SS
# Insert file in the folder 'material'
filename='material/'+now.strftime("%Y-%m-%d_%H-%M-%S.md")

# Create and open the file for writing
with open(filename, 'w') as file:
    file.write(f'''---
title: 
prompt: 
---''')