from .domain import contract, model
from .models import Service
from .mappers import service


class ServiceStorage(
    contract.ServiceStorageContrat
):
    @staticmethod
    def findall() \
        -> list[model.Service]:
        results = []

        for item in Service.objects.all().values():
            results.append(
                service(item)
            )

        return results
