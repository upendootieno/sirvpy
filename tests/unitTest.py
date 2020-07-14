import SirvPy
import sys
from keys import *

errors = 0
tests_completed = 0

def check_status_code(endpoint, response):
	if response.status_code == 200:
		global tests_completed
		tests_completed +=1
		print(" {} test Success".format(endpoint))
	else:
		print(" {} test Failed with error {}".format(endpoint, response.status_code))
		global errors
		errors +=1

def testSirvPy():
	try:
		#Access token
		access_token = SirvPy.get_access(clientId, clientSecret)['token']
	except Exception as e:
		print(" Exception : {}".format(e))
		sys.exit("Couldn't get access_token, stoping tests")

	try:
		#Search Files
		check_status_code("search_files", SirvPy.search_files(access_token))
	except Exception as e:
		print(" Exception : {}".format(e))

	try:
		#Storage info
		check_status_code("storage_info", SirvPy.storage_info(access_token))
	except Exception as e:
		print(" Exception : {}".format(e))

	try:
		#Storage stats
		check_status_code("storage_stats", SirvPy.storage_stats(access_token))
	except Exception as e:
		print(" Exception : {}".format(e))
	
	try:
		#Account info
		check_status_code("account_info", SirvPy.account_info(access_token))
	except Exception as e:
		print(" Exception : {}".format(e))
	
	try:
		#Get users
		check_status_code("get_users", SirvPy.get_users(access_token))
	except Exception as e:
		print(" Exception : {}".format(e))
	try:
		#Get limits
		check_status_code("get_limits", SirvPy.get_limits(access_token))
	except Exception as e:
		print(" Exception : {}".format(e))

	try:
		#Billing info
		check_status_code("billing_info", SirvPy.billing_info(access_token))
	except Exception as e:
		print(" Exception : {}".format(e))

	try:
		#Transfer Stats
		check_status_code("transfer_stats", SirvPy.transfer_stats(access_token))
	except Exception as e:
		print(" Exception : {}".format(e))

	try:
		#Account Events
		check_status_code("account_events", SirvPy.account_events(access_token))
	except Exception as e:
		print(" Exception : {}".format(e))

	try:
		#Get user info
		check_status_code("get_user_info", SirvPy.get_user_info(access_token, bearArts_ID))
	except Exception as e:
		print(" Exception : {}".format(e))

	try:
		#Get spin views
		check_status_code("get_spin_views", SirvPy.get_spins_views(access_token))
	except Exception as e:
		print(" Exception : {}".format(e))

	try:
		#Fetch URL
		check_status_code("fetch_url", SirvPy.fetch_url(access_token, "https://bit.ly/2OklqYe", "/TestFolder/meme.jpg"))
	except Exception as e:
		print(" Exception : {}".format(e))

	try:
		#JWT URL
		check_status_code("jwt", SirvPy.get_jwt_url(access_token, "/TestFolder/meme.jpg", 3200))
	except Exception as e:
		print(" Exception : {}".format(e))

	try:
		#File info
		check_status_code("file_info", SirvPy.get_file_info(access_token, "/TestFolder/meme.jpg"))
	except Exception as e:
		print(" Exception : {}".format(e))

	try:	
		#Read folder contents
		check_status_code("read_folder_contents", SirvPy.read_folder_contents(access_token, "/TestFolder"))
	except Exception as e:
		print(" Exception : {}".format(e))

	try:
		#Add file meta tags
		check_status_code("add_file_meta_tags", SirvPy.add_file_meta_tags(access_token, "/TestFolder/meme.jpg", ['this tag', 'that tag', 'tag tag']))
	except Exception as e:
		print(" Exception : {}".format(e))

	try:
		#Get file meta tags
		check_status_code("get_file_meta_tags", SirvPy.get_file_meta_tags(access_token, "/TestFolder/meme.jpg"))
	except Exception as e:
		print(" Exception : {}".format(e))

	try:
		#Delete file meta tag
		check_status_code("delete_file_meta_tag", SirvPy.delete_file_meta_tags(access_token, "/TestFolder/meme.jpg", ["that tag"]))
	except Exception as e:
		print(" Exception : {}".format(e))

	try:
		#Set meta title
		check_status_code("set_meta_title", SirvPy.set_meta_title(access_token, "/TestFolder/meme.jpg", "New meta title"))
	except Exception as e:
		print(" Exception : {}".format(e))

	try:
		#Get meta title
		check_status_code("get_meta_title", SirvPy.get_meta_title(access_token, "/TestFolder/meme.jpg"))
	except Exception as e:
		print(" Exception : {}".format(e))

	try:
		#Set folder options
		check_status_code("set_folder_options", SirvPy.set_folder_options(access_token, "/TestFolder"))
	except Exception as e:
		print(" Exception : {}".format(e))

	try:
		#Get folder options
		check_status_code("get_folder_options", SirvPy.get_folder_options(access_token, "/TestFolder"))
	except Exception as e:
		print(" Exception : {}".format(e))

	try:
		#Set Approval flag
		check_status_code("set_approval_flag", SirvPy.set_approval_flag(access_token, "/TestFolder/meme.jpg", True, "just a comment"))
	except Exception as e:
		print(" Exception : {}".format(e))

	try:
		#Get approval flag
		check_status_code("get_approval_flag", SirvPy.get_approval_flag(access_token, "/TestFolder/meme.jpg"))
	except Exception as e:
		print(" Exception : {}".format(e))

	try:
		#Set product meta
		check_status_code("set_product_meta", SirvPy.set_product_meta(access_token, "/TestFolder/meme.jpg", "MEME001", "Spongebob Meme", "Nickelodeon"))
	except Exception as e:
		print(" Exception : {}".format(e))

	try:
		#Get product meta
		check_status_code("get_product_meta", SirvPy.get_product_meta(access_token, "/TestFolder/meme.jpg"))
	except Exception as e:
		print(" Exception : {}".format(e))

	try:
		#upload File
		check_status_code("upload_file", SirvPy.upload_files(access_token, "/home/technicollins/Desktop/Projects/SirvPy/tests/kicc.jpg", "/TestFolder/kicc.jpg"))
	except Exception as e:
		print(" Exception : {}".format(e))

	try:
		#Convert video to spin
		check_status_code("convert_to_spin", SirvPy.convert_to_spin(access_token, "/TestFolder/Spins/Trainers.mp4"))
	except Exception as e:
		print(" Exception : {}".format(e))

	try:
		#Convert spin to video
		check_status_code("convert_to_video", SirvPy.convert_to_video(access_token, "/TestFolder/Spins/Trainers/Trainers.spin"))
	except Exception as e:
		print(" Exception : {}".format(e))

	try:
		#Set meta description
		check_status_code("set_meta_description", SirvPy.set_meta_description(access_token, "/TestFolder/meme.jpg", "New meta description"))
	except Exception as e:
		print(" Exception : {}".format(e))

	try:
		#Get meta description
		check_status_code("get_meta_description", SirvPy.get_meta_description(access_token, "/TestFolder/meme.jpg"))
	except Exception as e:
		print(" Exception : {}".format(e))
	
	try:
		#Copy file
		check_status_code("copy_file", SirvPy.copy_file(access_token, "/TestFolder/kicc.jpg", "/TestFolder/TestSubFolder/kicc.jpg"))
	except Exception as e:
		print(" Exception : {}".format(e))

	try:
		#Delete file
		check_status_code("delete_file", SirvPy.delete_file(access_token, "/TestFolder/TestSubFolder/kicc.jpg"))
	except Exception as e:
		print(" Exception : {}".format(e))

	try:
		#Update Account Info
		check_status_code("update_account_info", SirvPy.update_account_info(access_token, True))
	except Exception as e:
		print(" Exception : {}".format(e))

	try:
		#Remote Fetching
		check_status_code("remote_fetching", SirvPy.remote_fetching(access_token, False))
	except Exception as e:
		print(" Exception : {}".format(e))

	print("\n***************************\n{} Tests completed with {} errors\n***************************".format(tests_completed, errors))

#BEFORE RUNNING TESTS;
# 1: Delete meme.jpg and kicc.jpg from TestFolder
# 2: Delete Trainers folder from TestFolder/Spins

testSirvPy()