from setuptools import setup

setup(
    name='pytest-django-dotenv',
    version='0.1.1',
    author='Kamil Kucharski',
    author_email='kaniak274@gmail.com',
    description='Pytest plugin used to setup environment variables with django-dotenv',
    packages=['pytest_django_dotenv'],
    entry_points={'pytest11': ['env = pytest_django_dotenv.plugin']},
    install_requires=['pytest>=2.6.0', 'django-dotenv>=1.4.2'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6'
    ],
    url='https://github.com/kaniak274/pytest-django-dotenv'
)
