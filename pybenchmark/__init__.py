try:                    # py 2
    from profile import profile, stats, kpystones, pystones
    from meminfo import MemInfo
    from cpuinfo import CpuInfo
    from .gprofiler import GProfiler
except ImportError:     # py 3
    from .profile import profile, stats, kpystones, pystones
    from .meminfo import MemInfo
    from .cpuinfo import CpuInfo
    from .gprofiler import GProfiler
