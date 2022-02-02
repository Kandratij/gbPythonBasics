# Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
# Написать скрипт, который собирает все шаблоны в одну папку templates, например:
import os
import shutil


def copy_tmpl(src_dir, trg_dir):
    if src_dir.find(trg_dir) >= 0:
        return
    for elem in os.listdir(src_dir):
        src_name = os.path.join(src_dir, elem)
        if os.path.isdir(src_name):
            copy_tmpl(src_name, trg_dir)
        elif os.path.isfile(src_name):
            file_name, file_ext = os.path.splitext(elem)
            if file_ext == '.html':
                parent_dir = os.path.basename(src_dir)
                trg_subdir = os.path.join(trg_dir, parent_dir)
                if not os.path.exists(trg_subdir):
                    os.mkdir(trg_subdir)
                trg_name = os.path.join(trg_subdir, elem)
                try:
                    if src_name != trg_name:
                        shutil.copy(src_name, trg_name)
                except Exception as e:
                    print(f'copy error: {e}')


prj_dir = 'my_project'

if os.path.exists(prj_dir):
    tmpl_dir = os.path.join(prj_dir, 'templates')
    if not os.path.exists(tmpl_dir):
        os.mkdir(tmpl_dir)
    copy_tmpl('./my_project', tmpl_dir)
else:
    print(f'Не существует каталог {prj_dir}')

