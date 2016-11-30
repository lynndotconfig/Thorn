import kid
import os


extensions = {
    'html': 'text/html',
    'atom': 'application/atom+xml'
}


def render(start_response, template_file, vars):
    ext = template_file.split(".")
    contenttype = 'text/html'
    if len(ext) > 1 and (ext[1] in extensions):
        contenttype = extensions[ext[1]]
    template = kid.Template(file=os.path.join('template', template_file), **vars)
    body = template.serialize(encoding='utf-8')

    start_response("200 OK", [('Content-Type', contenttype)])
    return body
