# BSA

Botanical shopping Android application, with a Flask payment backend.

The Android application is in `app/`; the Flask backend is in `server/`. Install backend dependencies with `pip install -r server/requirements.txt`, configure `STRIPE_PUBLISHABLE_KEY` and `STRIPE_SECRET_KEY` in the server environment, and run `python server/app.py` for local development. Never commit payment credentials.

This is not a static website and cannot run on GitHub Pages. The Android app requires its own build environment and service configuration; the Flask backend requires a Python server.
