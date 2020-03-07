# docker-flask-mongodb-uwsgi-nginx

[![Author](https://img.shields.io/badge/author-alexander.sterpu%40gmail.com-blue.svg)](https://github.com/blry)

## Description

### Task

- To write a program which will extract data from Excel files.
- Please write a second program that will start an API web-service on port 8080 (use flask) that will return the stored data.
- All services should be running in Docker.

## Installation instructions

1. Create `mongodb_root_password` file in **./docker/shared/secrets/**.

    E.g.: `$ echo "S3cR3TPassword" >> docker/shared/secrets/mongodb_root_password`
2. `docker-compose up`
3. Done! You can access: http://127.0.0.1:8080/data?week_start=2016-08-10&week_end=2017-08-20

Note: 
* Put new ***.xlsx** files under `./parser/xlsx` folder
* Configure port in **.env** if needed

### Docker contents

- [Nginx](https://hub.docker.com/_/nginx)
- [uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/)
- [Flask](https://palletsprojects.com/p/flask/)
- [MongoDB](https://hub.docker.com/_/mongo)
- [OpenPyXL](https://openpyxl.readthedocs.io/en/stable/)

## Result:
[![Author](https://i.imgur.com/V3DoFdk.png)](https://github.com/blry)

## Contributing

Do not hesitate to improve this repository, creating your PR on GitHub with a description which explains it.

Ask your question on `alexander.sterpu@gmail.com`.
