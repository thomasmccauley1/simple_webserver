# Workorder Tracker

A Flask-based web application to log and visualize work orders I complete as a field tech.  
The application imports data from exported Q-stamps (CSV/Excel) into a PostgreSQL database,  
and provides a simple interface for browsing, filtering, and mapping work orders.

## Features
- Import CSV/Excel data into PostgreSQL
- View work orders in a web dashboard
- Search/filter by account number, address, or call type
- Future: map visualization with Leaflet.js
- Future: GPS integration for motorcycle routes

## Tech Stack
- Python (Flask, SQLAlchemy, Pandas)
- PostgreSQL
- HTML/CSS (Jinja templates)
- Optional: Docker for deployment

## Getting Started
```bash
git clone https://github.com/YOURUSERNAME/workorder-tracker.git
cd workorder-tracker
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt
flask run
