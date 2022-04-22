child_dict = {}
dead_list = []
description = []
married_dict = {}
each_share = {}
final_list = []
parents_dict = {}
grandparents_dict = {}
alive_counter=0
def get_ready_Dscrp():
    global description
    description = list(map(lambda n: " ".join(n.split()), description))
    description = list(map(lambda n: n.split(" "), description))
    prepare_child_dict()
    prepare_dead_dict()
    prepare_married_dict()
    prepare_parents_dict()
    prepare_grandparents()

def prepare_child_dict():
    global child_dict
    child_dict = {}
    for i in description:
        if i[0] == "CHILD":
            if i[1] not in child_dict.keys():
                child_dict[i[1]] = i[3:]
            elif i[1] in child_dict.keys():
                child_dict[i[1]].append(i[3])
            if i[2] not in child_dict.keys():
                child_dict[i[2]] = i[3:]
            elif i[1] in child_dict.keys():
                child_dict[i[2]].append(i[3])


def prepare_dead_dict():
    global dead_list
    dead_list = []
    for i in description:
        if i[0] == "DEPARTED":
            dead_list.append(i[1])

def prepare_married_dict():
    global married_dict
    married_dict = {}
    for i in description:
        if i[0] == "MARRIED":
            married_dict[i[1]] = i[2]
            married_dict[i[2]] = i[1]

def prepare_parents_dict():
    global parents_dict
    parents_dict = {}
    for i in description:
        if i[0] == "CHILD":
            for j in i[3:]:
                parents_dict[j]=i[1:3]

def prepare_grandparents():
    global grandparents_dict
    grandparents_dict = {}
    for i in description:
        if i[0] == 'CHILD':
            for j in i[3:]:
                grandparents_dict[j] = []
    for child in parents_dict.keys():
        for parents in parents_dict[child]:
            if parents in parents_dict.keys():
                grandparents_dict[child].append(parents_dict[parents])

def check_marry(name):
    global description
    alive_marry=0
    if name in married_dict:
        if married_dict[name] not in dead_list:
            alive_marry=1
        else:
            alive_marry=0
    else:
        alive_marry=0
    return alive_marry


def convert_dict_to_list(dict):
    view=dict.items()
    final_list=list(view)
    return final_list


def check_alive1(name):
    global description
    alive_counter=0
    if name in child_dict.keys():
        for child in child_dict[name]:
            if child not in description[-1]:
                if child not in dead_list:
                    alive_counter+=1
                else:
                    alive_counter+=check_alive1(child)
    else:
        alive_counter=0
    return alive_counter


def pg1(name):
    global description
    global each_share
    if check_alive1(name) !=0:
        if check_marry(name) != 0:
            each_share[married_dict[name]] = (1 / 4) * float(description[-1][-1])
            recursion_helper1((3 / 4) * float(description[-1][-1]), name)
        else:
            recursion_helper1(float(description[-1][-1]),name)
    else:
        if check_marry(name) != 0:
            each_share[married_dict[name]] = float(description[-1][-1])

def recursion_helper1(share_1,name):
    global description
    global each_share
    counter=0
    if name in child_dict.keys():
        for child in child_dict[name]:
            if child not in dead_list:
                counter+=1
            else:
                if check_alive1(child) !=0:
                    counter+=1
    if counter != 0:
        share=share_1/counter
        if name in child_dict:
            for child in child_dict[name]:
                if child not in dead_list:
                    each_share[child] = 0
                    each_share[child] += share
                else:
                    recursion_helper1(share,child)


def check_alive2(name):
    global description
    global alive_counter
    if name in parents_dict.keys():
        for parents in parents_dict[name]:
            if parents not in dead_list:
                alive_counter+=1
            else:
                for child in child_dict[parents]:
                    if child not in description[-1]:
                        if child not in dead_list:
                            alive_counter+=1
                        else:
                            check_alive1(child)
    else:
        alive_counter=0
    return alive_counter


def pg2(name):
    global description
    global each_share
    if check_alive2(name) != 0:
        if check_marry(name) != 0:
            each_share[married_dict[name]] = (1 / 2) * float(description[-1][-1])
            recursion_helper2((1 / 2) * float(description[-1][-1]),name)
        else:
            recursion_helper2(float(description[-1][-1]), name)
    else:
        if check_marry(name) != 0:
            each_share[married_dict[name]] = float(description[-1][-1])


def recursion_helper2(share_2,name):
    global description
    global each_share
    if name in parents_dict.keys():
        for parent in parents_dict[name]:
            share=share_2/2
            if parent not in dead_list:
                each_share[parent] = share
            else:
                if check_alive1(parent) != 0:
                    recursion_helper1(share,parent)


def check_alive3(name):
    global description
    global alive_counter
    if name in grandparents_dict.keys():
        for grandparents in grandparents_dict[name]:
            for each_grandparent in grandparents:
                if each_grandparent not in dead_list:
                    alive_counter += 1
                else:
                    for child in child_dict[each_grandparent]:
                        if child not in description[-1]:
                            if child not in dead_list:
                                alive_counter += 1
                            else:
                                check_alive1(child)
    return alive_counter

def pg3(name):
    global description
    global each_share
    if check_alive3(name) != 0:
        if check_marry(name) != 0:
            each_share[married_dict[name]] = (3 / 4) * float(description[-1][-1])
            recursion_helper3((1/4)*float(description[-1][-1]),name)
        else:
            recursion_helper3(float(description[-1][-1]), name)
    else:
        if check_marry(name) != 0:
            each_share[married_dict[name]] = float(description[-1][-1])


def recursion_helper3(share_3,name):
    global description
    global each_share
    if name in grandparents_dict.keys():
        for grandparents in grandparents_dict[name]:
            for each_grandparent in grandparents:
                share=share_3/4
                if each_grandparent not in dead_list:
                    each_share[each_grandparent] = share
                else:
                    if check_alive1(each_grandparent) != 0:
                        recursion_helper1(share,each_grandparent)


def inheritance(_Dscrp):
    global description
    global each_share
    global married_dict
    each_share={}
    description = _Dscrp
    get_ready_Dscrp()
    for i in description:
        if 'DECEASED' in i:
            if check_alive1(i[1]) != 0 or (check_alive1(i[1]) == 0 and check_marry(i[1]) != 0):
                pg1(i[1])
            if (check_alive1(i[1]) == 0 and check_alive2(i[1]) != 0) or (check_alive1(i[1]) == 0 and check_alive2(i[1]) == 0 and check_marry(i[1]) !=0):
                pg2(i[1])
            if (check_alive1(i[1]) == 0 and check_alive2(i[1]) == 0 and check_alive3(i[1]) !=0) or (check_alive1(i[1]) == 0 and check_alive2(i[1]) == 0 and check_alive3(i[1]) ==0 and check_marry(i[1]) !=0):
                pg3(i[1])
    return convert_dict_to_list(each_share)

