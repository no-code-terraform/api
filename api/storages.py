from .domain import contract, model
from .models import Service
from .mappers import service as s_mapper


class ServiceStorage(
    contract.ServiceStorageContrat
):
    @staticmethod
    def findall() \
        -> list[model.Service]:
        results = []

        for item in Service.objects.all().values():
            results.append(
                s_mapper(item)
            )

        return results
