# Exercise 9:

# Write a Python program to get the users environment.

import os
import pprint
# User's environment variables
u_env_var = os.environ
print("User's Environment variable:")
pprint.pprint(dict(u_env_var), width = 1)