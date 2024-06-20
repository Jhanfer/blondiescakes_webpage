source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
rm -rf backend
rm -rf public
reflex init
reflex export
unzip backend.zip -d backend
rm -r backend.zip
unzip frontend.zip -d public
rm -r frontend.zip
deactivate

