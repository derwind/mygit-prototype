import os
import sys


def init():
    mygit_dir = os.path.join(os.getcwd(), '_mygit')
    if os.path.exists(mygit_dir):
        print(f'MyGit repository already exists in {mygit_dir}/', file=sys.stderr)
        return

    for subdir in ['objects', 'refs/heads']:
        path = os.path.join(mygit_dir, subdir)
        os.makedirs(path)

    head_file = os.path.join(mygit_dir, 'HEAD')
    with open(head_file, 'w') as fout:
        print('ref: refs/heads/main', file=fout)


def add():
    ...
