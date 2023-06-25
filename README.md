# Music Streaming App REST API
This repository contains the code for a Music Streaming App REST API developed using Django and Django REST Framework. The API allows users to manage artists, albums, genres, songs, and playlists.

## Installation
Install the required dependencies:
```bash
pip install -r requirements.txt
```
Run the migrations to create the necessary database tables:
```bash
python manage.py migrate
```
Start the development server:
```bash
python manage.py runserver
```
## API Endpoints
### Genres

* GET POST /listen/genres/: List all genres or create a new genre 

* GET PUT DELETE /listen/genres/{id}/: Retrieve details of a specific genre, update or delete the genre

### Artists

* GET POST /listen/artists/: List all artists or create a new artist

* GET PUT DELETE /listen/artists/{id}/: Retrieve details of a specific artist, update or delete the artist

### Albums

* GET POST /listen/albums/: List all albums or create a new album

* GET PUT DELETE /listen/albums/{id}/: Retrieve details of a specific album, update or delete the album

### Songs

* GET POST /listen/songs/: List all songs or create a new song

* GET PUT DELETE /listen/songs/{id}/: Retrieve details of a specific song, update or delete the song

### Playlists

* GET POST /listen/playlist/: List all playlists or create a new playlist

* GET PUT DELETE /listen/playlist/{id}/: Retrieve details of a specific playlist, update or delete the playlist

## Authentication

* POST /auth/login/: Login and get the user Token

* POST /auth/logout/: Logout and delete the user Token

* POST /auth/registration/: Register a user and generate the Token at the same time

## Usage

1. Make sure the development server is running (python manage.py runserver).
2. Use a tool like Postman or cURL to make HTTP requests to the provided endpoints.
3. Authenticate the user by obtaining an access token using the /auth/login endpoint.
4. Include the access token in the request header for protected endpoints:

```bash
Authorization: Bearer <access_token>
```

Explore and interact with the available endpoints to manage artists, albums, genres, songs, and playlists.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to submit a pull request.
