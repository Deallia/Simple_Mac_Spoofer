import subprocess
import optparse




parser = optparse.OptionParser() 
parser.add_option( "--interface", dest="interface")
parser.add_option( "--mac", dest="mac")
(options, args) = parser.parse_args()

subprocess.call(f"ifconfig {options.interface} down", shell=True)
subprocess.call(f"ifconfig {options.interface} hw ether {options.mac}", shell=True)
subprocess.call(f"ifconfig {options.interface} up", shell=True)
