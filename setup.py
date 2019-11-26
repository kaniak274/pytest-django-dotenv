from setuptools import setup

setup(
    name='pytest-django-dotenv',
    version='0.1.0',
    author='Kamil Kucharski',
    author_email='kaniak274@gmail.com',
    packages=['pytest_django_dotenv'],
    entry_points={'pytest11': ['env = pytest_django_dotenv.plugin']},
    install_requires=['pytest>=2.6.0', 'django-dotenv>=1.4.2'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6'
    ]
)