FROM        ec2-deploy:base

# Copy project files
ENV        PROJECT_DIR   /srv/project

RUN         apt -y install nginx

# Copy project files
COPY        .   ${PROJECT_DIR}
WORKDIR     ${PROJECT_DIR}

# Virtualenv path
RUN         export VENV_PATH=$(pipenv --venv); echo $VENV_PATH;

# Run uWSGI (CMD)
#CMD         pipenv run uwsgi --ini ${PROJECT_DIR}/.config/uwsgi_http.ini

# Run Nginx
#CMD         nginx -g 'daemon off;'