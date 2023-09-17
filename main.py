from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
# Assuming you have a categorizer module and spotify module
import stats
import spotify

app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Spotify Mood Categorizer!"}

@app.get("/mood-message/")
def get_top_tracks_mood():
    try:
        # Fetch the top tracks
        tracks = spotify.get_top_tracks_features()
        avg_mood_vector = stats.get_avg_mood_vec()

        # Categorize the tracks based on the mood
        category, message = stats.categorize(avg_mood_vector, tracks)

        return {
            "category": category,
            "message": message,
            "tracks": tracks  
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)