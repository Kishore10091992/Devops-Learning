# parse log entry

log = "2026-07-08 INFO Application Started"

result = log.split()

print(result)

date = result[0]

level = result[1]

print(date)

print(level)