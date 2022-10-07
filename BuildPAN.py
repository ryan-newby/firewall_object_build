class BuildPAN:
    
    def __init__(self):
        self.description = "Build Palo Alto Objects"
    
    def build_objects(self, host_ip_dict):
        print("\n")
        for value in host_ip_dict.values():
            print("set shared address ip-" + value + " ip-netmask " + value + "/32")
        print("\n")
        for key, value in host_ip_dict.items():
            print("set shared address-group " + key + " static [ ip-" + value + " ]" )
        print("\n")