import json


def load_config():
    try:
        with open("./config.json", 'r') as config_file:
            usr_info = json.load(config_file)
    except FileNotFoundError:
        with open("./config.json", 'w') as config_file:
            initial_info = {'usr_name': 'B12345678', 'usr_pwd': 'ABIDE', 'cellphone_ip': '127.0.0.1',
                            'operator': 'njupt'}
            json.dump(initial_info, config_file)
            usr_info = json.dumps(initial_info)
            usr_info = json.loads(usr_info)

    return usr_info


def write_config(usr_name, usr_pwd, cell_ip, operator):
    with open("./config.json", 'w') as config_file:
        write_info = {'usr_name': usr_name, 'usr_pwd': usr_pwd, 'cellphone_ip': cell_ip, 'operator': operator}
        json.dump(write_info, config_file)

    return
