# Test translation with Helsinki-NLP and MarianMT

<hr>

Streamlit is used for gui and hosting
*Not tested, do not use in production*

A couple of small tests done with machine translation.
<br>
Code is small and easy to read.

### Live version:
https://tr-en-pt.streamlit.app/
<br>
https://tr-ua-pt.streamlit.app/
<br>
*(sometimes the app crashes or goes over the free limit
<br>
  works without any troubles locally)*

<hr>

Open a command prompt and `cd` to a new directory of your choosing:

(optional; recommended) Create a virtual environment with:
```
python -m venv "venv"
venv\Scripts\activate
```
To use locally enter `git clone https://github.com/vluz/HelsinkiNLP-tests.git`
<br>
Then issue `pip install -r requirements.txt` and let it finish
<br>
To run do `streamlit run trUAPT.py`
<br>or<br>
`streamlit run trENPT.py`
It'll open the gui in your browser
