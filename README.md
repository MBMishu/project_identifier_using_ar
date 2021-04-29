 |
   |-- project_identifier_using_Ar/                              
   |    |-- settings.py                  
   |    |-- wsgi.py                        # Start the app in production
   |    |-- urls.py                        # Define URLs served by all apps/nodes
   |    |
   |    |-- static/
   |    |    |-- <css, JS, images, marker>         # CSS files, Javascripts files
   |    |-- media/
   |    |    |-- <marker, video>         # marker , video file
   |    |
   |    |--view/
   |         | templates/                     # Templates used to render pages         
   |         |-- home/                
   |             |-- index.html      # home page
   |             |-- main.html         # show product in ar
   |-- home/                     
   |    |
   |    |-- urls.py                        
   |    |-- admin.py                        
   |    |-- controller/
   |         |-- views.py
   |    |-- model/
   |         |-- models.py
   |
   |
   |-- manage.py                           # Start the app - Django default start script
   |