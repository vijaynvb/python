import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Application Started")
logging.warning("Low Memory Warning")
logging.error("Database Connection Failed")