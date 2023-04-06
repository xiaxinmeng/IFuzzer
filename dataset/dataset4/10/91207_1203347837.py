def hardcode_stylesheet_htmlhelp(app):
    if getattr(app.builder, 'name', None) == 'htmlhelp':
        app.env.config.html_style = 'pydoctheme.css'

def setup(app):
    app.connect('builder-inited', hardcode_stylesheet_htmlhelp)