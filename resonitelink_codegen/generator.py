import logging
logging.basicConfig(format='%(asctime)s [%(levelname)-8s] %(name)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)
logger = logging.getLogger("CodeGenerator")

from typing import List, Generator
import os.path as path


class CodeGenerator():
    """
    Utility to auto-generate parts of the library.
    Each code generator is responsible for one file.
    
    """
    _generators : List['CodeGenerator'] = []
    _filepath : str

    def __init__(self, filepath : str):
        self._filepath = filepath
        CodeGenerator._generators.append(self)

    @classmethod
    def run_all(cls):
        logger.info("Running all generators...")
        for generator in cls._generators:
            generator.run()

    def run(self):
        """
        Runs this generator.

        """
        if not path.exists(self._filepath): 
            raise IOError(f"Not found: {path}")
        if not path.isfile(self._filepath): 
            raise IOError(f"Not a file: {path}")
        
        logger.info(f"Running code generator {type(self).__name__} on file: {self._filepath}")
        
        with open(self._filepath, mode='w') as file:
            file.write("#       >=============================================================================<\n")
            file.write("# NOTE: !!! THIS FILE IS AUTO-GENERATED! DO NOT EDIT! MODIFY CODEGENERATOR INSTEAD! !!!\n")
            file.write("#       >=============================================================================<\n")
            file.writelines(self.generate())

    def generate(self) -> Generator[str]:
        """
        To be implemented by extending class.
        Should yield each line to be included in the file.

        """
        raise NotImplementedError()
