from distutils.core import setup, Extension

module = Extension("perfectNumber", sources=["perfectNumber.c"])

setup(name="perfectNumber", ext_modules=[module])
