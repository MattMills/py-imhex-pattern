from setuptools import setup, Extension
from Cython.Build import cythonize
import os


extensions = [
    Extension(
        "PyImhexPattern.PatternLanguage",
        sources=["python/patternlanguage.pyx",],
        include_dirs=[
            "./cpp", 
            "external/PatternLanguage/lib/include/pl/", 
            "external/PatternLanguage/external/fmt/include/",
            "external/PatternLanguage/external/libwolv/libs/io/include",
            ],  
        language="c++",
        extra_compile_args=["/std:c++20"],
    ),
]

setup(
    name="py-imhex-pattern",
    version="0.1",
    packages=["py-imhex-pattern"],
    ext_modules=cythonize(extensions),
)
