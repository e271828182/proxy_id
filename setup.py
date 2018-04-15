from setuptools import setup

setup(
    name='proxy_id',
    version='1.0.0',
    description='High performance proxy pool',
    long_description='A proxy pool project modified from WiseDoge/ProxyPool',
    author=['Star',],
    author_email='e2.718@live.com',
    url='https://github.com/e271828182/proxy_id',
    packages=[
        'proxy_id'
    ],
    py_modules=['run'],
    include_package_data=True,
    platforms='any',
    install_requires=[
        'aiohttp',
        'requests',
        'flask',
        'redis',
        'pyquery'
    ],
    entry_points={
        'console_scripts': ['proxy_pool_run=run:cli']
    },
    license='apache 2.0',
    zip_safe=False,
    classifiers=[
        'Environment :: Console',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython'
    ]
)
