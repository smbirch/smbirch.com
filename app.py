from flask import Flask, render_template, request
import logging

logger = logging.getLogger("smbirchcom")
logging.basicConfig(
    filename="logs.log",
    level=logging.DEBUG,
    format=f"%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
)

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    ipaddr = request.environ.get("HTTP_X_REAL_IP", request.remote_addr)
    logger.info(f"/homepage : {ipaddr}")
    return render_template("index.html")


@app.route("/about", methods=["GET"])
def about():
    ipaddr = request.environ.get("HTTP_X_REAL_IP", request.remote_addr)
    logger.info(f"/about : {ipaddr}")
    return render_template("about.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
