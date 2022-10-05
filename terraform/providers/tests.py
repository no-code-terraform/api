import unittest
from unittest.mock import Mock
from terraform.providers.aws import Aws
from terraform.providers.provider import Provider


class TestProvider(unittest.TestCase):
    def test_module(self):
        emitter = Mock()
        emitter.emit_app_variable()
        emitter.emit_app_variable.assert_called()
        emitter.emit_module()
        emitter.emit_module.assert_called()
        self.provider = Provider(emitter)
        self.provider.module('', '', '', '')


class TestAws(unittest.TestCase):
    def setUp(self):
        self.emitter = Mock()
        self.aws = Aws(self.emitter)

    def test_provider(self):
        self.emitter.emit_app_variable()
        self.emitter.emit_app_variable.assert_called()
        self.emitter.emit_provider()
        self.emitter.emit_provider.assert_called()
        self.aws.provider('region', 'project')
