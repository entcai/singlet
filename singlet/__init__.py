# vim: fdm=indent
# author:     Fabio Zanini
# date:       15/08/17
# content:    Main singlet module.
# Module exporting
from .samplesheet import SampleSheet
from .counts_table import CountsTable, CountsTableSparse, CountsTableXR
from .dataset import Dataset
with open('_version.py', 'rt') as f:
    version = f.read().strip('\n')
