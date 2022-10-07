class BuildSRX:
        def __init__(self):
            self.description = "Build Juniper SRX Objects"
        
        def build_objects(self, host_ip_dict):
            print("\n")
            for value in host_ip_dict.values():
                print("set security address-book global address ip-" + value + " " + value + "/32")
            print("\n")
            for key, value in host_ip_dict.items():
                print("set security address-book global address-set " + key + " ip-" + value)
            print("\n")