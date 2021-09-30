import re

def memory_to_string(input):
	parsed = re.findall(r'([0-9]+)\s+to\s+(B|KB|MB|GB|TB|PB|EB|ZB|YB)', input)
	
	if not parsed[0]:
		return
	
	bytes = float(parsed[0][0])
	memory_type = parsed[0][1]
	unit_size = 1024
	
	if memory_type=='B':
		return bytes
	if memory_type == 'KB':
		result = unit_size
	if memory_type == 'MB':
		result = unit_size**2
	if memory_type == 'GB':
		result = unit_size**3
	if memory_type == 'TB':
		result = unit_size**4
	if memory_type == 'PB':
		result = unit_size**5
	if memory_type == 'EB':
		result = unit_size**6
	if memory_type == 'ZB':
		result = unit_size**7
	if memory_type == 'YB':
		result = unit_size**8
	
	return '%.2f'%(bytes/result)

	
def get_size_unit(bytes):
	SIZE_UNITS = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
	index = 0
	
	while bytes >= 1024:
		bytes /= 1024
		index += 1
	
	return SIZE_UNITS[index]
	
