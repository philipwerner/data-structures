from setuptools import setup

setup(
    name='data structure',
    package_dir={'': 'src'},
    py_modules=['bst', 'graph_1', 'dll', 'stack', 'deque', 'binheap', 'deque', 'que', 'priorityq'],
    author='Phil Werner',
    author_email='philip.r.werner@gmail.com',
    description='Data structure graph.',
    install_requires=[],
    extras_require={
        "test": ["pytest", "pytest-cov", "tox"]
    })
