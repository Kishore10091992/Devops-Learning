log = "192.168.1.10 connected successfully"

result = log.split() # ['192.168.1.10', 'connected', 'successfully']

ip = result[0]

status = result[1]

output = result[2]

print(f"your system is connected to {ip}")

print(f"And you system status is {status}")

print(f"so finally you system connected {output}")