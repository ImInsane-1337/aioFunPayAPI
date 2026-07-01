from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as f:
    long_desc = f.read()


setup(name='aioFunPayAPI',
      version="1.1.1",
      description='Прослойка между aioFunPayAPI и клиентом.',
      long_description=long_desc,
      long_description_content_type="text/markdown",
      author='Woopertail',
      author_email='woopertail@gmail.com',
      url='https://github.com/woopertail/aioFunPayAPI',
      packages=find_packages("."),
      license='GPL3',
      keywords='funpay bot api tools',
      install_requires=['aiohttp>=3.9.0', 'beautifulsoup4'],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Programming Language :: Python :: 3',
          'Environment :: Console',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
      ]
)
