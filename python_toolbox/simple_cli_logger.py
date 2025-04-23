
# Simple CLI Logger
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

def main():
    logging.info("Starting the process")
    try:
        result = 10 / 2
        logging.info(f"Result is {result}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
