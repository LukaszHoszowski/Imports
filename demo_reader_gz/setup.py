import setuptools

setuptools.setup(
    name="demo_reader_gz_plugin",
    version="0.0.2",
    description="Cool tool",
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    entry_point={
        'demo_reader.compression_plugins': ['gz = demo_reader_gz.gzipped']
    }
)
