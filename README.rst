Django Cookiecutter template for the new project

1. CD to new project folder location.
2. In your terminal type command: cookiecutter gh:svanke/cookiecutter-django
   Or run in python:
            from cookiecutter.main import cookiecutter
            cookiecutter('https://github.com/svanke/cookiecutter-django.git')
            
3. Fill in cookiecutter's answers(username and password can't be the same).
4. Using terminal create project's postgresql database. Name should be the same as {project_name}
    Type command in terminal: createdb -U {username} -W {project_name}
    Password same as used in cookiecutter's template.
5. CD to created project template. Create virtual environment with Python3
    Type command in terminal: python3 -m venv --copies .env
    Activate virtual env(command in terminal): source .env/bin/activate
6. Install django libraries(from requirements/local.txt)
    Type command in terminal: pip install -r requirements/local.txt
7. Open nvim and start creating your apps!
