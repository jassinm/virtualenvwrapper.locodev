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
    call('mkdir','-p', 'docs')
    call('mkdir','-p', 'tests')
    call('mkdir', '-p', project)
    call('touch', os.path.join(project, '__init__.py'))
