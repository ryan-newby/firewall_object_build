import dns.resolver
import csv

class BuildData:
  
  def __init__(self):
    self.description = "Build lists of hostnames, host IPs, dictionary of both"
    
  def create_list(self, csv_in):
    swap_list_2 = []
    with open(csv_in, newline='') as f:
      reader = csv.reader(f)
      swap_list_1 = list(reader)
      for i in swap_list_1:
        swap_list_2.append(i[0])
    return swap_list_2
 
  def create_ip_list(self, host_list):
    ip_list = []
    for i in host_list:
      result = dns.resolver.resolve(i, 'A')
      for val in result:
        ip_list.append(val.to_text())
    return ip_list
    
  def combine_host_ip(self, host_list, ip_list):
    host_ip_dict = {host_list[i]: ip_list[i] for i in range(len(host_list))}
    return host_ip_dict