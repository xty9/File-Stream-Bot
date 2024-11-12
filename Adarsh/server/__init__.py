from aiohttp import web
from .stream_routes import routes

async def web_server():
    try:
        web_app = web.Application(client_max_size=30000000)
        web_app.add_routes(routes)
        return web_app  # Return the web app if successful
    except Exception as e:
        logging.error(f"Error creating web server: {str(e)}")
        return web.HTTPInternalServerError(text="Error initializing server")  # Return an error response