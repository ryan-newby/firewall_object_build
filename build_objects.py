from BuildASA import BuildASA
from BuildSRX import BuildSRX
from BuildPAN import BuildPAN
from BuildData import BuildData

enum_pan = BuildPAN()
enum_srx = BuildSRX()
enum_asa = BuildASA()
enum_obj = BuildData()

def main():
  #Input CSV containing hostnames which will be resolved to IP addresses
  user_input = input("Absolute path to CSV file for input: \n")
  host_list = enum_obj.create_list(user_input)
  ip_list = enum_obj.create_ip_list(host_list)

  # Dictionary with hostnames and associated A records
  host_ip_dict = enum_obj.combine_host_ip(host_list, ip_list)
  print(host_ip_dict)

  # Create firewall Objects
  enum_pan.build_objects(host_ip_dict)
  enum_srx.build_objects(host_ip_dict)
  enum_asa.build_objects(host_ip_dict)

main()