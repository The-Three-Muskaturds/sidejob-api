# sidejob-api

How to run on local dev
create your own .venv 
pip install -r requirements.txt
configure ur .flaskenv file with your db credentials (refer to .env.example)

-- Migrations --
flask db migrate -m "some description" --> Queus up the migration
flask db upgrade --> Runs the migration 

flask db downgrade --> Reverts the previous migration, can chain this to keep downgrading.

flask db current --> grabs the current working migration of the db.