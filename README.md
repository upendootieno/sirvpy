# SirvPy
SirvPy is a python library for accessing the Sirv REST API

## Installation:

	pip install -i https://test.pypi.org/simple/ SirvPy==0.1.1

Import all SirvPy functions you'll need to use in your app.

	from SirvPy import get_access, upload_files
	
## Usage:

SirvPy saves you the pain of dealing with encoding and conversions between different types returned by Sirv upon making API calls.

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