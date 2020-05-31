#!/usr/bin/pytho
import metric_correlation_syslevel as mcsys
import metric_correlation_seglevel as mcseg
import os

def get_summary_correlations(mc, baseline, gold, system):
    # get correlation results
    baseline_results, system_results, sigs = mc.get_results(gold, baseline, system)

    relgains = [(lp, 100 * ((system_results[lp][0]/baseline_results[lp][0]) - 1), system_results[lp][1]) for lp in system_results]
    sorted_gains = sorted(relgains, key=lambda x: x[1])
    average = sum([x[1] for x in sorted_gains]) / len(sorted_gains)
    maximum = sorted_gains[-1][1]
    minimum = sorted_gains[0][1]

    print('%.2f & %.2f & %.2f' % (average, minimum, maximum), end = ' ')

    
def get_summary_correlations_small(mc, baseline, gold, system):
    # get correlation results
    baseline_results, system_results, sigs = mc.get_results(gold, baseline, system)

    assert len(system_results) == 1 and 'de-en' in system_results

    rel_gain = 100 * ((system_results['de-en'][0] / baseline_results['de-en'][0]) -1)

    
    print(' %.2f ' % rel_gain, end=' ')


def content_large_table(metric, testset):

    thisdir=os.path.dirname(os.path.abspath(__file__)) + '/'
    if metric == 'bleu':
        baseline = thisdir + '../metric-scores/' + testset + '/sacreBLEU'
    else:
        baseline = thisdir + '../metric-scores/' + testset + '/Meteor'
    system_prefix = thisdir + '../metric-scores/' + testset + '/'
    gold_sys = thisdir + '../metrics-task/DA-syslevel-' + testset + '.csv'
    gold_seg = thisdir + '../metrics-task/RR-seglevel-' + testset + '.csv'
    
    print(r'\midrule')
    print(r'\multirow{3}{*}{\pbox{2.3cm}{Baselines (+5)}}')
    print(r'& \beam && ', end=' ')
    get_summary_correlations(mcsys, baseline + '-syslevel.tsv', gold_sys, system_prefix + '/beam/par' + metric + '-beam.num=5-syslevel.tsv')
    print(' && ', end= ' ')
    get_summary_correlations(mcseg, baseline + '-seglevel.tsv', gold_seg, system_prefix + '/beam/par' + metric + '-beam.num=5-seglevel.tsv')
    print(r'\\')
    print(r'& \random && ', end=' ')
    get_summary_correlations(mcsys, baseline + '-syslevel.tsv', gold_sys, system_prefix + '/random/par' + metric + '-random.num=5-syslevel.tsv')
    print(' && ', end= ' ')
    get_summary_correlations(mcseg, baseline + '-seglevel.tsv', gold_seg, system_prefix + '/random/par' + metric + '-random.num=5-seglevel.tsv')
    print(r'\\')
    print(r'& \sampled && ', end=' ')
    get_summary_correlations(mcsys, baseline + '-syslevel.tsv', gold_sys, system_prefix + '/sampled/par' + metric + '-sampled.num=5-syslevel.tsv')
    print(' && ', end= ' ')
    get_summary_correlations(mcseg, baseline + '-seglevel.tsv', gold_seg, system_prefix + '/sampled/par' + metric + '-sampled.num=5-seglevel.tsv')
    print(r'\\')
    
    print(r'\midrule')
    print(r'\multirow{3}{*}{\pbox{2.3cm}{Diversity (+1)}}')
    print(r'& \laser && ', end=' ')
    get_summary_correlations(mcsys, baseline + '-syslevel.tsv', gold_sys, system_prefix + '/laser/par' + metric + '-laser.num=1-syslevel.tsv')
    print(' && ', end= ' ')
    get_summary_correlations(mcseg, baseline + '-seglevel.tsv', gold_seg, system_prefix + '/laser/par' + metric + '-laser.num=1-seglevel.tsv')
    print(r'\\')
    print(r'& \treelstm && ', end=' ')
    get_summary_correlations(mcsys, baseline + '-syslevel.tsv', gold_sys, system_prefix + '/treelstm/par' + metric + '-treelstm.num=1-syslevel.tsv')
    print(' && ', end= ' ')
    get_summary_correlations(mcseg, baseline + '-seglevel.tsv', gold_seg, system_prefix + '/treelstm/par' + metric + '-treelstm.num=1-seglevel.tsv')
    print(r'\\')

    print(r'\midrule')
    print(r'\multirow{2}{*}{\pbox{2.3cm}{Diversity (+5)}}')
    print(r' & \laser && ', end=' ')
    get_summary_correlations(mcsys, baseline + '-syslevel.tsv', gold_sys, system_prefix + '/laser/par' + metric + '-laser.num=5-syslevel.tsv')
    print(' && ', end= ' ')
    get_summary_correlations(mcseg, baseline + '-seglevel.tsv', gold_seg, system_prefix + '/laser/par' + metric + '-laser.num=5-seglevel.tsv')
    print(r'\\')
    print(r' & \treelstm && ', end=' ')
    get_summary_correlations(mcsys, baseline + '-syslevel.tsv', gold_sys, system_prefix + '/treelstm/par' + metric + '-treelstm.num=5-syslevel.tsv')
    print(' && ', end= ' ')
    get_summary_correlations(mcseg, baseline + '-seglevel.tsv', gold_seg, system_prefix + '/treelstm/par' + metric + '-treelstm.num=5-seglevel.tsv')
    print(r'\\')
    
    print(r'\midrule')
    print(r'\multirow{2}{*}{\pbox{2.3cm}{Output-specific (+1)}}')
    print(r'& \laser && ', end=' ')
    get_summary_correlations(mcsys, baseline + '-syslevel.tsv', gold_sys, system_prefix + '/mt-output-specific/par' + metric + '-constrained-laser.syslevel.tsv')
    print(' && ', end= ' ')
    get_summary_correlations(mcseg, baseline + '-seglevel.tsv', gold_seg, system_prefix + '/mt-output-specific/par' + metric + '-constrained-laser.seglevel.tsv')
    print(r'\\')
    print(r'& \treelstm && ', end=' ')
    get_summary_correlations(mcsys, baseline + '-syslevel.tsv', gold_sys, system_prefix + '/mt-output-specific/par' + metric + '-constrained-treelstm.syslevel.tsv')
    print(' && ', end= ' ')
    get_summary_correlations(mcseg, baseline + '-seglevel.tsv', gold_seg, system_prefix + '/mt-output-specific/par' + metric + '-constrained-treelstm.seglevel.tsv')
    print(r'\\')



    
