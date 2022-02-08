import pickle
import os


def savetxt(name_file, value,farmat):
    with open(str(str(name_file + '.' + farmat)), 'wb') as f:
        save = value
        pickle.dump(save, f)

def loadtxt(name_file,farmat):
    try:
        with open(str(str(name_file) + '.' + farmat), 'rb') as f:
            load = pickle.load(f)
            print(load)
    except:
        print('Нет файла.')
        
def delete_file(file_path,file_name_delete,farmat):
    os.remove(file_path + '/' + file_name_delete + '.' + farmat)
    print('файл удалён успешно')
#"C:/Users/User/Desktop/save_load_delete/" + file_name_delete + '.txt'
while True:
    n = input('Enter:')
    if n == 's':
        name = str(input())
        d = str(input())
        fo = str(input())
        savetxt(name, d, fo)
    elif n == 'l':
        loadname = str(input())
        formaat = str(input())
        loadtxt(loadname, formaat)
    else:
        name_delete = str(input())
        far = str(input())
        delete_file("C:/Users/User/Desktop/save_load_delete",name_delete, far)


