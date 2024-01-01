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
7. Create a Tailwind CSS compatible Django app, I like to call it theme(default):
   python manage.py tailwind init
8. Install Tailwind CSS dependencies, by running the following command (Make sure Node.js installed and path is set correctly):
   python manage.py tailwind install
9. Install npm libraries(flowbite, daisyUI and etc.) [Change and use yarn??? if thats even possible???]:
   npm install flowbite
   npm i -D daisyui@latest
10. Finally, you should be able to use Tailwind CSS classes in HTML. Start the development server by running the following command in your terminal:
   python manage.py tailwind startpython manage.py tailwind start
11. Open nvim and start creating your apps!
