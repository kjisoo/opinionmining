from setuptools import setup


try:
   with open('README.md') as f:
       readme = f.read()
except IOError:
   readme = ''


setup(
   name="opinionmining",
   version='0.0.1',
   py_modules=['noun_extract'],
   author='seopyoon',
   author_email='',
   url='https://github.com/seopyoon/opinionmining',
   description='',
   long_description=readme,
   install_requires=["konlpy==0.4.4", "JPype1==0.6.1"],
)
