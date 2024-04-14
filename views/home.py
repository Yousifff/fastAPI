from fastapi_chameleon import template
import fastapi
from starlette.requests import Request
from viewmodels.home.indexviewmodel import IndexViewModel
router = fastapi.APIRouter()

@router.get('/')
@template(template_file='home/index.pt')
def index(request: Request):
    vm = IndexViewModel(request)
    return vm.to_dict()


@router.get("/about")
@template(template_file='home/about.pt')
def about():
    return {}
