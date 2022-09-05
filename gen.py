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

def read_technologies(i, userdata):
    return (i+1, userdata)
def read_tools(i, userdata):
    return (i+1, userdata)
def read_languages(i, userdata):
    return (i+1, userdata)

def main():
    with open("tex_src") as file:
        output = file.read()

    with open("cv_data") as file:
        userdata = file.read().split('\n')[:-1]

    keyvals = dict()

    reading_projects = False
    projects_count = 0
    projects = [dict()]

    i = 0
    while i < len(userdata):
        item = userdata[i]
        (k, v) = get_keyval(item)
        if k == "projects":
            i, projects = read_projects(i, userdata)
        elif k == "technologies":
            i, technologies = read_technologies(i, userdata)
        elif k == "tools":
            i, tools = read_tools(i, userdata)
        elif k == "languages":
            i, languages = read_languages(i, userdata)
        else:
            keyvals[k] = v
        i += 1

    print(projects)
    print(keyvals)

    output = substitute(keyvals, output)

    # print(output)

if __name__ == '__main__':
    main()

