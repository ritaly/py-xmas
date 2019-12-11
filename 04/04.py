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

def main():
	some_logs = extract_from_file()
	print(get_logs(10, 60, some_logs))


if __name__ == '__main__':
	main()