def content_small_table(metric, testset):

    thisdir=os.path.dirname(os.path.abspath(__file__)) + '/'
    if metric == 'bleu':
        baseline = thisdir + '../metric-scores/' + testset + '/sacreBLEU'
    else:
        baseline = thisdir + '../metric-scores/' + testset + '/Meteor'
    system_prefix = thisdir + '../metric-scores/' + testset + '/'
    gold_sys = thisdir + '../metrics-task/DA-syslevel-' + testset + '.csv'
    gold_seg = thisdir + '../metrics-task/RR-seglevel-' + testset + '.500.csv'
        
    print(r'\midrule')
    # Beam
    get_summary_correlations_small(mcsys, baseline + '-syslevel.500.tsv', gold_sys, system_prefix + '/beam/par' + metric + '-beam.num=5-syslevel.500.tsv')
    print(r' & ', end=' ')
    get_summary_correlations_small(mcseg, baseline + '-seglevel.500.tsv', gold_seg, system_prefix + '/beam/par' + metric + '-beam.num=5-seglevel.500.tsv')
    print(r'\\')

    # Random
    get_summary_correlations_small(mcsys, baseline + '-syslevel.500.tsv', gold_sys, system_prefix + '/random/par' + metric + '-random.num=5-syslevel.500.tsv')
    print(r' & ', end=' ')
    get_summary_correlations_small(mcseg, baseline + '-seglevel.500.tsv', gold_seg, system_prefix + '/random/par' + metric + '-random.num=5-seglevel.500.tsv')
    print(r'\\')

    # Sampled
    get_summary_correlations_small(mcsys, baseline + '-syslevel.500.tsv', gold_sys, system_prefix + '/sampled/par' + metric + '-sampled.num=5-syslevel.500.tsv')
    print(r' & ', end=' ')
    get_summary_correlations_small(mcseg, baseline + '-seglevel.500.tsv', gold_seg, system_prefix + '/sampled/par' + metric + '-sampled.num=5-seglevel.500.tsv')
    print(r'\\')

    # Diversity (+1)
    print(r'\midrule')
    get_summary_correlations_small(mcsys, baseline + '-syslevel.500.tsv', gold_sys, system_prefix + '/laser/par' + metric + '-laser.num=1-syslevel.500.tsv')
    print(r' & ', end=' ')
    get_summary_correlations_small(mcseg, baseline + '-seglevel.500.tsv', gold_seg, system_prefix + '/laser/par' + metric + '-laser.num=1-seglevel.500.tsv')
    print(r'\\')
    get_summary_correlations_small(mcsys, baseline + '-syslevel.500.tsv', gold_sys, system_prefix + '/treelstm/par' + metric + '-treelstm.num=1-syslevel.500.tsv')
    print(r' & ', end=' ')
    get_summary_correlations_small(mcseg, baseline + '-seglevel.500.tsv', gold_seg, system_prefix + '/treelstm/par' + metric + '-treelstm.num=1-seglevel.500.tsv')
    print(r'\\')


    # Diversity (+5)
    print(r'\midrule')
    get_summary_correlations_small(mcsys, baseline + '-syslevel.500.tsv', gold_sys, system_prefix + '/laser/par' + metric + '-laser.num=5-syslevel.500.tsv')
    print(r' & ', end=' ')
    get_summary_correlations_small(mcseg, baseline + '-seglevel.500.tsv', gold_seg, system_prefix + '/laser/par' + metric + '-laser.num=5-seglevel.500.tsv')
    print(r'\\')
    get_summary_correlations_small(mcsys, baseline + '-syslevel.500.tsv', gold_sys, system_prefix + '/treelstm/par' + metric + '-treelstm.num=5-syslevel.500.tsv')
    print(r' & ', end=' ')
    get_summary_correlations_small(mcseg, baseline + '-seglevel.500.tsv', gold_seg, system_prefix + '/treelstm/par' + metric + '-treelstm.num=5-seglevel.500.tsv')
    print(r'\\')


    # Output-specificx (+1)
    print(r'\midrule')
    get_summary_correlations_small(mcsys, baseline + '-syslevel.500.tsv', gold_sys, system_prefix + '/mt-output-specific/par' + metric + '-constrained-laser.syslevel.500.tsv')
    print(r' & ', end=' ')
    get_summary_correlations_small(mcseg, baseline + '-seglevel.500.tsv', gold_seg, system_prefix + '/mt-output-specific/par' + metric + '-constrained-laser.seglevel.500.tsv')
    print(r'\\')
    get_summary_correlations_small(mcsys, baseline + '-syslevel.500.tsv', gold_sys, system_prefix + '/mt-output-specific/par' + metric + '-constrained-treelstm.syslevel.500.tsv')
    print(r' & ', end=' ')
    get_summary_correlations_small(mcseg, baseline + '-seglevel.500.tsv', gold_seg, system_prefix + '/mt-output-specific/par' + metric + '-constrained-treelstm.seglevel.500.tsv')
    print(r'\\')

    
