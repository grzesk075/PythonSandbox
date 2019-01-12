from string import Template as StrTemplate

g = 'Global Variable'
template = 'This is global variable g: $g'

def replace_placeholders(template):
    return StrTemplate(template).substitute(globals())


if __name__ == '__main__':
    print(replace_placeholders(template))
