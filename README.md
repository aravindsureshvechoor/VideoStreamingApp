# VideoStreamingApp

This app consist of two modules

1.users
2.streamapp

users:->

       Consist of usersignup, userlogin, with the help of JWT authentication
       
streamapp: -> 
	
	This module of the parts provide a bunch of features to users, so that 
	
 		1. A user can upload a new video.
 		2. A user can edit an existing video uploaded by him.
 		3. A user can play any videos he likes.
 		4. All the videos are available with an API, pagination included(10 files per page).
 		5. A user can deleta a video that he/she has uploaded.
 		6. Search funcitonality which brings the required video with respect to the search query.
 		
 		7.Video streaming is achived with the help of Python's OPEN CV library and also used THREADING module so that each video will be played on seperate threads.
 		
 		

INSTRUCTIONS:
	
	1.Clone the project from the github repository
	2.Install the necessary requirements mentioned in the requirements.txt file
	
	3.The root folder is where the requirements.txt and README file are kept
	  Staying in that directory, activate the virtual env ( name of the VENV = 'djvenv')
	4.Then move inside to the project folder(folder name = spritle)
	5.Now you can run the server using python manage.py runserver and use the app as you wish
	
	DETAILS ABOUT THE API'S ARE PROVIDED IN THE API SPECIFICATION DOCUMENT SHARED THROUGH GOOGLE DRIVE
	
 		
