# -*- encoding:utf-8 -*-
from setuptools import setup, find_packages
from libtry.version import __version__ as ver
import sys


sys.path.append('./libtry')
sys.path.append('./tests')

if __name__ == "__main__":
    setup(
        name = "ios-libtry",
        version = ver,
        author = "Shota Shimazu",
        author_email = "hornet.live.mf@gmail.com",
        classifiers=[
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
        ],
        packages = find_packages(exclude=('tests', 'shell')),
        include_package_data = True,
        zip_safe = False,
        install_requires = [
            # "Flask"
        ],
        entry_points = {
            'console_scripts':[
                'libtry = libtry.try:main',
            ],
        },
        description = "iOS library demo launcher",
        long_description = "libTry is CLI tools that automatically clone sample project and build & compaile & run it.",
        url = "https://github.com/shotastage/libTry/",
        license = "Apache",
        platforms = ["POSIX", "Mac OS X"],
        test_suite = "mirage_test.suite",
    )
