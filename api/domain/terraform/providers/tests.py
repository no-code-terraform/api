import unittest
from unittest.mock import Mock
from api.domain.terraform.providers.aws import Aws


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
