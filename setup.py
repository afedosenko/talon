import os
import sys
import contextlib

from distutils.spawn import find_executable
from setuptools import setup, find_packages


setup(name='talon',
      version='1.0.2',
      description=("Mailgun library "
                   "to extract message quotations and signatures."),
      long_description=open("README.rst").read(),
      author='Mailgun Inc.',
      author_email='admin@mailgunhq.com',
      url='https://github.com/mailgun/talon',
      license='APACHE2',
      packages=find_packages(exclude=['tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          "lxml==3.3.3",
          "regex",
          "chardet==2.3.0",
          "dnspython==1.11.1",
          "html2text",
          "nose==1.2.1",
          "numpy",
          "mock",
          "coverage",
          ]
      )


def install_pyml():
    '''
    Downloads and installs PyML
    '''
    try:
        import PyML
    except:
        pass
    else:
        return

    # install numpy first

    pyml_tarball = (
        'https://www.dropbox.com/s/qm8tzovr0y2p4cv/PyML-0.7.9.2.tar.gz?dl=1')
    pyml_srcidr = 'PyML-0.7.9'

    # see if PyML tarball needs to be fetched:
    # if not dir_exists(pyml_srcidr):
    run("wget %s" % pyml_tarball)
    run("tar -xvf PyML-0.7.9.2.tar.gz?dl=1")

    # compile&install:
    with cd(pyml_srcidr):
        python('setup.py build')
        python('setup.py install')


def run(command):
    if os.system(command) != 0:
        raise Exception("Failed '{}'".format(command))
    else:
        return 0


def python(command):
    command = '{} {}'.format('/usr/bin/python3', command)
    run(command)


def enforce_executable(name, install_info):
    if os.system("which {}".format(name)) != 0:
        raise Exception(
            '{} utility is missing.\nTo install, run:\n\n{}\n'.format(
                name, install_info))


def pip(command):
    command = '{} {}'.format(find_executable('pip3'), command)
    run(command)


def dir_exists(path):
    return os.path.isdir(path)


@contextlib.contextmanager
def cd(directory):
    curdir = os.getcwd()
    try:
        os.chdir(directory)
        yield {}
    finally:
        os.chdir(curdir)


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] in ['develop', 'install']:
        enforce_executable('curl', 'sudo aptitude install curl')

        # install_pyml()
