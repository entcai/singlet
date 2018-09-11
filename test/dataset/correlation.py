#!/usr/bin/env python
# vim: fdm=indent
'''
author:     Fabio Zanini
date:       07/08/17
content:    Test Dataset class.
'''
import numpy as np


# Script
if __name__ == '__main__':

    # NOTE: an env variable for the config file needs to be set when
    # calling this script
    from singlet.dataset import Dataset
    ds = Dataset(samplesheet='example_sheet_tsv', counts_table='example_table_tsv')

    print('Correlation features to phenotypes')
    r = ds.correlation.correlate_features_phenotypes(
            phenotypes=['quantitative_phenotype_1_[A.U.]'],
            features=['TSPAN6', 'DPM1'])
    assert(np.isclose(r.values[0, 0], -0.8, rtol=1e-1, atol=1e-1))
    print('Done!')

    print('Correlation features to phenotype')
    r = ds.correlation.correlate_features_phenotypes(
            phenotypes='quantitative_phenotype_1_[A.U.]',
            features=['TSPAN6', 'DPM1'])
    assert(np.isclose(r.values[0], -0.8, rtol=1e-1, atol=1e-1))
    print('Done!')

    print('Correlation feature to phenotypes')
    r = ds.correlation.correlate_features_phenotypes(
            phenotypes=['quantitative_phenotype_1_[A.U.]'],
            features='TSPAN6')
    assert(np.isclose(r.values[0], -0.8, rtol=1e-1, atol=1e-1))
    print('Done!')

    print('Correlation feature to phenotype')
    r = ds.correlation.correlate_features_phenotypes(
            phenotypes='quantitative_phenotype_1_[A.U.]',
            features='TSPAN6')
    assert(np.isclose(r, -0.8, rtol=1e-1, atol=1e-1))
    print('Done!')

    print('Correlation features to phenotypes (Pearson)')
    r = ds.correlation.correlate_features_phenotypes(
            phenotypes=['quantitative_phenotype_1_[A.U.]'],
            features=['TSPAN6', 'DPM1'],
            method='pearson',
            fillna=0)
    assert(np.isclose(r.values[1, 0], -0.6, rtol=1e-1, atol=1e-1))
    print('Done!')

    print('Correlation features to phenotypes (Pearson, with complex fillna)')
    r = ds.correlation.correlate_features_phenotypes(
            phenotypes='quantitative_phenotype_1_[A.U.]',
            features=['TSPAN6', 'DPM1'],
            method='pearson',
            fillna={'quantitative_phenotype_1_[A.U.]': 0})
    assert(np.isclose(r.values[1], -0.6, rtol=1e-1, atol=1e-1))
    print('Done!')

    print('Correlation phenotypes to phenotypes (Pearson, with complex fillna)')
    r = ds.correlation.correlate_phenotypes_phenotypes(
            phenotypes='quantitative_phenotype_1_[A.U.]',
            phenotypes2='quantitative_phenotype_1_[A.U.]',
            method='pearson',
            fillna={'quantitative_phenotype_1_[A.U.]': 0},
            fillna2={'quantitative_phenotype_1_[A.U.]': 0},
            )
    assert(np.isclose(r, 1, rtol=1e-1, atol=1e-1))
    print('Done!')

    print('Correlation features to features (Pearson)')
    r = ds.correlation.correlate_features_features(
            features=['TSPAN6', 'DPM1'],
            features2=['TSPAN6'],
            method='pearson')
    assert(np.isclose(r.values[0, 0], 1, rtol=1e-1, atol=1e-1))
    print('Done!')
