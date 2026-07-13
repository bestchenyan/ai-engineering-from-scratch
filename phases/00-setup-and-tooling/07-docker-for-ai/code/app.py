from flask import Flask, jsonify
import torch

app = Flask(__name__)

@app.route('/predict', methods=['GET'])
def predict():
    # 顺便帮你测一下 API 能不能调用 GPU
    cuda_available = torch.cuda.is_available()
    device_name = torch.cuda.get_device_name(0) if cuda_available else "None"
    
    return jsonify({
        "status": "success",
        "message": "Hello from AI Container!",
        "torch_version": torch.__version__,
        "GPU_available": cuda_available,
        "GPU_device": device_name
    })

if __name__ == '__main__':
    # 核心：必须监听 0.0.0.0，容器外的 Windows 才能访问到
    app.run(host='0.0.0.0', port=5000)