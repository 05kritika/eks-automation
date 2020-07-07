#import boto3
import sys
from subprocess import call
from subprocess import check_output

#if len(sys.argv) != 3:
#    print "Error wrong parameter number"
#    print "Usage: python installhelm.py install"
#    print "Example: python installhelm.py install"
#    sys.exit(1)

#install = sys.argv[1]
#delete = sys.argv[2]

if helm == "yes":
    "curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3"
    "chmod 700 get_helm.sh"
    "./get_helm.sh"
    "helm version"
else
     "exit"
fi

#mycommands = ["helm"]

#if install == "True":
#    mycommands.extend(["install", ""])
  #  exit
#else 
#    mycommands.extend(["apply","-auto-approve"])
#elif apply=="True":
#    mycommands.extend(["apply","-auto-approve"])
#else:
#    exit

#mycommands.extend([ "-var", "region="+myregion , "-var", "prefix="+prefix])
#mycommands.extend([ "-var", "region="+myregion])

#print mycommands
#call(mycommands
