This repository contains the following files:

models.py: contains the inference script of the two models, namely:
1. OPT Model for text completion
2. rmbg model for background removal

modelUI.py: contains the streamlit app, web UI for both model implementations

app.py: runs Flask API that listens on route /api/completion where the user can send the text and as a response get the completed text.

testflaskAPI.py: contains the code that can be run, after running app.py, to send the input text to route /api/completion and get the completed text as a response

requrements.txt: all the required libraries to successfully run this code
