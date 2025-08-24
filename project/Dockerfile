# for html file
# FROM nginx:alpine
# WORKDIR /myapp
# COPY . /usr/share/nginx/html
# EXPOSE 80



# for app.py file
# FROM python
# WORKDIR /newapp
# COPY ./app.py .
# CMD [ "python","app.py" ]


# for app1.py file 
# FROM python
# WORKDIR /myapp
# COPY ./app1.py .
# CMD ["python","app1.py"]


# for server file 
# FROM python
# WORKDIR /newapp
# COPY ./server.py .
# COPY ./server.txt .
# CMD ["python","server.py"]


# for api file 
FROM python
WORKDIR /myapp
COPY ./api.py .
RUN pip install requests
CMD ["python","api.py"]