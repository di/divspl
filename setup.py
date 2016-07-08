from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='divspl',
    version='0.0.2',
    description="Dustin Ingram's Very Special Programming Language.",
    long_description=readme(),
    url='https://github.com/di/divspl',
    author='Dustin Ingram',
    author_email='github@dustingram.com',
    keywords='fizz buzz rply',
    entry_points={
        'console_scripts': ['divspl = divspl.divspl:main']
    },
    license='MIT',
    packages=['divspl'],
    install_requires=['rply'],
    classifiers=['Intended Audience :: Developers'],
    zip_safe=False,
)
