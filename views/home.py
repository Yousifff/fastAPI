from fastapi_chameleon import template
import fastapi


router = fastapi.APIRouter()

@router.get('/')
@template(template_file='home/index.pt')
def index(user: str = 'anon'):
    return {
        'package_count': 274_000,
        'release_count': 2_234_847,
        'user_count': 73_874,
        'packages': [
            {'id':'fastapi','summary':"A great web framework development"},
            {'id':'uvicorn','summary':"Your favorite ASGI server"},
            {'id':'httpx','summary':"Request for an async world"}
        ]
    }


@router.get("/about")
@template(template_file='home/about.pt')
def about():
    return {}
