`python manage.py runserver`

- This will run the site locally. From here you can test changes and upload articles. CTRL + c will kill a local server that is running. 

`python manage.py collectstatic`

- This will gather static assests, like album imges you've uploaded, and send them to the AWS S3 bucket. Anything in the static folder in the repository, including CSS files, will be sent there. You will need to say yes to continue.
