import os

import markdown2
import jinja2

PUFFIN_PATH = os.path.abspath(os.path.dirname(__file__))

# REVIEW I almost feel like this could be a subclass of file
class Puffin(object):
    """Puffin objects can render themselves in a variety of published formats."""
    def __init__(self, filename):
        super(Puffin, self).__init__()
        self.filename = filename
        self.data = file(filename)
        self.style_path = os.path.join(PUFFIN_PATH, 'style')

    def render(self):
        """renders the puffin object into an html file"""
        content = markdown2.markdown(self.data.read())
        template = file(os.path.join(self.style_path, 'template')).read()
        return jinja2.Template(template).render({'content': content})

    def render_to_file(self, output_name=None):
        output = self.render()
        if output_name is None:
            output_name = self.filename.split('.')[0]
            output_name = '.'.join([output_name, 'html'])
        file(output_name, 'w').write(output)