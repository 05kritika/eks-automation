#import boto3
import sys
from subprocess import call
from subprocess import check_output

if len(sys.argv) != 5:
    print "Error wrong parameter number"
    print "Usage: python runterraform.py region prefix apply destroy"
    print "Example: python runterraform.py us-east-1 peppetest1 True False"
    sys.exit(1)

myregion = sys.argv[1]
prefix = sys.argv[2]
Apply = sys.argv[3]
Destroy = sys.argv[4]

mycommands = ["terraform"]

if destroy == "True":
    mycommands.extend(["destroy","--force"])
  #  exit
#else 
#    mycommands.extend(["apply","-auto-approve"])
elif apply=="True":
    mycommands.extend(["apply","-auto-approve"])
else:
    exit

mycommands.extend([ "-var", "region="+myregion , "-var", "prefix="+prefix])
#mycommands.extend([ "-var", "region="+myregion])

print mycommands
call(mycommands)
