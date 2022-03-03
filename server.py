from pyngrok import ngrok

try:
	ngrok_tunnel = ngrok.connect()
	ngrok_process = ngrok.get_ngrok_process()
	tunnels = ngrok.get_tunnels()
	print(tunnels)
	ngrok_process.proc.wait()
except KeyboardInterrupt:
    print(" Shutting down server.")
    ngrok.kill()