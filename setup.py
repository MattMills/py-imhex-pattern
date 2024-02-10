from setuptools import setup, Extension
import os

if os.name == 'nt':
    compiler_args = ['/std:c++20']
else:
    compiler_args = ['-std=c++23', '-Wno-stringop-overflow', '-Wno-dangling-reference',  '-fexceptions', '-frtti']


extensions = [
    Extension(
        'py-imhex-pattern',
        sources=['cpp/py-imhex-pattern.cpp', ],
        include_dirs=[
            "./cpp", 
            "external/PatternLanguage/lib/include/", 
            "external/PatternLanguage/external/fmt/include/",
            "external/PatternLanguage/external/libwolv/libs/io/include",
            "external/PatternLanguage/external/libwolv/libs/utils/include",
            "external/PatternLanguage/external/libwolv/libs/containers/include",
            "external/PatternLanguage/external/libwolv/libs/types/include",
            ],  
        language="c++",
        extra_compile_args=compiler_args, 
    ),
]

setup(
    name="py-imhex-pattern",
    version="0.1",
    author="Your Name",
    description="""Your module description""",
    packages=["py-imhex-pattern"],
    ext_modules=extensions,
)
