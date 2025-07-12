from flask import Flask, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import time

class RateLimiter:
    """
    简单的速率限制器实现，使用固定窗口算法。
    
    :param max_calls: 最大调用次数
    :param period: 时间窗口（秒）
    """
    def __init__(self, max_calls, period):
        self.max_calls = max_calls
        self.period = period
        self.calls = []

    def allow_call(self):
        """
        检查是否允许新的调用。
        
        :return: 如果允许调用返回 True，否则返回 False
        """
        now = time.time()
        # 移除时间窗口外的调用记录
        self.calls = [t for t in self.calls if t > now - self.period]
        if len(self.calls) < self.max_calls:
            self.calls.append(now)
            return True
        return False

app = Flask(__name__)
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["10 per second"]
)

@app.route('/')
@limiter.limit("10 per second")
def index():
    """
    带速率限制的 HTTP 接口，每秒最多处理 10 个请求。
    """
    return jsonify({
        "message": "请求成功",
        "status": "success"
    })

if __name__ == '__main__':
    app.run(debug=True)