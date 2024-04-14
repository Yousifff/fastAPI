from viewmodels.shared.viewmodel import ViewModelBase
from starlette.requests import Request
from typing import List
from services import packages_service, users_service
class IndexViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)
        self.package_count: int = packages_service.package_count()
        self.release_count: int = packages_service.release_count()
        self.user_count: int = users_service.user_count()
        self.packages: List = packages_service.latest_packages(limit=5)
