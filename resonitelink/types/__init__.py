# NOTE: This module NEEDS to be self-contained and separate from the rest of the type logic in utils.
#       Otherwise the code generator will fail, as the import order would mean models aren't fully 
#       registered when types get evaluated, causing the code generator to fail.

from .aliases import *
