from setuptools import setup
from setuptools.command.test import test as TestCommand

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = [
            '--strict',
            '--verbose',
            '--tb=long',
            'tests']
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

setup(name='humansort',
      version='0.1',
      description='String sorting for humans',
      classifiers=['License :: OSI Approved :: MIT License',
                   'Intended Audience :: Developers',
                   'Development Status :: 3 - Alpha'
                  ],
      url='http://github.com/coreygirard/humansort',
      author='Corey Girard',
      author_email='corey.r.girard@gmail.com',
      license='MIT',
      packages=['humansort'],
      zip_safe=False)
