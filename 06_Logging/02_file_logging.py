import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO
)

logging.info("Application Started")
logging.warning("Low Balance Warning")
logging.error("Transaction Failed")

print("Logs saved to app.log")