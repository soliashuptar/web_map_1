adr = str(input("Enter IP-adress: "))
mask = str(input("Enter mask: "))

# adr = "67.038.173.245"
# mask = "255.255.240.0"

adr = adr.split(".")
mask = mask.split(".")

net = []
vuz = []

for n1, n2 in zip(adr, mask):
    n3 = int(n1) & int(n2)
    net.append(str(n3))

net = ".".join(net)

for n1, n2 in zip(adr, mask):
    n3 = int(n1) & ((int(n2) * -1) - 1)
    vuz.append(str(n3))

vuz = ".".join(vuz)

print("Network number: ",net)
print("Nomer vuzla: ",vuz)