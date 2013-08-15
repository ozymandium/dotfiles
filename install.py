#!/usb/bin/env python3
"""
Installs all dotfiles. The preferred method is to rename existing dotfiles 
(those with the same name as files being installed) to `*.orig` and then
symlink to this folder.
"""
import os, shutil
try: # colors are pretty. woot.
  from termcolor import cprint
  print_info = lambda x: cprint(x, 'green','on_white')
  printf_files = lambda x: cprint(x, 'red','on_cyan')
except ImportError:
  print_files = print_info = print


intro_blurb = """Installing dotfiles.
*** All originals will be saved as `<filename>.orig` ***
"""

orig_tag = '.orig'
install_locs = [  # ( where in here ,  where in home )
  ('.bash_aliases',   '.bash_aliases'),
  ('.bash_profile',   '.bash_profile'),
  ('.bashrc',         '.bashrc'),
  ('.gitconfig',      '.gitconfig'),
  ('sublime2/Preferences (User).sublime-settings',         '.config/sublime-text-2/Packages/User/Preferences.sublime-settings'),
  ('sublime2/Preferences (Default).sublime-settings',     '.config/sublime-text-2/Packages/Default/Preferences.sublime-settings'),
  ('sublime2/LaTeX.sublime-settings',               '.config/sublime-text-2/Packages/User/LaTeX.sublime-settings'),
  ('sublime2/Python.sublime-settings',              '.config/sublime-text-2/Packages/User/Python.sublime-settings'),
  ('sublime2/Shell-Unix-Generic.sublime-settings',  '.config/sublime-text-2/Packages/User/Shell-Unix-Generic.sublime-settings'),
  ('sublime2/XML.sublime-settings',                 '.config/sublime-text-2/Packages/User/XML.sublime-settings'),
  ('sublime2/YAML.sublime-settings',                '.config/sublime-text-2/Packages/User/YAML.sublime-settings'),
]

dotf = os.path.dirname(__file__)
home = os.path.expanduser('~')


def backup_and_install(new, old):
  # save original if this is the first time installing dotfiles
  if os.path.isfile(old) and not os.path.isfile(old+orig_tag) :
    os.rename( old, old+orig_tag )
  shutil.copy2(new, old)


if __name__ == '__main__':
  print_info(intro_blurb)
  for from_, to_ in install_locs:
    from_ = os.path.join(dotf,from_)
    to_ = os.path.join(home,to_)
    print_files('\t' + from_ + '   --->    ' + to_)
    backup_and_install( from_, to_ )
  print('Done!')










