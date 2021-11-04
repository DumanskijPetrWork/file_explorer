import os
# from send2trash import send2trash
from os import path, listdir
import time  # временно для замера скорости


class Node:
    def __init__(self, _basename, _size, _parent=None):
        self.basename = _basename
        self.size = _size
        self.parent = _parent
        self.branches = None

    def get_branch(self, _branch: str):
        try:
            return self.branches[_branch]
        except Exception:
            return []


def discover_node(_full_path: str, _parent: Node):
    _basename = path.basename(_full_path)

    if path.islink(_full_path) or not path.exists(_full_path):
        # print(f'ФАЙЛ НЕ СУЩЕСТВУЕТ: {full_path}')
        return None

    _size = path.getsize(_full_path)
    _current = Node(_basename, _size, _parent)

    if path.isfile(_full_path):
        return _current

    elif path.isdir(_full_path):
        try:
            _branches = listdir(_full_path)
            if not _branches:
                return _current
            else:
                _branches = [discover_node(path.join(_full_path, b), _current) for b in _branches]
                _dict_branches = {}
                for b in _branches:
                    if b:
                        _size += b.size
                        if not b.basename.startswith('.'):
                            _dict_branches[b.basename] = b
                _current.size = _size
                _current.branches = _dict_branches
                return _current
        except PermissionError:
            # print('ФАЙЛ БЕЗ ДОСТУПА: ', _size, _basename)
            return None
    else:
        # print('ФАЙЛ ИНОГО ТИПА: ', _size, _basename)
        return None


class FileTree:
    def __init__(self, _root='/'):
        self.root = Node(_root, 0)
        self.current = self.root
        self.current_path = _root

    def path_up(self):
        if self.current.parent:
            self.current = self.current.parent
            self.current_path = path.dirname(self.current_path)
            return True
        return False

    def path_down(self, _branch: str):
        if path.isdir(self.current_path) & isinstance(self.current.branches, dict):
            if len(self.current.branches):
                _down = self.current.get_branch(_branch)
                self.current = _down
                self.current_path = path.join(self.current_path, _down.basename)
                return True
        return False

    def delete_node(self):
        _file = self.current
        if _file != self.root:
            try:
                # send2trash(self.current_path)
                _current = _file.parent
                print(_current)
                while _current:
                    _current.size -= self.current.size
                    _current = _current.parent
                self.path_up()
                del _file.parent.branches[_file.basename]
                return True
            except OSError:
                return False
        return False

    def build_tree(self):
        print('---ПРОЦЕСС НАЧАТ---')
        _start_time = time.time()

        _size = path.getsize(self.current_path)
        _branches = listdir(self.current_path)
        _branches = [discover_node(path.join(self.current_path, b), self.root) for b in _branches]
        _dict_branches = {}
        for b in _branches:
            if b:
                _size += b.size
                if not b.basename.startswith('.'):
                    _dict_branches[b.basename] = b
        self.root.size = _size
        self.root.branches = _dict_branches

        print("--- %s seconds ---" % (time.time() - _start_time))
        print('---ПРОЦЕСС ЗАВЕРШЕН---')


if __name__ == '__main__':
    os_tree = FileTree('/Users/dumanskij')  # '/Users'
    os_tree.build_tree()
