def retrieve_access_token():
	f_read = open('access_token.txt', 'r')
	access_token = str(f_read.read().strip())
	f_read.close()
	return access_token

def store_access_token(access_token):
    f_write = open('access_token.txt', 'w')
    f_write.write(str(access_token))
    f_write.close()
    return

def retrieve_time():
	f_read = open('token_timestamp.txt', 'r')
	timestamp = float(f_read.read().strip())
	f_read.close()
	return timestamp

def store_time(timestamp):
    f_write = open('token_timestamp.txt', 'w')
    f_write.write(str(timestamp))
    f_write.close()
    return