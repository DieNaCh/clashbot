import time
elixir = 0
generate = 2.8
timestart = time.perf_counter()
while elixir <= 10:
    print(elixir)
    elixir += 1
    time.sleep(generate)
    timenow = time.perf_counter()
    if(timenow - timestart) > 120:
        generate = 1.4
    elif(timenow - timestart) > 240:
        generate = 0.9

    