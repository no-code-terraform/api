import cerberus

from django.utils.translation import gettext as _

# https://docs.python-cerberus.org/en/stable/validation-rules.html


class CustomErrorHandler(cerberus.errors.BasicErrorHandler):
	messages = cerberus.errors.BasicErrorHandler.messages.copy()
	messages[cerberus.errors.REQUIRED_FIELD.code] = _('app.error.required')
	messages[cerberus.errors.UNKNOWN_FIELD.code] = _('app.error.unknown')
	messages[cerberus.errors.UNALLOWED_VALUE.code] = _('app.error.unallowed')
	messages[cerberus.errors.UNALLOWED_VALUES.code] = _('app.error.unallowed')
	messages[cerberus.errors.FORBIDDEN_VALUE.code] = _('app.error.forbidden')
	messages[cerberus.errors.FORBIDDEN_VALUES.code] = _('app.error.forbidden')
	messages[cerberus.errors.MIN_VALUE.code] = _('app.error.min')
	messages[cerberus.errors.MAX_VALUE.code] = _('app.error.max')
	messages[cerberus.errors.REGEX_MISMATCH.code] = _('app.error.mismatch')
	messages[cerberus.errors.EMPTY_NOT_ALLOWED.code] = _('app.error.required')
	messages[cerberus.errors.NOT_NULLABLE.code] = _('app.error.required')
	messages[cerberus.errors.COERCION_FAILED.code] = _('app.error.invalid')
	messages[cerberus.errors.MAPPING_SCHEMA.code] = _('app.error.invalid')
	messages[cerberus.errors.CUSTOM.code] = _('app.error.invalid')


def validate(
  data: dict,
  rules: dict,
) -> dict:
	v = cerberus.Validator(rules, error_handler=CustomErrorHandler)
	v.validate(data)
	return v.errors
