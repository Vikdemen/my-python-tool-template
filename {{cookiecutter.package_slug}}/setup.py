from setuptools import setup

setup(
    name='{{cookiecutter.package_name}}',
    version='0.1.0',
    package_dir={'': 'src'},
    packages=['{{cookiecutter.package_name}}'],
    url='{{cookiecutter.gh_url}}',
    license='MIT',
    author='{{cookiecutter.full_name}}',
    author_email='{{cookiecutter.email}}',
    description='{{cookiecutter.description}}',
    python_requires='>= 3.9'
)
