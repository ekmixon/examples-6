#!/usr/bin/env python

# Dynamically create the login.properties file used by the Hash Login service
# Creates a file in /tmp/login.properties

import os;

configfile = "../config/local-demo.env"
with open (configfile, "r") as fileHandler:
  login_properties = "/tmp/login.properties"
  if os.path.exists (login_properties):
    os.remove(login_properties)
  loginfile = open (login_properties, "w")

  # Get list of all lines in file
  listOfLines = fileHandler.readlines()

for line in listOfLines:
  if line.startswith("USER_"):
    line = line[5:]
    line = line.rstrip()
    user,username = line.split("=", 1)
    loginfile.write(f"{username}:{username}" + "1\n")

loginfile.close()
