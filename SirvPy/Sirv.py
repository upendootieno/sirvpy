import requests
import time
import ast #for conversion of str to dict

base_url = "https://api.sirv.com"

def get_access(clientId, clientSecret):

	from file_handling import retrieve_time, retrieve_access_token, store_time, store_access_token
	time_elapsed = (time.time() - retrieve_time())/60#find time elapsed in minutes

	if time_elapsed > 20:

		print("Getting new token")
		client_tokens = { 'clientId': clientId,'clientSecret': clientSecret }
		headers = {'Content-Type' : 'application/json'}
		endpoint = base_url + "/v2/token"
		sirv_api_request = requests.post(endpoint, headers = headers, json = client_tokens)
		byte_object = sirv_api_request.content
		content_dict = ast.literal_eval(byte_object.decode())#convert bytecode to str, then str to dict
		store_access_token(content_dict)#save the dictionary returned as str
		store_time(time.time())#store current epoch time

	else:
		print("Unexpired token present; Retrieving...\n token expires in {} minutes".format(str(20 - time_elapsed)))
		content_dict = ast.literal_eval(retrieve_access_token())#retrieve the string and convert to dict

	return content_dict


def upload_files(access_token, local_file, upload_path):
	endpoint = base_url + "/v2/files/upload"
	headers = {'Content-Type' : 'image/jpeg', 'authorization': 'bearer {}'.format(access_token)}
	open_file = open(local_file, 'rb')
	upload_path = {'filename': upload_path}#The path to which the file will be uploaded
	sirv_api_request = requests.post(endpoint, headers = headers, data = open_file, params = upload_path)
	
	if sirv_api_request.status_code == 200:
		print("Successfully uploaded file")
	else:
		print("Error {}. File upload failed".format(sirv_api_request.status_code))

	return sirv_api_request