from invoke import  task, run
from jinja2 import Environment, FileSystemLoader


template_env = Environment(loader=FileSystemLoader('.'))

@task
def build():
    template = template_env.get_template('source/index.html')
    rendered_template = template.render()
    with open('presentation/index.html', 'w') as fh:
        fh.write(rendered_template)

@task(build)
def publish():
    run('ghp-import -p presentation')
