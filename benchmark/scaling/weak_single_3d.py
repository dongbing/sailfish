#!/usr/bin/env python
"""Weak scaling with 3D single phase fluid."""

from examples.ldc_3d import LDCSim
from sailfish.controller import LBSimulationController
from sailfish.geo import EqualSubdomainsGeometry3D
from benchmark.scaling import util


def run_benchmark(num_blocks):
    # Lattice size is optimized for Tesla C2050.
    settings = {
        'max_iters': 5000,
        'every': 500,
        'quiet': True,
        'block_size': 128,
        'subdomains': num_blocks,
        'conn_axis': 'z',
        'mode': 'benchmark',
        'lat_nx': 254,
        'lat_ny': 192,
        'lat_nz': 300 * num_blocks,
        }

    ctrl = LBSimulationController(LDCSim, EqualSubdomainsGeometry3D, settings)
    timing_infos, min_timings, max_timings, subdomains = ctrl.run()
    util.save_result('weak_3d_single', num_blocks, timing_infos, min_timings,
            max_timings, subdomains)


if __name__ == '__main__':
    args = util.process_cmdline()
    run_benchmark(args.num_blocks)
