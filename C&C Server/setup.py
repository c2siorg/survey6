from setuptools import setup, find_packages
setup(
    name='cnc_server',
    version='0.1.0',
    packages=['src.main','src.main.data','src.main.service_methods','src.main.service_methods.grpc_bin'],
    install_requires=
    [
        'grpcio==1.47.0',
        'grpcio-tools==1.47.0',
        'protobuf==3.20.1',
        # 'six==1.16.0',
        'python-dotenv==0.20.0',
    ],
    description='Server of Survey6 tool',
    author='WebTelescope',
    scripts = ['cnc-server']
    
)