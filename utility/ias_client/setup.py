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

from __future__ import print_function

import os
import subprocess

from setuptools import setup, find_packages

if os.name == 'nt':
    conf_dir = "C:\\Program Files (x86)\\Suomi\\suomi\\conf"
else:
    conf_dir = "/etc/suomi"

setup(
    name='suomi-ias-client',
    version=subprocess.check_output(
        ['../../bin/get_version']).decode('utf-8').strip(),
    description='Suomi Suomi Attestation Service Client',
    author='Suomi',
    url='https://github.com/suomi/suomi-core',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    entry_points={})
