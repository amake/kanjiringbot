from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='kanjiringbot',
    version='1.0',
    description='A bot to tweet kanji rings',
    long_description=long_description,
    url='https://github.com/amake/kanjiringbot',
    author='Aaron Madlon-Kay',
    author_email='aaron@madlon-kay.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Education',
        'Topic :: Text Processing :: Linguistic',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='kanji hanzi ring twitter bot',
    py_modules=['kanjiring', 'bot', 'cjkinfo'],
    install_requires=['tweepy']
)
