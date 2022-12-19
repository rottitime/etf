To run this project:

    docker-compose up --build --force-recreate web

To populate the database with fake data: 

    docker-compose run web python manage.py add_fake_data