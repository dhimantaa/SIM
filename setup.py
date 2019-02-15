from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='SIM',
      version='0.0.1',
      description='Test technical indicator',
      long_description='Test technical indicator',
      classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
      ],
      url='https://github.com/dhimantaa/SIM',
      author='dhimantaa',
      author_email='dhimantarun19@gmail.com',
      license='Apache License 2.0',
      packages=['api',
                'feed',
                'plotter',
                'proxy',
                'technical'],
      install_requires=[
          'pandas',
          'requests',
          'lxml',
          'bs4',
          'numpy',
          'matplotlib'
      ],
      include_package_data=True,
      zip_safe=False)