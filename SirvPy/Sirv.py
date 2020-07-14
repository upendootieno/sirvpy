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

def fetch_url(access_token, url, filename):
	endpoint = base_url + "/v2/files/fetch"
	headers = {"Content-Type" : "application/json", "authorization": "bearer {}".format(access_token)}
	payload = {"url" : url, "filename" : filename}#The name and path of the file to spin
	sirv_api_request = convert(requests.post(endpoint, headers = headers, json = payload))

	return sirv_api_request

def get_folder_options(access_token, filename):
	endpoint = base_url + "/v2/files/options"
	headers = {"Content-Type" : "application/json", "authorization": "bearer {}".format(access_token)}
	payload = {"filename" : filename}
	sirv_api_request = convert(requests.get(endpoint, headers = headers, params = payload))

	return sirv_api_request

def set_folder_options(access_token, filename):
	endpoint = base_url + "/v2/files/options"
	headers = {"Content-Type" : "application/json", "authorization": "bearer {}".format(access_token)}
	payload = {"filename" : filename}
	query = {"scanSpins": True, "nameSpinsAfterFolder": True, "allowListing": True}
	sirv_api_request = requests.post(endpoint, headers = headers, params = payload, json = query)

	return sirv_api_request

def get_meta_description(access_token, filename):
	endpoint = base_url + "/v2/files/meta/description"
	headers = {"Content-Type" : "application/json", "authorization": "bearer {}".format(access_token)}
	payload = {"filename" : filename}
	sirv_api_request = convert(requests.get(endpoint, headers = headers, params = payload))

	return sirv_api_request

def set_meta_description(access_token, filename, description):
	endpoint = base_url + "/v2/files/meta/description"
	headers = {"Content-Type" : "application/json", "authorization": "bearer {}".format(access_token)}
	payload = {"description" : description}
	query = {"filename" : filename}
	sirv_api_request = requests.post(endpoint, headers = headers, params = query, json = payload)

	return sirv_api_request

def get_meta_title(access_token, filename):
	endpoint = base_url + "/v2/files/meta/title"
	headers = {"Content-Type" : "application/json", "authorization": "bearer {}".format(access_token)}
	payload = {"filename" : filename}
	sirv_api_request = convert(requests.get(endpoint, headers = headers, params = payload))

	return sirv_api_request

def set_meta_title(access_token, filename, title):
	endpoint = base_url + "/v2/files/meta/title"
	headers = {"Content-Type" : "application/json", "authorization": "bearer {}".format(access_token)}
	payload = {"title" : title}
	query = {"filename" : filename}
	sirv_api_request = requests.post(endpoint, headers = headers, params = query, json = payload)

	return sirv_api_request

def get_file_meta_tags(access_token, filename):
	endpoint = base_url + "/v2/files/meta/tags"
	headers = {"Content-Type" : "application/json", "authorization": "bearer {}".format(access_token)}
	payload = {"filename" : filename}
	sirv_api_request = convert(requests.get(endpoint, headers = headers, params = payload))

	return sirv_api_request

def add_file_meta_tags(access_token, filename, tags):
	endpoint = base_url + "/v2/files/meta/tags"
	headers = {"Content-Type" : "application/json", "authorization": "bearer {}".format(access_token)}
	payload = {"tags" : tags}
	query = {"filename" : filename}
	sirv_api_request = requests.post(endpoint, headers = headers, params = query, json = payload)

	return sirv_api_request

def delete_file_meta_tags(access_token, filename, tags):
	endpoint = base_url + "/v2/files/meta/tags"
	headers = {"Content-Type" : "application/json", "authorization": "bearer {}".format(access_token)}
	payload = {"tags" : tags}
	query = {"filename" : filename}
	sirv_api_request = requests.delete(endpoint, headers = headers, params = query, json = payload)

	return sirv_api_request

