from datetime import datetime

def extract_from_file():
  logs = {}
  with open('logs.csv') as fopen:
    for line in fopen:
      line = line.strip().split(', ')
      logs[int(line[0])] = line[1]

  return logs

def get_logs(start_interv, end_interv, logs_dict):
    logs_list = []
    for key, value in logs_dict.items():
        if key > start_interv and key < end_interv:
            logs_list.append(value)
    return set(logs_list)

def to_datestamp(date_as_text):
  date_format = datetime.strptime(date_as_text, '%d-%m-%Y')
  datestamp = datetime.timestamp(date_format)
  return datestamp


def main():
  some_logs = extract_from_file()

  user_start = to_datestamp('01-01-2019')
  user_end = to_datestamp('03-12-2019')
  
  print(get_logs(user_start, user_end, some_logs))

if __name__ == '__main__':
  main()