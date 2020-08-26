from http.server import BaseHTTPRequestHandler, HTTPServer
from selenium import webdriver
import random

fireFoxOptions = webdriver.FirefoxOptions()
fireFoxOptions.set_headless()
browser = webdriver.Firefox(firefox_options=fireFoxOptions)

hostName = "localhost"
serverPort = 9000
cutie = 'felix+argyle'

browser.get('https://duckduckgo.com/?q='+cutie+'&t=h_&iax=images&ia=images')

class MyServer(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header("Content-type", "text/html")
		self.end_headers()
		link = ""
		while True:
			link = random.choice(browser.find_elements_by_tag_name("img")).get_attribute('src')
			if link == None:
				continue
			if 'external-content' in link:
				break
		self.wfile.write(bytes(link, "utf-8"))

if __name__ == "__main__":      
	webServer = HTTPServer((hostName, serverPort), MyServer)
	print("Server started http://%s:%s" % (hostName, serverPort))

	try:
		webServer.serve_forever()
	except KeyboardInterrupt:
		pass

	webServer.server_close()
	print("Server stopped.")
