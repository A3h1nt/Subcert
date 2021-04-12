import requests
import eventlet
import json
import secrets
import sys
from colorama import Fore
import re
import pyfiglet
import socket
import argparse


outputfile = ''
domain_name = False

parser = argparse.ArgumentParser()
parser.add_argument('-d','--domain', required=True, help="Domain to query", type=str)
parser.add_argument('-o','--output', help="Output file name", type=str)

args = parser.parse_args()

domain_name = args.domain
outputfile = args.output

regex = "^((?!-)[A-Za-z0-9-]"+"{1,63}(?<!-)\\.)"+"+[A-Za-z]{2,6}"

# Compile the ReGex
p = re.compile(regex)

if (re.search(p,domain_name)):
        print(Fore.BLUE+"=========================================================")
        banner=pyfiglet.figlet_format("SUBCERT", font = "cyberlarge"  )
        print(Fore.WHITE+banner)
        print("                                            by: A3h1nt")
        print(Fore.BLUE+"========================================================="+Fore.WHITE)
else:
        print("Invalid Domain Name")
        sys.exit(0)


user_agents = []
user_agents.append('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko)')
user_agents.append('Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko')
user_agents.append('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36')
user_agents.append('Mozilla/5.0 (X11; CrOS armv7l 12105.100.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.144 Safari/537.36')


#creafting the URL
url = "https://crt.sh/?q="+domain_name+"&output=json"
headers = {}
headers['User-Agent']=secrets.choice(user_agents)

resp = requests.get(url,headers=headers)
resp=resp.text
site_json=json.loads(resp)



if len(site_json) < 2:
  print("\n["+Fore.RED+"*"+Fore.WHITE+"] " +"No Results Found \n")
  sys.exit(0)

#some empty lists to work with
first_list=[]
temp_list=[]
temp2_list=[]
temp3_list=[]
final_list=[]

# Getting the URL's and appending them to a list
for i in site_json:
  name=str(i['name_value'])
  first_list.append(name)
  # Removing the duplicates
  for j in first_list:
    if j not in temp_list:
      temp_list.append(j)

# Splitting up the pairs on the basis of new line character
# some results are like ['example.com','admin.example.com\nblog.example.com']
for k in range(len(temp_list)):
  a=temp_list[k]
  b=a.split('\n')
  temp2_list.append(b)


# Removing nested lists
def remove_nested(temp2_list):
  for i in temp2_list:
    if type(i) == list:
      remove_nested(i)
    else:
      temp3_list.append(i)

remove_nested(temp2_list)

# Removing duplicates from the new list
for i in temp3_list:
  if i not in final_list:
    final_list.append(i)

ip=''
if outputfile:
  f = open(outputfile, "a+" )
#Printing out stuff
with eventlet.Timeout(10):
  for i in final_list:
    try:
      if (re.search(p,i)):
        ip=socket.gethostbyname(i)
        if not ip:
          continue
        else:
          print(" ["+Fore.GREEN+"*"+Fore.WHITE+"] " +str(ip)+ "   -   " + str(i))
          if outputfile:
            f.write(str(i) + "\n")
    except:
          ''' this print statement is optional, you can uncomment this to display the subdomains even if there's an exception '''
          #print(" ["+Fore.GREEN+"*"+Fore.WHITE+"] " +str(ip)+ "   -   www." + str(i))
          continue
if outputfile:
  f.close()
