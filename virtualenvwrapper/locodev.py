import logging
import os
import subprocess


log = logging.getLogger(__name__)


def run(*args):
    p = subprocess.Popen(args, stdout=subprocess.PIPE)
    p.wait()
    return p


def call(*args):
    subprocess.call(args, shell=False)


def template(args):
    project = args[0].lower()
    call('git', 'init')
    call('touch', 'requirements.pip')
    call('touch', 'README.mkd')
    call('touch', 'MakeFile')
    call('touch', 'setup.py')
    call('mkdir', '-p', project)
    call('mkdir', '-p', os.path.join(project, 'docs'))
    call('touch', os.path.join(project, '__init__.py'))
    call('mkdir', '-p', os.path.join(project, 'tests'))
    call('touch', os.path.join(os.path.join(project, 'tests'), '__init__.py'))
