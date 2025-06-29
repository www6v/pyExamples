
import time
from concurrent.futures import ThreadPoolExecutor


def read_file():
    time.sleep(0.1)
    return "file result"

def read_db():
    time.sleep(0.2)
    return "db result"

def read_api():
    time.sleep(0.3)
    return "api result"    


if __name__ == "__main__":
   result1 = read_file()
#    print(result1)
   result2 = read_db()
#    print(result2)
   result3 = read_api()
#    print(result3)

   with ThreadPoolExecutor(max_workers=3) as executor:
      result = executor.submit(read_file)
      result2 = executor.submit(read_db)
      result3 = executor.submit(read_api)
      
      print(result.result())
      print(result2.result())
      print(result3.result())