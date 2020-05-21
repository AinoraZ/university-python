from distutils.core import setup, Extension

module = Extension("rationalNumber", sources=["rationalNumber.c"])

setup(name="rationalNumber", ext_modules=[module])
