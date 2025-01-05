import hashlib
import time

# initial_time = time.time()

# secret_key = "ckczppom"
# number = 0

# md5_hash = hashlib.md5(secret_key.encode()).hexdigest()
# while not md5_hash.startswith("000000"):
#     number += 1

#     md5_hash = hashlib.md5((secret_key + str(number)).encode()).hexdigest()
#     print(secret_key + str(number), md5_hash)

# print(time.time() - initial_time)

# ckczppom117946 | 6.421006917953491 seg | 5.659463167190552 seg (multiprocessing)

# ===========================================

from multiprocessing import Process, Value, Event, Lock

def calculate_hash(id_, secret_key, number, stop_event, lock):
    local_number = 0
    while not stop_event.is_set():
        
        with lock:
            local_number = number.value
            number.value += 1000
        
        for i in range(local_number, local_number + 1000):
            new_hash = hashlib.md5((secret_key + str(i)).encode()).hexdigest()

            if stop_event.is_set():
                break
            
            print(id_, secret_key + str(i), new_hash)
            if new_hash.startswith("000000"):
                stop_event.set()
                break


if __name__ == "__main__":
    initial_time = time.time()

    stop_event = Event()
    lock = Lock()

    processes = []

    number = Value("i", 0)

    for i in range(3):
        process = Process(target=calculate_hash, args=(i, "ckczppom", number, stop_event, lock))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

    print(time.time() - initial_time)

# ckczppom3938038 | 226.0365490913391 seg | 188.69810461997986 seg (multiprocessing)
