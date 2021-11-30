
debug = False
def get_prefix(n) -> int:
  return "".join([get_binarybyte_str(i) for i in n.split(".")]).count("1")

def get_wildcard(n) -> str:
  return ".".join([get_binarybyte_str(i).replace("1","!").replace("0","1").replace("!","0") for i in n.split(".")])

def get_broadcast(anet, n) -> str:
  wild = get_wildcard(n)
  _result = []
  _binary = []
  for i in range(len(anet.split("."))):
    _net, _mask, _wild = get_binarybyte_str(anet.split(".")[i]), get_binarybyte_str(n.split(".")[i]), wild.split(".")[i]
    _binary.append("".join([_net[j] if _wild[j] == "0" else "1" for j in range(len(_wild))]))
    _result.append(str(int(_binary[-1], 2)))
  if debug:
    print("Binary broadcast:", _binary)
  return ".".join(_result)    

def get_number_of_hosts(prefix: int) -> int:
  return 2 ** (32 - prefix) - 2

def get_binarybyte_str(num: str) -> str:
  # return binary representation of a byte as a string
  return bin(int(num))[2:].zfill(8)

def get_network_address(a, n) -> str:
  _result = []
  _binary = []
  for i in range(len(a.split("."))):
    abyte = get_binarybyte_str(a.split(".")[i])
    _netbyte = get_binarybyte_str(n.split(".")[i])
    _binary.append("".join([str(int(abyte[i])&int(_netbyte[i]))for i in range(len(abyte))]))
    _result.append(str(int(_binary[-1], 2)))
  if debug:
    print("Binary network address:", _binary)
  return ".".join(_result)

def get_first_IP(net_address: str) -> str:
  _result = net_address.split(".")[:3]
  _result.append(str(int(net_address.split(".")[-1])+1))
  return ".".join(_result)

def get_last_IP(net_address: str) -> str:
  _result = net_address.split(".")[:3]
  _result.append(str(int(net_address.split(".")[-1])-1))
  return ".".join(_result)
