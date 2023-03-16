from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)


# Define route for getting live cricket score
@app.route('/live-score')
def live_score():
    # Cricbuzz URL for live cricket score
    url = "https://www.cricbuzz.com/cricket-match/live-scores/recent-matches"

    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the div with class "cb-col cb-col-25 cb-mtch-blk" which contains the live score data
    score_div = soup.find('div', {'class': 'cb-col cb-col-100 cb-plyr-tbody cb-rank-hdr cb-lv-main'})

    # Extract the live score text from the div
    score_text = score_div.text.strip()

    # Return the live score as a JSON object
    return jsonify({'score': score_text})


if __name__ == '__main__':
    app.run(debug=True)
