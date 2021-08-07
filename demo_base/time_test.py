import datetime
import time

# time ns
time_ns = time.time_ns()
print(time_ns)
print(type(time_ns))

# time ms
time_ms = time_ns // 1000_000
print(time_ms)
print(type(time_ms))

# time seconds
time_sec = time_ms // 1000
print(time_sec)
print(type(time_sec))

timestamp = datetime.datetime.fromtimestamp(time_ns / 1e9)

print(timestamp.year)
print(type(timestamp.year))
print(type(timestamp.month))