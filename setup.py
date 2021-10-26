import setuptools

setuptools.setup(
    name="demo_reader",
    version="0.0.2",
    description="Cool tool",
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
)
