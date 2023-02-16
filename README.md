This purpose of this project is to create an "Evaluation Registry" for the Evaluation Task Force (ETF). This will allow researchers across government to register evaluations at an early stage, and will allow users to search the registry for evaluations in their chosen policy area. 


## How to run

To run this project:

    docker-compose up --build --force-recreate web

To populate the database with fake data: 

    docker-compose run web python manage.py add_fake_data

or

    make add-fake-data

**Note: This requires at least one user to be created to run correctly*

To reset the database:

    make reset-db

To check for syntax errors:

    make check-python-code

To update the requirement lockfiles

    make update-requirements

To run tests

    make test