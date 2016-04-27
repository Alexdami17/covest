MAX_EXP = 200
GRID_DEPTH = 3
INF = float('inf')
VERBOSE = True
PLOT_LOG_SCALE = True
USE_BIGFLOAT = False
STEP = 1.1
OPTIMIZATION_METHOD = 'L-BFGS-B'
# OPTIMIZATION_METHOD  = 'TNC'
INITIAL_GRID_COUNT = 20
INITIAL_GRID_STEP = 3
DEFAULT_ERR_SCALE = 10
DEFAULT_K = 21
DEFAULT_READ_LENGTH = 100
DEFAULT_REPEAT_MODEL = 0
DEFAULT_MIN_SINGLECOPY_RATIO = 0.3
AUTO_SAMPLE_TARGET_COVERAGE = 12
NOISE_THRESHOLD = 10**-6
try:
    from multiprocessing import cpu_count

    DEFAULT_THREAD_COUNT = cpu_count()
except NotImplementedError:
    DEFAULT_THREAD_COUNT = 2
