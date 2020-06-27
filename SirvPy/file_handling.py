import os
access_token_file = os.path.abspath('access_token.txt')
timestamp_file = os.path.abspath('token_timestamp.txt')
print(access_token_file)
print(timestamp_file)
def retrieve_access_token():
	f_read = open(access_token_file, 'r')
	access_token = str(f_read.read().strip())
	f_read.close()
	return access_token

def store_access_token(access_token):
    f_write = open(access_token_file, 'w')
    f_write.write(str(access_token))
    f_write.close()
    return

def retrieve_time():
	f_read = open(timestamp_file, 'r')
	timestamp = float(f_read.read().strip())
	f_read.close()
	return timestamp

def store_time(timestamp):
    f_write = open(timestamp_file, 'w')
    f_write.write(str(timestamp))
    f_write.close()
    return