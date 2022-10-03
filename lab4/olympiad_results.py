def get_members(n):
    members_list = []
    for i in range(n):
        print("Введите фамилию и количество баллов: ")
        member = input()
        members_list.append(member)
    return members_list


def get_entires(members_list):
    return list(map(lambda member: member.split(' '), members_list))


def get_members_hashmap(members_entries):
    members_hashmap = {}
    for member in members_entries:
        members_hashmap[member[0]] = int(member[1])
    return members_hashmap


def get_sorted_members_hashmap(members_hashmap):
    sorted_hashmap = {}
    sorted_keys = sorted(members_hashmap, key = members_hashmap.get, reverse=True)

    for key in sorted_keys:
        sorted_hashmap[key] = members_hashmap[key]

    return sorted_hashmap

def main():
    print("Введите количество участников олимпиады: ")
    n = int(input())

    sorted_hashmap = get_sorted_members_hashmap(get_members_hashmap(get_entires(get_members(n))))

    print(sorted_hashmap)

    print("Список участников (От самого большого количества баллов к меньшему): ")
    for key in sorted_hashmap:
        print(key)


main()