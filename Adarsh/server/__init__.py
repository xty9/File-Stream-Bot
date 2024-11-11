# © CodeXBots

from aiohttp import web
from .stream_routes import routes

async def web_server():
    try:
        web_app = web.Application(client_max_size=30000000)
        web_app.add_routes(routes)
        return web_app
    except Exception as e:
        logging.error(f"Error creating web server: {str(e)}")
        raise web.HTTPInternalServerError(text="Error initializing server")