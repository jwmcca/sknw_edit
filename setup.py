from setuptools import setup

descr = """sknw: skeleton analysis in Python.
Inspired by Juan Nunez-Iglesias's skan.
Edits by J. McCausland for custom cell segmentation purposes, 2023
"""

if __name__ == '__main__':
    setup(name='sknw_jwm',
        version='0.13',
        url='https://github.com/yxdragon/sknw',
        description='Analysis of object skeletons',
        long_description=descr,
        author='YXDragon',
        author_email='yxdragon@imagepy.org',
        license='BSD 3-clause',
        packages=['sknw_jwm'],
        package_data={},
        install_requires=[
            'numpy',
            'networkx',
            'numba'
        ],
    )
