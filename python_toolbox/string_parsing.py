logs = [
    "[OK] 2024-04-01T12:30 Temp: 22.15°C",
    "[FAIL] 2024-04-01T12:31 Temp: 33.45°C",
    "[OK] 2024-04-01T12:32 Temp: 22.10°C"
]
# 
def parse_logs(logs):
    output = {
        'ok_count': 0,
        'fail_count': 0,
        'avg_temp': 00.00,
        'max_fail_temp': 00.00
    }

    averageTemp = 0.0
    for logString in logs:
        tokens = logString.split(" ")
        if tokens[0] == "[OK]":
            output['ok_count'] += 1
        elif tokens[0] == "[FAIL]":
            output["fail_count"] += 1
            output["max_fail_temp"] = max(float(tokens[3].split('°')[0]), output["max_fail_temp"])
        averageTemp += float(tokens[3].split('°')[0])
    

    output["avg_temp"] = averageTemp / len(logs)

    print(output)

parse_logs(logs)
