import versioneer
import setuptools


setuptools.setup(name='xlink_kme_sbml_analysis,
      description='Analysis of models obtained with the Kinetic Simulation Framework for Crosslinks',
      author='Kai-Michael Kammer',
      author_email='kai-michael.kammer@uni-konstanz.de',
      url='https://github.com/stengel-laboratory/xlink-kme-sbml-analysis',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      packages=setuptools.find_packages(),
      install_requires=[
          'numpy',
          'pandas',
          'tellurium',
          'altair',
          'vegafusion',
          'vegafusion-python-embed',
          'vl-convert-python',
      ],
      license='MIT',
      python_requires='>=3.10'
      )
