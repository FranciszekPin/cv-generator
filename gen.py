#! /bin/python 
# gen.py -- generates latex source of CV

def get_keyval(s):
    splitted = s.split('@')
    return (splitted[0], splitted[1][1:])

def tokenize(s):
    return "==" + s + "=="

def substitute(keyvals, output):
    for k, v in keyvals.items():
        output = output.replace(tokenize(k), v)
    return output

def read_projects(i, userdata):
    projects = []
    projects_count = 0
    for item in userdata[i+1:]:
        (k, v) = get_keyval(item)
        i += 1
        if k == "projects":
            break
        if k == "link":
            projects_count += 1
            projects += [dict()]
        projects[projects_count-1][k] = v
    return i, projects


def read_list(i, userdata, tag):
    list_items = []
    for item in userdata[i+1:]:
        (k, v) = get_keyval(item)
        i += 1
        if k == tag:
            break
        list_items += [v]
    return i, list_items


def gen_tex_for_projects(projects):
    res = ""
    with open("tex_templates/project") as file:
        project_template = file.read()
    for project in projects:
        tmp = project_template
        for k, v in project.items():
            tmp = tmp.replace(tokenize(k), v)
        res += tmp
    return res

def gen_tex_for_list(items):
    res = ""
    with open("tex_templates/list") as file:
        list_template = file.read()
    with open("tex_templates/item") as file:
        item_template = file.read()
    item_list = ""
    for item in items:
        item_list += item_template.replace(tokenize("item"), item)
    item_list = list_template.replace(tokenize("itemlist"), item_list)
    return item_list
        

def main():
    with open("tex_templates/main") as file:
        output = file.read()

    with open("cv_data") as file:
        userdata = file.read().split('\n')[:-1]

    keyvals = dict()

    reading_projects = False
    projects_count = 0
    projects = [dict()]

    itemize = {"technologies": [], "tools": [], "languages": []}

    i = 0
    while i < len(userdata):
        item = userdata[i]
        (k, v) = get_keyval(item)
        if k == "projects":
            i, projects = read_projects(i, userdata)
        elif k in ["technologies", "tools", "languages"]:
            i, itemize[k] = read_list(i, userdata, k)
        else:
            keyvals[k] = v
        i += 1

    
    keyvals["projects"] = gen_tex_for_projects(projects)
    for k, v in itemize.items():
        keyvals[k] = gen_tex_for_list(v)

    output = substitute(keyvals, output)

    print(output)

if __name__ == '__main__':
    main()

