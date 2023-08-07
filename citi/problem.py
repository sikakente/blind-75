# You need to write

# cluster id -> string
# datetime -> string
# message -> string


# log files
# sequential
# 01_all.log -> 99_all.log 2GB
# Read the log files
# filter out messages based on cluster_id
# write it to a log file
# cannot write more than 100 lines per file
# write them
# 001_cluster_id

MAX_LINE_COUNT = 100


def write_log_line_to_file(log_message, file_name):
    with open(file_name, 'a') as f:
        f.write(log_message)


def filter_logs_by_cluster(cluster_id, log_file):
    line_count = 0

    with open(log_file, "r") as f:
        for log_line in f.readlines():
            split_log_lines = log_line.split(' ')
            log_cluster_id, datetime, message = split_log_lines[
                0], split_log_lines[1], split_log_lines[2]
            if log_cluster_id == cluster_id:
                line_count += 1
                filtered_log_line = f"{log_cluster_id} {datetime} {message}"
                file_name_count = (line_count // 100) + 1
                file_name = f"{file_name_count}_{cluster_id}.log"
                write_log_line_to_file(filtered_log_line, file_name)
