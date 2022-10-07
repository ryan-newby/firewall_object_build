class BuildASA:
        def __init__(self):
            self.description = "Build Cisco ASA Objects"
        
        def build_objects(self, host_ip_dict):
            print("\n")
            for key, value in host_ip_dict.items():
                print("object-group network " + key)
                print("network-object host " + value)
                
            print("\n")