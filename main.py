import sys
import os

input_str = sys.argv[1]

args = input_str.split('-')

def print_default():
  print("ssh-[l]-[local bind]-[remote ip]-[remote port]-[config item]")
  print("ssh-[r]-[remote port]-[local ip]-[local port]-[config item]")
  print("ssh-[d]-[local bind]-[config item]")

def on_arg_error():
  print_default()
  os.system('pause')
  exit(1)

if (len(args) < 1):
  on_arg_error()

arg0 = args[0]
if arg0 != 'ssh':
  on_arg_error()

arg1 = args[1]
command = ""
if arg1 == 'l' and len(args) >= 6:
  command = "-NL %s:%s:%s %s" % (args[2],args[3],args[4],args[5])
elif arg1 == 'r' and len(args) >= 6:
  command = "-NR %s:%s:%s %s" % (args[2],args[3],args[4],args[5])
elif arg1 == 'd' and len(args) >= 4:
  command = "-ND %s %s" % (args[2],args[3])
else:
  on_arg_error()

config = '-o ExitOnForwardFailure=yes '

command = 'ssh ' + config + command
print(command)

while True:
  os.system(command)
  os.system('timeout 3')
