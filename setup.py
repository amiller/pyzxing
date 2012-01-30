from setuptools import setup
from setuptools.extension import Library, Extension
from glob import glob
import numpy as np
import re


def get_cython_version():
    """
    Returns:
        Version as a pair of ints (major, minor)

    Raises:
        ImportError: Can't load cython or find version
    """
    import Cython.Compiler.Main
    match = re.search('^([0-9]+)\.([0-9]+)',
                      Cython.Compiler.Main.Version.version)
    try:
        return map(int, match.groups())
    except AttributeError:
        raise ImportError


# Only use Cython if it is available, else just use the pre-generated files
try:
    cython_version = get_cython_version()
    # Requires Cython version 0.13 and up
    if cython_version[0] == 0 and cython_version[1] < 13:
        raise ImportError
    from Cython.Distutils import build_ext
    source_ext = '.pyx'
    cmdclass = {'build_ext': build_ext}
except ImportError:
    source_ext = '.cpp'
    cmdclass = {}


ext_modules = [
    Extension('pyzxing._pyzxing',
              sources=['pyzxing/_pyzxing.pyx',
                       'pyzxing/NumpyBitmapSource.cpp'] +
                       glob('zxing_cpp/core/src/zxing/*.cpp') +
                       glob('zxing_cpp/core/src/zxing/*/*.cpp') +
                       glob('zxing_cpp/core/src/zxing/*/*/*.cpp') +
                       glob('zxing_cpp/core/src/zxing/*/*/*/*.cpp') +
                       glob('zxing_cpp/core/src/zxing/*/*/*/*/*.cpp'),
              include_dirs=['zxing_cpp/core/src'],
              language='c++'
              )
    ]



setup(
    name='pyzxing',
    cmdclass=cmdclass,
    version='0.1',
    author="Andrew Miller <amiller@dappervision.com>",
    license='GNU Affero General Public License V3',
    packages=['pyzxing'],
    ext_modules = ext_modules,
    install_requires=['distribute']
)
