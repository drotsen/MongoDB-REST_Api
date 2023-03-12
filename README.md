# FirstAPI-MongoDB
# some GIT commands
set GIT_SSL_NO_VERIFY=true  or git config --global http.sslverify "false" 
update: git config http.sslCAinfo "/path/to/ca-bundle.crt"

git remote add origin https://github.com/drotsen/MongoDB-REST_Api.git
git push -u origin main
# setting virtual envoirment
python -m venv venv
venv\Scripts\activate.bat

alt 2:
pip install virtualenv
virtualenv [directory]

deactivate:
deactivate
# If your virtual environment is in a directory called 'venv':
rm -r venv