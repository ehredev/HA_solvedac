from flask import Flask, jsonify, request
import requests
import os
import datetime

app = Flask(__name__)

# 기본 handle (config.json에서 사용자 지정 가능)
HANDLE = os.environ.get("HANDLE", "happyicus1")

@app.route("/", methods=["GET"])
def home():
    # Solved.ac API URL
    api_url = f"https://solved.ac/api/v3/user/grass?handle={HANDLE}&topic=today-solved"
    try:
        # API 요청
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()

        if datetime.datetime.now().hour >= 6:
            curdate = datetime.datetime.now().isoformat()[:10]
        else:
            delt = datetime.timedelta(days=-1)
            curdate = (datetime.datetime.now()+delt).isoformat()[:10]
        
        for i in data['grass']:
            if i['date'] == curdate:
                status = "품"
                break
            else:
                status = "안품"
    
        print(status)
        return jsonify({"status": status})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)