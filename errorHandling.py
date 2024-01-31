import logging

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.DEBUG)
logging.info("Start")
try:
    age = int(input("Enter Your age: "))

    now = age + 1
    print(now)
except Exception as err:
    logging.warning("Only Integer value Allow")
    # logging.error("Only Integer value Allow")
else:
    logging.info("Try Runs")
finally:
    logging.info("Completed Successfully")

print("End")
