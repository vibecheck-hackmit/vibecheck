# vibecheck: *tailored advice based on your music vibe.*
Feeling uncertain about your emotions? 
Discover insights from your recent song choices and get tailored advice based on your music vibe!

# deployment
First, you will need to use `spotipy` to create a `.cache` file in the `api`
directory. First, install the `spotipy` library using your Python package manager of choice.
Then, got to the Spotify developer portal and create an app. Make sure to add your Spotify account's email in the
dashboard. Get your client id and client secret
and put them in a `.creds/spotify.json` file as follows,
```json
{
  "CLIENT_ID":"CLIENT_ID_HERE",
  "CLIENT_SECRET":"CLIENT_SECRET_HERE"
}
```
Next, from inside the `api` directory, run the following in a python interactive terminal.
```py
with open('.creds/spotify.json', 'r') as f:
    creds = json.load(f)
    
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=creds['CLIENT_ID'],
    client_secret=creds['CLIENT_SECRET'],
    redirect_uri="http://localhost:8888/callback", 
    scope=["user-top-read"]
))

```
Finally, you can launch the site using `docker` by the following sequence of commands,
```
docker compose -f docker-compose-prod.yml build
docker compose -f docker-compose-prod.yml up -d
```
Note: For developers, you can use `docker-compose-dev.yml` to bind mount the files for a snappier development experience. 
