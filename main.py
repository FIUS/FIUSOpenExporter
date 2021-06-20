import prometheus_client
import requests
prometheus_gauge = prometheus_client.Gauge(
    'room_openstate', '0 if room is closed 1 if room is open')

def fetch_website():
    r = requests.get(
        "https://fius.informatik.uni-stuttgart.de/isOpen.php", timeout=10)
    is_open = r.text.strip() == "open"
    is_open_number = 1 if is_open else 0
    return is_open_number

prometheus_gauge.set_function(fetch_website)