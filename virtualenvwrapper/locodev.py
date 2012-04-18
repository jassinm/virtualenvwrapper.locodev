import logging
import os
import subprocess
import shutil


log = logging.getLogger(__name__)


def run(*args):
    p = subprocess.Popen(args, stdout=subprocess.PIPE)
    p.wait()
    return p


def call(*args):
    return subprocess.check_output(args, shell=False)


def template(args):
    project = args[0].lower()
    call('git', 'clone', 'https://locojay@github.com/locojay/samplemod.git', project)

    currentdir = call('pwd').replace('\n','')

    git_path= os.path.join(os.path.join(currentdir, '%s' % project), '.git')
    shutil.rmtree(git_path)

    sample_dir = os.path.join(currentdir, project)
    for f in os.listdir(sample_dir):
        shutil.move(os.path.join(sample_dir, f), currentdir)
    shutil.rmtree(sample_dir)
    shutil.move(os.path.join(currentdir, 'sample'), os.path.join(currentdir,project))

    call('git', 'init')

