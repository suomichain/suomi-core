# Copyright 2017 Suomi Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------------------

import os
import sys
import toml


def _select_dir(suomi_home_dir, windows_dir, default_dir):
    """Returns the directory value, selected using the SUOMI_HOME
    environment variable (if set) or OS defaults.
    """
    if 'SUOMI_HOME' in os.environ:
        return os.path.join(os.environ['SUOMI_HOME'], suomi_home_dir)

    if os.name == 'nt':
        base_dir = \
            os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0])))
        return os.path.join(base_dir, windows_dir)

    return default_dir


def get_config_dir():
    """Returns the suomi configuration directory based on the
    SUOMI_HOME environment variable (if set) or OS defaults.
    """
    return _select_dir('etc', 'conf', '/etc/suomi')


def _get_dir(toml_config_setting,
             suomi_home_dir,
             windows_dir,
             default_dir):
    """Determines the directory path based on configuration.

    Arguments:
        toml_config_setting (str): The name of the config setting related
            to the directory which will appear in path.toml.
        suomi_home_dir (str): The directory under the SUOMI_HOME
            environment variable.  For example, for 'data' if the data
            directory is $SUOMI_HOME/data.
        windows_dir (str): The windows path relative to the computed base
            directory.
        default_dir (str): The default path on Linux.

    Returns:
        directory (str): The path.
    """
    conf_file = os.path.join(get_config_dir(), 'path.toml')
    if os.path.exists(conf_file):
        with open(conf_file) as fd:
            raw_config = fd.read()
        toml_config = toml.loads(raw_config)
        if toml_config_setting in toml_config:
            return toml_config[toml_config_setting]

    return _select_dir(suomi_home_dir, windows_dir, default_dir)


def get_data_dir():
    """Returns the configured data directory."""
    return _get_dir(
        toml_config_setting='data_dir',
        suomi_home_dir='data',
        windows_dir='data',
        default_dir='/var/lib/suomi')


def get_key_dir():
    """Returns the configured key directory."""
    return _get_dir(
        toml_config_setting='key_dir',
        suomi_home_dir='keys',
        windows_dir=os.path.join('conf', 'keys'),
        default_dir='/etc/suomi/keys')
