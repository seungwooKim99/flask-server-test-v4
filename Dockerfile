FROM python

# Install requirements
RUN pip install --no-cache-dir --upgrade pip
# RUN pip install --no-cache-dir pymysql pandas flask flask_restx
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Add source code

ADD app /home/app
ADD requirements.txt /home
ADD manage.py /home

WORKDIR /home
# Set environment variables
ENV FLASK_APP=manage.py

# ENTRYPOINT
ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]