from logger import Logger

def main():
    logger = Logger()
    print("Test")
    logger.log("This is a log")

    logger.error("Test error")
    logger.f_log("Try file log")

main()
