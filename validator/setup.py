# Copyright 2016, 2017 Suomi Corporation
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
import subprocess

from setuptools import setup, find_packages

if os.name == 'nt':
    conf_dir = "C:\\Program Files (x86)\\Suomi\\suomi\\conf"
    data_dir = "C:\\Program Files (x86)\\Suomi\\suomi\\data"
    log_dir = "C:\\Program Files (x86)\\Suomi\\suomi\\logs"
else:
    conf_dir = "/etc/suomi"
    data_dir = "/var/lib/suomi"
    log_dir = "/var/log/suomi"

data_files = [
    (conf_dir, ['packaging/path.toml.example',
                'packaging/log_config.toml.example',
                'packaging/validator.toml.example']),
    (os.path.join(conf_dir, "keys"), []),
    (data_dir, []),
    (log_dir, []),
]

if os.path.exists("/etc/default"):
    data_files.append(
        ('/etc/default', ['packaging/systemd/suomi-validator']))

if os.path.exists("/lib/systemd/system"):
    data_files.append(('/lib/systemd/system',
                       ['packaging/systemd/suomi-validator.service']))

setup(
    name='suomi-validator',
    version=subprocess.check_output(
        ['../bin/get_version']).decode('utf-8').strip(),
    description='Suomi Validator',
    author='Suomi',
    url='https://github.com/suomichain/suomi-core',
    packages=find_packages(),
    install_requires=[
        "cbor>=0.1.23",
        "colorlog",
        "protobuf",
        "lmdb",
        "requests",
        "suomi-signing",
        "toml",
        "PyYAML",
        "pyzmq",
        "netifaces",
        "pyformance"
    ],
    data_files=data_files,
    entry_points={
        'console_scripts': [
            'suomi-validator = suomi_validator.server.cli:main'
        ]
    })
