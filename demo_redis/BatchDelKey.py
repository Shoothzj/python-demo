from rediscluster import RedisCluster

startup_nodes = [{"host": "127.0.0.1", "port": "7000"}]
password = ""
keyPrefix = ""

rc = RedisCluster(startup_nodes=startup_nodes, password=password, skip_full_coverage_check=True, decode_responses=True)

file = open("sample.txt")
readlines = file.readlines()

for line in readlines:
    key = keyPrefix + line[:-1]
    print("del key " + key)
    print("end")
    if len(key) > 10:
        rc.delete(key)
