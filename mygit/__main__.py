import argparse
from .mygit import init, add


def command_init(args):
    init()


def command_add(args):
    add()


def main():
    '''Entrypoint'''

    parser = argparse.ArgumentParser(prog='mygit-prototype', description='A prototype of an imitation of Git')
    subparsers = parser.add_subparsers()

    subparser = subparsers.add_parser('init', help='mygit-init - Create an empty MyGit repository')
    subparser.set_defaults(handler=command_init)

    subparser = subparsers.add_parser('add', help='mygit-add - Add file contents to the index')
    subparser.set_defaults(handler=command_add)

    args = parser.parse_args()
    if hasattr(args, 'handler'):
        args.handler(args)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
