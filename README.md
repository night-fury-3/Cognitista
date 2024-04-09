<h2>API key configuration</h2>
First, make the .env file in the project folder, and set the OpenAI, Together and Pinecone settings as follows.

OPENAI_API_KEY=sk-
PINECONE_API_KEY=
PINECONE_ENV=
TOGETHER_API_KEY=

And please install aws-cli and set the aws configuration settings like aws secret key, region and so on.

<h2>Install packages</h2>
pip install -r requirements.txt

<h2>Database Migration</h2>
python manage.py migrate
And to create superuser for this system, run following command
python manage.py createsuperuser

<h2>Running the application</h2>
python manage.py runserver