def get_approval_flag(access_token, filename):
	endpoint = base_url + "/v2/files/meta/approval"
	headers = {"Content-Type" : "application/json", "authorization": "bearer {}".format(access_token)}
	payload = {"filename" : filename}
	sirv_api_request = convert(requests.get(endpoint, headers = headers, params = payload))

	return sirv_api_request

def set_approval_flag(access_token, filename, approved, comment):
	endpoint = base_url + "/v2/files/meta/approval"
	headers = {"Content-Type" : "application/json", "authorization": "bearer {}".format(access_token)}
	payload = {"approved" : approved, "comment": comment}
	query = {"filename" : filename}
	sirv_api_request = requests.post(endpoint, headers = headers, params = query, json = payload)

	return sirv_api_request

def delete_file(access_token, filename):
	endpoint = base_url + "/v2/files/delete"
	headers = {"Content-Type" : "application/json", "authorization": "bearer {}".format(access_token)}
	payload = {"filename" : filename}
	sirv_api_request = requests.post(endpoint, headers = headers, params = payload)

	return sirv_api_request

def copy_file(access_token, copy_from, copy_to):
	endpoint = base_url + "/v2/files/copy"
	headers = {"Content-Type" : "application/json", "authorization": "bearer {}".format(access_token)}
	payload = {"from" : copy_from, "to" : copy_to}
	sirv_api_request = requests.post(endpoint, headers = headers, params = payload)

	return sirv_api_request

def read_folder_contents(access_token, dirname):
	endpoint = base_url + "/v2/files/readdir"
	headers = {"Content-Type" : "application/json", "authorization": "bearer {}".format(access_token)}
	payload = {"dirname" : dirname}
	sirv_api_request = convert(requests.get(endpoint, headers = headers, params = payload))

	return sirv_api_request

def get_product_meta(access_token, filename):
	endpoint = base_url + "/v2/files/meta/product"
	headers = {"Content-Type" : "application/json", "authorization": "bearer {}".format(access_token)}
	payload = {"filename" : filename}
	sirv_api_request = convert(requests.get(endpoint, headers = headers, params = payload))

	return sirv_api_request

def set_product_meta(access_token, filename, product_id, product_name, brand):
	endpoint = base_url + "/v2/files/meta/product"
	headers = {"Content-Type" : "application/json", "authorization": "bearer {}".format(access_token)}
	payload = {"filename" : filename}
	query = {"id" : product_id, "name" : product_name, "brand" : brand}
	sirv_api_request = requests.post(endpoint, headers = headers, params = payload, json = query)

	return sirv_api_request

def get_file_info(access_token, filename):
	endpoint = base_url + "/v2/files/stat"
	headers = {"Content-Type" : "application/json", "authorization": "bearer {}".format(access_token)}
	payload = {"filename" : filename}
	sirv_api_request = convert(requests.get(endpoint, headers = headers, params = payload))

	return sirv_api_request

def get_jwt_url(access_token, filename, expiry):
	endpoint = base_url + "/v2/files/jwt"
	headers = {"Content-Type" : "application/json", "authorization": "bearer {}".format(access_token)}
	payload = {"filename" : filename, "expiresIn" : expiry}
	sirv_api_request = convert(requests.post(endpoint, headers = headers, json = payload))

	return sirv_api_request

def update_account_info(access_token, minify):
	endpoint = base_url + "/v2/account"
	headers = {"Content-Type" : "application/json", "authorization": "bearer {}".format(access_token)}
	payload = {"minify" :  {"enabled" : minify}} 
	sirv_api_request = requests.post(endpoint, headers = headers, json = payload)

	return sirv_api_request

def remote_fetching(access_token, enabled):
	endpoint = base_url + "/v2/account/fetching"
	headers = {"Content-Type" : "application/json", "authorization": "bearer {}".format(access_token)}
	payload = {"enabled" :  enabled} 
	sirv_api_request = requests.post(endpoint, headers = headers, json = payload)

	return sirv_api_request