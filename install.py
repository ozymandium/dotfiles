#!/usb/bin/env python2.7
"""
Installs all dotfiles. The preferred method is to rename existing dotfiles 
(those with the same name as files being installed) to `*.orig` and then
symlink to this folder.
"""
import sys, os
try: # colors are pretty. woot.
  from termcolor import cprint
  print_info = lambda x: cprint(x, 'green','on_white')
  printf_files = lambda x: cprint(x, 'red','on_cyan')
except ImportError:
  print_files = print_info = print


orig_tag = '.orig'
install_locs = [
   # where in here    # where in home    
  ('.bash_aliases',   '.bash_aliases'),
  ('.bash_profile',   '.bash_profile'),
  ('.bashrc',         '.bashrc'),
  ('.gitconfig',      '.gitconfig'),
]

dotf = os.path.dirname(__file__)
home = os.path.expanduser('~')


def backup_and_install(new, old):
  os.rename( old, old+orig_tag )
  os.symlink(new, old)


if __name__ == '__main__':
  print_info("""
Installing dotfiles.
*** All originals will be saved as `<filename>.orig` ***
""")
  for from_, to_ in install_locs:
    from_ = os.path.join(dotf,from_)
    to_ = os.path.join(home,to_)
    print_files('\t' + from_ + '   --->    ' + to_)
    backup_and_install( from_, to_ )
  print 'Done!'