def write_summary_table(metric, testset):
    # main table
    print(r'\begin{table}[ht]')
    # first subtable
    print(r'\begin{subtable}{0.8\linewidth}')
    print(r'\centering\small')
    print(r'\scalebox{0.7}{')
    print(r'\begin{tabular}{llrrrrrrrr}')
    print(r'\toprule')
    print(r'&&& \multicolumn{3}{c}{System} && \multicolumn{3}{c}{Segment} \\')
    print(r'Approach & Method & \hphantom{oo} & Ave. & Min & Max & \hphantom{oo} & Ave. & Min & Max \\')
    content_large_table(metric, testset)
    # end first subtable
    print(r'\bottomrule')
    print(r'\end{tabular}}')
    print(r'\end{subtable}')

    # begin first subtable
    print(r'\begin{subtable}{0.19\linewidth}')
    print(r'\small')
    print(r'\scalebox{0.7}{')
    print(r'\begin{tabular}{rr}')
    print(r'\toprule')
    print(r'System & Segment \\')
    print(r'\multicolumn{2}{c}{de--en} \\')
    content_small_table(metric, testset)
    # end second subtable
    print(r'\bottomrule')
    print(r'\end{tabular}}')
    print(r'\end{subtable}')
    
    # end main table
    print(r'\end{table}')





if __name__ == '__main__':

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('metric', choices=('bleu', 'meteor'))
    parser.add_argument('testset', choices=('newstest2018', 'newstest2019'))
    args = parser.parse_args()

    
    write_summary_table(args.metric, args.testset)