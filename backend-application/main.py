from config.settings.settings import app



from fastapi import Request

@app.get('/all_endpoints')
def get_all_endpoints(
    request : Request
):
    url_list = [
        {'path': f'http://127.0.0.1:5000{route.path}', 'name': route.name}
        for route in request.app.routes
    ]
    return url_list