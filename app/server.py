import json
import os
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from calculator import DistributedCalculator

NODE_NAME = os.getenv("NODE_NAME", "Node-Local-Dev")
PORT = int(os.getenv("PORT", 8080))

class DistributedAPIHandler(BaseHTTPRequestHandler):
    """
    HTTP Request Handler cung cấp các REST API cho hệ thống phân tán:
    - /health: Kiểm tra tình trạng hoạt động (Healthcheck)
    - /api/info: Trả về thông tin node phân tán
    - /api/calculate: Thực hiện phép toán phân tán
    """

    def _set_headers(self, status_code=200, content_type="application/json; charset=utf-8"):
        self.send_response(status_code)
        self.send_header("Content-Type", content_type)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

    def do_GET(self):
        parsed_url = urlparse(self.path)
        path = parsed_url.path
        params = parse_qs(parsed_url.query)

        if path == "/" or path == "/health":
            self._set_headers(200)
            response = {
                "status": "HEALTHY",
                "node": NODE_NAME,
                "message": "Distributed Node is running smoothly"
            }
            self.wfile.write(json.dumps(response, indent=2).encode("utf-8"))

        elif path == "/api/info":
            self._set_headers(200)
            response = {
                "service": "CS420-Distributed-Calculator-API",
                "node_identifier": NODE_NAME,
                "python_version": sys.version.split()[0],
                "endpoints": [
                    "/health",
                    "/api/info",
                    "/api/calculate?op=add&a=5&b=10"
                ]
            }
            self.wfile.write(json.dumps(response, indent=2).encode("utf-8"))

        elif path == "/api/calculate":
            op = params.get("op", [""])[0]
            try:
                a = float(params.get("a", [0])[0])
                b = float(params.get("b", [0])[0])

                calc = DistributedCalculator()
                if op == "add":
                    res = calc.add(a, b)
                elif op == "sub":
                    res = calc.subtract(a, b)
                elif op == "mul":
                    res = calc.multiply(a, b)
                elif op == "div":
                    res = calc.divide(a, b)
                elif op == "pow":
                    res = calc.power(a, b)
                else:
                    self._set_headers(400)
                    self.wfile.write(json.dumps({
                        "error": f"Phép toán '{op}' không được hỗ trợ. Dùng add, sub, mul, div, pow."
                    }).encode("utf-8"))
                    return

                self._set_headers(200)
                self.wfile.write(json.dumps({
                    "node": NODE_NAME,
                    "operation": op,
                    "a": a,
                    "b": b,
                    "result": res,
                    "status": "SUCCESS"
                }, indent=2).encode("utf-8"))

            except ValueError as ve:
                self._set_headers(400)
                self.wfile.write(json.dumps({"error": str(ve)}).encode("utf-8"))
            except Exception as e:
                self._set_headers(500)
                self.wfile.write(json.dumps({"error": f"Lỗi nội bộ: {str(e)}"}).encode("utf-8"))

        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Không tìm thấy endpoint"}).encode("utf-8"))

def run(server_class=HTTPServer, handler_class=DistributedAPIHandler, port=PORT):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"[*] Node [{NODE_NAME}] đang lắng nghe tại cổng {port}...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[*] Đang tắt máy chủ...")
        httpd.server_close()

if __name__ == "__main__":
    run()
