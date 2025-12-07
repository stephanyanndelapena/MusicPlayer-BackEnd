I. Project Overview
- This repository contains the backend component of Stopify, a full‑stack music management system developed as part of an academic requirement for PEITEL.
- The backend is implemented using the Django framework and exposes a RESTful API that supports the creation, retrieval, updating, and deletion (CRUD) of music tracks and playlists.
- The server is designed to integrate seamlessly with a React Native frontend and is deployed using an online hosting service.

II. Key Features
- Fully functional CRUD operations for Tracks and Playlists
- Many‑to‑Many relational structure between Tracks and Playlists
- API endpoints implemented using Django and Django REST Framework
- File handling for audio files and artwork
- Online deployment via Render.com

III. Technologies Used
- Python 3
- Django
- Django REST Framework
- SQLite
- Render.com

IV. System Requirements
- Python 3.10 or higher
- Pip package manager
- Virtual environment (recommended)

V. Installation and Setup
Clone the repository:
- git clone https://github.com/stephanyanndelapena/MusicPlayer-BackEnd
- cd MusicPlayer-BackEnd
Create and activate a virtual environment:
- python -m venv venv
- source venv/bin/activate (for Linux/Mac)
- venv\Scripts\activate (for Windows)
Install dependencies:
- pip install -r requirements.txt
Apply migrations:
- python manage.py migrate
- Start the development server:
- python manage.py runserver

VI. API Endpoints (Summary)
<br><img width="640" height="502" alt="image" src="https://github.com/user-attachments/assets/b4f03eb3-5ad3-4b3c-a433-c0fb528cc612" />

VII. Deployment Notes
- The backend must be hosted online (e.g., Render.com) to allow cross‑platform communication with the React Native frontend.
- Ensure that CORS is configured correctly using django-cors-headers.

VIII. Acknowledgements
- This backend system was developed in partial fulfillment of the requirements for PEITEL – System Development.

IX. Project Contributors
- THEEANNA JETHER D. ALEJOS
- STEPHANY ANN S. DELA PEÑA
- GRACIELLA E. PASTORAL
- BRYAN OLIVER M. GALANG
