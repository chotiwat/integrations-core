from .utils import make_metric_tree

METRICS = {
    'runtime.load_error': {
        'tags': (),
        'method': 'count',
    },
    'runtime.override_dir_not_exists': {
        'tags': (),
        'method': 'count',
    },
    'runtime.override_dir_exists': {
        'tags': (),
        'method': 'count',
    },
    'runtime.load_success': {
        'tags': (),
        'method': 'count',
    },
    'runtime.num_keys': {
        'tags': (),
        'method': 'gauge',
    },
    'cluster_manager.cds.config_reload': {
        'tags': (),
        'method': 'count',
    },
    'cluster_manager.cds.update_attempt': {
        'tags': (),
        'method': 'count',
    },
    'cluster_manager.cds.update_success': {
        'tags': (),
        'method': 'count',
    },
    'cluster_manager.cds.update_failure': {
        'tags': (),
        'method': 'count',
    },
    'cluster_manager.cds.version': {
        'tags': (),
        'method': 'gauge',
    },
    'http.no_route': {
        'tags': ('stat_prefix', ),
        'method': 'count',
    },
    'http.no_cluster': {
        'tags': ('stat_prefix', ),
        'method': 'count',
    },
    'http.rq_redirect': {
        'tags': ('stat_prefix', ),
        'method': 'count',
    },
    'http.rq_total': {
        'tags': ('stat_prefix', ),
        'method': 'count',
    },
    '': {
        'tags': (),
        'method': '',
    },
}

METRIC_TREE = make_metric_tree(METRICS)
