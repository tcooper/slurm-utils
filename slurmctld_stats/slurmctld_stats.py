#!/usr/bin/env python

'''
slurmctld_stats.py
A script to query/print slurmctld statistics using pyslurm in a format
compatible with transmission to Graphite on standard port.
'''

from __future__ import print_function

def display(stats_dict):

    prefix="<prefix>"
    if stats_dict:
        req_time=stats_dict['req_time']
        for key, value in stats_dict.iteritems():
            if key in ['rpc_user_stats', 'rpc_type_stats']:
                label = 'rpc_user_id'
                if key == 'rpc_type_stats':
                    label = 'rpc_type_id'
                for rpc_key, rpc_val in value.iteritems():
                    if label == 'rpc_user_id':
                        rpc_key = pwd.getpwuid(rpc_key)[0]
                    for rpc_val_key, rpc_value in rpc_val.iteritems():
                        print("{0}.slurmctld.stats.{1}.{2}.{3} {4} {5}".format(prefix, key, rpc_key, rpc_val_key, rpc_value, req_time))
            else:
                print("{0}.slurmctld.stats.{1} {2} {3}".format(prefix, key, value, req_time))


if __name__ == "__main__":

    import pwd
    import time

    import pyslurm

    try:
        stats = pyslurm.statistics()
        s = stats.get()
        display(s)
    except ValueError as e:
        print("Error - {0}".format(e.args[0]))

