# vim: tabstop=4 shiftwidth=4 softtabstop=4
# Copyright 2009-2012 10gen, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Test class of 3PAR Client System Level APIS"""

import sys
import os
sys.path.insert(0, os.path.realpath(os.path.abspath('../')))

import unittest
import test_HP3ParClient_base


class HP3ParClientSystemTestCase(test_HP3ParClient_base.HP3ParClientBaseTestCase):

    def setUp(self):
        super(HP3ParClientSystemTestCase, self).setUp()

    def tearDown(self):
        # very last, tear down base class
        super(HP3ParClientSystemTestCase, self).tearDown()

    def test_getStorageSystemInfo(self):
        self.printHeader('getStorageSystemInfo')
        info = self.cl.getStorageSystemInfo()
        self.assertIsNotNone(info)

        self.printFooter('getStorageSystemInfo')

    def test_getWSAPIConfigurationInfo(self):
        self.printHeader('getWSAPIConfigurationInfo')

        info = self.cl.getWsApiVersion()
        self.assertIsNotNone(info)
        self.printFooter('getWSAPIConfigurationInfo')

#testing
#suite = unittest.TestLoader().loadTestsFromTestCase(HP3ParClientSystemTestCase)
#unittest.TextTestRunner(verbosity=2).run(suite)
