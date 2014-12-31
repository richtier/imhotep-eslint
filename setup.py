from setuptools import setup, find_packages

setup(
    name='imhotep-eslint',
    version='0.0.1',
    packages=find_packages(),
    url='https://github.com/hayes/imhotep-eslint',
    license='MIT',
    author='Michael Hayes',
    author_email='michael@hayes.io',
    description='An imhotep plugin for eslint',
    entry_points={
        'imhotep_linters': [
            '.js = imhotep-eslint.plugin:Eslint'
        ],
    },
)
