# https://docs.pytest.org/en/7.1.x/reference/reference.html#hooks
# -*- coding: utf-8 -*-

"""
Plugin for pytest environment configuration.

Here stored all conftest.py related stuff: hooks, fixtures, params etc
"""

import datetime
import logging
import os
import pprint
import json

import pytest

_log = logging.getLogger('Main.Pytest')


LOG_NAME = 'pytest.log'
CFG_CLI_FILE = 'cli_cfg.txt'
CFG_PARAMS_FILE = 'run_config.py'
CFG_PARAMS_FILE_SECTION = 'params'
TEST_RESULTS_DIR = os.environ.get('TEST_RESULTS_DIR', '/tmp')

COMMON_LOGO = r"""
# ########################
#  Pink Panther Testing  #
##########################
#  .--.            .--.  #
# ( (`\\."--``--".//`) ) #
#  '-.   __   __    .-'  #
#   /   /__\ /__\   \    #
#  |    \ 0/ \ 0/    |   #
#  \     `/   \`     /   #
#   `-.  /-'''-\  .-`    #
#     /  '.___.'  \      #
#     \     I     /      #
#      `;--'`'--;`       #
#        '.___.'         #
##########################
"""

USAGE = """
usage: pytest [options] [file_or_dir] [arg1] [arg2] ... [argN]
 args format:
   --<arg_name>=<arg_value>

 mandatory arguments:
   * setup config, required one of:
     --setup_cfg        - path to file with json params that we pass to test. 
"""


class Cfg:
    """Stores setup config data, path to current log directory etc."""
    params = {}
    log_dir = ''
    cli_args = {}


def get_logo():
    """Get logo banner."""
    return COMMON_LOGO


def pytest_load_initial_conftests(early_config, parser, args):
    """Parse cli arguments according format and register all unknown arguments."""
    print(get_logo())
    try:
        # parse args
        unknown_args = parser.parse_known_and_unknown_args(args)[-1]
        _log.info(unknown_args)
        args_dict = {curr_arg.split('=')[0]: curr_arg.split('=')[1] for curr_arg in unknown_args}
        if not args_dict:
            raise ValueError('Error while parsing arguments')

        all_started_with_double_dash = all(curr_name.startswith('--') for curr_name in args_dict.keys())
        if not all_started_with_double_dash:
            raise ValueError('Invalid argument name. Additional args should be specified as --<param name>')

        # check --setup_cfg
        setup_key_present = any(curr_key == '--setup_cfg' for curr_key in args_dict.keys())
        if not setup_key_present:
            raise ValueError('One of required arguments is not specified')

        # add args as known parser options
        for arg_name in args_dict.keys():
            parser.addoption(arg_name, action='store', default=args_dict[arg_name])
        Cfg.cli_args = args_dict

    except Exception as g_exc:
        _log.error(str(g_exc))
        raise pytest.UsageError(USAGE)


def pytest_runtest_setup(item):
    """Call setup procedures for each test function."""
    _log.info('=' * 80)
    _log.info(f'RUNNING TEST CASE: [{item.name}] ')


def pytest_runtest_teardown(item, nextitem):
    """Call teardown procedures for each test function."""
    _log.info('=' * 79)


def pytest_configure(config):
    """Modify captured pytest configuration."""
    try:
        if hasattr(config.option, 'setup_cfg'):
            if config.option.setup_cfg is None:
                raise ValueError('--setup_cfg argument is empty')
            with open(config.option.setup_cfg, 'r') as j_fh:
                curr_config = json.load(j_fh)
            Cfg.params.update(curr_config)
        else:
            raise ValueError('One of required arguments is not specified')

    except Exception as g_exc:
        raise RuntimeError(f'Error during pytest configuration: {g_exc}')


@pytest.fixture(autouse=True, scope='class')
def create_log_dir_for_test_class(request, pytestconfig):
    """Generate log folders with unique names for each test class within logs base dir."""
    try:
        log_base_dir = TEST_RESULTS_DIR
        test_class_ = request.cls
        class_name = test_class_.__name__

        # create new log_dir as "timestamp_testName"
        subdir_path = '[{0:}]_{1:}'.format(datetime.datetime.now().strftime('%Y%m%d-%H%M%S'), class_name)
        log_dir = os.path.join(log_base_dir, subdir_path)
        os.makedirs(log_dir, exist_ok=True)
        Cfg.log_dir = log_dir

        if hasattr(request.config.option, 'setup_cfg'):
            curr_setup_cfg = request.config.option.setup_cfg
        else:
            raise ValueError('One of required arguments is not specified')

        with open(os.path.join(log_dir, CFG_CLI_FILE), 'w') as t_cli:
            t_cli.write('=' * 100)
            t_cli.write('\nSETUP_CONFIG:\n\n{0:}\n'.format('\n'.join(str(curr_setup_cfg).split(','))))
            t_cli.write('=' * 100)
            t_cli.write('\nCLI ARGS: {0:}\n'.format(Cfg.cli_args))
            t_cli.write('=' * 100 + '\n')

        with open(os.path.join(log_dir, CFG_PARAMS_FILE), 'w') as t_cfg:
            t_cfg.write('{0:} = {1:}\n'.format(CFG_PARAMS_FILE_SECTION, pprint.pformat(Cfg.params, indent=4)))

        logging_plugin = pytestconfig.pluginmanager.get_plugin('logging-plugin')
        full_fname = os.path.join(log_dir, LOG_NAME)
        logging_plugin.set_log_path(full_fname)
        _log.info('Test params saved as: "{0}"'.format(os.path.join(log_dir, CFG_PARAMS_FILE)))

    except Exception as g_exc:
        raise RuntimeError('Error during pytest configuration: {0:}'.format(g_exc))


def pytest_assertion_pass(item, lineno, orig, expl):
    """Do additional actions for passed assert."""
    _log.info('[+] Assertion Pass')


def pytest_report_teststatus(report):
    """
    Log the test result of each test function.

    This hook can get called up to 3 times for one test function.
    Test Setup, Call, and Teardown. This hook function will log test results for each test.
    """
    if report.when == 'setup' and report.outcome != 'passed':
        _log.info(f'---- [SETUP {report.outcome.upper()}] ----'.rjust(80, ' '))
    elif report.when == 'call':
        _log.info(f'---- [{report.outcome.upper()}] ----'.rjust(80, ' '))
    elif report.when == 'teardown' and report.outcome != 'passed':
        _log.info(f'---- [TEARDOWN {report.outcome.upper()}] ----'.rjust(80, ' '))
