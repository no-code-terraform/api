from api.storages import ServiceStorage
from .contract import ServiceStorageContrat


def service_storage() -> ServiceStorageContrat:
    return ServiceStorage
