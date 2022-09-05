# SPDX-License-Identifier: MIT

import json
import logging
import sys
from os.path import dirname

from drain3 import TemplateMiner
from drain3.template_miner_config import TemplateMinerConfig

import csv
import codecs

# persistence_type = "NONE"
# persistence_type = "REDIS"
# persistence_type = "KAFKA"
persistence_type = "FILE"

logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(message)s')

if persistence_type == "KAFKA":
    from drain3.kafka_persistence import KafkaPersistence

    persistence = KafkaPersistence("drain3_state", bootstrap_servers="localhost:9092")

elif persistence_type == "FILE":
    from drain3.file_persistence import FilePersistence

    persistence = FilePersistence("drain3_state.bin")

elif persistence_type == "REDIS":
    from drain3.redis_persistence import RedisPersistence

    persistence = RedisPersistence(redis_host='',
                                   redis_port=25061,
                                   redis_db=0,
                                   redis_pass='',
                                   is_ssl=True,
                                   redis_key="drain3_state_key")
else:
    persistence = None

config = TemplateMinerConfig()
config.load(dirname(__file__) + "/drain3.ini")
config.profiling_enabled = False

template_miner = TemplateMiner(persistence, config)
print(f"Drain3 started with '{persistence_type}' persistence")
print(f"{len(config.masking_instructions)} masking instructions are in use")
print(f"Starting training mode. Reading from std-in ('q' to finish)")

# 读文件
in_log_file = "HDFS.log"
path = "F:\LogAnomalyDetection\Log_Parse_Drain3\examples\Parsed"

# 打开CSV文件
csvfile = open(path + '.csv', 'w', newline='')  # python3下
writer = csv.writer(csvfile, delimiter=',')

while True:
    with open(in_log_file) as f:
        lines = f.readlines()

    Flag = True
    # https://blog.csdn.net/qq_23926575/article/details/72788485

    dic = json.loads(result_json)
    keys = list(dic.keys())
    print(keys)
    writer.writerow(keys)
    # 遍历日志文件
    for line in lines:
        result = template_miner.add_log_message(line)
        print(result)
        result_json = json.dumps(result)
        # print(result_json)
        template = result["template_mined"]
        params = template_miner.extract_parameters(template, line)
        # print("Parameters: " + str(params))

        dic = json.loads(line)

        # 读取json数据的每一行，将values数据一次一行的写入csv中
        writer.writerow(list(dic.values()))






print("Training done. Mined clusters:")
for cluster in template_miner.drain.clusters:
    print(cluster)

print(f"Starting inference mode, matching to pre-trained clusters. Input log lines or 'q' to finish")
while True:
    log_line = input("> ")
    if log_line == 'q':
        break
    cluster = template_miner.match(log_line)
    if cluster is None:
        print(f"No match found")
    else:
        template = cluster.get_template()
        print(f"Matched template #{cluster.cluster_id}: {template}")
        print(f"Parameters: {template_miner.get_parameter_list(template, log_line)}")
