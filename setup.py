from distutils.core import setup
import sys

py_version_t = sys.version_info[:2]
py_version_s = ".".join([str(x) for x in py_version_t])

if __name__ == '__main__':
    version_ext = ""
    if 'sdist' in sys.argv:
        version_ext = '-py'+py_version_s

    setup(
        name = 'dyn_options',
        version = '0.1'+version_ext,
        description = 'object oriented command line processor',
        author = 'Fons Haffmans',
        author_email = 'fons.haffmans@gmail.com',
        url = 'http://github.com/fons/dyn_options/tree/master',
        download_url = 'http://github.com/fons/dyn_options/tree/master',
        license = "BSD",
        packages = ['dyn_options',],
    )

