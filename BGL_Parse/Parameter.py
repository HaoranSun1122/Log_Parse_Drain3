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

# 读文件
in_log_file = "BGL.log"
path = "F:\LogAnomalyDetection\Log_Parse_Drain3\BGL_Parse\Parsed_Parameter"

# 打开CSV文件

csvfile = open(path + '.csv', 'w', newline='')  # python3下
writer = csv.writer(csvfile, delimiter=',')

while True:
    with open(in_log_file) as f:
        lines = f.readlines()


    # 遍历日志文件

    for line in lines:
        result = template_miner.add_log_message(line)
        result_json = json.dumps(result)
        dic = json.loads(result_json)
        template = result["template_mined"]
        params = template_miner.extract_parameters(template, line)
        print(params)
        writer.writerow(params)
        Parameter_List = []
        Parameter_Str = ''
        for i in range(len(params)):
            print(list(params[i]))
            # print(str(list(params[i])).replace('[', '').replace(']', '').replace("'", "").replace('"', '').split(', '))
            # Parameter_List = Parameter_List + str(list(params[i])).replace('[', '').replace(']', '').replace("'", "").replace('"', '').split(', ')
            # 此处修改为str
            # Parameter_Str = Parameter_Str + str(list(params[i])).replace('[', '').replace(']', '').replace("'", "").replace('"', '') + ", "
            # Parameter_List.append(str(list(params[i])).replace('[', '').replace(']', '').replace("'", "").replace('"', ''))
        # Parameter_Str = Parameter_Str[:-2]
        # Parameter_List.append(Parameter_Str)
        print(Parameter_List)
        # writer.writerow(Parameter_List)
        # print(Parameter_Str)
        print(Parameter_List)
        print("------------------------------------------")


    #     解析字符串，把“去掉之后，然后把后面的删掉
