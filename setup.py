__version__ = '0.0.5'

import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(name='sshare',
                 version=__version__,
                 author='Altertech',
                 author_email='pr@altertech.com',
                 description='Secure share client',
                 long_description=long_description,
                 long_description_content_type='text/markdown',
                 url='https://github.com/alttch/sshare',
                 packages=setuptools.find_packages(),
                 include_package_data=True,
                 license='Apache License 2.0',
                 install_requires=[
                     'requests', 'pyyaml', 'requests_toolbelt', 'tqdm',
                     'neotermcolor'
                 ],
                 classifiers=(
                     'Programming Language :: Python :: 3',
                     'License :: OSI Approved :: Apache Software License',
                     'Topic :: Communications',
                 ),
                 scripts=['bin/sshare'])
