import http.server
import random
import time

from prometheus_client import start_http_server, Counter, Gauge, Summary, Histogram

REQUESTS = Counter('hello_worlds_total', 'Hello Worlds requested.', labelnames=['path', 'method'])
EXCEPTIONS = Counter('hello_world_exceptions_total', 'Exceptions serving Hello World.')
SALES = Counter('hello_word_sales_euro_total', 'Euros made serving Hello World.')


INPROGRESS = Gauge('hello_worlds_inprogress', 'Number of Hello Worlds in progress.')
LAST = Gauge('hello_world_last_time_seconds', 'The last time a Hello World was served.')


LATENCY = Summary('hello_world_latency_seconds', 'Time for a request Hello World.')
LATENCY_HISTOGRAM = Histogram('hello_world_latency_seconds_histo', 'Time for a request Hello World.')


class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/gauge":
            INPROGRESS.inc()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Hello Gauge")
            LAST.set(time.time())
            INPROGRESS.dec()
        elif self.path == "/summary":
            start = time.time()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Hello Summary")
            LATENCY.observe(time.time() - start)
            LATENCY_HISTOGRAM.observe(time.time() - start)
        else:
            REQUESTS.labels(self.path, self.command).inc()
            with EXCEPTIONS.count_exceptions():
                if random.random() < 0.2:
                    raise Exception
            euros = random.random()
            SALES.inc(euros)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Hello Word")


if __name__ == "__main__":
    start_http_server(8000)
    server = http.server.HTTPServer(('0.0.0.0', 8001), MyHandler)
    server.serve_forever()