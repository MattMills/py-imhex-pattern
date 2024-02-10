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
            "external/PatternLanguage/external/libwolv/libs/utils/include",
            "external/PatternLanguage/external/libwolv/libs/containers/include",
            "external/PatternLanguage/external/libwolv/libs/types/include",
            ],  
        language="c++",
        extra_compile_args=["-std=c++23", '-Wno-stringop-overflow', '-Wno-dangling-reference',  '-fexceptions', '-frtti'], #windows: /std:c++20
        extra_link_args=["-std=c++23"],
    ),
]

setup(
    name="py-imhex-pattern",
    version="0.1",
    packages=["py-imhex-pattern"],
    ext_modules=cythonize(extensions),
)
