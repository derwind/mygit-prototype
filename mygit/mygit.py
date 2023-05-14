from __future__ import annotations
import os
import sys


def mygit_path():
    return os.path.join(os.getcwd(), '_mygit')


def root_path():
    return os.path.abspath(os.path.join(mygit_path(), '..'))


def init():
    mygit_dir = mygit_path()
    if os.path.exists(mygit_dir):
        print(f'MyGit repository already exists in {mygit_dir}/', file=sys.stderr)
        return

    for subdir in ['objects', 'refs/heads']:
        path = os.path.join(mygit_dir, subdir)
        os.makedirs(path)

    head_file = os.path.join(mygit_dir, 'HEAD')
    with open(head_file, 'w') as fout:
        print('ref: refs/heads/main', file=fout)


def add(file_paths: list[str]):
    mygit_dir = mygit_path()
    if not os.path.exists(mygit_dir):
        print('fatal: not a mygit repository (or any of the parent directories): _mygit', file=sys.stderr)
        return

    for path in file_paths:
        if not os.path.exists(path):
            print(f"fatal: pathspec '{path}' did not match any files", file=sys.stderr)
            return

    root_dir = root_path()
    index_path = os.path.join(mygit_dir, 'index')
    with open(index_path, 'w') as fout:
        for path in file_paths:
            path = os.path.relpath(path, root_dir)
            print(path, file=fout)
