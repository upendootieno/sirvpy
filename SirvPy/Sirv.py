import requests
import time
import json #for parsing str into dict
import ast #for parsing single quote "json" to dict

base_url = "https://api.sirv.com"

#This function converts the response returned by API call to dict
def convert(response):
	content_dict = json.loads(response.content)
	return content_dict

def get_access(clientId, clientSecret):

	from .file_handling import retrieve_time, retrieve_access_token, store_time, store_access_token
	time_elapsed = (time.time() - retrieve_time())/60#find time elapsed in minutes

	if time_elapsed > 20:

		print("Getting new token")
		payload = { "clientId": clientId,"clientSecret": clientSecret }
		headers = {"Content-Type" : "application/json"}
		endpoint = base_url + "/v2/token"
		sirv_api_request = convert(requests.post(endpoint, headers = headers, json = payload))#make request and convert response to dict		
		store_access_token(sirv_api_request)#save the dictionary returned as str
		store_time(time.time())#store current epoch time

	else:
		print("Unexpired token present; Retrieving...\n token expires in {} minutes".format(str(20 - time_elapsed)))
		sirv_api_request = ast.literal_eval(retrieve_access_token())#retrieve the string and convert to dict

	return sirv_api_request


def upload_files(access_token, local_file, upload_path):
	endpoint = base_url + "/v2/files/upload"
	headers = {"Content-Type" : "image/jpeg", "authorization": "bearer {}".format(access_token)}
	upload_path = {"filename": upload_path}#The path to which the file will be uploaded TBD

	if str(local_file.__class__) == "<class 'str'>":
		print("User passed a File Path")
		open_file = open(local_file, 'rb')
		sirv_api_request = requests.post(endpoint, headers = headers, data = open_file, params = upload_path)
	elif str(local_file.__class__) == "<class 'django.core.files.uploadedfile.InMemoryUploadedFile'>":
		print("User passed a django uploadfile")
		sirv_api_request = requests.post(endpoint, headers = headers, data = local_file, params = upload_path)
	else:
		print("Unsupported file source")

	if sirv_api_request.status_code == 200:
		print("Successfully uploaded file")
	else:
		print("Error {}. File upload failed".format(sirv_api_request.status_code))

	return sirv_api_request

def search_files(access_token):
	endpoint = base_url + "/v2/files/search"
	headers = {"Content-Type" : "application/json", "authorization": "bearer {}".format(access_token)}
	payload = {"query": "basename:*"}
	sirv_api_request = convert(requests.post(endpoint, headers = headers, json = payload))

	return sirv_api_request

def storage_info(access_token):
	endpoint = base_url + "/v2/account/storage"
	headers = {"Content-Type" : "application/json", "authorization": "bearer {}".format(access_token)}
	sirv_api_request = convert(requests.get(endpoint, headers = headers))

	return sirv_api_request

def storage_stats(access_token):
	endpoint = base_url + "/v2/stats/storage"
	headers = {"Content-Type" : "application/json", "authorization": "bearer {}".format(access_token)}
	sirv_api_request = convert(requests.get(endpoint, headers = headers))

	return sirv_api_request

def account_info(access_token):
	endpoint = base_url + "/v2/account"
	headers = {"Content-Type" : "application/json", "authorization": "bearer {}".format(access_token)}
	sirv_api_request = convert(requests.get(endpoint, headers = headers))

	return sirv_api_request

def get_users(access_token):
	endpoint = base_url + "/v2/account/users"
	headers = {"Content-Type" : "application/json", "authorization": "bearer {}".format(access_token)}
	sirv_api_request = convert(requests.get(endpoint, headers = headers))

	return sirv_api_request

def get_limits(access_token):
	endpoint = base_url + "/v2/account/limits"
	headers = {"Content-Type" : "application/json", "authorization": "bearer {}".format(access_token)}
	sirv_api_request = convert(requests.get(endpoint, headers = headers))

	return sirv_api_request

def billing_info(access_token):
	endpoint = base_url + "/v2/billing/plan"
	headers = {"Content-Type" : "application/json", "authorization": "bearer {}".format(access_token)}
	sirv_api_request = convert(requests.get(endpoint, headers = headers))

	return sirv_api_request

def transfer_stats(access_token):
	endpoint = base_url + "/v2/stats/http"
	headers = {"Content-Type" : "application/json", "authorization": "bearer {}".format(access_token)}
	sirv_api_request = convert(requests.get(endpoint, headers = headers))

	return sirv_api_request

def account_events(access_token):
	endpoint = base_url + "/v2/account/events/search"
	headers = {"Content-Type" : "application/json", "authorization": "bearer {}".format(access_token)}
	#payload = {"level" : "info", "module" : "", "level" : "", "type" : ""}
	payload = {"level" : "info"}
	sirv_api_request = convert(requests.post(endpoint, headers = headers, json = payload))

	return sirv_api_request

def get_user_info(access_token, user_id):
	endpoint = base_url + "/v2/user"
	headers = {"Content-Type" : "application/json", "authorization": "bearer {}".format(access_token)}
	payload = {"userId": user_id}
	sirv_api_request = convert(requests.get(endpoint, headers = headers, params = payload))

	return sirv_api_request

def get_spins_views(access_token):
	endpoint = base_url + "/v2/stats/spins/views"
	headers = {"Content-Type" : "application/json", "authorization": "bearer {}".format(access_token)}
	sirv_api_request = convert(requests.get(endpoint, headers = headers))

	return sirv_api_request

def convert_to_spin(access_token, filename):
	endpoint = base_url + "/v2/files/video2spin"
	headers = {"Content-Type" : "application/json", "authorization": "bearer {}".format(access_token)}
	payload = {"filename": filename, "options": {"start" : 0, "end" : 3, "frames" : 30}}#The name and path of the file to spin
	sirv_api_request = convert(requests.post(endpoint, headers = headers, json = payload))

	return sirv_api_request

def convert_to_video(access_token, filename):
	endpoint = base_url + "/v2/files/spin2video"
	headers = {"Content-Type" : "application/json", "authorization": "bearer {}".format(access_token)}
	payload = {"filename": filename, "options": {"width" : 1920, "height" : 1080, "loops" : 10, "row": "single"}}#The name and path of the file to spin
	sirv_api_request = convert(requests.post(endpoint, headers = headers, json = payload))

	return sirv_api_request