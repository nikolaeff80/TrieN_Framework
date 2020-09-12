"""
Using the template engine jinja2
"""
import os

from jinja2 import Template


def render(template_name, folder='templates', **kwargs):
    """
    A minimal example of working with the template engine
    :param folder: folder with template
    :param template_name: template name
    :param kwargs: parameters to pass to the template
    :return:
    """
    file_path = os.path.join(folder, template_name)
    with open(file_path, encoding='utf-8') as f:
        template = Template(f.read())
    return template.render(**kwargs)


if __name__ == '__main__':
    output_test = render('authors.html', object_list=[{'name': 'Nikolay'}, {'name': 'Geekbrains'}])
    print(output_test)
