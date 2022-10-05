from api.domain import constant

PROVIDERS = [
    constant.PROVIDER_AWS,
    constant.PROVIDER_GCP,
    constant.PROVIDER_SCW,
]

SERVICE_EXTRA_TYPES = [
    constant.SERVICE_EXTRA_TYPE_ARRAY,
    constant.SERVICE_EXTRA_TYPE_INTEGER,
    constant.SERVICE_EXTRA_TYPE_STRING,
    constant.SERVICE_EXTRA_TYPE_OBJECT,
]

SERVICE_TYPES = [
    constant.SERVICE_TYPE_COMPUTE,
    constant.SERVICE_TYPE_DATABASE,
    constant.SERVICE_TYPE_STORAGE,
]
