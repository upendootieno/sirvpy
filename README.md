# SirvPy
SirvPy is a python library for accessing the Sirv REST API

## Installation:

	pip install -i https://test.pypi.org/simple/ SirvPy==1.0

Import all SirvPy functions you'll need to use in your app.

	from SirvPy import get_access, upload_files
	
## Usage:

SirvPy saves you the pain of dealing with conversions between different types returned by Sirv upon making API calls.

### Endpoints:

**1: Requesting Access tokens from Sirv**

You have to create an API Client on Sirv first https://my.sirv.com/#/account/settings/api. Save the "Client ID" and "Client Secret" somewhere. You'll need this for the next step

Sirv requires both the Client ID and Client Secret while requesting for an access token. In your application, save these in variables like so;

	clientId = 'CLIENT ID'
	clientSecret = 'CLIENT SECRET'

Next, call the get_access() function and pass your variables as arguments.

	access_token = get_access(clientId, clientSecret)

The return type is a dictionary. In most cases, you'll only need the token, which you can get from the dictionary returned.

	access_token = get_access(clientId, clientSecret)['token']

	NOTE: Sirv REST API access tokens last for only 20 minutes. SirvPy can tell whether a token is expired by use of timestamps. The get_access() method makes an api call IF AND ONLY IF your previous access token has expired, otherwise it returns the previous access token. 

**2: Uploading a file**

SirvPy provides a means for both web apps and simple python apps to interact with the upload API.

The upload_files() function takes 3 arguments;
i)   Your access token
ii)  The absolute path to your local file OR the file selected by a web app user
iii) The path to which you want to upload your file

*example use;*

>a) Simple raw Python app

	local_filename = '/absolute/path/to/file/myfile.jpg'
	upload_path = '/myfolder/oldman.jpg'
	upload_files(access_token, local_filename, upload_path)

>b) Django Web App

Your template file (HTML)

	<form method="post" enctype="multipart/form-data">
		{% csrf_token %}
		<input type="file" name="file_upload">
		<button type = "submit">Upload File</button>		
	</form>


views.py

	def my_view(request):
		if request.method == 'POST':
			upload_files(access_token, request.FILES['file_upload'], upload_path)
	
		return render(request, 'myhtml.html')

**3: Searching for files**

Sirv's rest API offers a very wide range of options to search for files. For this reason, the latest version of SirvPy only supports searching of ALL files in the authenticated user's account. Future versions of SirvPy will allow more flexibility that is already being offered directly by Sirv REST API. You can look up all the other queries that you can use to search for files here; https://api.sirv.com/v2/docs?path=/v2/files/search#POST

To search for files, call the 'search_files()' function and pass the your access token as argument.

*example use;*

	search_files(access_token)

The return type is a dictionary of all files in the authenticated user's account.

**4: Checking Storage stats**

	storage_stats(access_token)

**5: Checking Storage info**

	storage_info(access_token)

**6: Checking account info**

	account_info(access_token)

**7: Getting users**
	
	get_users(access_token)

**8: Get API usage limits**

	get_limits(access_token)

**9: Get Billing info**

	billing_info(access_token)

**10: Get Transfer Stats**

	transfer_stats(access_token)

**11: Account Events**

	account_events(access_token)

**12: Get user info**

user_id is one of the parameters and can be acquired by calling the get_users() function

	get_user_info(access_token, user_id)

**13: Get Spins Views**

	get_spins_views(access_token)

**14: Convert Video To Spin**

Specify the video file you want to spin.

	convert_to_spin(access_token, "/path/to/video/file")

**15: Convert spin to video**

	convert_to_video(access_token)

**16: Fetch image from URL**

	fetch_url(access_token, url/to/image, "/path/to/upload/to/filename")

**17: Get folder options**

This feature will work for users with enterprise accounts only

	get_folder_options(access_token, "/path/to/file")

**18: Set folder options**

	set_folder_options(access_token, "/path/to/file")

**19: Get meta description**

	get_meta_description(access_token, "/path/to/file")

**20: Set meta description**

	get_meta_description(access_token, "/path/to/file", description)

**21: Get meta title**

	get_meta_title(access_token, "/path/to/file")

**22: Set meta title**

	get_meta_title(access_token, "/path/to/file", title)

**23: Get file meta tags**

	get_file_meta_tags(access_token, "/path/to/file")

**24: Add file meta tags**

	add_file_meta_tags(access_token, "/path/to/file", ["list", "of", "tags"])

**25: Delete file meta tags**

	delete_file_meta_tags(access_token, "/path/to/file", ["list", "of", "tags"])

**26: Get approval flag**

	get_approval_flag(access_token, "/path/to/file")

**27: Set approval flag**
	
	set_approval_flag(access_token, "/path/to/file", approved, comment)

approved is boolean; True or False

**28: Delete file or empty directory**

	delete_file(access_token, "/path/to/file")

**29: Copy file**

	copy_file(access_token, "/file/to/copy", "/path/to/copy/to")

**30: Read folder Contents**

	read_folder_contents(access_token, "/path/to/dir")

**31: Get product meta**
	
	get_product_meta(access_token, "/path/to/file")

**32: Set Product meta**

	set_product_meta(access_token, "/path/to/file")

**33: Get file info**

**34: Get JWT protected url**
	
	get_jwt_url(access_token, "/path/to/file", expiry)

expiry is number of seconds

**35: Update Account Info**

	update_account_info(access_token, minify)

Minify is boolean; True or False

**36: Remote Fetching**

	Remote_fetching(access_token, enabled)

Enabled is boolean; True or False