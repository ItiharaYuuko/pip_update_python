import os

def create_temp_up_list():
    f_name = 'pip_up_temp.dump'
    comm_ls_cr = 'pip list -o > %s' %s f_name
    os.system(comm_ls_cr)
    return f_name

def list_update(f_name):
    with open(f_name, 'r') as input_file:
        for line in input_file.lines()[2:]:
            package_name = line.split(' ')[0]
            if package_name == 'pip':
                pip_up_comm = 'python -m pip install pip --uograde'
                os.system(pip_up_comm)
            else
                up_comm = 'pip install %s --upgrade' % package_name
                os.system(up_comm)
    print('Upgrade all done.')

def purge_temp_file(f_name):
    os.remove(f_name)
    print('%s removed.' % f_name)

if __name__ == '__main__':
    temp_file_name = create_temp_up_list()
    list_update(temp_file_name)
    purge_temp_file(temp_file_name)
