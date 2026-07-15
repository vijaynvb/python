import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="custom_app.log"
)

logging.info("Application Started")
logging.warning("Low Memory Warning")
logging.error("Database Connection Failed")