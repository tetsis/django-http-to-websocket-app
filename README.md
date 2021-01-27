# Django Http to WebSocket App
This is a simple web application using [Django Channels](https://channels.readthedocs.io/en/stable/) framework and sending WebSocket message from [Django](https://docs.djangoproject.com/) view.
And this application uses database in consumber.

# Flow
```
```


# Test run
```
pip install -r requirements.txt
docker run -p 5432:5432 -e POSTGRES_HOST_AUTH_METHOD=trust -d postgres:9 
docker run -p 6379:6379 -d redis:5
cd httptowebsocket
python manage.py migrate
python manage.py runserver
```
Access to [http://127.0.0.1:8000/room/](http://127.0.0.1:8000/room/)

# Run by docker compose
```
docker-compose build
docker-compose up -d
```
Access to [http://127.0.0.1:8000/room/](http://127.0.0.1:8000/room/)

# References
- [How to send message from django view to consumer (django-channels)? - Stack Overflow](https://stackoverflow.com/questions/59943869/how-to-send-message-from-django-view-to-consumer-django-channels)
- [Channel Layers - Document of Django Channels](https://channels.readthedocs.io/en/stable/topics/channel_layers.html)
- [Database Access - Document of Django Channels](https://channels.readthedocs.io/en/stable/topics/databases.html)

