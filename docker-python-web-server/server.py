from http.server import SimpleHTTPRequestHandler as Handler, HTTPServer as Server

PORT = 8000
Server(("", PORT), Handler).serve_forever()
