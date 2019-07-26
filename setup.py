from setuptools import setup, find_packages

version = '0.0.1'

setup(
    name="alerta-kentik",
    version=version,
    description='Alerta webhook for Kentik',
    url='http://localhost/',
    license='',
    author='',
    author_email='',
    packages=find_packages(),
    py_modules=['alerta_kentik'],
    install_requires=[
    ],
    include_package_data=True,
    zip_safe=True,
    entry_points={
        'alerta.webhooks': [
            'kentik = alerta_kentik:KentikWebhook'
        ]
    }
)
