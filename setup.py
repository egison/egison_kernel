from setuptools import setup, find_packages


setup(name='egison_kernel',
      version='0.0.1',
      description='Egison Kernel for Jupyter Notebook',
      install_requires=[
          'ipykernel',
          'pexpect',
      ],
      author='Satoshi Egi',
      author_email='egi@egison.org',
      url='https://github.com/egison/egison_kernel',
      packages=find_packages(),
      entry_points="""
      [console_scripts]
      """,)
